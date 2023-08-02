# NHL Stats API Getter

Pull results from NHL's Stats RestAPI and store them into a SQLite3 Database. Uses Python's `multiprocess.Pool` to run concurrent API calls to speed up the process of calling multiple Games/Players/Season's stats. 

Documentations for the RestAPI's ends points can be found [here](https://gitlab.com/dword4/nhlapi).


## Dependencies and Requirements

External Libraries Needed:

- pandas: Used to format and clean retrieve data before storing them into a SQLite3 Database

## Usage

In a command line temrinal, call `python main.py aaaa bbbb` in the root directoy of the project, where `aaaa` represents the start year and `bbbb` represent the end year of data you wish to retrieve form the API.

Note that for the 2022-2023 seasons, you will use 2022 as the year to represent the season.  Currently if the year is invalid, the program will crash due to 404 error when retrieving the data (to be fixed).

Saves a SQLite3 database called `database.db` in the root directory of the project once the data is retrieve.

If `database.db` already exsist and `python main.py aaaa bbbb` is called, it will update the database with the new stats retrieved.  This can be used to append new seasons to the database.

The resulting database is used for: 
- [NHL Stats Visualizer](https://github.com/ackyxu/NHLStatsVisualizer).

## Table Relationships

There are the following table in the database produced:

|Table Name	|Primary Key(s)   	|Description|  
|-----		|---				|---	|	
|Boxscores	|gameID, id |Stores the final Boxscores per game for each player that played in the game	|	
|GamePlays  |sequence, gameID |Stores the indivdual game events for a specific game, indentified by the sequence that it occured. |
|Players|id  	|Stores the names and postion type of all players that played in the seasons retrieved   	|
|Schedule 	|gameID| Stores the date that the game corresponding to the gameID was played and the home/away teams in that game|
|Teams|id|   Stores the name of all the teams that played in the seasons retrieved|


*Note: Team.id is represented by teamID in the other tables.*