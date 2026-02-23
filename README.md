# Prototyp: Sicheres Authentifizierungs-System (Python)

Dieses Projekt demonstriert die Grundlagen der sicheren Benutzerverwaltung und Passwort-Speicherung. Anstatt Passwörter im Klartext zu speichern, nutzt dieses Tool kryptographisches Hashing, um die Integrität und Vertraulichkeit der Benutzerdaten zu gewährleisten.

## 🚀 Funktionen

* **Sichere Passworteingabe:** Verwendung des `getpass`-Moduls, um zu verhindern, dass Passwörter während der Eingabe im Terminal sichtbar sind ("Shoulder Surfing Protection").
* **SHA-256 Hashing:** Umwandlung von Passwörtern in einen eindeutigen digitalen Fingerabdruck.
* **Lokale Benutzerverwaltung:** Erstellung und Verifizierung von Benutzerkonten innerhalb der Programmlaufzeit.

## 🛠 Funktionsweise (Illustration)

### 1. Der Registrierungsprozess (Hashing)

Wenn ein Nutzer ein Passwort erstellt, passiert Folgendes:

* **Eingabe:** `MeinPasswort123`
* **Verarbeitung:** Das Passwort wird durch den SHA-256 Algorithmus gejagt.
* **Ergebnis:** Ein 64-stelliger Hexadezimal-String.

**Visualisierung:**

```text
[ Nutzer-Passwort ] --(SHA-256 Algorithm)--> [ 4813494d137e1631bba30... ]
                                                        |
                                               (Speicherung im System)

```

### 2. Der Login-Prozess (Vergleich)

Das System speichert niemals das Passwort selbst. Beim Login wird die Eingabe erneut gehasht und mit dem gespeicherten Hash verglichen.

| Schritt | Aktion | Ergebnis |
| --- | --- | --- |
| **1** | Nutzer gibt Passwort ein | `MeinPasswort123` |
| **2** | System hasht Eingabe | `4813494d137e...` |
| **3** | Abgleich mit Datenbank | `4813494d137e...` == `4813494d137e...`? |
| **4** | Entscheidung | **Erfolgreich!** |

---

## 💻 Installation & Nutzung

1. Stelle sicher, dass Python installiert ist.
2. Klone dieses Repository oder kopiere die Datei.
3. Starte das Programm über das Terminal:
```bash
python python.py

```