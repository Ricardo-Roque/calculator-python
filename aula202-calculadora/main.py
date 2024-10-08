import sys

from info import Info
from variables import WINDOW_ICON_PATH
from styles import setupTheme
from PySide6.QtGui import QIcon
from main_window import MainWindow
from display import Display
from buttons import ButtonsGrid
from PySide6.QtWidgets import QApplication

if __name__ == '__main__':
    # Cria a aplicação
    app = QApplication(sys.argv)
    setupTheme() 
    window = MainWindow()

    # Define o ícone
    icon = QIcon(str(WINDOW_ICON_PATH))
    window.setWindowIcon(icon)
    app.setWindowIcon(icon)

    #Info
    info = Info('Sua conta')
    window.addWidgetToVLayout(info)

    # Display
    display = Display()
    window.addWidgetToVLayout(display)

    # Grid
    buttonsgrid = ButtonsGrid(display, info, window)
    window.vLayout.addLayout(buttonsgrid)

    # Executa tudo
    window.adjustFixedSize()
    window.show()
    app.exec()