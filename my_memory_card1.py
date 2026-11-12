#create a memory card application
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,  QPushButton, QHBoxLayout, QVBoxLayout, QLabel, QMessageBox, QRadioButton, QGroupBox, QButtonGroup
from PyQt5.QtGui import QFont
from random import shuffle, randint

class Question:
    def __init__(self,text,right_answer,wrong_answer1,wrong_answer2,wrong_answer3):
        self.text = text
        self.right_answer = right_answer
        self.wrong_answer1 = wrong_answer1
        self.wrong_answer2 = wrong_answer2
        self.wrong_answer3 = wrong_answer3

question_list = []
question_list.append(Question('Як правильно відкривати кейс в КС?',"Дістати картину Габена та поцілувати її","Сказати шо КС не регає","Пікати мід з бізоном","Написати ЕЗЗЗЗ Габену на пошту"))
question_list.append(Question("Кокакола іс пума?","Офкорс Лондон іс тзе капітал оф Брітан", "Макдональдс","Нет","ДАААААААААААААААААААААААААА"))
question_list.append(Question('Яка компанія створила першу літаючу машину?', "Тесла", "БМВ", "Запоріжець", "Вольво"))
question_list.append(Question("Що говорити госнікам якщо стонули","Забей мне капт","Вась","Тримайте документи моєї півної свинки","Я не при делах"))
question_list.append(Question("Що робити якщо тімейт Купив АВП на 4 раунді?","Дати 360 ноускоп в повітрі з Мухи","Кінути молік йому під ноги","Кікнуть його","Стопнути  його на вікні"))
question_list.append(Question('Сколько матері Габена',"200 тон","5 гривень","67",""))

app = QApplication([]) 
#створення віджетів головного вікна
window = QWidget()
window.resize(200, 150) 
window.setWindowTitle("Опрос")



RadioButtonsGroup = QGroupBox('Варіанти')
question = QLabel("Якій худший день?")
question1 = QRadioButton('Понеділок')
question2 = QRadioButton('Четверг')
question3 = QRadioButton('Субботу')
question4 = QRadioButton("П'ятниця")
Button = QPushButton("Відповідь")

Ticks_Group = QButtonGroup()
Ticks_Group.addButton(question1)
Ticks_Group.addButton(question2)
Ticks_Group.addButton(question3)
Ticks_Group.addButton(question4)

Answer_Group = QGroupBox('Результат')
result = QLabel('Тут буде результат',alignment=Qt.AlignCenter)
correct = QLabel('Тут буде правильна відповідь', alignment=Qt.AlignCenter)
result_lineVertical1 = QVBoxLayout()
result_lineVertical1.addWidget(result, alignment=Qt.AlignCenter)
result_lineVertical1.addWidget(correct, alignment=Qt.AlignCenter)
Answer_Group.setLayout(result_lineVertical1)
Answer_Group.hide()

font = QFont("Times New Roman", 15, QFont.Bold)
question.setFont(font)

layout1 = QVBoxLayout()
layout2 = QHBoxLayout()
layout3 = QHBoxLayout()

layout2.addWidget(question1, alignment=Qt.AlignCenter)
layout2.addWidget(question2, alignment=Qt.AlignCenter)
layout3.addWidget(question3, alignment=Qt.AlignCenter)
layout3.addWidget(question4, alignment=Qt.AlignCenter)

layout1.addLayout(layout2)
layout1.addLayout(layout3)
RadioButtonsGroup.setLayout(layout1)

RadioButtonsGroup.setLayout(layout1)

MainHline1 = QHBoxLayout()
MainHline2 = QHBoxLayout()
MainHline3 = QHBoxLayout()

MainHline1.addWidget(question, alignment=Qt.AlignCenter)
MainHline2.addWidget(RadioButtonsGroup, alignment=Qt.AlignCenter)
MainHline3.addWidget(Button, alignment=Qt.AlignCenter)

Mainvline1 = QVBoxLayout()
Mainvline1.addLayout(MainHline1, stretch=1)
Mainvline1.addLayout(MainHline2, stretch=48)
Mainvline1.addStretch(10)
Mainvline1.addLayout(MainHline3, stretch=5)
Mainvline1.addSpacing(5)

window.setLayout(Mainvline1)

def show_result():
    RadioButtonsGroup.hide()
    Answer_Group.show()
    Button.setText('Наступне ззапитання')

def show_questions():
    RadioButtonsGroup.show()
    Answer_Group.hide()
    Button.setText('Відповідь')

    Ticks_Group.setExclusive(False)
    question1.setChecked(False)
    question2.setChecked(False)
    question3.setChecked(False)
    question4.setChecked(False)
    Ticks_Group.setExclusive(True)

answers = [question1, question2, question3, question4]

def ask_question(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong_answer1)
    answers[2].setText(q.wrong_answer2)
    answers[3].setText(q.wrong_answer3)
    question.setText(q.text)
    correct.setText('Правильна відповідь:' + q.right_answer)
    show_questions()

def right_wrong():
    window.total += 1
    if Ticks_Group.checkedButton() is None:
        return
    if answers[0].isChecked():
        result.setText("Правильно!")
        window.score += 1
    else:
        result.setText("Невірно")
    show_result()
    rating = window.score/window.total * 100
    print('Дано відповідей',window.total)
    print('Правильних відповідей',window.score)
    print('Успішність',rating,"%")


def next_question():
    random_question = randint(0, len(question_list) - 1)
    q = question_list[random_question]
    ask_question(q)

def button_on():
    if Button.text() == 'Відповідь':
        right_wrong()
    else:
        next_question()

Button.clicked.connect(button_on)

window.score = 0
window.total = 0


window.show()
app.exec_()




