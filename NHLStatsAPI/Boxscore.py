from .GameRoster import GameRoster


class Boxscore:
    def __init__(self, dictBS: dict, gameID: int) -> None:
        self.gameRoster = {}
        self.team_away_id = dictBS["teams"]["away"]["team"]["id"]
        self.team_away_roster = GameRoster(dictBS["teams"]["away"]["players"],"RI"+str(gameID)+"a",gameID,self.team_away_id)
        self.team_home_id = dictBS["teams"]["home"]["team"]["id"]
        self.team_home_roster = GameRoster(dictBS["teams"]["home"]["players"],"RI"+str(gameID)+"h",gameID,self.team_home_id)