from PyQt5.QtWidgets import (QWidget, QLabel, QPushButton, QRadioButton, QSpinBox,
                             
                            QGroupBox, QButtonGroup, QVBoxLayout, QHBoxLayout)
test_win = QWidget ()
test_win.resize (600, 500)
test_win.move (200, 200)
test_win.setWindowTitle ("Memori Card")
test_win.show ()

btn_menu = QPushButton ("Menu") 
btn_rest = QPushButton ("Pest")
btn_time = QSpinBox ()
lbl_rest = QLabel ("Minuts")

lbl_ques = QLabel ("???")

box_qw = QGroupBox ()
box_qw.setTitle ("ans")
btn_group = QButtonGroup ()
rbt_list = list()
for i in range (4):
    rbt = QRadioButton ()
    btn_group.addButton (rbt)
    rbt_list.append (rbt)

btn_check = QPushButton ("Check")

main_line = QVBoxLayout ()
line_h1 = QHBoxLayout ()
line_h2 = QHBoxLayout ()
line_h3 = QHBoxLayout ()
line_h4 = QHBoxLayout ()

line_h1.addWidget (btn_menu)
line_h1.addWidget (btn_rest)
line_h1.addWidget (btn_time)
line_h1.addWidget (lbl_rest)

line_h2.addWidget (lbl_ques)

line_h3.addWidget (box_qw)
line_h5 = QHBoxLayout ()
line_v1 = QVBoxLayout ()
line_v2 = QVBoxLayout ()
line_v1.addWidget (rbt_list[0])
line_v1.addWidget (rbt_list[1])
line_v2.addWidget (rbt_list[2])
line_v2.addWidget (rbt_list[3])
line_h5.addLayout (line_v1)
line_h5.addLayout (line_v2)
box_qw.setLayout (line_h5)

line_h4.addWidget (btn_check)
main_line.addLayout (line_h1)
main_line.addLayout (line_h2)
main_line.addLayout (line_h3)
main_line.addLayout (line_h4)

box_ans = QGroupBox ()
box_ans.setTitle ("Answer")
lbl_rezult = QLabel ()
lbl_rght_ans = QLabel ()
line_v3 = QVBoxLayout ()
line_v3.addWidget (lbl_rght_ans)
line_v3.addWidget (lbl_rezult)
box_ans.setLayout (line_v3)
line_h3.addWidget (box_ans)
box_ans.hide ()




test_win.setLayout (main_line)

