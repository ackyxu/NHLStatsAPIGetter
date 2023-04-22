from Team import Team


class Teams:
	
	def __init__(self, teamsJSON: any) -> None:
		self.teams = []
		for teamJSON in teamsJSON["teams"]:
			team = Team(teamJSON)
			self.teams.append(team)
   
