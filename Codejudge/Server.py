# first of all import the socket library
import socket               

# Constant
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