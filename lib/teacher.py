from user import User  # Make sure this import path matches your project

import random
from user import User

class Teacher(User):
    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)
        self.knowledge = ["Math", "Science", "History"]  # Can be anything

    def teach(self):
        return random.choice(self.knowledge)

