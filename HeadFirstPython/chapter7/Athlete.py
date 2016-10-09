class AthleteList(list):
	def __init__(self,filename,added_times=[]):
		list.__init__([])
		self.filename=filename
		dataList=self.get_coach_data(self.filename)
		self.name=dataList.pop(0)
		self.dob=dataList.pop(0)
		self.extend(dataList)
		self.extend(added_times)
	def sanitize(self,time_string):
		if "-" in time_string:
			splitter="-"
		elif ":" in time_string:
			splitter=":"
		else:
			return time_string
		(mins,secs)=time_string.split(splitter)
		return mins+"."+secs
	def top3(self):
		return sorted(set([self.sanitize(m) for m in self]))[0:3]
	def get_coach_data(self,filename):
		content=[]
		with open(self.filename) as data:
			content=data.readline().strip().split(",")
		return content

sarah=AthleteList("sarah2.txt")
james=AthleteList("james2.txt")
print(sarah.name + "'s fastest times" + str(sarah.top3()))
print(james.name + "'s fastest times" + str(james.top3()))
