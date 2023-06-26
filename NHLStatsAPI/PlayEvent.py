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
            self.teamID = {}

    def retrievePlayers(self,play):
        output = {}
        
        try:
            players = play["players"]
            for j in players:
                output[j["player"]["id"]] = j["playerType"]
            return output
        except:
            return output

        


    def getPlayers(self):
        return self.players
        
        
    