import json

data ={
    "Name :":"Nishan",
    "Address :":"Kalutara",
    "Age :" :"21"
}

with open("pythonFOlders/textFOlders/humenData",'w')as json_file:
    json_data=json.dumps(data,indent=4)
    json_file.write(json_data)

with open("pythonFOlders/textFOlders/humenData",'r')as json_object:
    json_o =json.load(json_object)
    print(json_o)



  