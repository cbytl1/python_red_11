import json
import csv
from datetime import datetime

class Note:
    def __init__(self, id, title, content):
        self.id = id
        self.title = title
        self.content = content
        self.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'content': self.content,
            'timestamp': self.timestamp
        }

class NotesManager:
    def __init__(self, json_filename='data/notes.json', csv_filename='data/notes.csv'):
        self.json_filename = json_filename
        self.csv_filename = csv_filename
        self.notes = self.load_notes()

    def load_notes(self):
        try:
            with open(self.json_filename, 'r', encoding='utf-8') as file:
                notes_data = json.load(file)
                return [Note(**data) for data in notes_data]
        except FileNotFoundError:
            return []

    def save_notes(self):
        with open(self.json_filename, 'w', encoding='utf-8') as file:
            json.dump([note.to_dict() for note in self.notes], file, ensure_ascii=False, indent=4)

    def create_note(self, title, content):
        new_note = Note(len(self.notes) + 1, title, content)
        self.notes.append(new_note)
        self.save_notes()

    def view_notes(self):
        return self.notes

    def edit_note(self, id, title, content):
        for note in self.notes:
            if note.id == id:
                note.title = title
                note.content = content
                note.timestamp = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
                self.save_notes()
                return True
        return False

    def delete_note(self, id):
        self.notes = [note for note in self.notes if note.id != id]
        self.save_notes()

    def import_notes(self, csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                note = Note(
                    id=int(row['id']),
                    title=row['title'],
                    content=row['content']
                )
                self.notes.append(note)
            self.save_notes()

    def export_notes(self):
        with open(self.csv_filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'content', 'timestamp'])
            writer.writeheader()
            for note in self.notes:
                writer.writerow(note.to_dict())

    def search_notes(self, search_term):
        return [note for note in self.notes if search_term.lower() in note.title.lower() or
                search_term.lower() in note.content.lower()]

