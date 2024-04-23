class Team:
    def __init__(self):
        self.members=[]
    
    def addMember(self,name):
        self.members.append(name)
    
    def displayMembers(self):
        for member in self.members:
            print(member)
    
team=Team()
team.addMember("ram")
team.addMember("gopal")
team.displayMembers()