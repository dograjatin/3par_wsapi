'''
with open("C:\\Users\\jatin\\Desktop\\Development\\3par_cpg\\config.json", "r") as jsonFile:
    data = json.load(jsonFile)
    print(data)

data["cpg_number"] = ""

with open("C:\\Users\\jatin\\Desktop\\Development\\3par_cpg\\config.json", "w") as jsonFile:
    json.dump(data, jsonFile)

with open("C:\\Users\\jatin\\Desktop\\Development\\3par_cpg\\config.json", "r") as jsonFile:
    data = json.load(jsonFile)
    print(data)
'''