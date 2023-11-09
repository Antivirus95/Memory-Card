class Question: 
    def __init__(self, qw, ans, wrong_1, wrong_2, wrong_3):
        self.qw = qw 
        self.ans = ans
        self.wrong_1 = wrong_1
        self.wrong_2 = wrong_2
        self.wrong_3 = wrong_3
        self.count = 0
        self.count_right = 0
    def ans_right (self):
        self.count += 1
        self.count_right += 1
    def ans_wrong (self):
        self.count +=1

qw1 = Question ("Кого зів лев", "тебе", "рибу", "свекруху", "картоплю")
qw2 = Question ("Да", "Yes", "Не", "дА", "Мможе")
qw_list = [qw1, qw2] 
