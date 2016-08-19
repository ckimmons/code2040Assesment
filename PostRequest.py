# Stage 1.
import requests
from ApiRequestHandler import ValidateProblem

GITHUB_URL = 'https://github.com/ckimmons/code2040Assesment'
VALIDATE_URL = 'http://challenge.code2040.org/api/register'

ValidateProblem(VALIDATE_URL, 'github', GITHUB_URL)
