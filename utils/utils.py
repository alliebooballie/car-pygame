import json
from datetime import datetime
# import requests

class GameEvent:
    def __init__(self, player_id, event_type, item=None, position=None):
        self.timestamp = datetime.utcnow().isoformat() + "Z"
        self.player_id = player_id
        self.event_type = event_type  # e.g. "MOVE", "COLLECT", "DIE"
        self.item = item            # e.g. "gold_coin", "trap", "sword"
        self.position = position      # e.g. [x, y]

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "player_id": self.player_id,
            "event_type": self.event_type,
            "item": self.item,
            "position": self.position,
        }

    def to_json(self):
        return json.dumps(self.to_dict())
    

#Integration with Flask! Need Handler
def logEvent(game_event):
    json_payload = game_event.to_json()
    print(json_payload)
    # requests.post("http://localhost:5000/events", json=json_payload.to_dict())