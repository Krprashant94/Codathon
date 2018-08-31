import socket
import json
import sys
import os

PORT = 63

class Client:
	"""Client Class"""
	def __init__(self, ip=None, port=63):
		self.ip = ip
		self.port = port
		if ip !=None:
			self.server = socket.socket()
			self.server.connect((ip, port))
		self.login = False
		self.email = '0'
		self.name = '0'
		self.roll = '0'

	def __del__(self):
		try:
			self.server.close()
		except:
			pass
			

	def register(self, email, name, roll):
		self.email = email
		self.name = name
		self.roll = roll
		self.server.sendall(json.dumps(["register", email, name, roll]).encode())
		self.password = self.server.recv(1024)
		print("Your Password is : "+self.password.decode("utf-8"))

	def userLogin(self, user, password):
		self.server.sendall(json.dumps(["login", user, password]).encode())
		response = self.server.recv(1024)
		if response.decode("utf-8") == "True":
			self.login = True

	def get(self):
		os.system("start http://localhost:"+str(PORT))

	def submitAnswer(self, email, password, problem_no, filename):
		file = open(filename, 'r') 
		solution = file.read()
		file.close()
		lang = filename.split('.')[-1]
		self.server.sendall(json.dumps(["submit", email, password, problem_no, solution, lang, filename]).encode())
		print(self.server.recv(1024).decode("utf-8"))

	def status(self, email, password):
		self.server.sendall(json.dumps(["status", email, password]).encode())
		print(self.server.recv(1024).decode("utf-8"))

	def compile(self, ques, filename):
		"""Not in use"""
		file = open(filename, 'r')
		solution = file.read()
		file.close()
		lang = filename.split('.')[-1]
		self.server.sendall(json.dumps(["compile", ques, lang, solution]).encode())
		response = self.server.recv(1024)
		print(response.decode("utf-8"))

	def reset(self):
		self.server.sendall(json.dumps(["reset"]).encode())

if len(sys.argv) <=1:
	exit()

if sys.argv[1] == 'help':
	print("------------------------------------------------------")
	print("---------------Codathon 2018--------------------------")
	print("--------------Command Helper--------------------------")
	print("------------------------------------------------------")
	print("codathon register email name roll   [return password]")
	print("codathon submit email password problem_no solution_file ")
	print("codathon login user password")
	print("codathon get [return all problem] or localhost:"+str(PORT)+" in browser")
	print("codathon status email password [return your status]")
	print("------------------------------------------------------")
	print("solution_file must have extansion .py, .c, .cpp or .java")
	print("Java programmer must write the packege name as user.mail_id[till @].q[qustion_no]")
	print("Java programmer must use class name starting with capital latter only")
	print("C++ programmer must use int main() with return 0")
	print("------------------------------------------------------")
elif sys.argv[1] == 'register':
	if len(sys.argv) != 5:
		print('Wrong Command type "codathon.py help" to get help.')
		exit()
	c = Client("127.0.0.1", PORT)
	c.register(sys.argv[2], sys.argv[3], sys.argv[4])

elif sys.argv[1] == 'submit':
	if len(sys.argv) != 6:
		print('Wrong Command type "codathon.py help" to get help.')
		exit()
	c = Client("127.0.0.1", PORT)
	c.submitAnswer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])

elif sys.argv[1] == 'login':
	if len(sys.argv) != 4:
		print('Wrong Command type "codathon.py help" to get help.')
		exit()
	c = Client("127.0.0.1", PORT)
	c.userLogin(sys.argv[2], sys.argv[3])

elif sys.argv[1] == 'get':
	if len(sys.argv) != 2:
		print('Wrong Command type "codathon.py help" to get help.')
		exit()
	c = Client()
	c.get()

elif sys.argv[1] == 'status':
	if len(sys.argv) != 4:
		print('Wrong Command type "codathon.py help" to get help.')
		exit()
	c = Client("127.0.0.1", PORT)
	c.status(sys.argv[2], sys.argv[3])
elif sys.argv[1] == 'reset':
	c = Client("127.0.0.1", PORT)
	c.reset()