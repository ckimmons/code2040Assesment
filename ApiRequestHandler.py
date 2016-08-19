import requests
import json
TOKEN = '0bb28905c84012d47d113eb090120e12'

def RecieveProblem(url):
    myDictionary = {'token': TOKEN}
    request = requests.post(url, data=myDictionary);
    return request.text

def ValidateProblem(url, outputName, toSend):
    myDictionary ={'token' : TOKEN, outputName : toSend}
    output = requests.post(url, data=myDictionary);
    print(output.text)

def JsonLoader(text):
    dictionary = Json.Loads(text)
    return dictionary
