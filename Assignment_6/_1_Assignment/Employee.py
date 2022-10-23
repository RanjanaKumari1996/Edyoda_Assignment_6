import json

file = open("E:\RanjanaDigiServices\CustomerDocuments\Assignmet_1\Assignment_6\_1_Assignment\Employee.json","r")

data = json.load(file)

#Employee data reads from employee.json file

print (data) 

#list of employee objects

for i in data['Emp_details']:
    print(data)