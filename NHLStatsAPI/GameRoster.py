from Player import Player


class GameRoster:
    """
    Create a class that contains the roster for a single team 

    @params:
    gameRosterDict: a dictionary that contains all players for a team in a game, from Boxscores
    rosterID: RI + gameID for the game + a: away/ h:home, given from parent call
    """
    def __init__(self, gameRosterDict: dict, rosterID: str, gameID: int) -> None:
        self.id = rosterID
        self.gameRoster: dict = {}
        self.__getRoster(gameRosterDict, gameID)


    def __getRoster(self,gameRosterDict: dict, gameID: int):
        for playerID, playerDict in gameRosterDict.items():
            player: Player = Player(playerDict, gameID)
            trueID = player.id
            self.gameRoster[trueID] = player