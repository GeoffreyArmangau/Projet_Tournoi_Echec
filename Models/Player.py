class Player:
    def __init__(self, first_name, last_name, date_of_birth, age, identification):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth = date_of_birth
        self.age = age
        self.identification = identification
    
    def Player_Dictionary(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "date_of_birth": self.date_of_birth,
            "age": self.age,
            "identification": self.identification
        }

