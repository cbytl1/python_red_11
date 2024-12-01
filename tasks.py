import json
import csv
from datetime import datetime

class Task:
    def __init__(self, id, title, description, done=False, priority="Низкий", due_date=None):
        self.id = id
        self.title = title
        self.description = description
        self.done = done
        self.priority = priority
        self.due_date = due_date

    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'done': self.done,
            'priority': self.priority,
            'due_date': self.due_date,
        }

class TaskManager:
    def __init__(self, json_filename='data/tasks.json', csv_filename='data/tasks.csv'):
        self.json_filename = json_filename
        self.csv_filename = csv_filename
        self.tasks = self.load_tasks()

    def load_tasks(self):
        try:
            with open(self.json_filename, 'r', encoding='utf-8') as file:
                tasks_data = json.load(file)
                return [Task(**data) for data in tasks_data]
        except FileNotFoundError:
            return []

    def save_tasks(self):
        with open(self.json_filename, 'w', encoding='utf-8') as file:
            json.dump([task.to_dict() for task in self.tasks], file, ensure_ascii=False, indent=4)

    def create_task(self, title, description, priority="Низкий", due_date=None):
        new_task = Task(len(self.tasks) + 1, title, description, False, priority, due_date)
        self.tasks.append(new_task)
        self.save_tasks()

    def view_tasks(self):
        return self.tasks

    def edit_task(self, id, title=None, description=None, done=None, priority=None, due_date=None):
        for task in self.tasks:
            if task.id == id:
                if title: task.title = title
                if description: task.description = description
                if done is not None: task.done = done
                if priority: task.priority = priority
                if due_date: task.due_date = due_date
                self.save_tasks()
                return True
        return False

    def delete_task(self, id):
        self.tasks = [task for task in self.tasks if task.id != id]
        self.save_tasks()

    def import_tasks(self, csv_file):
        with open(csv_file, 'r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            for row in reader:
                task = Task(
                    id=int(row['id']),
                    title=row['title'],
                    description=row['description'],
                    done=row['done'].lower() == 'true',
                    priority=row['priority'],
                    due_date=row['due_date']
                )
                self.tasks.append(task)
            self.save_tasks()

    def export_tasks(self):
        with open(self.csv_filename, 'w', encoding='utf-8', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=['id', 'title', 'description', 'done', 'priority', 'due_date'])
            writer.writeheader()
            for task in self.tasks:
                writer.writerow(task.to_dict())
