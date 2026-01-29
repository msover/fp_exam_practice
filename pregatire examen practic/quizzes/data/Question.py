from data.Enums import Difficulty


class Question:
    def __init__(self, qid: int, text: str, a: str, b: str, c: str, answer: str, difficulty: Difficulty):
        self._qid = qid
        self._text = text
        self._a = a
        self._b = b
        self._c = c
        self._answer = answer
        self._difficulty = difficulty

    @property
    def qid(self):
        return self._qid

    @qid.setter
    def qid(self, other: int):
        self._qid = other

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, other: str):
        self._text = other

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, other: str):
        self._a = other

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, other: str):
        self._b = other

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, other: str):
        self._c = other

    @property
    def answer(self):
        return self._answer

    @answer.setter
    def answer(self, other: str):
        self._answer = other

    @property
    def difficulty(self):
        return self._difficulty

    @difficulty.setter
    def difficulty(self, other: Difficulty):
        self._difficulty = other

    @classmethod
    def parseLine(cls, line: str):
        try:
            line = line.strip('\n')
            line = line.split(";")
            qid = int(line[0])
            text = line[1]
            a = line[2]
            b = line[3]
            c = line[4]
            answer = line[5]
            difficulty = Difficulty.EASY
            match line[6]:
                case "easy":
                    difficulty = Difficulty.EASY
                case "medium":
                    difficulty = Difficulty.MEDIUM
                case "hard":
                    difficulty = Difficulty.HARD
            return Question(qid, text, a, b, c, answer, difficulty)
        except (ValueError or IndexError):
            raise ValueError("Invalid question format")

    @classmethod
    def makeLine(cls, question):
        return (f'{question.qid};{question.text};{question.a};{question.b};'
                f'{question.c};{question.answer};{question.difficulty.value}\n')

    def __eq__(self, other):
        if not isinstance(other, Question):
            return False
        if self._qid == other._qid:
            return True
        return False

    def __str__(self):
        return f"{self.text} a: {self.a} b: {self.b} c: {self.c}"