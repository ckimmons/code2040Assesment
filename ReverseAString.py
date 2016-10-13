# Stage 2.
# Reverses a string, posts the result.
from ApiRequestHandler import RecieveProblem, ValidateProblem

REQUEST_URL = 'http://challenge.code2040.org/api/reverse'
VALIDATE_URL = 'http://challenge.code2040.org/api/reverse/validate'

# Uses the slicing operator to return the reversed string.
def ReverseAString(string):
    return string[::-1]

string = ReceiveProblem(REQUEST_URL)
reverse = ReverseAString(string)

ValidateProblem(VALIDATE_URL, 'string', reverse)
