from .ProcessGamePlays import ProcessGamePlays
from .ProcessBoxscores import ProcessBoxscore
import sqlite3
from sqlite3 import Error, Connection
import pandas as pd
import shutil
from datetime import date, datetime

class ProcessDatabase:
    conn = None
    playerColumns = ["id","firstname","lastname","positionName","positionType"]
    gamePlaysKeys = ["sequence", "gameID"]
    def ConnectDatabase(self, database: str):
        try:
            self.conn = sqlite3.connect(database+".db")
            print("success")
     
        except Error as e:
            print("failed")
            print(e)


    def GamePlaysToDatabase(self, pgp: ProcessGamePlays):
        df = pgp.toDataFrame()
        if(self.conn):
            df.to_sql("GamePlays", self.conn, if_exists="append",index=False)
        else:
            print("Error: No Database Connected")
        
        
    def BoxscoresToDatabase(self, pb: ProcessBoxscore):
        boxscores = pb.toDataFrame()
        players = boxscores[self.playerColumns]
        players = players.drop_duplicates(subset=self.playerColumns)
        
        boxscores=boxscores.drop(self.playerColumns[1:], axis=1)
        if(self.conn):
            boxscores.to_sql("Boxscores", self.conn, if_exists="append",index=False)
            players.to_sql("Players", self.conn, if_exists="append",index=False)
        else:
            print("Error: No Database Connected")

    def BoxscoreDropDuplicate(self):
        df = pd.read_sql_query("SELECT * FROM Boxscores", self.conn)
        df = df.drop_duplicates(subset=["gameID","id"])
        df.to_sql("Boxscores", self.conn,if_exists="replace", index=False)

    def PlayersDropDuplicate(self):
        df = pd.read_sql_query("SELECT * FROM Players", self.conn)
        df = df.drop_duplicates(subset=self.playerColumns)
        df.to_sql("Players", self.conn,if_exists="replace", index=False)

    def GamePlaysDropDuplicate(self):
        df = pd.read_sql_query("SELECT * FROM GamePlays", self.conn)
        df = df.drop_duplicates(subset=self.gamePlaysKeys)
        df.to_sql("GamePlays", self.conn,if_exists="replace", index=False)

    def queryDatabase(self, sql_query: str):
        self.conn.row_factory = sqlite3.Row
        cur = self.conn.cursor()
        cur.execute(sql_query)
        return cur.fetchall()
        

    def backupDatabase(self, databaseName):
        today = date.today()
        now = datetime.now()
        backupName = "_".join((databaseName,now.strftime("time_%H_%M_%S"),today.strftime("date_%m_%d_%Y")))
        shutil.copyfile(databaseName+".db", backupName+".db")

    def __del__(self):
        self.CloseConnection()

    def CloseConnection(self):
        self.conn.close()
        print("Connection Closed")
        
        