import json
import csv
from datetime import datetime

class FinanceRecord:
    def __init__(self, id, amount, category, date=None, description=None):
        self.id = id
        self.amount = amount
        self.category = category
        self.date = date if date else datetime.now().strftime("%d-%m-%Y")
        self.description = description

    def to_dict(self):
        return {
            'id': self.id,
            'amount': self.amount,
            'category': self.category,
            'date': self.date,
            'description': self.description
        }

class FinanceManager:
    def __init__(self, json_filename='data/finance.json', csv_filename='data/finance.csv'):
        self.json_filename = json_filename
        self.csv_filename = csv_filename
        self.records = self.load_records()

    def load_records(self):
        try:
            with open(self.json_filename, 'r', encoding='utf-8') as file:
                records_data = json.load(file)
                return [FinanceRecord(**data) for data in records_data]
        except FileNotFoundError:
            return []

    def save_records(self):
        with open(self.json_filename, 'w', encoding='utf-8') as file:
            json.dump([record.to_dict() for record in self.records], file, ensure_ascii=False, indent=4)

    def add_record(self, amount, category, date=None, description=None):
        new_record = FinanceRecord(len(self.records) + 1, amount, category, date, description)
        self.records.append(new_record)
        self.save_records()

    def delete_record(self, id):
        self.records = [record for record in self.records if record.id != id]
        self.save_records()

    def import_records(self, csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                record = FinanceRecord(
                    id=int(row['id']),
                    amount=float(row['amount']),
                    category=row['category'],
                    date=row['date'],
                    description=row['description']
                )
                self.records.append(record)
            self.save_records()

    def export_records(self):
        with open(self.csv_filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'amount', 'category', 'date', 'description'])
            writer.writeheader()
            for record in self.records:
                writer.writerow(record.to_dict())

    def filter_records(self, category=None, date=None):
        filtered_records = self.records
        if category:
            filtered_records = [record for record in filtered_records if record.category == category]
        if date:
            filtered_records = [record for record in filtered_records if record.date == date]
        return filtered_records