from data.Enums import Difficulty
from data.Question import Question
from service.Service import Service


class UI:
    def __init__(self):
        self.ongoing = False
        self.service = Service()

    def processCommand(self, command: str) -> None | str:
        command = command.split(' ')
        if not self.ongoing:
            match command[0]:
                case "add":
                    try:
                        questionString = ''
                        for string in command[1:]:
                            questionString += string
                            questionString += ' '
                        questionString = questionString[:-1]
                        question = Question.parseLine(questionString)
                    except (ValueError, IndexError) as e:
                        print(e)
                        return None
                    try:
                        self.service.addQuestion(question)
                    except ValueError as e:
                        print(e)
                case "create":
                    try:
                        difficulty = command[1]
                        if difficulty == "easy":
                            difficulty = Difficulty.EASY
                        elif difficulty == "medium":
                            difficulty = Difficulty.MEDIUM
                        elif difficulty == "hard":
                            difficulty = Difficulty.HARD
                        else:
                            raise ValueError("invalid input")
                        numberOfQuestions = int(command[2])
                        filename = command[3]
                    except (ValueError , IndexError) as e:
                        print(e)
                        return None
                    self.service.newQuiz(difficulty, numberOfQuestions, filename)
                case "start":
                    try:
                        self.service.openFile(command[1])
                        self.ongoing = True
                    except (ValueError , IndexError) as e:
                        print(e)
                        return None
                case _:
                    print("invalid input")
                    return None
        else:
            return command[0]

