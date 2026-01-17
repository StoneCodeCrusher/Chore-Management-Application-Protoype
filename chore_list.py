from chore import Chore

class ChoreList:
    def __init__(self):
        self.chores = []
        
    def add_chore(self, name, frequency):
        chore = Chore(name, frequency)
        self.chores.append(chore)
        
    def get_all(self):
        return self.chores
     
    def get_by_frequency(self, frequency):
        return [chore for chore in self.chores if chore.frequency == frequency]

    def mark_chore_complete(self, name):
        for chore in self.chores:
            if chore.name == name:
                chore.mark_complete()
                break
        