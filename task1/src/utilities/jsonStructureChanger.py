import json
import pathlib


def make_json(jsonToModify, jsonModified):

  newData = []

  with open(jsonToModify, encoding='utf-8') as jsonf:
    oldData = json.load(jsonf)
    
    for rows in oldData:
      row = {        
        'CrimeId': rows['CrimeId'],
        'OriginalCrimeTypeName': rows['OriginalCrimeTypeName'],
        'OffenseDate': rows['OffenseDate'],
        'CallDateTime': rows['CallDateTime'],
        'Disposition': rows['Disposition'],
        'Location': {
          "Address": rows['Address'],
          "City": rows['City'],
          "State": rows['State'],
          "AddressType": rows['AddressType']
        }
      }
      newData.append(row)    

  with open(jsonModified, 'w', encoding='utf-8') as jsonf:
    jsonf.write(json.dumps(newData, indent=2))

jsonToModify = pathlib.Path(__file__).parent.resolve().joinpath('../json_example.json')
jsonModified = pathlib.Path(__file__).parent.resolve().joinpath('../json_example_modified.json')

make_json(jsonToModify, jsonModified)
