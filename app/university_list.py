from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QListWidget,
    QLineEdit,
    QListWidgetItem
)

from database import (
    get_universities,
    get_university_by_id
)

from university_details import UniversityDetails



class UniversityList(QWidget):

    def __init__(self):

        super().__init__()

        self.setWindowTitle(
            "University Database"
        )

        self.resize(600,500)


        layout = QVBoxLayout()


        self.search = QLineEdit()

        self.search.setPlaceholderText(
            "Search university..."
        )


        self.search.textChanged.connect(
            self.load_data
        )


        self.list = QListWidget()


        # Connect only once
        self.list.itemClicked.connect(
            self.show_details
        )


        layout.addWidget(
            self.search
        )

        layout.addWidget(
            self.list
        )


        self.setLayout(layout)


        self.load_data()



    def load_data(self):

        self.list.clear()


        universities = get_universities()


        keyword = self.search.text().lower()


        for university in universities:

            name = university[1]

            country = university[2]


            text = (
                f"{name} | {country}"
            )


            if keyword in text.lower():

                item = QListWidgetItem(text)


                # Store database ID
                item.setData(
                    1,
                    university[0]
                )


                self.list.addItem(item)



    def show_details(self, item):

        university_id = item.data(1)


        university = get_university_by_id(
            university_id
        )


        self.details = UniversityDetails(
            university
        )

        self.details.show()