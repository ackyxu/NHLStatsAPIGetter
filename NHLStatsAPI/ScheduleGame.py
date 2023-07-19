class ScheduleGame:
    
    def __init__(self, gameDict: dict) -> None:
        self.gameID = gameDict["gamePk"]
        self.gameDate = gameDict["gameDate"]
        self.homeTeamID = gameDict["teams"]["home"]["team"]["id"]
        self.awayTeamID = gameDict["teams"]["away"]["team"]["id"]