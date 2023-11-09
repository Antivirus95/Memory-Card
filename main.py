from PyQt5.QtWidgets import QApplication, QMessageBox
app = QApplication ([])
from win_test import*   
from data import qw_list, Question
from random import choice, shuffle
from win_edit import*  
qw = ""
choice_f = ""

def stat ():
    count = 0
    count_right = 0
    good = 0
    for q in qw_list :
        count += q.count
        count_right += q.count_right
    if count != 0:
        
        good = count_right / count * 100
    lbl_count.setText(f"Count of answers: {count}")
    lbl_count_right.setText(f"Count of right answers: {count_right}")
    lbl_good.setText(f"Cound of good: {good}")


def new_qw ():
    global qw 
    qw1 = choice (qw_list)
    while qw1 == qw:
        qw1 = choice (qw_list) 
    qw = qw1

    ans_list = [qw.ans, qw.wrong_1, qw.wrong_2, qw.wrong_3]
    shuffle (ans_list)

    lbl_ques.setText (qw.qw)
    for i in range (4):
        rbt_list [i].setText (ans_list [i])

def check_ans ():
    if btn_check.text () == "Check":
        if choice_f == qw.ans:
            lbl_rezult.setText ("Good")
            qw.ans_right ()

        else:
            lbl_rezult.setText ("F")
            qw.ans_wrong ()
        lbl_rght_ans.setText (qw.ans)
        box_qw.hide()
        box_ans.show()
        btn_check.setText ("next")
    else:
        new_qw()
        box_qw.show()
        box_ans.hide()
        btn_check.setText ("Check")

def clear ():
    edit_ans.clear ()
    edit_qw.clear ()
    edit_wrong1.clear ()
    edit_wrong2.clear ()
    edit_wrong3.clear ()

def add_qw ():
    qw_text = edit_qw.text ()
    ans_text = edit_ans.text ()
    wrong1_text = edit_wrong1.text ()
    wrong2_text = edit_wrong2.text ()
    wrong3_text = edit_wrong3.text ()
    if qw_text != "" and ans_text != "" and wrong1_text != "" and wrong2_text != "" and wrong3_text != "" :

        q = Question (qw_text, ans_text, wrong1_text, wrong2_text, wrong3_text)
        qw_list.append (q)
        clear ()

    else:
        messege_qw = QMessageBox ()
        messege_qw.setText ("text")
        messege_qw.exec ()














def click_ans (rbn):
    global choice_f 
    choice_f = rbn.text ()


new_qw ()
def show_menu ():
    test_win.hide ()
    win_edit.show ()

    stat ()


def show_test():
    test_win.show ()
    win_edit.hide ()

btn_group.buttonClicked.connect(click_ans)
btn_check.clicked.connect(check_ans)
btn_menu.clicked.connect (show_menu)
btn_add_qw.clicked.connect (add_qw)
btn_clear.clicked.connect (clear)

btn_back.clicked.connect (show_test)


test_win.show ()
app.exec ()