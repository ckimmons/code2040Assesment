import requests
import json
TOKEN = '0bb28905c84012d47d113eb090120e12'

def RecieveProblem(url):
    my_dictionary = {'token': TOKEN}
    request = requests.post(url, data=my_dictionary);
    return request.text

def ValidateProblem(url, key, value):
    my_dictionary ={'token' : TOKEN, key : value}
    output = requests.post(url, data=my_dictionary);
    print(output.text)

def JsonLoader(text):
    dictionary = Json.Loads(text)
    return dictionary