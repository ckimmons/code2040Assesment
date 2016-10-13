from ApiRequestHandler import RecieveProblem, ValidateProblem, JsonLoader

REQUEST_URL = 'http://challenge.code2040.org/api/prefix'
VALIDATE_URL = 'http://challenge.code2040.org/api/prefix/validate'

text = ReceiveProblem(REQUEST_URL)
dictionary = JsonLoader(text)
prefix = dictionary.get('prefix')
listOfWords = dictionary.get('array')
wordsWithoutPrefix = []

for word in listOfWords:
    if word.startswith(prefix) is False:
        wordsWithoutPrefix.append(word)

ValidateProblem(VALIDATE_URL, 'array', wordsWithoutPrefix)
