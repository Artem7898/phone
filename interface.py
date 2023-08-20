import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QTextEdit, QDialog


class PhoneDirectoryApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Phone Directory")
        self.setGeometry(100, 100, 600, 400)

        self.central_widget = QWidget(self)
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()

        self.entries_text = QTextEdit(self)
        self.layout.addWidget(self.entries_text)

        self.add_button = QPushButton("Add New Entry", self)
        self.add_button.clicked.connect(self.add_entry)
        self.layout.addWidget(self.add_button)

        self.central_widget.setLayout(self.layout)

        self.directory = []

    def display_entries(self):
        entries_text = ""
        for entry in self.directory:
            entries_text += f"Name: {entry['first_name']} {entry['patronymic']} {entry['surname']}\n"
            entries_text += f"Organization: {entry['organization']}\n"
            entries_text += f"Work Phone: {entry['work_phone']}\n"
            entries_text += f"Personal Phone: {entry['personal_phone']}\n"
            entries_text += "-" * 50 + "\n"
        self.entries_text.setPlainText(entries_text)

    def add_entry(self):
        entry_dialog = EntryDialog(self)
        if entry_dialog.exec_() == QDialog.Accepted:
            new_entry = entry_dialog.get_entry()
            self.directory.append(new_entry)
            self.display_entries()


class EntryDialog(QDialog):
    def __init__(self, parent):
        super().__init__(parent)
        self.setWindowTitle("Add New Entry")
        self.setGeometry(200, 200, 300, 200)

        layout = QVBoxLayout()

        self.surname_input = QLineEdit(self)
        self.surname_input.setPlaceholderText("Surname")
        layout.addWidget(self.surname_input)

        self.first_name_input = QLineEdit(self)
        self.first_name_input.setPlaceholderText("First Name")
        layout.addWidget(self.first_name_input)

        self.patronymic_input = QLineEdit(self)
        self.patronymic_input.setPlaceholderText("Patronymic")
        layout.addWidget(self.patronymic_input)

        self.organization_input = QLineEdit(self)
        self.organization_input.setPlaceholderText("Organization")
        layout.addWidget(self.organization_input)

        self.work_phone_input = QLineEdit(self)
        self.work_phone_input.setPlaceholderText("Work Phone")
        layout.addWidget(self.work_phone_input)

        self.personal_phone_input = QLineEdit(self)
        self.personal_phone_input.setPlaceholderText("Personal Phone")
        layout.addWidget(self.personal_phone_input)

        self.add_button = QPushButton("Add", self)
        self.add_button.clicked.connect(self.accept)
        layout.addWidget(self.add_button)

        self.setLayout(layout)

    def get_entry(self):
        entry = {
            "surname": self.surname_input.text(),
            "first_name": self.first_name_input.text(),
            "patronymic": self.patronymic_input.text(),
            "organization": self.organization_input.text(),
            "work_phone": self.work_phone_input.text(),
            "personal_phone": self.personal_phone_input.text()
        }
        return entry


def main():
    app = QApplication(sys.argv)
    phone_directory_app = PhoneDirectoryApp()
    phone_directory_app.show()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
