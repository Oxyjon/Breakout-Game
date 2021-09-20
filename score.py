from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.ht()
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(300, 270)
        self.write(f'Score: {self.score}', align='center', font=('Courier', 15, 'bold'))

    def add_point(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f'Game Over', align='center', font=('Courier', 20, 'bold'))