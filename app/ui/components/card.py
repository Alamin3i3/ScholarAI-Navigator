from PyQt6.QtWidgets import QFrame, QVBoxLayout



class Card(QFrame):


    def __init__(self):

        super().__init__()


        self.setObjectName(
            "Card"
        )

        self.setMinimumHeight(
            120
        )


        self.layout = QVBoxLayout()


        self.setLayout(
            self.layout
        )