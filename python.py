import hashlib
import getpass

kennwort_manager = {}

def konto_erstellen():
    benutzername = input("Eingabe Benutzername: ")
    passwort = getpass.getpass("Eingabe Passwort: ")
    hashed_passwort = hashlib.sha256(passwort.encode()).hexdigest()
    kennwort_manager[benutzername] = hashed_passwort
    print("Konto erfolgreich erstellt!")

