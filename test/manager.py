from libcontractvm import Wallet, WalletExplorer, ConsensusManager
from forumdapp import ForumManager

class Manager ():
	"""
	This class handles references to ForumManager and Wallet for Users A and B, and can be used to switch from one user to another
	"""
	def ini (consMan):
		"""
		This method create a Manager Object, and initialize its fields  
		
		@type  consMan: ConsensusManager
		@rtype:   	Manager
		"""
		manager = Manager ()
		#Creation of Wallet Objects, One for User A and another one for User B
		manager.walletA=walletA = WalletExplorer.WalletExplorer (wallet_file='testA.wallet')
		manager.walletB=walletB = WalletExplorer.WalletExplorer (wallet_file='testB.wallet')
		
		#Creation of ForumManagers Objects [This allows to switch between two users in test application]
		manager.bsManA=ForumManager.ForumManager (consMan, wallet=manager.walletA)
		manager.bsManB=ForumManager.ForumManager (consMan, wallet=manager.walletB)

		#At start, the actual Manager utilized is the one associated with user A
		manager.actualMan=manager.bsManA
		manager.actualWallet= manager.walletA
		return manager
	
	def changeUser (self):
		"""
		This method allow to switch between two users. To do this change Manager fields actualMan and actualWallet
		"""
		if self.actualMan==self.bsManA:
			self.actualMan=self.bsManB
			self.actualWallet=self.walletB
		else:
			self.actualMan=self.bsManA
			self.actualWallet=self.walletA
	
	def getUser (self):
		"""
		This method return a string representing the current user
		"""
		if self.actualMan==self.bsManA:
			return 'A'
		else:
			return 'B'
