from requests import Response
from .ProcessAPI import ProcessAPI
from .ScheduleGames import ScheduleGames
from multiprocessing import Pool, Lock, Manager
from pandas import DataFrame
import os

def init_pool_processes(the_lock):
    '''Initialize each process with a global variable lock.
    '''
    global lock
    lock = the_lock


class ProcessSchedule:
    scheduleURL = r"https://statsapi.web.nhl.com/api/v1/schedule?season=%s&gameType=R"
    def __init__(self,game_threads = os.cpu_count(), season_threads = os.cpu_count()) -> None:
        self.scheduleByYear: dict(int,ScheduleGames) = {}
        self.game_threads = game_threads
        self.season_threads = season_threads
     

    def getSchedule(self, yearRange: tuple[int, int], multi_thread=True):
        if (yearRange[1] < yearRange[0]):
            print("Please check if the range of year is in accending order")
		
        else:
            if multi_thread:
                self.scheduleByYear = Manager().dict()
                lock = Lock()
                pool = Pool(self.season_threads,initializer=init_pool_processes,initargs=(lock,))
                years = [year for year in range(yearRange[0],yearRange[1]+1)]
                pool.map(self.getScheduleRequest,years)
                # pool.close()
                # pool.join()
            else:
                for year in range(yearRange[0],yearRange[1]+1):
                    print("here")
                    self.getScheduleRequest(year, multi_thread=False)

    def getScheduleRequest(self, year:int, multi_thread = True):
            yearStr:str = f"{year}{year+1}"
            response: Response = ProcessAPI(self.scheduleURL%yearStr)

            if (response.getStatusCode() == 200):
                schedulegames: ScheduleGames = ScheduleGames(response.getJSON())
                if multi_thread:
                    lock.acquire()
                    self.scheduleByYear[year] = schedulegames
                    lock.release()
                else:
                    self.scheduleByYear[year] = schedulegames
                    
        
    def getGameIDs(self):
        gameIDs = []
        for year, scheduleGames in self.scheduleByYear.items():
            
            tempList = scheduleGames.getGameIDList()
            gameIDs += tempList
            
        return gameIDs

    def toDataFrame(self, to_dict = False):
        sgDictList = []
        for year in self.scheduleByYear:
            sgs = self.scheduleByYear[year]
            for sg in sgs.scheduleGames:
                season = str(year)+str(year+1)
                sgDict = vars(sg)
                sgDict["season"] = season
                sgDictList.append(sgDict)

        sgDictList = sorted(sgDictList,key= lambda d: d["gameID"])
        if to_dict:
            return sgDictList
        else:
            return DataFrame(sgDictList)
                        
                
        