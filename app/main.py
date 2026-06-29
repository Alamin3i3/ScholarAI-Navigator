import sys
from PyQt6.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout

class MainWindow(QWidget):
    
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ScholerAI Naigator")
        self.resize(800,500)

        layout = QVBoxLayout()

        title = QLabel("ScholerAI Navigator")
        title.setStyleSheet(""" 
                font-size: 28px;
                font-weight: bold;
                """)
        
        subtile = QLabel(
            "University Research Assistant - version 0.1"
        )

        layout.addWidget(title)
        layout.addWidget(subtile)

        self.setLayout(layout)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

sys.exit(app.exec())

                        