import json


sample_json = """
[ 
   { 
      "id":1,
      "name":"name1",
      "color":[ 
         "red",
         "green"
      ]
   },
   { 
      "id":2,
      "name":"name2",
      "color":[ 
         "pink",
         "yellow"
      ]
   }
]"""

data = []

try:
    data = json.loads(sample_json)
except Exception as e:
    print(e)

dataList = [item.get('name') for item in data]
print(dataList)
