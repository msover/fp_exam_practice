from UI.UI import UI


class GameController:
    def __init__(self):
        self.ui = UI()

    def loop(self):
        while True:
            self.ui.processCommand(input(">"))
            while self.ui.ongoing:
                question = self.ui.service.loadQuestion()
                if question is None:
                    self.ui.ongoing = False
                    break
                print(question)
                command = self.ui.processCommand(input(">"))
                while not self.ui.service.isCorrectAnswer(question, command):
                    print("wrong")
                    command = self.ui.processCommand(input(">"))
                print("right")
            quizScore = self.ui.service.getQuizScore()
            if quizScore:
                print(f"your score is {quizScore}")