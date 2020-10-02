import json
from difflib import get_close_matches

def predict(w):
    data={"comps":["comps"],"compscience":["comps"],"etronix":["etrx"],"etronixandtelecomm":["extc"],"extc":["extc"],"mechan":["mech"],"IT":["it"],"Information technology":["it"]}
    w= w.lower()

    if w in data:
        return data[w]
    elif w.title() in data:
        return data[w.tile()]
    elif w.upper() in data:
        return data[w.upper()]
    elif len(get_close_matches(w, data.keys())) > 0:
        return data[get_close_matches(w, data.keys())[0]]
    else:
        return "The Department doesn't exist. Please double check it."
    