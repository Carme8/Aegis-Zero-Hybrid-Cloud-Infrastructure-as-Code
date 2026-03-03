import time
import re

# Simulazione della risposta di Amazon Comprehend
def mock_comprehend_pii(text):
    print(f"[AWS AI] Analisi del documento in corso con Amazon Comprehend...")
    time.sleep(1.5) # Pausa scenica per simulare l'elaborazione cloud
    
    # Regex che simula l'AI trovando email e telefoni
    redacted_text = re.sub(r'[\w\.-]+@[\w\.-]+', '[EMAIL_REDACTED]', text)
    redacted_text = re.sub(r'\+39\s\d{3}\s\d{7}', '[PHONE_REDACTED]', redacted_text)
    
    return redacted_text

def main():
    filename = "pii_test.txt"
    
    print("-" * 50)
    print(f"PROJECT SHIELD: UPLOAD FILE '{filename}'")
    print("-" * 50)

    try:
        # 1. Legge il file originale (INPUT)
        with open(filename, 'r') as f:
            original_content = f.read()
        
        print(f"\n[INPUT] Contenuto Originale (Non Sicuro):")
        print(f"> {original_content}")
        print("\n" + "." * 30 + "\n")

        # 2. Chiama l'AI (Simulazione)
        clean_content = mock_comprehend_pii(original_content)

        # 3. Mostra il risultato (OUTPUT)
        print(f"\n[OUTPUT] Contenuto Sanificato (Protetto da Shield):")
        print(f"> \033[92m{clean_content}\033[0m") # Stampa in verde
        print(f"\n[LOG] Dati originali spostati in 'Vault-Quarantine' (S3 Object Lock).")
        print("-" * 50)

    except FileNotFoundError:
        print(f"ERRORE: Assicurati che il file '{filename}' sia nella stessa cartella dello script!")

if __name__ == "__main__":
    main()