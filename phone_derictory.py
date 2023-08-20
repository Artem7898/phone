import os
from typing import Dict

DIRECTORY_FILE = "phone_directory.txt"


def load_directory():
    """
     Загрузите записи каталога из файла.
     Возвращаеться список:
     Список словарей, представляющих каждую запись
    """
    directory = []
    if os.path.exists(DIRECTORY_FILE):
        with open(DIRECTORY_FILE, "r") as file:
            for line in file:
                entry_data = line.strip().split(";")
                entry = {
                    "surname": entry_data[0],
                    "first_name": entry_data[1],
                    "patronymic": entry_data[2],
                    "organization": entry_data[3],
                    "work_phone": entry_data[4],
                    "personal_phone": entry_data[5]
                }
                directory.append(entry)
    return directory


def save_directory(directory):
    """
    Сохраните записи каталога в файл.
    Каталог (список): Список записей каталога.
    """
    with open(DIRECTORY_FILE, "w") as file:
        for entry in directory:
            line = f"{entry['surname']};{entry['first_name']};{entry['patronymic']};{entry['organization']};{entry['work_phone']};{entry['personal_phone']}\n"
            file.write(line)


def display_entries(entries):
    """
    Отображать записи постранично.
    Записи (список): Список записей каталога.
    """
    page_size = 5
    for i in range(0, len(entries), page_size):
        print("\nPage", (i // page_size) + 1)
        print("-" * 50)
        for entry in entries[i:i + page_size]:
            print("Name:", f"{entry['first_name']} {entry['patronymic']} {entry['surname']}")
            print("Organization:", entry['organization'])
            print("Work Phone:", entry['work_phone'])
            print("Personal Phone:", entry['personal_phone'])
            print("-" * 50)


def add_entry(directory):
    """
    Добавьте новую запись в каталог.
    Каталог (список): Список записей каталога.
    """

    entry = {}
    entry['surname'] = input("Enter surname: ")
    entry['first_name'] = input("Enter first name: ")
    entry['patronymic'] = input("Enter patronymic: ")
    entry['organization'] = input("Enter organization: ")
    entry['work_phone'] = input("Enter work phone: ")
    entry['personal_phone'] = input("Enter personal phone: ")
    directory.append(entry)
    save_directory(directory)
    print("Entry added successfully!")


def edit_entry(directory):
    """
    Отредактируйте существующую запись в каталоге.
    Каталог (список): Список записей каталога.
    """
    surname = input("Enter the surname of the entry to edit: ")
    for entry in directory:
        if entry['surname'] == surname:
            entry['first_name'] = input("Enter new first name: ")
            entry['patronymic'] = input("Enter new patronymic: ")
            entry['organization'] = input("Enter new organization: ")
            entry['work_phone'] = input("Enter new work phone: ")
            entry['personal_phone'] = input("Enter new personal phone: ")
            save_directory(directory)
            print("Entry edited successfully!")
            return
    print("Entry not found.")


def search_entries(entries):
    """
    Поиск записей по характеристикам.
    Записи (список): Список записей каталога.
    """
    search_term = input("Enter search term: ").lower()
    search_results = []
    for entry in entries:
        if (search_term in entry['surname'].lower() or
                search_term in entry['first_name'].lower() or
                search_term in entry['patronymic'].lower() or
                search_term in entry['organization'].lower() or
                search_term in entry['work_phone'].lower() or
                search_term in entry['personal_phone'].lower()):
            search_results.append(entry)
    if search_results:
        display_entries(search_results)
    else:
        print("No matching entries found.")


def main():
    directory = load_directory()

    while True:
        print("\nPhone Directory")
        print("1. Display entries")
        print("2. Add new entry")
        print("3. Edit entry")
        print("4. Search entries")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            display_entries(directory)
        elif choice == "2":
            add_entry(directory)
        elif choice == "3":
            edit_entry(directory)
        elif choice == "4":
            search_entries(directory)
        elif choice == "5":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
