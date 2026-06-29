import sys

from PyQt6.QtWidgets import QApplication

from ui.main_window import MainWindow
from ui.theme.theme_manager import ThemeManager


app = QApplication(sys.argv)

theme = ThemeManager(app)

theme = ThemeManager(app)
theme.load_theme(
    "dark"
)


window = MainWindow()

window.show()


sys.exit(
    app.exec()
)