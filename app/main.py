import sys

from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QListWidget,
    QStackedWidget
)


from dashboard import Dashboard
from university_list import UniversityList
from university_form import UniversityForm



class MainWindow(QMainWindow):


    def __init__(self):

        super().__init__()


        self.setWindowTitle(
            "ScholarAI Navigator"
        )

        self.resize(
            1000,
            600
        )


        # Sidebar

        self.sidebar = QListWidget()


        self.sidebar.addItem(
            "Dashboard"
        )

        self.sidebar.addItem(
            "Universities"
        )

        self.sidebar.addItem(
            "Add University"
        )


        # Pages

        self.pages = QStackedWidget()


        self.dashboard = Dashboard()

        self.university_list = UniversityList()

        self.form = UniversityForm()



        self.pages.addWidget(
            self.dashboard
        )

        self.pages.addWidget(
            self.university_list
        )

        self.pages.addWidget(
            self.form
        )


        self.sidebar.currentRowChanged.connect(
            self.pages.setCurrentIndex
        )


        self.setCentralWidget(
            self.pages
        )


        self.addDockWidget(
            1,
            self.sidebar
        )



app = QApplication(sys.argv)


window = MainWindow()

window.show()


sys.exit(
    app.exec()
)