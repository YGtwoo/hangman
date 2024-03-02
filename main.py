from frontend.hangman_menu import Menu
from PyQt5 import QtCore, QtGui, QtWidgets

def main():
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    games_menu = Menu()
    games_menu.setup_ui(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()