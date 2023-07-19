from .ProcessSchedule import ProcessSchedule
from .Boxscore import Boxscore
from .Boxscores import Boxscores
from .ProcessAPI import ProcessAPI
import pandas as pd
from multiprocessing import Pool
import time
import os


class ProcessBoxscore:
    boxscoredDict = {}
    scoresURL: str = r"https://statsapi.web.nhl.com/api/v1/game/%s/boxscore"
    def __init__(self, game_threads = os.cpu_count(), season_threads = os.cpu_count()) -> None:
        self.failedRequest: set(str) = set()
        self.game_threads = game_threads
        self.season_threads = season_threads
    
    def getBoxscores(self, gameIDs: list[str]) -> Boxscores:
        bs: Boxscores = Boxscores()
        for gameID in gameIDs:
            result = self.getBoxscoresByID(gameID)
            if result is not None:
                bs.addBoxscore(result[0], result[1])
            time.sleep(0.005)
        print("good")
        return bs

    def getBoxscoresMultiProcess(self, gameIDs: list[str]) -> Boxscores:
        bs: Boxscores = Boxscores()
        pool = Pool(self.game_threads)
        results = pool.map(self.getBoxscoresByID,gameIDs)
        for result in results:
            if result is not None:
                bs.addBoxscore(result[0], result[1])
        return bs
    
    def getBoxscoresByID(self, gameID) -> Boxscore or None:
            response: ProcessAPI = ProcessAPI(self.scoresURL%str(gameID))
            if (response.getStatusCode() == 200):
                time.sleep(0.005)
                return  (gameID,Boxscore(response.getJSON(), gameID))
            else:
                time.sleep(0.005)
                self.failedRequest.add(gameID)
                return None
            
        
    
    def toDataFrame(self, bs: Boxscores = None, to_dict = False)-> pd.DataFrame:
        dfList = []

        if (bs):
            for id,boxscore in bs.boxscores.items():
                rosterDictA = boxscore.team_away_roster.gameRoster
                rosterDictH = boxscore.team_home_roster.gameRoster


                for id, playerStat in rosterDictA.items():
                    dfList.append(playerStat.__dict__)

                for id, playerStat in rosterDictH.items():
                    dfList.append(playerStat.__dict__)
        else:
            for year,bsr in self.boxscoredDict.items():
                for id,boxscore in bsr.boxscores.items():
                    rosterDictA = boxscore.team_away_roster.gameRoster
                    rosterDictH = boxscore.team_home_roster.gameRoster

                    for id, playerStat in rosterDictA.items():
                        psDict = playerStat.__dict__
                        psDict["year"] = year
                        dfList.append(psDict)

                    for id, playerStat in rosterDictH.items():
                        psDict = playerStat.__dict__
                        psDict["year"] = year
                        dfList.append(psDict)
        
        # df.set_index(["id"], inplace=True)
        numericFeilds = {"assists","goals","shots","hits","faceOffWins","faceOffTaken",
                         "takeaways", "giveaways"}
        emptyValue = {" ",''}
        for line in dfList:
            for key in line:
                if key in numericFeilds:
                    if line[key] not in emptyValue:
                        line[key] = int(line[key])
                    else:
                        line[key] = 0
    

        if to_dict:
            return dfList
        else:
            return pd.DataFrame(dfList)

    def toCSV(self, path, bs)-> None:
        df = self.toDataFrame(bs)
        df.to_csv(path)
    
    def processBoxscores(self, yearRange: tuple[int,int], multi_games=True, ps = None):
        for year in range(yearRange[0],yearRange[1]+1):
            self.getBoxscoresByYear(year, multi_games = multi_games, ps=ps)

    def processBoxscoresMultiProcess(self, yearRange: tuple[int,int]):
        yearList = range(yearRange[0],yearRange[1]+1)
        pool = Pool(self.season_threads)
        pool.map(self.getBoxscoresByYear,yearList)

    def getBoxscoresByYear(self,year:int, multi_games: bool = False, ps=None):
            if not ps:
                ps = ProcessSchedule()
                ps.getSchedule((year,year))
            psList = ps.scheduleByYear[year].getGameIDList()
            if multi_games:
                bs = self.getBoxscoresMultiProcess(psList)
            else:
                bs = self.getBoxscores(psList)
            self.boxscoredDict[year] = bs
            print(year)
            # self.toCSV(f"./{year}.csv",bs)

    def getBoxscoreDictYear(self, year:int):
        return self.boxscoredDict[year]
        