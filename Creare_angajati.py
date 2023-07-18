import json
import random

class Utilizator():
       def __init__(self, nume, prenume, id, companie):
        self.nume = nume
        self.prenume= prenume
        self.id = id
        self.companie = companie


def generate_unique_id():
    return random.randint(1000, 9999)

def creare_angajati(nume, prenume, companie):
    angajat = {
        "nume": nume,
        "prenume": prenume,
        "id": generate_unique_id(),
        "companie": companie
    }
    return angajat

angajati = []

# Exemplu de date pentru angajati
date_angajati = [
    ("Popescu", "Ion", "ABC Company"),
    ("Ionescu", "Maria", "XYZ Corporation"),
    ("Radu", "Alexandru", "123 Industries"),
    ("Dumitrescu", "Ana", "DEF Group"),
    ("Gheorghe", "Andrei", "UVW Ltd."),
    ("Constantin", "Elena", "456 Enterprises"),
    ("Mihai", "Cristina", "HIJ Corp."),
    ("Stan", "Vlad", "KLM Co."),
    ("Florescu", "Roxana", "789 Group"),
    ("Popa", "Mihai", "NOP Ltd."),
    ("Diaconu", "Andreea", "QRS Enterprises"),
    ("Georgescu", "Cătălina", "STU Corporation"),
    ("Iacob", "Marian", "VWX Company"),
    ("Pop", "Andrei", "YZA Group"),
    ("Munteanu", "Simona", "BCD Ltd."),
    ("Stanciu", "Daniel", "EFG Corporation"),
    ("Ionel", "Adrian", "GHI Enterprises"),
    ("Radulescu", "Laura", "JKL Co."),
    ("Popescu", "Gabriel", "MNO Group"),
    ("Marinescu", "Diana", "PQR Company")
]

# Crearea listei de angajati
for nume, prenume, companie in date_angajati:
    angajat = creare_angajati(nume, prenume, companie)
    angajati.append(angajat)

# Salvarea listei de angajati intr-un fisier JSON
with open("angajati.json", "w") as fisier_json:
    json.dump(angajati, fisier_json, indent=4)
