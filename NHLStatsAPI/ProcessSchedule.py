from requests import Response
from .ProcessAPI import ProcessAPI
from .ScheduleGames import ScheduleGames


class ProcessSchedule:
    scheduleURL = r"https://statsapi.web.nhl.com/api/v1/schedule?season=%s&gameType=R"
    def __init__(self) -> None:
        self.scheduleByYear: dict(int,ScheduleGames) = {}

    def getSchedule(self, yearRange: tuple[int, int]):
        if (yearRange[1] < yearRange[0]):
            print("Please check if the range of year is in accending order")
		
        else:
            for year in range(yearRange[0],yearRange[1]+1):
                yearStr:str = f"{year}{year+1}"
                response: Response = ProcessAPI(self.scheduleURL%yearStr)
                
                if (response.getStatusCode() == 200):
                    schedulegames: ScheduleGames = ScheduleGames(response.getJSON())
                    self.scheduleByYear[year] = schedulegames
    
    
    def getGameIDs(self):
        gameIDs = []
        for year, scheduleGames in self.scheduleByYear.items():
            
            tempList = scheduleGames.getGameIDList()
            gameIDs += tempList
            
        return gameIDs
					
                
        