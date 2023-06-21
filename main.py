from NHLStatsAPI.ProcessTeams import ProcessTeams
from NHLStatsAPI.Team import Team
from NHLStatsAPI.Teams import Teams


def main():
    # request =  ProcessAPI(r"https://statsapi.web.nhl.com/api/v1/teams/1/roster?season=20162017")
    # response = request.getText()
    # statusCode = request.getStatusCode()
    # print(statusCode)

	pt = ProcessTeams()
	pt.requestTeams((2017,2017))
	teams: Teams = pt.teamsDict[2017]
	for team in teams:
		team: Team = team
		print(team.__dict__)
    



if __name__ == "__main__":
    
	main()