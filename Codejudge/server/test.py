import subprocess as sub
import threading
from subprocess import PIPE, STDOUT
class RunCmd(threading.Thread):
	def __init__(self, cmd, timeout):
		threading.Thread.__init__(self)
		self.cmd = cmd
		self.timeout = timeout

	def run(self):
		self.p = sub.Popen(self.cmd, stdin=PIPE, stdout=PIPE, stderr=PIPE)
		stdout_data = self.p.communicate(input=("1").encode())[0]
		self.p.wait()
		print(stdout_data)

	def Run(self):
		self.start()
		self.join(self.timeout)

		if self.is_alive():
			self.p.terminate()      #use self.p.kill() if process needs a kill -9
			self.join()

RunCmd(["a", ""], 5).Run()