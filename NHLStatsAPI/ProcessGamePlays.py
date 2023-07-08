from .GamePlays import GamePlays
from .ProcessAPI import ProcessAPI
from .ProcessSchedule import ProcessSchedule
from multiprocessing import Pool
import time
import pandas as pd
import os
class ProcessGamePlays:
    gameURL: str = r"https://statsapi.web.nhl.com/api/v1/game/%s/feed/live"
    gamePlaysSeason: dict = {}
    def __init__(self, game_threads = os.cpu_count(), season_threads = os.cpu_count()) -> None:
        self.failedRequest: set(str) = set()
        self.game_threads = game_threads
        self.season_threads = season_threads

    def processGamePlays(self, yearRange: tuple[int,int], multi_games=True, ps=None):
        for year in range(yearRange[0],yearRange[1]+1):
            self.getGamePlaysByYear(year, multi_games = multi_games, ps=ps)

    def getGamePlaysByYear(self,year:int, multi_games: bool = False, ps=None):
            if not ps:
                ps = ProcessSchedule()
                ps.getSchedule((year,year))
            psList = ps.scheduleByYear[year].getGameIDList()
            if multi_games:
                gamePlays = self.getGamePlaysMultiProcess(psList)
            else:
                gamePlays = self.getGamePlays(psList)
            self.gamePlaysSeason[year] = gamePlays
            print(year)
            # self.toCSV(f"./{year}.csv",bs)


    
    def getGamePlaysByID(self, gameID) -> GamePlays or None:
            response: ProcessAPI = ProcessAPI(self.gameURL%str(gameID))
            if (response.getStatusCode() == 200):
                time.sleep(0.005)
                return  (gameID,GamePlays(response.getJSON()))
            else:
                time.sleep(0.005)
                self.failedRequest.add(gameID)
                return None

    def getGamePlaysMultiProcess(self, gameIDs: list[str]) -> dict:
        pool = Pool(self.game_threads)
        results = pool.map(self.getGamePlaysByID,gameIDs)
        gamePlays = {}
        for result in results:
            if result is not None:
                gamePlays[result[0]] = result[1]
        return gamePlays

    def getGamePlays(self, gameIDs: list[str]) -> dict:
        gamePlays = {}
        for gameID in gameIDs:
            result = self.getGamePlaysByID(gameID)
            if result is not None:
                gamePlays[result[0]] = result[1]
        return gamePlays

    def toDataFrame(self):
        gameList = []
        for year,games in self.gamePlaysSeason.items():
            for gameID,events in games.items():
                eventsList = events.toDict()
                gameList += eventsList

        return pd.DataFrame(gameList)