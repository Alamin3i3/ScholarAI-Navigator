from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QPushButton
)

from database import delete_university
from university_edit import UniversityEdit


class UniversityDetails(QWidget):

    def __init__(self, university):

        super().__init__()

        self.university = university

        self.setWindowTitle(
            "University Details"
        )

        self.resize(500,500)


        layout = QVBoxLayout()


        name = QLabel(
            f"Name: {university[1]}"
        )

        country = QLabel(
            f"Country: {university[2]}"
        )

        website = QLabel(
            f"Website: {university[3]}"
        )

        program = QLabel(
            f"Program: {university[4]}"
        )

        tuition = QLabel(
            f"Tuition: {university[5]}"
        )

        deadline = QLabel(
            f"Deadline: {university[6]}"
        )

        requirements = QLabel(
            f"Requirements:\n{university[7]}"
        )

        notes = QLabel(
            f"Notes:\n{university[8]}"
        )

        status = QLabel(
            f"Status: {university[9]}"
        )


        delete_button = QPushButton(
            "Delete University"
        )


        delete_button.clicked.connect(
            self.delete_data
        )

        edit_button = QPushButton(
            "Edit university"
        )

        edit_button.clicked.connect(
            self.edit_data
        )


        layout.addWidget(name)
        layout.addWidget(country)
        layout.addWidget(website)
        layout.addWidget(program)
        layout.addWidget(tuition)
        layout.addWidget(deadline)
        layout.addWidget(requirements)
        layout.addWidget(notes)
        layout.addWidget(status)
        layout.addWidget(delete_button)
        layout.addWidget(edit_button)


        self.setLayout(layout)



    def delete_data(self):

        delete_university(
            self.university[0]
        )

        self.close()

    def edit_data(self):

        self.edit_window = UniversityEdit(
        self.university
        )

        self.edit_window.show()