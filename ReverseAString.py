# Stage 2.
# Reverses a string, posts the result.
from ApiRequestHandler import RecieveProblem, ValidateProblem

REQUEST_URL = 'http://challenge.code2040.org/api/reverse'
VALIDATE_URL = 'http://challenge.code2040.org/api/reverse/validate'

string = RecieveProblem(REQUEST_URL)

# Uses the slicing operator to return the reversed string.
reverse = string[::-1]

ValidateProblem(VALIDATE_URL, 'string', reverse)
