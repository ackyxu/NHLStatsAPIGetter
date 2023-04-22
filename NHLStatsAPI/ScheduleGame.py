class ScheduleGame:
    
    def __init__(self, gameDict: dict) -> None:
        self.gameID = gameDict["gamePk"]
        self.gameDate = gameDict["gameDate"]