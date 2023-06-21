from .Boxscore import Boxscore
from .Boxscores import Boxscores
from .ProcessAPI import ProcessAPI
import pandas as pd
import time


class ProcessBoxscore:
    scoresURL: str = r"https://statsapi.web.nhl.com/api/v1/game/%s/boxscore"
    def __init__(self) -> None:
        self.boxscores: Boxscores() = Boxscores()
        self.failedRequest: set(str) = set()
    
    def getBoxscores(self, gameIDs: list[str]):
        
        for gameID in gameIDs:
            response: ProcessAPI = ProcessAPI(self.scoresURL%str(gameID))
            if (response.getStatusCode() == 200):
                boxscore: Boxscore = Boxscore(response.getJSON(), gameID)
                self.boxscores.addBoxscore(gameID, boxscore)
            else:
                self.failedRequest.add(gameID)
            time.sleep(0.005)
    
    def toDataFrame(self)-> pd.DataFrame:
        dfList = []
        for id,boxscore in self.boxscores.boxscores.items():
            rosterDictA = boxscore.team_away_roster.gameRoster
            rosterDictH = boxscore.team_home_roster.gameRoster


            for id, playerStat in rosterDictA.items():
                dfList.append(playerStat.__dict__)

            for id, playerStat in rosterDictH.items():
                dfList.append(playerStat.__dict__)

        df = pd.DataFrame(dfList)
        # df.set_index(["id"], inplace=True)
        return df

    def toCSV(self, path)-> None:
        df = self.toDataFrame()
        df.to_csv(path)
        