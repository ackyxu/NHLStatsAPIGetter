class EventPlayer:
    # key: player ID val: event type
    playerDict = {}
    def __init__(self, eventPlayersJSON: dict):
        for index in eventPlayersJSON:
            self.playerDict[eventPlayersJSON[index]["player"]["id"]] = eventPlayersJSON[index]["player"]["playerType"]