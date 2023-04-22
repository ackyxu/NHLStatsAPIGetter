class Player:
    def __init__(self, playerDict: dict, gameID: int) -> None:
        self.gameID = gameID
        self.firstname = ""
        self.lastname = ""
        self.id = None
        self.positionName = playerDict["position"]["name"]
        self.positionType = playerDict["position"]["type"]
        self.assists = ""
        self.goals = ""
        self.shots = ""
        self.hits = ""
        self.faceOffWins = ""
        self.faceOffTaken = ""
        self.takeaways = ""
        self.giveaways = ""
        self.evenTimeOnIce = ""
        self.powerPlayTimeOnIce = ""
        self.shortHandedTimeOnIce = ""
        self.__getPlayerStats(playerDict)
        self.__getPlayerInfo(playerDict)

    def __getPlayerInfo(self,  playerDict: dict):
        try:
            playerDict["person"]
        except Exception:
            return 
        
        try:
            self.firstname = playerDict["person"]["firstName"]
        except Exception:
            pass

        try:
            self.lastname = playerDict["person"]["lastName"]
        except Exception:
            pass

        try:
           self.id = playerDict["person"]["id"]
        except Exception:
            pass
        

    def __getPlayerStats(self, playerDict: dict):
        try:
            playerDict["stats"]["skaterStats"]
        except Exception:
            return 


        try:
            self.assists = playerDict["stats"]["skaterStats"]["assists"]
        except Exception:
            pass

        try:
            self.goals = playerDict["stats"]["skaterStats"]["goals"]
        except Exception:
            pass

        try:
            self.shots = playerDict["stats"]["skaterStats"]["shots"]
        except Exception:
            pass

        try:
            self.hits = playerDict["stats"]["skaterStats"]["hits"]
        except Exception:
            pass
        
        try:
            self.faceOffWins = playerDict["stats"]["skaterStats"]["faceOffWins"]
        except Exception:
            pass

        try:
            self.faceOffTaken = playerDict["stats"]["skaterStats"]["faceoffTaken"]
        except Exception:
            pass

        try:
            self.takeaways = playerDict["stats"]["skaterStats"]["takeaways"]
        except Exception:
            pass

        try:
            self.giveaways = playerDict["stats"]["skaterStats"]["giveaways"]
        except Exception:
            pass

        try:
            self.evenTimeOnIce = playerDict["stats"]["skaterStats"]["evenTimeOnIce"]
        except Exception:
            pass

        try:
            self.powerPlayTimeOnIce = playerDict["stats"]["skaterStats"]["powerPlayTimeOnIce"]
        except Exception:
            pass

        try:
            self.shortHandedTimeOnIce = playerDict["stats"]["skaterStats"]["shortHandedTimeOnIce"]
        except Exception:
            pass
        
        