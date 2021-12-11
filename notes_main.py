from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QBoxLayout, QListWidget, QLabel


add = QApplication([])
Notes1 = QWidget()
Notes1.setWindowTitle("Розумні нотатки")
Notes1.resize(900, 600)
button = QPushButton("Створити нотатки")
button1 = QPushButton("Видалити нотатки")
button2 = QPushButton("Зберегти замітку")
button3 = QPushButton("Додати до нотатку")
button4 = QPushButton("Відкріпити від нотатка")
button5 = QPushButton("Шукати замітку по тегу")

line = QVBoxLayout()


list_Notes1 = QListWidget()
list_Notes1 = QLabel("Список нотаток")




Notes1.show()
add.exec()