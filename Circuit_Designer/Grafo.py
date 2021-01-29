class Grafo:
	def __init__(self):
		self.NodeList=[]

	def getNodoList(self):
		return self.NodeList

	def getNodo(self,nombre):
		for nodo in self.NodeList:
			if (nodo.Name == nombre):
				return nodo.getDic

	def getGeneralDic(self):
		newDic = {}
		for Node in self.NodeList:
			newDic[Node.getName] = Node.getConnections
		return newDic

	def setNodo(self,node):
		self.NodeList.append

	def generate(self,Dic):
		List = []
		for key in Dic:
			newNode = Nodo(key)
			for keys in Dic[key]:
				newNode.setConnections(keys,Dic[key][keys])
			List.append(newNode)
			




class Nodo:
	def __init__(self,Name):
		self.Name = Name
		self.Conecction = {}

	def getName(self):
		return self.Name

	def setConnections(self,name,peso):
		self.Conecction.update({name:peso})

	def getConnection(self):
		newDic = self.Conecction
		return newDic

