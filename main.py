from notes import NotesManager
from tasks import TaskManager
from contacts import ContactsManager
from finance import FinanceManager
from calculator import Calculator

def main():
    notes_manager = NotesManager()
    task_manager = TaskManager()
    contacts_manager = ContactsManager()
    finance_manager = FinanceManager()
    calculator = Calculator()

    while True:
        print("\n--- Меню ---")
        print("1. Управление заметками")
        print("2. Управление задачами")
        print("3. Управление контактами")
        print("4. Управление финансами")
        print("5. Калькулятор")
        print("6. Выход")

        choice = input("Выберите опцию: ")

        if choice == '1':
            while True:
                print("\n--- Заметки ---")
                print("1. Добавить заметку")
                print("2. Просмотреть все заметки")
                print("3. Редактировать заметку")
                print("4. Удалить заметку")
                print("5. Импортировать заметки из CSV")
                print("6. Экспортировать заметки в CSV")
                print("7. Назад")

                note_choice = input("Выберите опцию: ")
                if note_choice == '1':
                    title = input("Введите заголовок заметки: ")
                    content = input("Введите содержимое заметки: ")
                    notes_manager.create_note(title, content)
                elif note_choice == '2':
                    notes = notes_manager.view_notes()
                    for note in notes:
                        print(f"{note.id}: {note.title} - {note.content} (Создано: {note.timestamp})")
                elif note_choice == '3':
                    id = int(input("Введите ID заметки для редактирования: "))
                    title = input("Введите новый заголовок заметки: ")
                    content = input("Введите новое содержимое заметки: ")
                    notes_manager.edit_note(id, title, content)
                elif note_choice == '4':
                    id = int(input("Введите ID заметки для удаления: "))
                    notes_manager.delete_note(id)
                elif note_choice == '5':
                    csv_file = input("Введите имя CSV-файла для импорта: ")
                    notes_manager.import_notes(csv_file)
                elif note_choice == '6':
                    notes_manager.export_notes()
                    print("Заметки экспортированы в CSV.")
                elif note_choice == '7':
                    break
                else:
                    print("Неверный выбор.")

        elif choice == '2':
            while True:
                print("\n--- Задачи ---")
                print("1. Добавить задачу")
                print("2. Просмотреть все задачи")
                print("3. Редактировать задачу")
                print("4. Удалить задачу")
                print("5. Импортировать задачи из CSV")
                print("6. Экспортировать задачи в CSV")
                print("7. Назад")

                task_choice = input("Выберите опцию: ")
                if task_choice == '1':
                    title = input("Введите заголовок задачи: ")
                    description = input("Введите описание задачи: ")
                    priority = input("Введите приоритет (Низкий/Средний/Высокий): ")
                    due_date = input("Введите срок выполнения (дд-мм-гггг, оставьте пустым для отсутствия): ") or None
                    task_manager.create_task(title, description, priority, due_date)
                elif task_choice == '2':
                    tasks = task_manager.view_tasks()
                    for task in tasks:
                        print(f"{task.id}: {task.title} - {task.description} (Статус: {'Выполнено' if task.done else 'Не выполнено'})")
                elif task_choice == '3':
                    id = int(input("Введите ID задачи для редактирования: "))
                    done = input("Завершена ли задача? (да/нет): ").strip().lower() == 'да'
                    task_manager.edit_task(id, done=done)
                elif task_choice == '4':
                    id = int(input("Введите ID задачи для удаления: "))
                    task_manager.delete_task(id)
                elif task_choice == '5':
                    csv_file = input("Введите имя CSV-файла для импорта: ")
                    task_manager.import_tasks(csv_file)
                elif task_choice == '6':
                    task_manager.export_tasks()
                    print("Задачи экспортированы в CSV.")
                elif task_choice == '7':
                    break
                else:
                    print("Неверный выбор.")

        elif choice == '3':
            while True:
                print("\n--- Контакты ---")
                print("1. Добавить контакт")
                print("2. Просмотреть все контакты")
                print("3. Удалить контакт")
                print("4. Импортировать контакты из CSV")
                print("5. Экспортировать контакты в CSV")
                print("6. Назад")

                contact_choice = input("Выберите опцию: ")
                if contact_choice == '1':
                    name = input("Введите имя контакта: ")
                    phone = input("Введите телефон контакта (оставьте пустым для отсутствия): ") or None
                    email = input("Введите email контакта (оставьте пустым для отсутствия): ") or None
                    contacts_manager.add_contact(name, phone, email)
                elif contact_choice == '2':
                    contacts = contacts_manager.contacts
                    for contact in contacts:
                        print(f"{contact.id}: {contact.name} - {contact.phone} - {contact.email}")
                elif contact_choice == '3':
                    id = int(input("Введите ID контакта для удаления: "))
                    contacts_manager.delete_contact(id)
                elif contact_choice == '4':
                    csv_file = input("Введите имя CSV-файла для импорта: ")
                    contacts_manager.import_contacts(csv_file)
                elif contact_choice == '5':
                    contacts_manager.export_contacts()
                    print("Контакты экспортированы в CSV.")
                elif contact_choice == '6':
                    break
                else:
                    print("Неверный выбор.")

        elif choice == '4':
            while True:
                print("\n--- Финансы ---")
                print("1. Добавить запись")
                print("2. Просмотреть все записи")
                print("3. Удалить запись")
                print("4. Импортировать записи из CSV")
                print("5. Экспортировать записи в CSV")
                print("6. Фильтровать записи")
                print("7. Назад")

                finance_choice = input("Выберите опцию: ")
                if finance_choice == '1':
                    amount = float(input("Введите сумму записи: "))
                    category = input("Введите категорию: ")
                    date = input("Введите дату (формат дд-мм-гггг, оставьте пустым для текущей): ") or None
                    description = input("Введите описание (оставьте пустым для отсутствия): ") or None
                    finance_manager.add_record(amount, category, date, description)
                elif finance_choice == '2':
                    records = finance_manager.records
                    for record in records:
                        print(f"{record.id}: Сумма: {record.amount}, Категория: {record.category}, Дата: {record.date}, Описание: {record.description}")
                elif finance_choice == '3':
                    id = int(input("Введите ID записи для удаления: "))
                    finance_manager.delete_record(id)
                elif finance_choice == '4':
                    csv_file = input("Введите имя CSV-файла для импорта: ")
                    finance_manager.import_records(csv_file)
                elif finance_choice == '5':
                    finance_manager.export_records()
                    print("Финансовые записи экспортированы в CSV.")
                elif finance_choice == '6':
                    category = input("Введите категорию для фильтрации (оставьте пустым для всех записей): ") or None
                    date = input("Введите дату для фильтрации (оставьте пустым для всех записей): ") or None
                    filtered_records = finance_manager.filter_records(category, date)
                    for record in filtered_records:
                        print(f"{record.id}: Сумма: {record.amount}, Категория: {record.category}, Дата: {record.date}, Описание: {record.description}")
                elif finance_choice == '7':
                    break
                else:
                    print("Неверный выбор.")

        elif choice == '5':
            while True:
                print("\n--- Калькулятор ---")
                print("1. Сложение")
                print("2. Вычитание")
                print("3. Умножение")
                print("4. Деление")
                print("5. Вычислить выражение")
                print("6. Назад")

                calc_choice = input("Выберите опцию: ")
                if calc_choice == '1':
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))
                    result = calculator.add(a, b)
                    print(f"Результат: {result}")
                elif calc_choice == '2':
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))
                    result = calculator.subtract(a, b)
                    print(f"Результат: {result}")
                elif calc_choice == '3':
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))
                    result = calculator.multiply(a, b)
                    print(f"Результат: {result}")
                elif calc_choice == '4':
                    a = float(input("Введите первое число: "))
                    b = float(input("Введите второе число: "))
                    try:
                        result = calculator.divide(a, b)
                        print(f"Результат: {result}")
                    except ValueError as e:
                        print(e)
                elif calc_choice == '5':
                    expression = input("Введите выражение для вычисления: ")
                    try:
                        result = calculator.calculate(expression)
                        print(f"Результат: {result}")
                    except ValueError as e:
                        print(e)
                elif calc_choice == '6':
                    break
                else:
                    print("Неверный выбор.")

        elif choice == '6':
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")

if __name__ == "__main__":
    main()