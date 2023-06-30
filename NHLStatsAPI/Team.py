class Team:
    
    id: int
    abbrv: str
    teamName: str 
    locationName: str 
    divisionName: str
    divisionShortName: str 
    
    def __init__(self, teamJSON: dict) -> None:
        self.id = teamJSON["id"]
        self.abbrv = teamJSON["abbreviation"]
        self.teamName = teamJSON["teamName"]
        self.locationName = teamJSON["locationName"]
        self.divisionName = teamJSON["division"]["name"]  
        self.divisionShortName = teamJSON["division"]["nameShort"] 
         
        
		