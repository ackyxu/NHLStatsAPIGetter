from ScheduleGame import ScheduleGame


class ScheduleGames:
    def __init__(self, scheduleGamesJSON: dict) -> None:
        self.scheduleGames: list[ScheduleGame] = []
        self.__getScheduleGames(scheduleGamesJSON)
    
    
    def __getScheduleGames(self,scheduleGamesJSON: dict):
        for dates in scheduleGamesJSON["dates"]:
            for gameDict in dates["games"]:
                scheduleGame: ScheduleGame = ScheduleGame(gameDict)
                self.scheduleGames.append(scheduleGame)
                
    def getGameIDList(self) -> list[str]:
        output: list(str) = []
        
        for game in self.scheduleGames:
            output.append(game.gameID)
        
        return output
                