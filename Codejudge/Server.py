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
		self.conn.execute('''CREATE TABLE USER
			(NAME         TEXT     NOT NULL,
			EMAIL         TEXT     NOT NULL PRIMARY KEY,
			PASSWORD      TEXT     NOT NULL,
			ROLL          TEXT     NOT NULL,
			P1            TEXT     NOT NULL,
			P1_TIME       TEXT     NOT NULL,
			P2            TEXT     NOT NULL,
			P2_TIME       TEXT     NOT NULL,
			P3            TEXT     NOT NULL,
			P3_TIME       TEXT     NOT NULL,
			P4            TEXT     NOT NULL,
			P4_TIME       TEXT     NOT NULL,
			P5            TEXT     NOT NULL,
			P5_TIME       TEXT     NOT NULL,
			P6            TEXT     NOT NULL,
			P6_TIME       TEXT     NOT NULL,
			P7            TEXT     NOT NULL,
			P7_TIME       TEXT     NOT NULL);''')

	def insert(self, name, email, roll):
		password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(8))
		conn.execute('INSERT INTO COMPANY (NAME, EMAIL, PASSWORD, ROLL, P1, P1_TIME, P2, P2_TIME, P3, P3_TIME, P4, P4_TIME, P5, P5_TIME, P6, P6_TIME, P7, P7_TIME) VALUES ( "'+name+'", "'+email+'", "'+password+'", "'+roll+'", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0")');
	def updateScore(seld, email, question_no, test_match, time_now):
		row_problem = self.P[int(question_no)-1]
		row_time = self.P_TIME[int(question_no)-1]
		conn.execute('UPDATE USER set '+row_problem+' = '+test_match+' where EMAIL = '+email)
		conn.execute('UPDATE USER set '+row_time+' = '+time_now+' where EMAIL = '+email)
	def getScore(self, where, condition):
		cursor = conn.execute("SELECT id, name, address, salary from COMPANY")
		for row in cursor:
			for i in range(len(self.column)):
				print(self.column[i]+" = "+ row[i])


d = Database()        
exit();
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
		c.send(b"xaDad1")
	if command[0] == 'submit':
		c.send(b'100')
	if command[0] == 'login':
		c.send(b'True')
	if command[0] == 'get':
		c.send(b'question html page')
	if command[0] == 'status':
		c.send(b'Rank : 1358\nScore : 1350\nTime Left : 3 hr 30min 10s')
	# Close the connection with the client
	c.close()