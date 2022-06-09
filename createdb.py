import json
db = {
    "name": "Hristo Bakovski",
    "age": 21,
    "intnames": ["stoinost1","stoinost2","stoinost3","stoinost4","stoinost5","stoinost6","stoinost7","stoinost8","stoinost9","stoinost10"],
    "boolnames": ["nost1","nost2","nost3","nost4","nost5","nost6","nost7","nost8","nost9","nost10"],
    "days": [
        {"ints": [0,0,0,0,0,0,0,0,0,0], "bools": [False,False,False,False,False,False,False,False,False,False]},
        {"ints": [0,0,0,0,0,0,0,0,0,0], "bools": [False,False,False,False,False,False,False,False,False,False]},
        {"ints": [0,0,0,0,0,0,0,0,0,0], "bools": [False,False,False,False,False,False,False,False,False,False]},
        {"ints": [0,0,0,0,0,0,0,0,0,0], "bools": [False,False,False,False,False,False,False,False,False,False]},
        {"ints": [0,0,0,0,0,0,0,0,0,0], "bools": [False,False,False,False,False,False,False,False,False,False]},
        {"ints": [0,0,0,0,0,0,0,0,0,0], "bools": [False,False,False,False,False,False,False,False,False,False]}
    ]
}
print(json.dumps(db))