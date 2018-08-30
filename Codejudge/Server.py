import os
import sqlite3
import random
import string
import socket

class Database:
	"""docstring for Database"""

	def __init__(self, ):
		self.P = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
		self.P_TIME = ['P1_TIME', 'P2_TIME', 'P3_TIME', 'P4_TIME', 'P5_TIME', 'P6_TIME', 'P7_TIME']
		self.column = ['NAME', 'EMAIL', 'PASSWORD', 'ROLL', 'P1', 'P1_TIME', 'P2', 'P2_TIME', 'P3', 'P3_TIME', 'P4', 'P4_TIME', 'P5', 'P5_TIME', 'P6', 'P6_TIME', 'P7', 'P7_TIME']
		self.conn = sqlite3.connect('user.db')

	def __del__(self):
		self.conn.close()

	def insert(self, email, name, roll):
		password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
		try:
			self.conn.execute('INSERT INTO USER (NAME, EMAIL, PASSWORD, ROLL, P1, P1_TIME, P2, P2_TIME, P3, P3_TIME, P4, P4_TIME, P5, P5_TIME, P6, P6_TIME, P7, P7_TIME) VALUES ( "'+name+'", "'+email+'", "'+password+'", "'+roll+'", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0")')
			self.conn.commit()
			return password
		except:
			return "Fail"

	def updateScore(self, email, question_no, test_match, time_now):
		row_problem = self.P[int(question_no)-1]
		row_time = self.P_TIME[int(question_no)-1]
		self.conn.execute('UPDATE USER set '+row_problem+' = "'+test_match+'" where EMAIL = "'+email+'"')
		self.conn.execute('UPDATE USER set '+row_time+' = "'+time_now+'" where EMAIL = "'+email+'"')
		self.conn.commit()

	def getScore(self, auth, where='1', condition='1'):
		cursor = self.conn.execute('SELECT * from USER WHERE PASSWORD = "'+auth+'" AND '+where+' = "'+condition+'"' )
		for row in cursor:
			for i in range(len(self.column)):
				print(self.column[i]+" = "+ row[i])



class compiler:
	"""docstring for compiler"""
	def __init__(self, lang):
		super(compiler, self).__init__()
		if lang == 'c':
			self.batch_file_name = 'c_batch_file.bat'
		elif lang == 'cpp':
			self.batch_file_name = 'cpp_batch_file.bat'
		elif lang == 'java':
			self.batch_file_name = 'java_batch_file.bat'
		elif lang == 'py':
			self.batch_file_name = 'py_batch_file.bat'
		self.error = False
		self.error_text = "None"
		self.compile_percentage = 0
	def compile(self, filename):
		data = exec(self.batch_file_name)
		# process the data
		self.error = true?false
		self.error_text = 'None'?Text
		return self.compile_percentage

	def getLastError(self):
		return self.error_text


		
d = Database()
d.updateScore('kr.prashsant94@gmail.com', '1', '35.5', '35105')
d.getScore('6DW7DF8U', 'EMAIL','kr.prashsant94@gmail.com')

# Constant
START_TIME_STAMP = 0
MAX_SUBMIT_SIZE = 2048 + 50 #50 byte for header data
port = 12345

# next create a socket object
s = socket.socket()         
print ("Server successfully created")

 
s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)     
print ("socket is listening")

# a forever loop until we interrupt it or 
# an error occurs
while True:
	# Establish connection with client.
	# send a thank you message to the client.

	c, addr = s.accept()
	command = eval(c.recv(MAX_SUBMIT_SIZE).decode("utf-8"))
	print ('Recived : '+ str(addr)+" --> "+str(command[0]))
	if command[0] == 'register':
		password = d.insert(command[1], command[2], command[3])
		if not os.path.exists("user/"+command[1]):
			os.makedirs("user/"+command[1])
		c.send(password.encode())
	if command[0] == 'submit':
		if not os.path.exists("user/"+command[1]+"/"+command[-3]):
			os.makedirs("user/"+command[1]+"/"+command[-3])
		h = open("user/"+command[1]+"/"+command[-3]+"/abc."+command[-1], 'w')
		h.write(command[-2])
		h.close()
		# @return (float) : % match with real Test cases
		compiler = Compiler(lang)
		score = compiler.compile("user/"+command[1]+"/"+command[-3]+"/abc."+command[-1], 'w')
		lastError = compiler.getLastError()
		c.send(b'100')
	if command[0] == 'login':
		c.send(b'True')
	if command[0] == 'get':
		c.send(b'question html page')
	if command[0] == 'status':
		c.send(b'Rank : 1358\nScore : 1350\nTime Left : 3 hr 30min 10s')
	if command[0] == 'compile':
		c.send(b'98.55')
	# Close the connection with the client
	c.close()