#logging system/module for python scripts wrote by ~ reshals
#v0.1 PROTOTYPE

import time
#make sure to create Instances directories and their given log files
class Logger:
	def __init__(self, Data_Path, Instances=["sys"]):
		self.data_path = Data_Path
		self.instances = Instances
	def entry(self, entry, instance, files=["all"]):
		for file in files:
			with open(f"{self.data_path}/{instance}/{file}", "w+") as fileObj:
				time_entry = time.localtime()
				time_entry = f"{time_entry.tm_mday}/{time_entry.tm_mon}/{time_entry.tm_year} | {time_entry.tm_hour}:{time_entry.tm_min}:{time_entry.tm_sec}"
				fileObj.writelines(f"{time_entry} <$> {entry}\n")