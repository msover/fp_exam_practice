from data.Enums import Difficulty
from data.Question import Question
from repo.Quiz import Quiz


class Repo:
    def __init__(self):
        self.quiz = Quiz()
        self.filename = ''

    def read(self):
        self.quiz.wipe()
        if self.filename == '':
            raise FileNotFoundError("No filename provided")
        with open(self.filename, 'r') as file:
            for line in file:
                self.quiz.add(Question.parseLine(line))

    def write(self):
        if self.filename == '':
            raise FileNotFoundError("No filename provided")
        with open(self.filename, 'w') as file:
            for question in self.quiz:
                file.write(Question.makeLine(question))

    def add(self, question: Question):
        self.quiz.add(question)
        self.write()

    def remove(self, question: Question):
        self.quiz.remove(question)
        self.write()

    def setQuiz(self, other: list[Question]):
        self.quiz.questionList = other[:]
        self.write()

    def openFile(self, filename):
        self.filename = filename
        try:
            self.read()
        except FileNotFoundError:
            self.write()
            self.read()