import requests
import json
TOKEN = '0bb28905c84012d47d113eb090120e12'

# Recieves a string from the CODE2040 assessment server.
def ReceiveProblem(url):
    my_dictionary = {'token': TOKEN}
    request = requests.post(url, data=my_dictionary);
    return request.text

# Creates a dictionary from the key and value, and sends the
# POST request to the url meant to validate stages.
def ValidateProblem(url, key, value):
    my_dictionary ={'token' : TOKEN, key : value}
    output = requests.post(url, json=my_dictionary);
    print(output.text)

# Turns the string recieved from RecievedProblem into a usable dictionary.
def JsonLoader(text):
    dictionary = json.loads(text)
    return dictionary
