import hashlib
import getpass

kennwort_manager = {}

def konto_erstellen():
    benutzername = input("Eingabe Benutzername: ")
    passwort = getpass.getpass("Eingabe Passwort: ")
    

