# Uses the requests API to make a HTTP POST request.

import requests

apiKey = '0bb28905c84012d47d113eb090120e12'
githubUrl = 'https://github.com/ckimmons/code2040Assesment'

dictionary = {'token': apiKey, 'github': githubUrl}
r = requests.post("http://challenge.code2040.org/api/register", data=dictionary);
print(r.text)
