contacts = [ 
    {
        "name": "Tadeáš",
        "email": "tadeas@email.cz",
        "telefon": "777 777 777",
    },
    {
        "name": "Tadeáš",
        "email": "tadeas@email.com",
        "telefon": "888 888 888"

    }
]

# Vypsání prvního kontaktu
print(contacts[0])
print(contacts[1])

# Vypsání hodnoty klíče "name" z položky indexu 0 (vytisknutí klíče -> př. ["name"])
print(contacts[0]["name"])

# Přidání kontaktu (přidání položky do listu -> .append)
name = "Tadeáš"
email = "tadeas2@gmail.com"
phone = ""

contact = {
    "name": name,
    "email": email,
    "telefon": phone
}

contacts.append(contact)
print(contacts)