#CarInventoryNode.py

from Car import *
class CarInventoryNode():
    def __init__(self, car):
        self.cars = [car]
        self.make = car.make.upper()
        self.model = car.model.upper()
        self.left = None
        self.right = None
        self.parent = None
        
    def getMake(self):
        return self.make
        
    def getModel(self):
        return self.model
        
    def getParent(self):
        return self.parent

    def setParent(self, parent):
        self.parent = parent
            
    def getLeft(self):
        return self.left

    def setLeft(self, left):
        self.left = left

    def getRight(self):
        return self.right

    def setRight(self, right):
        self.right = right
    
    def __gt__(self, rhs):
        if self.make > rhs.make:
            return True
        if self.make < rhs.make:
            return False       
        if self.make == rhs.make:
            if self.model > rhs.model:
                return True
            if self.model < rhs.model:
                return False     
            if self.model == rhs.model:
                return False
    
    def __lt__(self, rhs):
        if self.make < rhs.make:
            return True
        if self.make > rhs.make:
            return False       
        if self.make == rhs.make:
            if self.model < rhs.model:
                return True
            if self.model > rhs.model:
                return False     
            if self.model == rhs.model:
                return False

    def __eq__(self, rhs):
        if (self.make == rhs.make) and (self.model == rhs.model):
            return True

            
    def __str__(self):
        result = ""
        for car in self.cars:
            result += str(car) + "\n"
        return result
