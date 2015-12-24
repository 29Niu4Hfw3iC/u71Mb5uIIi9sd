import time
from libcontractvm import Wallet, ConsensusManager, DappManager

class ForumManager (DappManager.DappManager):
	"""
	This class handles calls from Test Scripts and redirects them to ForumDapp API
	"""
	def __init__ (self, consensusManager, wallet = None):
		super (ForumManager, self).__init__(consensusManager, wallet)

	"""
	Methods to call API methods on POSTS
	"""
	def createPost (self, title, content):
		return self.produceTransaction ('forumdapp.post', [title, content])

	def commentPost (self, idPost, content):
		return  self.produceTransaction ('forumdapp.postcomment', [idPost, content])

	def getPostInfo (self, idPost):
		return self.consensusManager.jsonConsensusCall ('forumdapp.get', [idPost])['result']


	"""
	Methods to call API methods on POLLS
	"""
	def listPost (self):
		return self.consensusManager.jsonConsensusCall ('forumdapp.getlist', [])['result']

	def createPoll (self, title, answers, deadline, player):
		return self.produceTransaction ('forumdapp.postpoll', [title, answers, deadline, player])

	def getPollInfo (self, idPoll):
		return self.consensusManager.jsonConsensusCall ('forumdapp.getpollinfo', [idPoll])['result']
		
	def listPolls (self):
		return self.consensusManager.jsonConsensusCall ('forumdapp.listpolls', [])['result']

	def vote (self, idPoll, choise, player):
		return self.produceTransaction ('forumdapp.vote', [idPoll, choise, player])
	

	"""
	Methods for expert part
	"""
	def getUserInfo (self, player):
		return self.consensusManager.jsonConsensusCall ('forumdapp.getuserinfo', [player])['result']

	def editComment (self, commid, comment, player):
		return self.produceTransaction ('forumdapp.editcomment', [commid, comment, player])

	def editPost(self, postid, title, content, player):
		return self.produceTransaction ('forumdapp.editpost', [postid, title, content, player])
	
	def deletComment(self, commid, player):
		return self.produceTransaction ('forumdapp.deletecomment', [commid, player])
	
	def deletPost(self, postid, player):
		return self.produceTransaction ('forumdapp.deletepost', [postid, player])
	
	def deletPoll(self, pollid, player):
		return self.produceTransaction ('forumdapp.deletepoll', [pollid, player])

	
	
		