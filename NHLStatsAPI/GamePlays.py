from .PlayEvent import PlayEvent

class GamePlays:

    def __init__(self, gameDict):
        self.gameID = gameDict["gamePk"]
        self.playEvents: list(PlayEvent) = self.retrievePlayEvents(gameDict["liveData"]["plays"]["allPlays"])
        self.homeTeam = gameDict["gameData"]["teams"]["home"]["id"]
        self.awayTeam = gameDict["gameData"]["teams"]["away"]["id"]
        self.gameType = gameDict["gameData"]["game"]["type"]
        self.gameSeason = gameDict["gameData"]["game"]["season"]

    def retrievePlayEvents(self, plays: list[dict]):
        playEvents = []
        for play in plays:
            playEvent = PlayEvent(play)
            playEvents.append(playEvent)
        return playEvents
        
        