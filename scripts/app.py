import boto3
import json
from http.server import BaseHTTPRequestHandler, HTTPServer

# Configurazione con credenziali fake per LocalStack
ENDPOINT = "http://host.k3d.internal:4566"
REGION = "us-east-1"

# AGGIUNTO: aws_access_key_id e aws_secret_access_key
dynamodb = boto3.resource(
    'dynamodb', 
    endpoint_url=ENDPOINT, 
    region_name=REGION,
    aws_access_key_id='fakeMyKeyId',
    aws_secret_access_key='fakeAppleSecretAccessKey'
)
table = dynamodb.Table('ghost-infra-metadata')

class Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = json.loads(self.rfile.read(content_length))
            
            # Scrive su DynamoDB
            table.put_item(Item={'id': post_data['id'], 'data': post_data['content']})
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            self.wfile.write(b'{"status": "Dato salvato nel Ghost Cloud!"}')
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            self.wfile.write(str(e).encode())

def run():
    print("Aegis API in ascolto sulla porta 80...")
    server = HTTPServer(('0.0.0.0', 80), Handler)
    server.serve_forever()

if __name__ == "__main__":
    run()