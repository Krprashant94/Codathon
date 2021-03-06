import socket
import json
import sys
import os
import time

PORT = 63
if os.path.isfile('ip'):
	f=open('ip', 'r')
	IP = f.read()
	f.close()
else:
	f=open('ip', 'w')
	IP = input('Enter Server IP Address : ')
	f.write(IP)
	f.close()

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
		self.password = self.password.decode("utf-8")
		if self.password != 'Fail':
			print("Your Password is : "+self.password)
		else:
			print("Already Register !!!")

	def userLogin(self, user, password):
		self.server.sendall(json.dumps(["login", user, password]).encode())
		response = self.server.recv(1024)
		if response.decode("utf-8") == "True":
			self.login = True

	def get(self):
		os.system("start http://"+IP+":"+str(PORT))

	def submitAnswer(self, email, password, problem_no, filename):
		file = open(filename, 'r') 
		solution = file.read()
		file.close()
		lang = filename.split('.')[-1]
		self.server.sendall(json.dumps(["submit", email, password, problem_no, solution, lang, filename]).encode())
		print(self.server.recv(1024).decode("utf-8"))


	def status(self, email, password):
		self.server.sendall(json.dumps(["status", email, password]).encode())
		res = eval(self.server.recv(1024).decode("utf-8"))
		h = open('./score/index.html', 'r')
		html = h.read()

		html = html.replace("{{name}}", res[0])
		html = html.replace("{{score1}}", res[4])
		html = html.replace("{{time1}}", res[5])
		html = html.replace("{{score2}}", res[6])
		html = html.replace("{{time2}}", res[7])
		html = html.replace("{{score3}}", res[8])
		html = html.replace("{{time3}}", res[9])
		html = html.replace("{{score4}}", res[10])
		html = html.replace("{{time4}}", res[11])
		html = html.replace("{{score5}}", res[12])
		html = html.replace("{{time5}}", res[13])
		html = html.replace("{{score6}}", res[14])
		html = html.replace("{{time6}}", res[15])
		html = html.replace("{{score7}}", res[16])
		html = html.replace("{{time7}}", res[17])
		
		html = html.replace("{{time_score1}}", str(0.2*float(res[5])))
		html = html.replace("{{total1}}", str(float(res[4]) + 0.2*float(res[5])))
		html = html.replace("{{time_score2}}", str(0.2*float(res[7])))
		html = html.replace("{{total2}}", str(float(res[6]) + 0.2*float(res[7])))
		html = html.replace("{{time_score3}}", str(0.4*float(res[9])))
		html = html.replace("{{total3}}", str(float(res[8]) + 0.4*float(res[9])))
		html = html.replace("{{time_score4}}", str(0.4*float(res[11])))
		html = html.replace("{{total4}}", str(float(res[10]) + 0.4*float(res[11])))
		html = html.replace("{{time_score5}}", str(0.4*float(res[13])))
		html = html.replace("{{total5}}", str(float(res[12]) + 0.4*float(res[13])))
		html = html.replace("{{time_score6}}", str(0.6*float(res[15])))
		html = html.replace("{{total6}}", str(float(res[14]) + 0.6*float(res[15])))
		html = html.replace("{{time_score7}}", str(0.6*float(res[17])))
		html = html.replace("{{total7}}", str(float(res[16]) + 0.6*float(res[17])))

		html = html.replace("{{all_total}}", str(float(res[4]) + 0.2*float(res[5]) + float(res[6]) + 0.2*float(res[7]) + float(res[8]) + 0.4*float(res[9]) + float(res[10]) + 0.4*float(res[11]) + float(res[12]) + 0.4*float(res[13]) + float(res[14]) + 0.6*float(res[15]) + float(res[16]) + 0.6*float(res[17])))

		h.close()
		h = open('./score/scorebord.html', 'w')
		h.write(html)
		h.close()
		os.system("start ./score/scorebord.html")

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
	c = Client(IP, PORT)
	c.register(sys.argv[2], sys.argv[3], sys.argv[4])

elif sys.argv[1] == 'submit':
	if len(sys.argv) != 6:
		print('Wrong Command type "codathon.py help" to get help.')
		exit()
	c = Client(IP, PORT)
	c.submitAnswer(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
	del c
	time.sleep(2)
	c = Client(IP, PORT)
	c.status(sys.argv[2], sys.argv[3])

elif sys.argv[1] == 'login':
	if len(sys.argv) != 4:
		print('Wrong Command type "codathon.py help" to get help.')
		exit()
	c = Client(IP, PORT)
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
	c = Client(IP, PORT)
	c.status(sys.argv[2], sys.argv[3])

elif sys.argv[1] == 'reset':
	c = Client(IP, PORT)
	c.reset()