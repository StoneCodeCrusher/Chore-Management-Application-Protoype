class Chore_Schedule:
    valid_references = {"Daily", "Weekly", "Monthly", "Yearly"}
    
    def __init__(self, frequency):
        if frequency not in self.valid_references:
            raise ValueError(f"Invalid schedule: {frequency}")
        self.frequency = frequency
       
    def __str__(self):
        return self.frequency