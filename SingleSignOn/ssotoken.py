import random


class SSOToken():
    def __init__(self):
        self.id = random.randrange(100000)

    def __eq__(self, o):
        return self.id == o.id

    def __repr__(self):
        return str(self.id)
