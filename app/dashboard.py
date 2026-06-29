from PyQt6.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)


class Dashboard(QWidget):

    def __init__(self):

        super().__init__()


        layout = QVBoxLayout()


        title = QLabel(
            "Welcome to ScholarAI Navigator"
        )


        info = QLabel(
            """
            Your personal university research assistant.

            Manage:
            - Universities
            - Applications
            - Requirements
            - Notes
            """
        )


        layout.addWidget(title)

        layout.addWidget(info)


        self.setLayout(layout)