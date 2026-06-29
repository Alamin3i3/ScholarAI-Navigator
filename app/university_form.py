from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QVBoxLayout,
    QMessageBox
)

from database import add_university


class UniversityForm(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Add University")
        self.resize(400,600)

        layout = QVBoxLayout()


        self.name = QLineEdit()
        self.name.setPlaceholderText("University Name")


        self.country = QLineEdit()
        self.country.setPlaceholderText("Country")


        self.website = QLineEdit()
        self.website.setPlaceholderText("Website")


        self.program = QLineEdit()
        self.program.setPlaceholderText("Program")


        self.tuition = QLineEdit()
        self.tuition.setPlaceholderText("Tuition Fee")


        self.deadline = QLineEdit()
        self.deadline.setPlaceholderText("Deadline")


        self.requirements = QTextEdit()
        self.requirements.setPlaceholderText(
            "Requirements"
        )


        self.notes = QTextEdit()
        self.notes.setPlaceholderText(
            "Notes"
        )


        self.status = QLineEdit()
        self.status.setPlaceholderText(
            "Status (Interested/Applied)"
        )


        save_button = QPushButton("Save University")

        save_button.clicked.connect(
            self.save_data
        )


        layout.addWidget(
            QLabel("University Information")
        )

        layout.addWidget(self.name)
        layout.addWidget(self.country)
        layout.addWidget(self.website)
        layout.addWidget(self.program)
        layout.addWidget(self.tuition)
        layout.addWidget(self.deadline)
        layout.addWidget(self.requirements)
        layout.addWidget(self.notes)
        layout.addWidget(self.status)

        layout.addWidget(save_button)


        self.setLayout(layout)



    def save_data(self):

        add_university(
            self.name.text(),
            self.country.text(),
            self.website.text(),
            self.program.text(),
            self.tuition.text(),
            self.deadline.text(),
            self.requirements.toPlainText(),
            self.notes.toPlainText(),
            self.status.text()
        )


        QMessageBox.information(
            self,
            "Success",
            "University Saved!"
        )