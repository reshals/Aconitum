#logging system/module for python scripts wrote by ~ reshals
#v0.2 PROTOTYPE

import time
#make sure to create Instances directories and their given log files

global Queue
Queue = []

class Logger:
	def __init__(self, Instances=["sys"], data_path = "log"):
		self.data_path = data_path
		self.instances = Instances
	def entry(self, entry, instance, files=["all"]):
		for file in files:
			#with open(f"{self.data_path}/{instance}/{file}", "w+") as fileObj:
			time_entry = time.localtime()
			time_entry = f"{time_entry.tm_mday}/{time_entry.tm_mon}/{time_entry.tm_year} | {time_entry.tm_hour}:{time_entry.tm_min}:{time_entry.tm_sec}"
			path = f"{self.data_path}/{instance}/{file}"
			Queue.append(f"{time_entry} <$> {entry};{path}")

class LogFlasher:
	def __init__(self):
		while(True):
			if(len(Queue)>0):
				queue_entry = Queue.pop()
				entry = queue_entry.split(";")[0]
				path = queue_entry.split(";")[1]
				with open(path, 'a+') as FileObj:
					FileObj.writelines(f"{entry}\n")
					print(f"{queue_entry} | WAS FINISHED")
			else:
				break
