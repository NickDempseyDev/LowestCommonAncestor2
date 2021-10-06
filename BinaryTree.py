class BinaryTree:
	
	def __init__(self, fileName):
		self.root = None
		self.createTree(fileName)

	def __init__(self, arr):
		self.root = None
		self.createTree(arr)

	def put(self, node, number):
		if(node == None):
			self.root = Node(number)
			return
		
		if(number < node.key):
			if node.left == None:
				node.left = Node(number)
				return
			else:
				self.put(node.left, number)

		if(number > node.key):
			if node.right == None:
				node.right = Node(number)
				return
			else:
				self.put(node.right, number)
		return

	def createTree(self, fileName):
		file = open(fileName, "r")
		numbers = file.read().splitlines()
		for i in numbers:
			self.put(self.root, int(i))
		file.close()

	def createTree(self, arr):
		for i in arr:
			self.put(self.root, i)
	
	def print(self):
		print(self.printTree(self.root, ""))

	def printTree(self, node, prefix):
		if node == None:
			return prefix + "-None\n"	
		return prefix + "-" + str(node.key) + "\n" + self.printTree(node.right, prefix + " |") + self.printTree(node.left, prefix + "  ")

	def printTreeOneLine(self):
		if self.root == None:
			return "()"
		return "(" + self.printTreeOneLineRecur(self.root) + ""

	def printTreeOneLineRecur(self,node):
		if node == None:
			return ""
		tempStr = "(" + self.printTreeOneLineRecur(node.left) + ")"
		tempStr += str(node.key)
		tempStr += "(" + self.printTreeOneLineRecur(node.right) + ")"

		return tempStr
		

class Node:
    # Constructor to create a new binary node
    def __init__(self, key):
        self.key =  key
        self.left = None
        self.right = None