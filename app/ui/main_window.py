from PyQt6.QtWidgets import (
    QMainWindow,
    QWidget,
    QHBoxLayout,
    QStackedWidget
)


from ui.sidebar import Sidebar


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
            1200,
            700
        )


        self.setup_ui()



    def setup_ui(self):

        container = QWidget()


        layout = QHBoxLayout(
            container
        )


        # Sidebar

        self.sidebar = Sidebar()


        # Pages

        self.pages = QStackedWidget()


        self.dashboard = Dashboard()


        self.university_list = UniversityList()


        self.university_form = UniversityForm()



        self.pages.addWidget(
            self.dashboard
        )


        self.pages.addWidget(
            self.university_list
        )


        self.pages.addWidget(
            self.university_form
        )



        layout.addWidget(
            self.sidebar
        )


        layout.addWidget(
            self.pages
        )



        self.setCentralWidget(
            container
        )



        self.connect_buttons()



    def connect_buttons(self):

        self.sidebar.dashboard_btn.clicked.connect(
            lambda:
            self.pages.setCurrentIndex(0)
        )


        self.sidebar.university_btn.clicked.connect(
            lambda:
            self.pages.setCurrentIndex(1)
        )


        self.sidebar.add_btn.clicked.connect(
            lambda:
            self.pages.setCurrentIndex(2)
        )