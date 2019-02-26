class School():
    
    def __init__(self, name=None, roster = {}):
        self.name = name
        self.roster = roster
        
    def add_student(self, student, grade):
        if not grade in self.roster:             #check if grade-key exists in dic
            self.roster[grade] = []
        self.roster[grade].append(student)
        
    def grade(self, grade):
        if not grade in self.roster:
            return "No students in that grade."
        return self.roster[grade]
    
    def sort_roster(self):
        for key in self.roster.keys():
            self.roster[key].sort()
        return self.roster