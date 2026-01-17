
class Chore:
    def __init__(self, name, frequency):
        self.name = name
        self.frequency = frequency
        self.completed = False

    def __repr__(self):
        return f"Chore(name={self.name}, frequency={self.frequency}, completed={self.completed})"
        
    def mark_complete(self):
        self.completed = True
