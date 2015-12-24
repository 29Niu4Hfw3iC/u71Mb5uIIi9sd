import logging

from contractvmd import dapp, config, proto
from contractvmd.chain import message

logger = logging.getLogger(config.APP_NAME)

class ForumProto:
	"""
	This class stores the dapp code and a list of types of messages that the app can handle 
	"""
	DAPP_CODE = [ 0x01, 0x04 ]
	METHOD_POST = 0x01
	METHOD_POSTCOMMENT = 0x02
	METHOD_POSTPOLL= 0x03
	METHOD_VOTE= 0x04
	METHOD_EDITCOMMENT= 0x05
	METHOD_EDITPOST= 0x06
	METHOD_DELETECOMMENT= 0x07
	METHOD_DELETEPOST= 0x08
	METHOD_DELETEPOLL= 0x09
	METHOD_LIST = [METHOD_POST, METHOD_POSTCOMMENT, METHOD_POSTPOLL, METHOD_VOTE, METHOD_EDITCOMMENT, METHOD_EDITPOST, METHOD_DELETECOMMENT, METHOD_DELETEPOST, METHOD_DELETEPOLL]

class PostMessage (message.Message):
	"""
	This class handles post messages
	"""
	def post (title, content):
		"""
		Creation and inizialitation of a PostMessage
		"""
		m = PostMessage ()
		m.ID=m.Hash
		m.Title = title
		m.Content = content
		m.Comments=[]
		m.DappCode = ForumProto.DAPP_CODE
		m.Method = ForumProto.METHOD_POST
		return m

	def toJSON (self):
		"""
		PostMessage converted to JSON to send the message to the blockchain
		"""
		data = super (PostMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_POST:
			data['id'] = self.ID
			data['title'] = self.Title
			data['content'] = self.Content
			data['comments']= self.Comments
		else:
			return None
		return data

class CommentMessage (message.Message):
	"""
	This class handles comment massages
	"""
	def post (idPost, content):
		"""
		Creation and inizialitation of a CommentMessage
		"""
		mComment = CommentMessage ()
		mComment.ID=mComment.Hash
		mComment.IDPost=idPost
		mComment.Content = content
		mComment.DappCode = ForumProto.DAPP_CODE
		mComment.Method = ForumProto.METHOD_POSTCOMMENT
		return mComment

	def toJSON (self):
		"""
		CommentMessage converted to JSON to send the message to the blockchain
		"""
		data = super (CommentMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_POSTCOMMENT:
			data['id'] = self.ID
			data['idPost'] = self.IDPost
			data['content'] = self.Content
		else:
			return None
		return data

class PollMessage (message.Message):
	"""
	This class handles poll massages 
	"""
	def post (title, answers, deadline, player):
		"""
		Creation and inizialitation of a PollMessage
		"""
		mPoll = PollMessage ()
		mPoll.ID=mPoll.Hash
		mPoll.IDPlayer=player
		mPoll.Title = title
		mPoll.Answers = answers
		mPoll.Deadline = deadline
		mPoll.DappCode = ForumProto.DAPP_CODE
		mPoll.Method = ForumProto.METHOD_POSTPOLL
		return mPoll

	def toJSON (self):
		"""
		PollMessage converted to JSON to send the message to the blockchain
		"""
		data = super (PollMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_POSTPOLL:
			data['id'] = self.ID
			data['title']= self.Title
			data['answers'] = self.Answers
			data['deadline'] = self.Deadline
			
		else:
			return None
		return data

class VoteMessage (message.Message):
	"""
	This class handles vote messages
	"""
	def post (idPoll, choise):
		mVote = VoteMessage ()
		mVote.ID=mVote.Hash
		mVote.IDPoll=idPoll
		mVote.Choise = choise
		mVote.DappCode = ForumProto.DAPP_CODE
		mVote.Method = ForumProto.METHOD_VOTE
		return mVote

	def toJSON (self):
		"""
		VoteMessage converted to JSON to send the message to the blockchain
		"""
		data = super (VoteMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_VOTE:
			data['id'] = self.ID
			data['idPoll'] = self.IDPoll
			data['choise'] = self.Choise
		else:
			return None
		return data

class EditCommentMessage (message.Message):
	"""
	This class handles editcomment messages
	"""
	def post (commid, comment, player):
		mEditComment = EditCommentMessage ()
		mEditComment.ID=commid
		mEditComment.Comment=comment
		mEditComment.Player = player
		mEditComment.DappCode = ForumProto.DAPP_CODE
		mEditComment.Method = ForumProto.METHOD_EDITCOMMENT
		return mEditComment

	def toJSON (self):
		"""
		EditCommentMessage converted to JSON to send the message to the blockchain
		"""
		data = super (EditCommentMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_EDITCOMMENT:
			data['id'] = self.ID
			data['comment'] = self.Comment
			data['player'] = self.Player
		else:
			return None
		return data

class EditPostMessage (message.Message):
	"""
	This class handles editpost messages
	"""
	def post ( postid, title, content, player):
		mEditPost = EditPostMessage ()
		mEditPost.ID=postid
		mEditPost.Title=title
		mEditPost.Content=content
		mEditPost.Player = player
		mEditPost.DappCode = ForumProto.DAPP_CODE
		mEditPost.Method = ForumProto.METHOD_EDITPOST
		return mEditPost

	def toJSON (self):
		"""
		EditPostMessage converted to JSON to send the message to the blockchain
		"""
		data = super (EditPostMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_EDITPOST:
			data['id'] = self.ID
			data['title'] = self.Title
			data['content'] = self.Content
			data['player'] = self.Player
		else:
			return None
		return data

class DeleteCommentMessage (message.Message):
	"""
	This class handles editcomment messages
	"""
	def post (commid, player):
		mDeleteComment = DeleteCommentMessage ()
		mDeleteComment.ID=commid
		mDeleteComment.Player = player
		mDeleteComment.DappCode = ForumProto.DAPP_CODE
		mDeleteComment.Method = ForumProto.METHOD_DELETECOMMENT
		return mDeleteComment

	def toJSON (self):
		"""
		DeleteCommentMessage converted to JSON to send the message to the blockchain
		"""
		data = super (DeleteCommentMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_DELETECOMMENT:
			data['id'] = self.ID
			data['player'] = self.Player
		else:
			return None
		return data
	
class DeletePostMessage (message.Message):
	"""
	This class handles editcomment messages
	"""
	def post (postid, player):
		mDeletePost = DeletePostMessage ()
		mDeletePost.ID=postid
		mDeletePost.Player = player
		mDeletePost.DappCode = ForumProto.DAPP_CODE
		mDeletePost.Method = ForumProto.METHOD_DELETEPOST
		return mDeletePost

	def toJSON (self):
		"""
		DeletePostMessage converted to JSON to send the message to the blockchain
		"""
		data = super (DeletePostMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_DELETEPOST:
			data['id'] = self.ID
			data['player'] = self.Player
		else:
			return None
		return data

class DeletePollMessage (message.Message):
	"""
	This class handles editcomment messages
	"""
	def post (pollid, player):
		mDeletePost = DeletePollMessage ()
		mDeletePost.ID=pollid
		mDeletePost.Player = player
		mDeletePost.DappCode = ForumProto.DAPP_CODE
		mDeletePost.Method = ForumProto.METHOD_DELETEPOLL
		return mDeletePost

	def toJSON (self):
		"""
		DeletePollMessage converted to JSON to send the message to the blockchain
		"""
		data = super (DeletePollMessage, self).toJSON ()

		if self.Method == ForumProto.METHOD_DELETEPOLL:
			data['id'] = self.ID
			data['player'] = self.Player
		else:
			return None
		return data
	
class ForumCore (dapp.Core):
	"""
	CORE CLASSE is used when a message arrives from the blockchain, and store messages on the local DB
	"""

	def __init__ (self, chain, database):
		"""
		This method initializes the database with two lists: posts and polls
		Structure of objects in the lists:

		posts is a list of {id (String), title (String), content (String), comments (List of String), idPlayer (String)}
			All fields are self-explanatory except idPlayer (address of the User who created the Post), this was supposed to be used for Expert Part of the Project

		polls is a list of {id (String), title (String), answers(See below), deadline (float), voters (List of String), idPlayer (String)}
			idPlayer the same as posts
			answers is a List of 3-Tuple such as each tuple has the form (idVotes (List of String), choise (String), votes (Integer))
				idVotes is need to store the id of all votes for that choise
				choise is the option of the poll
				votes is the number of votes a choise took
			voters is the list of all the users that had voted in that poll (checked to avoid multiple votes by a single user) (I don't store the association idVoter-idVote because in testScript this association is never requir)
		"""
		database.init ('posts', [])
		database.init ('polls', [])
		super (ForumCore, self).__init__ (chain, database)

	#########################################################################################
	#Methods for Posts
	def post (self, idPost, title, content, player):
		"""
		Add a post arrived by message from the blockchain to the DB
		"""
		self.database.listappend ('posts', {'id': idPost, 'title': title, 'content': content, 'comments': [], 'idPlayer': player})


	def postComment (self, idComment, idPost, content, player):
		"""
		Add a comment arrived by message from the blockchain to the DB
		"""
		list=self.database.get ('posts')

		#Get each element of the posts list, pick the one with the right id
		for x in list:
			if(x['id']==idPost):
				#Add to the post the new comment
				x['comments'].append({'id' : idComment, 'idPost' : idPost, 'content' : content, 'idPlayer': player})
				#Set again the correct list
				self.database.set('posts', list)
				return
				
	
	def get (self, idPost):
		"""
		Get a post with idPost, if not in DB return None
		"""
		for x in self.database.get ('posts'):
			if(x['id']==idPost):
				return x
		return None


	def getlist (self):
		"""
		Return all the list posts on the db 
		"""
		return self.database.get ('posts')


	#########################################################################################
	#Methods for Polls
	def postPoll (self, idPool, title, answers, deadline, player):
		"""
		Add a poll arrived by message from the blockchain to the DB (Fields description in the __init__ method comment)
		"""
		self.database.listappend ('polls', {'id': idPool, 'title': title, 'answers': answers, 'deadline': deadline, 'voters': [], 'idPlayer': player})


	def vote (self, idVote, idPoll, choise, player):
		"""
		Add the 1 vote to the choise of a Poll
		"""
		#Check if the the User player has already voted the poll
		alreadyVoted=self.addVoter(idPoll, player)
		
		#if User player hasn't voted
		if not alreadyVoted:
			
			list=self.database.get ('polls')
			#Get the right poll
			for poll in list:
				if poll['id']==idPoll:
					for a in poll['answers']:
						#Get the righe choise
						if a[1]==choise:
							t=a
							poll['answers'].remove(a)
							#add the idVote to the choise (that choise has a vote with idVote)
							t[0].append(idVote)

							#add 1 vote to the choise
							t= (t[0], t[1], t[2]+1)

							poll['answers'].append(t)
							#Set the list with the updated vote
							self.database.set('polls', list)
							return
								

	def addVoter(self, idPoll, player):
		"""
		Check if player has already voted, add him if not and return false, return true otherwise
		"""
		list=self.database.get ('polls')
		#Get the right poll
		for poll in list:
			if poll['id']==idPoll:
				for voter in poll['voters']:
					if player==voter:
						#if present return true
						return True

				#If not present, add him to the list and return false
				poll['voters'].append(player)
				self.database.set('polls', list)
				return False

	
	def getPollInfo (self, idPoll):
		"""
		Return the poll with idPoll
		"""
		for x in self.database.get ('polls'):
			if(x['id']==idPoll):
				return x
		return None
	

	def getListPolls (self):
		"""
		Return the list of all polls
		"""
		return self.database.get ('polls')

	#########################################################################################
	#Methods for Expert Part
	def getUserInfo (self, player):
		"""
		Return a 3-TUple (list of post, list of comment, list of poll) for player
		"""
		listPosts=[]
		listComments=[]
		listPolls=[]
		
		for x in self.database.get ('posts'):
			if x['idPlayer']==player :
				listPosts.append(x)
			for comment in x['comments']:
				if comment['idPlayer']==player:
					listComments.append(comment)
				
		for p in self.database.get ('polls'):
			if p['idPlayer']==player:
				listPolls.append(p)

		return (listPosts, listComments, listPolls)
		
	
	def editComment (self, commid, comment, player):
		"""
		Edit a comment if player is the owner of the comment and store the update in the DB
		"""
		l=self.database.get ('posts')	
		
		for post in l:
			for c in post['comments']:
				if c['id']==commid and c['idPlayer']==player:
					c['content']=comment
					self.database.set('posts', l)
					return
	
	def editPost (self, postid, title, content, player):
		"""
		Edit a post if player is the owner of the post and store the update in the DB
		"""
		l=self.database.get ('posts')	
		
		for post in l:
			if post['id']==postid and post['idPlayer']==player:
				post['content']=content
				post['title']=title
				self.database.set('posts', l)
				return
	
	def deleteComment (self, commid, player):
		"""
		Delete a comment if player is the owner of the comment and store the update in the DB
		"""
		l=self.database.get ('posts')	
		
		for post in l:
			for c in post['comments']:
				if c['id']==commid and c['idPlayer']==player:
					post['comments'].remove(c)
					self.database.set('posts', l)
					return
	
	def deletePost (self, postid, player):
		"""
		Delete a post if player is the owner of the post and store the update in the DB
		"""
		l=self.database.get ('posts')	
		
		for post in l:
			if post['id']==postid and post['idPlayer']==player:
				l.remove(post)
				self.database.set('posts', l)
				return
				
				
	def deletePoll (self, pollid, player):
		"""
		Delete a poll if player is the owner of the poll and store the update in the DB
		"""
		l=self.database.get ('polls')	
		
		for poll in l:
			if poll['id']==pollid and poll['idPlayer']==player:
				l.remove(poll)
				self.database.set('polls', l)
				return
		

class ForumAPI (dapp.API):
	"""
	API CLASSE is to receive request from ForumManager
	"""
	def __init__ (self, core, dht, api):
		"""
		Link the calls of ForumManager to methods of API
		"""
		self.api = api
		rpcmethods = {}

		rpcmethods["post"] = {
			"call": self.method_post,
			"help": {"args": ["title", "content"], "return": {}}}

		rpcmethods["postcomment"] = {
			"call": self.method_post_comment,
			"help": {"args": ["idPost", "content"], "return": {}}}

		rpcmethods["get"] = {
			"call": self.method_get,
			"help": {"args": ["id"], "return": {}}}

		rpcmethods["getlist"] = {
			"call": self.method_getlist,
			"help": {"args": [], "return": {}}}

		rpcmethods["postpoll"] = {
			"call": self.method_post_poll,
			"help": {"args": ["title", "answers", "deadline", "player"], "return": {}}}

		rpcmethods["vote"] = {
			"call": self.method_vote,
			"help": {"args": ["idPoll", "choise"], "return": {}}}
		
		rpcmethods["getpollinfo"] = {
			"call": self.method_get_poll_info,
			"help": {"args": ["idPoll"], "return": {}}}

		rpcmethods["listpolls"] = {
			"call": self.method_list_polls,
			"help": {"args": [], "return": {}}}

		rpcmethods["getuserinfo"] = {
			"call": self.method_get_user_info,
			"help": {"args": ["player"], "return": {}}}
		
		rpcmethods["editcomment"] = {
			"call": self.method_edit_comment,
			"help": {"args": ["commid", "comment", "player"], "return": {}}}

		rpcmethods["editpost"] = {
			"call": self.method_edit_post,
			"help": {"args": ["postid", "title", "content","player"], "return": {}}}
		
		rpcmethods["deletecomment"] = {
			"call": self.method_delete_comment,
			"help": {"args": ["commid", "player"], "return": {}}}
		
		rpcmethods["deletepost"] = {
			"call": self.method_delete_post,
			"help": {"args": ["postid", "player"], "return": {}}}
		
		rpcmethods["deletepoll"] = {
			"call": self.method_delete_poll,
			"help": {"args": ["pollid", "player"], "return": {}}}
		
		#Errors returned to ForumManager
		errors = {
			'NO_POST_WITH_THAT_ID': {'code': -2, 'message': 'There is not a post with that ID'},
			'POST_WITH_THAT_ID_ALREADY_EXISTS': {'code': -3, 'message': 'A post with that ID already exists'},
			'NO_POSTS': {'code': -4, 'message': 'No posts in the database'},
			'NO_POST': {'code': -5, 'message': 'No Post with that id in the database'},
			'NO_POLLS': {'code': -6, 'message': 'No polls in the database'},
			'NO_POLL': {'code': -7, 'message': 'No Poll with that id in the database'},
			'ALREADY_VOTED': {'code': -8, 'message': 'You have already voted'},
			'NO_OWNER': {'code': -9, 'message': 'You are not the owner'}}

		super (ForumAPI, self).__init__(core, dht, rpcmethods, errors)


	def method_post (self, title, content):
		"""
		Create a PostMessage and send the transaction
		"""
		msg = PostMessage.post (title, content)	
		return self.createTransactionResponse (msg)


	def method_post_comment (self, idPost, content):
		"""
		Create a CommentMessage and send the transaction if the idPost exists, otherwise return an error
		"""
		if self.core.get (idPost)!=None:
			msg = CommentMessage.post (idPost, content)
			return self.createTransactionResponse (msg)
		else:
			return self.createErrorResponse ('NO_POST_WITH_THAT_ID')


	def method_get (self, idPost):
		"""
		Return a post if the idPost exists, otherwise return an error
		"""
		x=self.core.get (idPost)	
		if x==None:
			return self.createErrorResponse ('NO_POST')
		else:
			return x

	
	def method_getlist (self):
		"""
		Return the list of posts if it is not empty, otherwise return an error
		"""
		l=self.core.getlist ()	
		if len(l)>0:
			return l
		else:
			return self.createErrorResponse ('NO_POSTS')
	
		
	def method_post_poll (self, title, answers, deadline, player):
		"""
		Create a PollMessage and send the transaction (create the right 3-Tuple as specified in comments of __init__ in API)
		"""
		answersData=[]
		for a in answers:
			answersData.append(([],a,0))
		
		msg = PollMessage.post (title, answersData, deadline, player)
		return self.createTransactionResponse (msg)
		
	
	def method_vote (self, idPoll, choise, player):
		"""
		Create a VoteMessage and send the transaction if the idPoll exists, otherwise return an error
		"""
		x=self.core.getPollInfo (idPoll)	
		if x==None:
			return self.createErrorResponse ('NO_POLL')
		
		msg = VoteMessage.post (idPoll, choise)
		return self.createTransactionResponse (msg)


	def method_get_poll_info (self, idPoll):
		"""
		Return the poll with idPoll if exists, otherwise return an error
		"""
		x=self.core.getPollInfo (idPoll)	
		if x==None:
			return self.createErrorResponse ('NO_POLL')
		else:
			return x
			

	def method_list_polls (self):	
		"""
		Return the list of polls if it is not empty, otherwise return an error
		"""
		l=self.core.getListPolls ()	
		if len(l)>0:
			return l
		else:
			return self.createErrorResponse ('NO_POLLS')
		

	def method_get_user_info (self, player):
		"""
		Return the list of all data send by player 
		"""
		l=self.core.getUserInfo(player)	
		return l

	def method_edit_comment (self, commid, comment, player):
		"""
		Create a EditCommentMessage and sent it if the player is the owner of the comment (this check is done again in core when arrive a message)
		"""
		l=self.core.getlist ()	
		
		for post in l:
			for c in post['comments']:
				if c['id']==commid and c['idPlayer']==player:
					msg = EditCommentMessage.post (commid, comment, player)
					return self.createTransactionResponse (msg)
		
			
		return self.createErrorResponse ('NO_OWNER')

	def method_edit_post (self, postid, title, content, player):
		"""
		Create a EditPostMessage and sent it if the player is the owner of the post (this check is done again in core when arrive a message)
		"""
		l=self.core.getlist ()	
		for post in l:
			if post['id']==postid and post['idPlayer']==player:			
				msg = EditPostMessage.post ( postid, title, content, player)
				return self.createTransactionResponse (msg)
		
		return self.createErrorResponse ('NO_OWNER')
	
	def method_delete_comment (self, commid, player):
		"""
		Create a DeleteCommentMessage and sent it if the player is the owner of the comment (this check is done again in core when arrive a message)
		"""
		l=self.core.getlist ()	
		
		for post in l:
			for c in post['comments']:
				if c['id']==commid and c['idPlayer']==player:
					msg = DeleteCommentMessage.post (commid, player)
					return self.createTransactionResponse (msg)
		
		return self.createErrorResponse ('NO_OWNER')
	
	def method_delete_post (self, postid, player):
		"""
		Create a DeletePostMessage and sent it if the player is the owner of the post (this check is done again in core when arrive a message)
		"""
		l=self.core.getlist ()	
		
		for post in l:
			if post['id']==postid and post['idPlayer']==player:
				msg = DeletePostMessage.post (postid, player)
				return self.createTransactionResponse (msg)
		
		return self.createErrorResponse ('NO_OWNER')
	
	
	def method_delete_poll (self, pollid, player):
		"""
		Create a DeletePostPoll and sent it if the player is the owner of the poll (this check is done again in core when arrive a message)
		"""
		l=self.core.getListPolls ()	
		
		for poll in l:
			if poll['id']==pollid and poll['idPlayer']==player:
				msg = DeletePollMessage.post (pollid, player)
				return self.createTransactionResponse (msg)
		
		return self.createErrorResponse ('NO_OWNER')
		

class forumdapp (dapp.Dapp):
	"""
	This class links all the others dapp classes and handles new messages from blockchain
	"""
	def __init__ (self, chain, db, dht, apiMaster):
		self.core = ForumCore (chain, db)
		apiprov = ForumAPI (self.core, dht, apiMaster)
		super (forumdapp, self).__init__(ForumProto.DAPP_CODE, ForumProto.METHOD_LIST, chain, db, dht, apiprov)
	
	
	def handleMessage (self, m):
		"""
		For each type of message, handle it with the right core method (when a message arrive from the blockchain, this class send the message to core to save it on DB)
		"""
		if m.Method == ForumProto.METHOD_POST:
			logger.pluginfo ('Found new post with ID %s e Titolo: %s', m.Hash, m.Data['title'])
			self.core.post (m.Hash, m.Data['title'], m.Data['content'], m.Player)
		elif m.Method == ForumProto.METHOD_POSTCOMMENT:
			logger.pluginfo ('Found new comment for post %s, content: %s', m.Data['idPost'], m.Data['content'] )
			self.core.postComment ( m.Hash, m.Data['idPost'], m.Data['content'], m.Player)
		elif m.Method == ForumProto.METHOD_POSTPOLL:
			logger.pluginfo ('Found new poll %s, title: %s', m.Hash, m.Data['title'])
			self.core.postPoll ( m.Hash, m.Data['title'], m.Data['answers'], m.Data['deadline'],  m.Player )
		elif m.Method == ForumProto.METHOD_VOTE:
			logger.pluginfo ('Found new vote for poll %s, choise: %s by %s', m.Data['idPoll'], m.Data['choise'], m.Player)
			self.core.vote ( m.Hash, m.Data['idPoll'], m.Data['choise'], m.Player)
		elif m.Method == ForumProto.METHOD_EDITCOMMENT:
			logger.pluginfo ('Found new edit for comment %s, new comment: %s', m.Data['id'], m.Data['comment'])
			self.core.editComment (  m.Data['id'], m.Data['comment'], m.Data['player'])
		elif m.Method == ForumProto.METHOD_EDITPOST:
			logger.pluginfo ('Found new edit for post %s, new title: %s', m.Data['id'], m.Data['title'])
			self.core.editPost (  m.Data['id'], m.Data['title'], m.Data['content'], m.Data['player'])
		elif m.Method == ForumProto.METHOD_DELETECOMMENT:
			logger.pluginfo ('Found new delete message for comment %s', m.Data['id'])
			self.core.deleteComment (  m.Data['id'], m.Data['player'])
		elif m.Method == ForumProto.METHOD_DELETEPOST:
			logger.pluginfo ('Found new delete message for post %s', m.Data['id'])
			self.core.deletePost (  m.Data['id'], m.Data['player'])
		elif m.Method == ForumProto.METHOD_DELETEPOLL:
			logger.pluginfo ('Found new delete message for poll %s', m.Data['id'])
			self.core.deletePoll (  m.Data['id'], m.Data['player'])
			
