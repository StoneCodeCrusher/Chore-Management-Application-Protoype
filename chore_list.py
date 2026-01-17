from chore import Chore
from chore_schedule import Chore_Schedule

class ChoreList:
    def __init__(self):
        self.chores = []
        
    def add_chore(self, name, frequency):
        schedule = Chore_Schedule(frequency)
        chore = Chore(name,schedule)
        self.chores.append(Chore(name,schedule))
        
    ##returns chores array
    def get_all(self):
        return self.chores
     
    def get_filtered(self, frequency = None):
        if frequency is None:
            return self.chores
        return [chore for chore in self.chores 
                if chore.chore_schedule.frequency == frequency]
        

    def is_valid_name(self,name):
        cleaned = name.replace(" ", "")
        return bool(cleaned) and cleaned.isalnum()
        
    def mark_chore_complete(self, name):
        for chore in self.chores:
            if chore.name == name:
                chore.mark_complete()
                return True
                break
        return False
        
    def remove_chore(self, chore):
        if chore in self.chores:
            self.chores.remove(chore)

        