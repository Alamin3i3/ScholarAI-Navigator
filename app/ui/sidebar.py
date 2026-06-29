from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QPushButton
)



class Sidebar(QWidget):

    def __init__(self):

        super().__init__()


        self.setFixedWidth(
            220
        )


        layout = QVBoxLayout()



        self.dashboard_btn = QPushButton(
            "🏠 Dashboard"
        )


        self.university_btn = QPushButton(
            "🎓 Universities"
        )


        self.add_btn = QPushButton(
            "➕ Add University"
        )


        self.settings_btn = QPushButton(
            "⚙ Settings"
        )

        self.setStyleSheet("""
        QPushButton {
                text-align:left;
                padding-left:20px;}
        """)



        layout.addWidget(
            self.dashboard_btn
        )


        layout.addWidget(
            self.university_btn
        )


        layout.addWidget(
            self.add_btn
        )


        layout.addWidget(
            self.settings_btn
        )


        layout.addStretch()



        self.setLayout(
            layout
        )