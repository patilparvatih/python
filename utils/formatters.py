import json

def prettyPrint(data:dict|list):
  print(json.dumps(data,indent=5))
