import hashlib
import getpass

kennwort_manager = {}

def konto_erstellen():
    benutzername = input("Eingabe Benutzername: ")
    passwort = getpass.getpass("Eingabe Passwort: ")
    hashed_passwort = hashlib.sha256(passwort.encode()).hexdigest()
    kennwort_manager[benutzername] = hashed_passwort
    print("Konto erfolgreich erstellt!")


def login():
    benutzername = input("Eingabe Benutzername: ")
    passwort = getpass.getpass("Eingabe Passwort: ")
    hashed_passwort = hashlib.sha256(passwort.encode()).hexdigest()
    if benutzername in kennwort_manager.keys() and kennwort_manager[benutzername] == hashed_passwort:
        print("Login erfolgreich!")
    else:
        print("Falscher Benutzername oder Passwort!")

def main():
    while True:
        print("1 = Konto erstellen")
        print("2 = Login")
        print("3 = Beenden")
        auswahl = input("Auswahl: ")
        if auswahl == "1":
            konto_erstellen()
        elif auswahl == "2":
            login()
        elif auswahl == "3":
            break
        else:
            print("Ungültige Auswahl!")
