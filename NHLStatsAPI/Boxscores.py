from .Boxscore import Boxscore


class Boxscores:
	def __init__(self) -> None:
		self.boxscores: dict(str,Boxscore) = {}

	def addBoxscore(self,gameID: str, boxscore: Boxscore):
		self.boxscores[gameID] = boxscore