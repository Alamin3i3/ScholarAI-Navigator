from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QTextEdit,
    QPushButton,
    QMessageBox
)

from database import update_university



class UniversityEdit(QWidget):

    def __init__(self, university):

        super().__init__()

        self.university = university


        self.setWindowTitle(
            "Edit University"
        )

        self.resize(400,600)


        layout = QVBoxLayout()


        self.name = QLineEdit(
            university[1]
        )

        self.country = QLineEdit(
            university[2]
        )

        self.website = QLineEdit(
            university[3]
        )

        self.program = QLineEdit(
            university[4]
        )

        self.tuition = QLineEdit(
            university[5]
        )

        self.deadline = QLineEdit(
            university[6]
        )


        self.requirements = QTextEdit()

        self.requirements.setText(
            university[7]
        )


        self.notes = QTextEdit()

        self.notes.setText(
            university[8]
        )


        self.status = QLineEdit(
            university[9]
        )


        save = QPushButton(
            "Save Changes"
        )


        save.clicked.connect(
            self.save_changes
        )


        for widget in [
            self.name,
            self.country,
            self.website,
            self.program,
            self.tuition,
            self.deadline,
            self.requirements,
            self.notes,
            self.status,
            save
        ]:

            layout.addWidget(widget)


        self.setLayout(layout)



    def save_changes(self):

        update_university(

            self.university[0],

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
            "Updated",
            "University updated successfully"
        )


        self.close()