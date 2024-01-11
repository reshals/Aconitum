#logging system/module for python scripts wrote by ~ reshals
#v0.3 PROTOTYPE

import time
import sys

#make sure to create Instances directories and their given log files on host system
#Config
Empty_Queue_Sleep_Time_Sec = 10

#Global Declarations
global Queue
global Queue_Empty
global entry_id
Queue_Empty = True
Queue = []
entry_id = 1


class Logger:
	def __init__(self, Instances=["sys"], data_path = "log"):
		self.data_path = data_path
		self.instances = Instances
	def entry(self, entry, instance, files=["all"]):
		global Queue_Empty
		global Queue
		for file in files:
			time_entry = time.localtime()
			time_entry = f"{time_entry.tm_mday}/{time_entry.tm_mon}/{time_entry.tm_year} | {time_entry.tm_hour}:{time_entry.tm_min}:{time_entry.tm_sec}"
			path = f"{self.data_path}/{instance}/{file}"
			Queue.append(f"{time_entry} <$> {entry}<*;*>{path}")
			Queue_Empty = False
			print(Queue_Empty)

class LogFlasher:
	def __init__(self):
		while(True):
			global Queue_Empty
			global Queue
			global entry_id
			print(Queue_Empty)

			if(Queue_Empty == False):
				while not (Queue_Empty):
					if(len(Queue)>0):
						queue_entry = Queue.pop()
						entry = queue_entry.split("<*;*>")[0]
						path = queue_entry.split("<*;*>")[1]
						with open(path, 'a+') as FileObj:
							FileObj.writelines(f"{entry} : {entry_id}\n")
							entry_id += 1
							print(f"{queue_entry} | WAS FINISHED")
					else:
						Queue_Empty = True
						break
			time.sleep(Empty_Queue_Sleep_Time_Sec)


#debug
if(__name__ == "__main__"):
	import threading
	logflasher_thread = threading.Thread(target=LogFlasher)
	logflasher_thread.start()
	print(sys.argv[1])
	logger = Logger(["sys"], "log")

