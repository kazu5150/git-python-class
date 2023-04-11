class Account(object):
	"""docstring for Account"""
	def __init__(self, name, balance):
		self.name = name
		self.balance = balance

	def withdraw(self, price):
		self.balance -= price
		self.show_blance()

	def depsit(self, price):
		self.balance += price
		self.show_blance()

	def show_blance(self):
		print(f"{self.name}さんの残高は{self.balance}です。")



kazu = Account("KAZU", 1000000)
kazu.depsit(100000)
