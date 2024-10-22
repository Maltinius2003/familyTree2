import json

def load_json_as_dict(file_path):
    # JSON-Datei lesen und in ein Dictionary umwandeln
    with open(file_path, "r") as file:
        data_dict = json.load(file)
    return data_dict

# Beispielaufruf der Funktion
file_path = "test_event_types.json"
result = load_json_as_dict(file_path)
print(result)
