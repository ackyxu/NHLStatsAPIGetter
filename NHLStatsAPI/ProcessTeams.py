from requests import Response
from .ProcessAPI import ProcessAPI
from .Teams import Teams
import pandas as pd

class ProcessTeams: 

	teamURL: str = "https://statsapi.web.nhl.com/api/v1/teams"
	filterSeasons: str = "?season="

 
	def __init__(self) -> None:
		self.teamsDict: dict = {}
    
	def requestTeams(self, yearRange: tuple[int,int]):

		if (yearRange[1] < yearRange[0]):
			print("Please check if the range of year is in accending order")
		
		else:
			for year in range(yearRange[0],yearRange[1]+1):
				yearStr:str = f"{year}{year+1}"
				reqURL: str = self.teamURL + self.filterSeasons + yearStr
				response: Response = ProcessAPI(reqURL)
				if (response.getStatusCode() == 200):
					teams: Teams = Teams(response.getJSON())
					self.teamsDict[year] = teams.teams

	def toDataFrame(self, to_dcit = False):
		teams = []
		for year in self.teamsDict:
			for team in self.teamsDict[year]:
				teams.append(vars(team))
		if to_dcit:
			return teams
		else:
			df = (pd.DataFrame(teams)).drop_duplicates(subset=["id", 'abbrv'])
			return df
        
     
					


