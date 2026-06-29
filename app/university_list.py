from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTableWidget,
    QTableWidgetItem,
    QHeaderView
)


from database import get_universities



class UniversityList(QWidget):

    def __init__(self):

        super().__init__()

        self.all_universities = []

        self.setup_ui()

        self.load_universities()



    def setup_ui(self):

        layout = QVBoxLayout()


        # Title

        title = QLabel(
            "🎓 Universities"
        )

        title.setObjectName(
            "Title"
        )


        layout.addWidget(
            title
        )



        # Search

        search_layout = QHBoxLayout()


        self.search_box = QLineEdit()

        self.search_box.setPlaceholderText(
            "Search universities..."
        )


        self.search_button = QPushButton(
            "🔍 Search"
        )


        search_layout.addWidget(
            self.search_box
        )


        search_layout.addWidget(
            self.search_button
        )


        layout.addLayout(
            search_layout
        )



        # Table

        self.table = QTableWidget()


        self.table.setColumnCount(
            4
        )


        self.table.setHorizontalHeaderLabels(
            [
                "University",
                "Country",
                "Program",
                "Status"
            ]
        )


        self.table.setAlternatingRowColors(
            True
        )


        self.table.verticalHeader().setVisible(
            False
        )


        self.table.setSelectionBehavior(
            QTableWidget.SelectionBehavior.SelectRows
        )


        self.table.setEditTriggers(
            QTableWidget.EditTrigger.NoEditTriggers
        )


        header = self.table.horizontalHeader()


        header.setSectionResizeMode(
            0,
            QHeaderView.ResizeMode.Stretch
        )


        header.setSectionResizeMode(
            1,
            QHeaderView.ResizeMode.ResizeToContents
        )


        header.setSectionResizeMode(
            2,
            QHeaderView.ResizeMode.Stretch
        )


        header.setSectionResizeMode(
            3,
            QHeaderView.ResizeMode.ResizeToContents
        )



        layout.addWidget(
            self.table
        )


        self.setLayout(
            layout
        )



        # Search connection

        self.search_box.textChanged.connect(
            self.search_universities
        )



    def load_universities(self):


        self.all_universities = get_universities()


        self.display_universities(
            self.all_universities
        )



    def display_universities(self, universities):


        self.table.setRowCount(
            len(universities)
        )


        for row, university in enumerate(universities):

            # database order:
            # id,name,country,website,program,tuition,deadline,requirements,notes,status


            self.table.setItem(
                row,
                0,
                QTableWidgetItem(
                    university[1]
                )
            )


            self.table.setItem(
                row,
                1,
                QTableWidgetItem(
                    university[2]
                )
            )


            self.table.setItem(
                row,
                2,
                QTableWidgetItem(
                    university[4]
                )
            )


            self.table.setItem(
                row,
                3,
                QTableWidgetItem(
                    university[9]
                )
            )



    def search_universities(self):


        text = self.search_box.text().lower()



        if text == "":

            self.display_universities(
                self.all_universities
            )

            return



        filtered = []


        for university in self.all_universities:


            name = str(
                university[1]
            ).lower()


            country = str(
                university[2]
            ).lower()


            if (
                text in name
                or text in country
            ):

                filtered.append(
                    university
                )



        self.display_universities(
            filtered
        )