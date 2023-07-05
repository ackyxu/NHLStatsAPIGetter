import pandas as pd
class PlayEvent:

    def __init__(self, play: dict):
        self.players: dict = self.retrievePlayers(play)
        self.playType = play["result"]
        self.period = play["about"]["period"]
        self.periodType = play["about"]["periodType"]
        self.periodTime = play["about"]["periodTime"]
        self.coordinates = play["coordinates"]
        try:
            self.teamID = play["team"]["id"]
        except:
            self.teamID = ""

        try:
            self.teamTriCode = play["team"]["triCode"]
        except:
            self.teamTriCode = ""

    def retrievePlayers(self,play):
        output = {}
        
        try:
            players = play["players"]
            for j in players:
                output[j["player"]["id"]] = j["playerType"]
            return output
        except:
            return output

    def toDict(self, sequence, gameID, gameSeason) -> dict:
        eventDict = {
                        "sequence" : sequence,
                        "season": gameSeason,
                        "gameID" : gameID,
                        "teamID": self.teamID,
                        "teamTriCode": self.teamTriCode,
                        "playType": self.playType["eventTypeId"],
                        "playTypeSec": "",
                        "period": self.period,
                        "periodType": self.periodType,
                        "periodTime": self.periodTime,
                        "coorX": "",
                        "coorY": "",
                        
                        "player1" : "",
                        "player1Type" : "",

                        "player2" : "",
                        "player2Type" : "",

                        "player3" : "",
                        "player3Type" : "",

                        "player4" : "",
                        "player4Type" : "",
                    }
        i = 1

        for key,value in self.players.items():
            eventDict["player%d"%i] = key
            eventDict["player%dType"%i] = value
            i+=1

        try:
            eventDict["coorX"] = self.coordinates["x"]
            eventDict["coorY"] = self.coordinates["y"]
        except:
            pass

        try:
            eventDict["playTypeSec"] = self.playType["secondaryType"]
        except:
            pass
         
            

        return eventDict


    def getPlayers(self):
        return self.players
        
        
    