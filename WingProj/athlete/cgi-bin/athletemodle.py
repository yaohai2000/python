import pickle

from AthleteList import AthleteList
from AthleteList import get_coach_data

def put_to_store(files_list):
    all_athlete={}
    for file in files_list:
        athlete = get_coach_data(file)
        all_athlete[athlete.name]=athlete
    try:
        with open("athlete_data","wb") as store:
            pickle.dump(all_athlete,store)
    except IOError as err:
        print("IO Error: " + str(err))
    print(all_athlete)
    return all_athlete
    
def get_from_store():
    try:
        with open("athlete_data","rb") as store:
            all_athletes=pickle.load(store)
        print(all_athletes)
        return all_athletes
    except IOError as err:
        print("Load Error: " + str(err))

#put_to_store(["data/sarah2.txt","data/james2.txt","data/mikey2.txt","data/julie2.txt"])
get_from_store()