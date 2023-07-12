from NHLStatsAPI.ProcessGamePlays import ProcessGamePlays
import NHLStatsAPI.ProcessDatabase as pdata
from NHLStatsAPI.ProcessSchedule import ProcessSchedule
from NHLStatsAPI.ProcessBoxscores import ProcessBoxscore
from NHLStatsAPI.NHLStatsAPI import NHLStatsAPI
import sys

def main(years):
    # request =  ProcessAPI(r"https://statsapi.web.nhl.com/api/v1/teams/1/roster?season=20162017")
    # response = request.getText()
    # statusCode = request.getStatusCode()
    # print(statusCode)
    interface = NHLStatsAPI()
    interface.updateDatabase(years, backup=False)



if __name__ == "__main__":
    years = list(range(int(sys.argv[1]), int(sys.argv[2]) + 1))
    main(years)