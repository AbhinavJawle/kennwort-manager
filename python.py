import hashlib
import getpass
import json
import os

DATA_FILE = "daten.json"
kennwort_manager = {}

def daten_laden():
    global kennwort_manager
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            kennwort_manager = json.load(f)

def daten_speichern():
    with open(DATA_FILE, "w") as f:
        json.dump(kennwort_manager, f)

def konto_erstellen():
    benutzername = input("Eingabe Benutzername: ")
    passwort = getpass.getpass("Eingabe Passwort: ")
    hashed_passwort = hashlib.sha256(passwort.encode()).hexdigest()
    kennwort_manager[benutzername] = hashed_passwort
    daten_speichern()
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
    daten_laden()
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

if __name__ == "__main__":
    main()