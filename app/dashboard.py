from PyQt6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QListWidget
)


from ui.components.card import Card



class Dashboard(QWidget):

    def __init__(self):

        super().__init__()


        self.setup_ui()



    def setup_ui(self):


        main_layout = QVBoxLayout()



        # Header

        title = QLabel(
            "ScholarAI Navigator"
        )

        title.setObjectName(
            "Title"
        )


        subtitle = QLabel(
            "University research assistant"
        )


        main_layout.addWidget(
            title
        )


        main_layout.addWidget(
            subtitle
        )



        # Statistics cards


        cards_layout = QHBoxLayout()



        university_card = Card()

        university_card.layout.addWidget(
            QLabel("🎓 Universities")
        )

        university_card.layout.addWidget(
            QLabel("25")
        )



        country_card = Card()

        country_card.layout.addWidget(
            QLabel("🌍 Countries")
        )

        country_card.layout.addWidget(
            QLabel("12")
        )



        favorite_card = Card()

        favorite_card.layout.addWidget(
            QLabel("⭐ Favorites")
        )

        favorite_card.layout.addWidget(
            QLabel("5")
        )




        cards_layout.addWidget(
            university_card
        )


        cards_layout.addWidget(
            country_card
        )


        cards_layout.addWidget(
            favorite_card
        )



        main_layout.addLayout(
            cards_layout
        )



        # Recent universities


        recent_title = QLabel(
            "Recent Universities"
        )


        self.recent_list = QListWidget()


        self.recent_list.addItems(
            [
                "MIT - USA",
                "University of Oxford - UK",
                "University of Melbourne - Australia"
            ]
        )



        main_layout.addWidget(
            recent_title
        )


        main_layout.addWidget(
            self.recent_list
        )



        # Quick actions


        action_title = QLabel(
            "Quick Actions"
        )


        add_button = QPushButton(
            "➕ Add University"
        )


        search_button = QPushButton(
            "🔍 Search Universities"
        )


        main_layout.addWidget(
            action_title
        )


        main_layout.addWidget(
            add_button
        )


        main_layout.addWidget(
            search_button
        )



        main_layout.addStretch()



        self.setLayout(
            main_layout
        )