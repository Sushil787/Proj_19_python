import json

# a Python object (dict):
x = {
  "sushil": "Student",
  "age": 30,
  "city": "Bhaktapur"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#JSON load
'''import json

x = '{"sushant poudel" : "OOP","Shukabathau":"Statistic","Surya Bam":"DS","Gopal":"MP","Raman K":"Maths II"}'
y = json.loads(x)
print(y["Gopal"])'''
