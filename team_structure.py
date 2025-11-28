class Employee:
    def __init__(self, name : str, position: str, salary: int):
        self.name = name
        self.position = position
        self.salary = salary

    def info(self):
        return f"Name: {self.name}, Position: {self.position}, Salary: {self.salary}" 
       
    def bonus(self, increase_percent):
        self.salary += self.salary * (increase_percent / 100)
    
    
class Manager(Employee):
    def __init__(self, name: str, position: str, salary: int, team: list):
        super().__init__(name, position, salary)
        self.team = team

    def bonus(self, increase_percent):
        team_bonus = 1000 * len(self.team)
        self.salary += self.salary * (increase_percent / 100) + team_bonus
        

    def add_team_member(self, member):
        self.team.append(member)
        return f"Added team member from employee: {member}"
    
    def hierarchy_info(self):
        hierarchy = { self.name : [member.name for member in self.team] }
        return hierarchy