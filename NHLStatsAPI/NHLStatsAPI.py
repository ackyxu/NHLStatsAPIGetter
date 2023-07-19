from .ProcessTeams import ProcessTeams
from .ProcessGamePlays import ProcessGamePlays
from .ProcessDatabase import ProcessDatabase
from .ProcessSchedule import ProcessSchedule
from .ProcessBoxscores import ProcessBoxscore
import os

class NHLStatsAPI:

    def __init__(self, databaseName: str = "database"):
        self.database = ProcessDatabase()
        self.databaseName = databaseName

    def updateDatabase(self, years: int | list[int],backup = True):
        pb = ProcessBoxscore()
        ps = ProcessSchedule()
        pgp = ProcessGamePlays()
        pt = ProcessTeams()

        if backup and os.path.exists(self.databaseName+".db"):
            self.database.backupDatabase(self.databaseName)

                    
        if type(years) == int:
            yearRange = (years,years)
        elif type(years) == list:
            yearRange = (years[0], years[-1])
            
        
        ps.getSchedule(yearRange)
        pt.requestTeams(yearRange)

        pb.processBoxscores(yearRange, ps=ps)
        pgp.processGamePlays(yearRange, ps=ps)

        
        self.database.ConnectDatabase(self.databaseName)
        self.updateScheduleDatabase(ps, connect=False)
        self.updateTeamsDatabase(pt, connect=False)
        self.database.BoxscoresToDatabase(pb)
        self.database.GamePlaysToDatabase(pgp)


    def updateScheduleDatabase(self, ps: ProcessSchedule, connect=True):
        if connect:
            self.database.ConnectDatabase(self.databaseName)
        self.database.ScheduleToDatabase(ps)

    def updateTeamsDatabase(self, pt: ProcessTeams, connect=True):
        if connect:
            self.database.ConnectDatabase(self.databaseName)
        self.database.TeamsToDatabase(pt)

    def maintainDatabase(self):
        self.database.ConnectDatabase(self.databaseName)
        self.database.PlayersDropDuplicate()
        self.database.BoxscoreDropDuplicate()
        self.database.GamePlaysDropDuplicate()
        self.database.ScheduleDropDuplicate()

    def performQuery(self, sql_query: str):
        self.database.ConnectDatabase(self.databaseName)

        return self.database.queryDatabase(sql_query)