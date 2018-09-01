import threading
from subprocess import Popen, PIPE, STDOUT
import os
import sqlite3
import random
import string
import socket
import subprocess as sub
import threading
import time

class TLE(threading.Thread):
	def __init__(self, cmd, problam_num, timeout, email):
		threading.Thread.__init__(self)
		self.cmd = cmd
		self.timeout = timeout
		self.problam_num = problam_num
		self.email = email

	def run(self):
		h1 = open('problam/'+str(self.problam_num)+'/input', 'r')
		h2 = open('problam/'+str(self.problam_num)+'/output', 'r')

		inputs = h1.read()
		outputs = h2.read()
		h1.close()
		h2.close()

		self.p = sub.Popen(self.cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout_data = self.p.communicate(input=(inputs).encode())[0]
		self.p.wait()

		a = outputs.split('\n')
		b = stdout_data.decode('utf-8').strip().split('\r\n')

		allCount = len(a)
		matchCount = [i == j for i, j in zip(a, b)].count(True)
		match_case = 100*matchCount/allCount

		timeScore = str(int(START_TIME_STAMP - int(time.time()))) if match_case != 0 else '0'

		db = Database()
		db.updateScore(self.email, self.problam_num, str(match_case), timeScore)


	def Run(self):
		self.start()
		self.join(self.timeout)

		if self.is_alive():
			self.p.terminate()      #use self.p.kill() if process needs a kill -9
			self.join()

class Database:
	"""docstring for Database"""

	def __init__(self, ):
		self.P = ['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7']
		self.P_TIME = ['P1_TIME', 'P2_TIME', 'P3_TIME', 'P4_TIME', 'P5_TIME', 'P6_TIME', 'P7_TIME']
		self.column = ['NAME', 'EMAIL', 'PASSWORD', 'ROLL', 'P1', 'P1_TIME', 'P2', 'P2_TIME', 'P3', 'P3_TIME', 'P4', 'P4_TIME', 'P5', 'P5_TIME', 'P6', 'P6_TIME', 'P7', 'P7_TIME', 'TLE', 'SIZE']
		self.conn = sqlite3.connect('user.db')

	def __del__(self):
		self.conn.close()

	def insert(self, email, name, roll):
		password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(10))
		try:
			self.conn.execute('INSERT INTO USER (NAME, EMAIL, PASSWORD, ROLL, P1, P1_TIME, P2, P2_TIME, P3, P3_TIME, P4, P4_TIME, P5, P5_TIME, P6, P6_TIME, P7, P7_TIME, TLE, SIZE) VALUES ( "'+name+'", "'+email+'", "'+password+'", "'+roll+'", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0")')
			self.conn.commit()
			return password
		except:
			return "Fail"
	def login(self, username, password):
		try:
			cursor = self.conn.execute('SELECT * from USER WHERE EMAIL = "'+username+'" AND PASSWORD = "'+password+'"' )
			row = cursor.fetchone()
			if row is None:
				return False
			return True
		except Exception as e:
			print(e)
			return False
	def updateScore(self, email, question_no, test_match, time_now):
		row_problem = self.P[int(question_no)-1]
		row_time = self.P_TIME[int(question_no)-1]
		self.conn.execute('UPDATE USER set '+row_problem+' = "'+test_match+'" where EMAIL = "'+email+'"')
		self.conn.execute('UPDATE USER set '+row_time+' = "'+time_now+'" where EMAIL = "'+email+'"')
		self.conn.commit()

	def getScore(self, where='1', condition='1'):
		cursor = self.conn.execute('SELECT * from USER WHERE '+where+' = "'+condition+'"' )
		l = []
		for row in cursor:
			for i in range(len(self.column)):
				l.append(row[i])
		return l


class Compiler:
	# ""docstring for compiler""
	def __init__(self, lang, email):
		self.language = lang

		self.compile_error = False
		self.error_text = "None"
		self.compile_percentage = 0
		self.email = email

	def compile(self, filename, problam_num):
		if self.language == "c":
			return self.__compile_c(filename, problam_num)
		elif self.language == "cpp":
			return self.__compile_cpp(filename, problam_num)
		elif self.language == "java":
			return self.__compile_java(filename, problam_num)
		elif self.language == "py":
			return self.__compile_python(filename, problam_num)

	def __compile_c(self, filename, problam_num):
		try:
			compile_error = os.system('gcc "'+ filename + '" -o "'+ filename.split(".")[0] +'"')
			if compile_error == 1:
				self.compile_error = True
				self.error_text = "Unable to compile"
				return
			
			# Run
			a = TLE('"'+ filename.split(".")[0] +'.exe"', problam_num, 2, self.email).Run()
			return 'Submitted'

		except Exception as e:
			return "Execution Error..."
		
	def __compile_cpp(self, filename, problam_num):
		try:
			compile_error = os.system('g++ "'+ filename + '" -o "'+ filename.split(".")[0] +'"')
			if compile_error == 1:
				self.compile_error = True
				self.error_text = "Unable to compile"
				return
			
			# Run 
			a = TLE('"' + filename.split(".")[0] + '.exe"', problam_num, 2, self.email).Run()
			return 'Submitted'

		except Exception as e:
			return "Execution Error..."

	def __compile_java(self, filename, problam_num):
		try:
			compile_error = os.system('javac "'+ filename+'"')
			if compile_error == 1:
				self.compile_error = True
				self.error_text = "Unable to compile"
				return
			
			# Run 
			a = TLE('java "'+filename.split(".")[0]+'"', problam_num, 2, self.email).Run()
			return 'Submitted'

		except Exception as e:
			return "Execution Error..."


	def __compile_python(self, filename, problam_num):		
		try:
			a = TLE('python "'+filename+'"', problam_num, 2, self.email).Run()
			return 'Submitted'
		except Exception as e:
		 	return "Execution Error..."


	def getLastError(self):
		if self.compile_error:
			return self.error_text
		else:
			return False

def executer(command, c):
	lang_comp = Compiler(command[5], command[1])
	score = lang_comp.compile(file_path+'/'+command[6], command[3])
	lastError = lang_comp.getLastError()
	if lastError == False:
		c.sendall(str(score).encode())
	else:
		c.sendall(str(lastError).encode())

d = Database()
# XMCDK30WBJ
# kr.prashsant94@gmail.com
# print(d.getScore('EMAIL', 'a@a'))

# Constant
START_TIME_STAMP = 1535803758 + 7200 #int(time.time())
MAX_SUBMIT_SIZE = 2048 + 50 #50 byte for header data
port = 63

# next create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)         
print ("Server successfully created. AT : "+str(START_TIME_STAMP))

 
s.bind(('', port))
print ("socket binded to %s" %(port))

# put the socket into listening mode
s.listen(5)     
print ("socket is listening")

# a forever loop until we interrupt it or 
# an error occurs
while True:
	try:
		# Establish connection with client.
		# send a thank you message to the client.

		c, addr = s.accept()
		try:
			command = eval(c.recv(MAX_SUBMIT_SIZE).decode("utf-8"))
			print ('Recived : '+ str(addr)+" --> "+str(command[0]))
			if command[0] == 'register':
				password = d.insert(command[1], command[2], command[3])
				dir_location = "user/"+command[1].split('@')[0]
				dir_location = dir_location.replace('.', '') 
				if not os.path.exists(dir_location):
					os.makedirs(dir_location)
				c.send(password.encode())

			elif command[0] == 'reset':
				print("Server Closed...")
				break

			elif command[0] == 'submit':
				if d.login(command[1], command[2]):
					file_path = "user/"+command[1].split('@')[0]+"/q"+command[3]
					file_path = file_path.replace('.', '')
					if not os.path.exists(file_path):
						os.makedirs(file_path)
					h = open(file_path+"/"+command[6], 'w')
					h.write(command[4])
					h.close()
					
					try:
						t1 = threading.Thread(target=executer, args=(command, c ))
						t1.start()
						t1.join()
					except Exception as e:
						print(e)
				else:
					c.sendall(b'Invalid Login')

			elif command[0] == 'status':
				if d.login(command[1], command[2]):
					status = d.getScore('EMAIL',command[1])
					c.sendall(str(status).encode())
				else:
					c.sendall(b'Invalid Login')

			elif command[0] == 'compile':
				c.sendall(b'Invalid...')

		except:
			filename = 'static/index.html'
			f = open(filename, 'r')
			c.sendall(str.encode("HTTP/1.0 200 OK\n",'iso-8859-1'))
			c.sendall(str.encode('Content-Type: text/html\n', 'iso-8859-1'))
			c.send(str.encode('\r\n'))
			# send data per line
			for l in f.readlines():
				# print('Sent ', repr(l))
				c.sendall(str.encode(""+l+"", 'iso-8859-1'))
			l = f.read(1024)
			f.close()

		# Close the connection with the client
		c.close()
	except Exception as e:
		print(e)
		print("Crashed...")