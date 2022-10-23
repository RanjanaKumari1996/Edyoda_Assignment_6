import json


file = open("E:\RanjanaDigiServices\CustomerDocuments\Assignmet_1\Assignment_6\_1_Assignment\_Indian_states.json","w")
data={
    "Punjab":"Chandigarh",
    "Bihar":"Patna",
    "Jammu and Kashmir":"Shri Nagar",
    "Ladakh":"Leh",
    "Keral":"Bangalore",
    "Tamilnadu":"Chennai",
    "Manipur":"Imphal",
    "Mizoram":"Iwzol",
    "Madhya Pradesh":"Bhopal",
}
json.dump(data,file)