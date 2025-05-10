""" 
Define a class team with instance object variable a list of team member names provide methods to input member names and display member names

"""
import numpy as np
class Team:
    def __init__(self):
        self.__members=np.array([])
        
    def addMembers(self,name):
        self.__members=np.append(self.__members,name)
    
    def displayMembers(self):
        return self.__members
    

team=Team()

team.addMembers("ramesh")
team.addMembers("ram")
print(team.displayMembers())
    