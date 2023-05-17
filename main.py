from pages import SignUp
from PyQt6.QtWidgets import *
import sys
def main():
    app = QApplication(sys.argv)

    window = SignUp()
    window.show()

    app.exec()

if __name__ == '__main__':
    main()
