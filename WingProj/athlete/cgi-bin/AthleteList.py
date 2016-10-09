class AthleteList(list):
    def __init__(self,a_name,a_dob=None,a_times=[]):
        list.__init__([])
        self.name=a_name
        self.dob=a_dob
        self.extend(a_times)
    def top3(self):
        return sorted(set([sanitize(m) for m in self]))[0:3]
    

def sanitize(time_string):
    if("-") in time_string:
        splitter = "-"
    elif(":") in time_string:
        splitter = ":"
    else:
        return (time_string)
    (mins,secs)=time_string.strip().split(splitter)
    return mins + "." + secs

def get_coach_data(filename):
    try:
        with open(filename) as data:
            content = data.readline().strip().split(",")
            athlete=AthleteList(content.pop(0),content.pop(0),content)
            return athlete
    except IOError as err:
        print("An Error Occurs: " + str(err))

            
           
            
            
        
        
    
        