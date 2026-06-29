from pathlib import Path


class ThemeManager:


    def __init__(self, app):

        self.app = app

        self.current_theme = "dark"



    def load_theme(self, theme):

        self.current_theme = theme


        path = Path(
            __file__
        ).parent / f"{theme}.qss"


        with open(
            path,
            "r",
            encoding="utf-8"
        ) as file:

            stylesheet = file.read()


        self.app.setStyleSheet(
            stylesheet
        )