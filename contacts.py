import json
import csv

class Contact:
    def __init__(self, id, name, phone=None, email=None):
        self.id = id
        self.name = name
        self.phone = phone
        self.email = email

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'phone': self.phone,
            'email': self.email
        }

class ContactsManager:
    def __init__(self, json_filename='data/contacts.json', csv_filename='data/contacts.csv'):
        self.json_filename = json_filename
        self.csv_filename = csv_filename
        self.contacts = self.load_contacts()

    def load_contacts(self):
        try:
            with open(self.json_filename, 'r', encoding='utf-8') as file:
                contacts_data = json.load(file)
                return [Contact(**data) for data in contacts_data]
        except FileNotFoundError:
            return []

    def save_contacts(self):
        with open(self.json_filename, 'w', encoding='utf-8') as file:
            json.dump([contact.to_dict() for contact in self.contacts], file, ensure_ascii=False, indent=4)

    def add_contact(self, name, phone=None, email=None):
        new_contact = Contact(len(self.contacts) + 1, name, phone, email)
        self.contacts.append(new_contact)
        self.save_contacts()

    def delete_contact(self, id):
        self.contacts = [contact for contact in self.contacts if contact.id != id]
        self.save_contacts()

    def import_contacts(self, csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact = Contact(
                    id=int(row['id']),
                    name=row['name'],
                    phone=row['phone'],
                    email=row['email']
                )
                self.contacts.append(contact)
            self.save_contacts()

    def export_contacts(self):
        with open(self.csv_filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'name', 'phone', 'email'])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())

    def search_contacts(self, search_term):
        return [contact for contact in self.contacts if search_term.lower() in contact.name.lower()]
