#CarInventory.py

from CarInventoryNode import *
class CarInventory():
    def __init__(self):
        self.root = None # A BST just needs a reference to the root node
        self.size = 0 # Keeps track of number of nodes

    def addCar(self, car):
        if self.root:
            self._put(car, self.root)
        else:
            self.root = CarInventoryNode(car)

	# helper method to recursively walk down the tree
    def _put(self,car,currentNode):
        tempCarNode = CarInventoryNode(car)
        if tempCarNode == currentNode:
            currentNode.cars.append(car)
        else: 
            if tempCarNode < currentNode:
                if currentNode.getLeft():
                    self._put(car,currentNode.left)
                else:
                    currentNode.left = \
                    CarInventoryNode(car)
                    currentNode.left.parent = currentNode
            else:
                if currentNode.getRight():
                    self._put(car,currentNode.right)
                else:
                    currentNode.right = \
                    CarInventoryNode(car)
                    currentNode.right.parent = currentNode

    def doesCarExist(self, car):
        if self.root:
            res = self._get(car,self.root)
            if res:
                for i in res.cars:
                    if car == i:
                        return True
                return False
            else:
                return False
        else:
            return False

	# helper method to recursively walk down the tree
    def _get(self,car,currentNode): 
        tempCarNode = CarInventoryNode(car)
        if not currentNode:
            return None
        elif currentNode == tempCarNode:
            return currentNode
        elif tempCarNode < currentNode:
            return self._get(car,currentNode.left)
        else:
            return self._get(car,currentNode.right)


    def _inOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += str(self._inOrder(currentNode.getLeft()))
            ret += str(currentNode)
            ret += str(self._inOrder(currentNode.getRight()))
        return ret
    
    def _preOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += str(currentNode)
            ret += str(self._preOrder(currentNode.getLeft()))
            ret += str(self._preOrder(currentNode.getRight()))
        return ret

    def _postOrder(self, currentNode):
        ret = ""
        if currentNode:
            ret += str(self._postOrder(currentNode.getLeft()))
            ret += str(self._postOrder(currentNode.getRight()))
            ret += str(currentNode)
        return ret

    def inOrder(self):
        return self._inOrder(self.root)
        
    def preOrder(self):
        return self._preOrder(self.root)
        
    def postOrder(self):
        return self._postOrder(self.root)

    def getBestCar(self, make, model):
        tempcar = Car(make, model, 0, 0)
        tempCarNode = CarInventoryNode(tempcar)
        currentNode = self.root
        found = self._get(tempCarNode, self.root)
        if found:
            best_car = found.cars[0]
            for i in found.cars:
                if i > best_car:
                    best_car = i
                    return best_car
        return found
            

    def getWorstCar(self, make, model):
        tempcar = Car(make, model, 0, 0)
        tempCarNode = CarInventoryNode(tempcar)
        currentNode = self.root
        found = self._get(tempCarNode, self.root)
        if found:
            worst_car = found.cars[0]
            for i in found.cars:
                if i < worst_car:
                    worst_car = i
            return worst_car
        return found

    def _getTotalInventoryPrice(self, currentNode):
        price = 0
        if currentNode:
            price += self._getTotalInventoryPrice(currentNode.getLeft())
            price += self._getTotalInventoryPrice(currentNode.getRight())
            for car in currentNode.cars:
                price += car.price
        return price

    def getTotalInventoryPrice(self):
        return self._getTotalInventoryPrice(self.root)

        
        


