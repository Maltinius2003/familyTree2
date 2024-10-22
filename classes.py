class person:
    def __init__(self, id, name, last_name_change_event, attributes, gender, last_gender_change_event):
        self.id = id
        self.name = name
        self.last_name_change_event = last_name_change_event
        self.attributes = attributes
        self.gender = gender
        self.last_gender_change_event = last_gender_change_event

class name:
    def __init__(self, id, type, main_name, name_parts, namedafter, patron_saint):
        self.id = id
        self.type = type # 0: unknown, 1: civilian, 2: noble, 3: custom (religios names under titles)
        self.main_name = main_name # name that is used in the tree
        self.name_parts = name_parts # list of name parts
        self.namedafter = namedafter # tupel, list of part ids that are named after another person, list of ids, create new if not in list
        self.patron_saint = patron_saint # id, create new if not in list


class name_part:
    def __init__(self, id, text, type, attributes, namedafter):
        self.id = id
        self.text = text
        self.type = type # 0: first name, 1: last name, 2: title, 3: prefix, 4: suffix, 5: von/van (nobility) 
        self.attributes = attributes 
        self.namedafter = namedafter # id, create new if not in list


class event:
    def __init__(self, id, participants, date, type, endsevent, attributes, new_names, old_names, new_titles, old_titles):
        self.id = id
        self.participants = participants
        self.date = date
        self.type = type
        self.endsevent = endsevent
        self.starts_attributes = attributes # attributes that become valid with this event, eg religion, house, dynasty
        self.ends_attributes = attributes
        self.new_names = new_names # new names that gain validity with this event
        self.old_names = old_names # old names that lose validity with this event
        self.new_titles = new_titles # new titles that gain validity with this event
        self.old_titles = old_titles # are not part of the name, like bishop, cardinal, saint

class attribute:
    def __init__(self, upperlevel_type, type, people, name, date, place):
        self.upperlevel_type = upperlevel_type
        self.type = type
        self.people = people # like patrones, 
        self.name = name
        self.date = date # 
        self.place = place