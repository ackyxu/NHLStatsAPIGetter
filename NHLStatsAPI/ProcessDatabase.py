from .ProcessBoxscores import ProcessBoxscore
import sqlite3
from sqlite3 import Error, Connection
import pandas as pd


class ProcessDatabase:
    conn = None
    def ConnectDatabase(self, database: str):
        try:
            self.conn = sqlite3.connect(database+".db")
            print("success")
     
        except Error as e:
            print("failed")
            print(e)


        
    def BoxscoresToDatabase(self, pb: ProcessBoxscore):
        df = pb.toDataFrame()
        if(self.conn):
            df.to_sql("Boxscores", self.conn, if_exists="append",index=False)
        else:
            print("Error: No Database Connected")

    def BoxscoreDropDuplicate(self):
        df = pd.read_sql_query("SELECT * FROM Boxscores", self.conn)
        df = df.drop_duplicates(subset=["gameID","id"])
        df.to_sql("Boxscores", self.conn,if_exists="replace", index=False)




    def __del__(self):
        self.conn.close()

    def CloseConnection(self):
        self.conn.close()
        print("Connection Closed")
        
        