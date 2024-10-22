class person:
    def __init__(self, id, name, last_name_change_event, attributes, gender, last_gender_change_event):
        self.id = id
        self.name = name
        self.last_name_change_event = last_name_change_event
        self.attributes = attributes
        self.gender = gender
        self.last_gender_change_event = last_gender_change_event

class name:
    def __init__(self, id, type):
        self.id = id
        self.type = type

class event:
    def __init__(self, id, participants, date, type, endsevent, attributes):
        self.id = id
        self.participants = participants
        self.date = date
        self.type = type
        self.endsevent = endsevent
        self.attributes = attributes

