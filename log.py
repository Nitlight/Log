class LoggerParam:
    def __init__(self, tag = "", message = "", place = ""):
        self.message = message
        self.tag = tag
        self.place = place

    def parse_to_dict(self):
        return {
            "tag" : self.tag,
            "message" : self.message,
            "place" : self.place
        }