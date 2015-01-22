dataDict = {
    "a":{
        "r": 1,
        "s": 2,
        "t": 3
        },
    "b":{
        "u": 1,
        "v": {
            "x": 1,
            "y": 2,
            "z": 3
        },
        "w": 3
        }
}    

mapList = ["a", "r"]



# Get a given data from a dictionary with position provided as a list
def getFromDict():    
    for k in mapList: dataDict = dataDict[k]
    return dataDict

# Set a given data in a dictionary with position provided as a list
def setInDict(value): 
    for k in mapList[:-1]: dataDict = dataDict[k]
    dataDict[mapList[-1]] = value
    
print getFromDict()
#setInDict(dataDict, mapList, 78)
#print setInDict(dataDict, mapList, 78)