from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import*
from file_helper import*

app = QApplication([])

notes = read_from_file()


app.setStyleSheet("""
        QPushButton{
            background-color: #FFFF00;
            color: black;
        }
        QLabel{
            background-color: blue;
            color: white;
        }
    """)


window = QWidget()
window.resize(500,500)
main_line = QHBoxLayout()
h2 = QVBoxLayout()
text_field = QTextEdit()
notes_list_lbl = QLabel("Список заміток")
notes_list = QListWidget()
notes_list.addItems(notes)
h3 = QHBoxLayout()
create = QPushButton("Створити замітку")
remove = QPushButton("Видалити замітку")
save = QPushButton("Зберегти замітку")
tags_list_lbl = QLabel("Список тегів")
tags_list = QListWidget()
tag_line = QLineEdit()
h4 = QHBoxLayout()
add = QPushButton("Додати до замітки")
unplug = QPushButton("Відкріпити від замітки")
search = QPushButton("Шукати замітку")



main_line.addWidget(text_field)
h2.addWidget(notes_list_lbl)
h2.addWidget(notes_list)
h3.addWidget(create)
h3.addWidget(remove)
h2.addLayout(h3)
h2.addWidget(save)
h2.addWidget(tags_list_lbl)
h2.addWidget(tags_list)
h2.addWidget(tag_line)
h4.addWidget(add)
h4.addWidget(unplug)
h2.addLayout(h4)
h2.addWidget(search)
main_line.addLayout(h2)

def show_note():
    key = notes_list.currentItem().text()
    text_field.setText(notes[key]["текст"])
    tags_list.clear()
    tags_list.addItems(notes[key]["теги"])

notes_list.itemClicked.connect(show_note)

def add_note():
    note_name, ok = QInputDialog.getText(window,"Нова нотатка","Введіть назву нотатки ")

    if ok == True:
        notes[note_name] = {
            "текст": "",
            "теги": [

            ]
        }


        notes_list.clear()
        notes_list.addItems(notes)
        write_in_file(notes)

def save_note_funk():
    text = text_field.toPlainText()
    if text:

        note_key = notes_list.currentItem().text()
        notes[note_key]["текст"] = text
        write_in_file(notes)

save.clicked.connect(save_note_funk)


def remove_funk():
    note_key = notes_list.currentItem().text()
    notes.pop(note_key)
    notes_list.clear()
    notes_list.addItems(notes)
    write_in_file(notes)

remove.clicked.connect(remove_funk)

def add_tag():
    text = tag_line.text()
    note_key = notes_list.currentItem().text()
    notes[note_key]["теги"].append(text)
    write_in_file(notes)
    tags_list.clear()
    tags_list.addItems(notes[note_key]["теги"])

add.clicked.connect(add_tag)



create.clicked.connect(add_note)
window.setLayout(main_line)
window.show()
app.exec()
