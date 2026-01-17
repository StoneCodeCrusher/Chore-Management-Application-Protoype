from datetime import datetime

class Chore:
    def __init__(self, name, schedule):
        self.name = name
        self.chore_schedule = schedule
        self.completed = False
        self.created_on = datetime.now()
        self.completed_on = None

    def __repr__(self):
        return f"Chore(name={self.name}, frequency={self.frequency}, completed={self.completed})"
        
    def mark_complete(self):
        self.completed = True
        self.completed_on = datetime.now()
    
    def mark_incomplete(self):
        self.completed = False
        self.completed_on = None
    
    def toggle_complete(self):
        if self.completed:
            self.mark_incomplete()
        else:
            self.mark_complete()