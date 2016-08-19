# stage 3.
# Find a string in an array of strings.
from ApiRequestHandler import RecieveProblem, ValidateProblem, JsonLoader
REQUEST_URL = 'http://challenge.code2040.org/api/haystack'
VALIDATE_URL = 'http://challenge.code2040.org/api/haystack/validate'

text = RecieveProblem(REQUEST_URL)
dictionary = JsonLoader(text)
listOfStrings = dictionary.get('haystack')
index = listOfStrings.index(dictionary.get("needle"))
ValidateProblem(VALIDATE_URL, 'needle', index)
