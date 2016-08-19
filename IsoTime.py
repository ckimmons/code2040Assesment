# Stage 5.
# Add interval (in seconds) to ISO-formatted time.
from ApiRequestHandler import RecieveProblem, ValidateProblem, JsonLoader
from datetime import datetime, timedelta
import dateutil.parser
from time import strftime

ISO8601_FORMAT = '%Y-%m-%d %H:%M:%S'
REQUEST_URL = 'http://challenge.code2040.org/api/dating'
VALIDATE_URL = 'http://challenge.code2040.org/api/dating/validate'

def AddIntervalToDate(date_string, interval):
    # Must remove the 'T' from the string to properly calculate the new date.
    S = ' '
    date = S.join(date_string.split('T'))
    date = date[:-1]
    # Formats the date to the IS08601 format.
    date = datetime.datetime.strptime(date, ISO8601_FORMAT)
    new_date = date + datetime.timedelta(seconds=interval)
    new_date = new_date.isoformat()
    # Python's datetime format does not include the 'Z', so we must add that to
    # the end of the string.
    new_date += 'Z'
    return new_date


text = RecieveProblem(REQUEST_URL)
dictionary = JsonLoader(text)
date = dictionary.get('datestamp')
interval = dictionary.get('interval')
datestamp = AddIntervalToDate(date, interval)
ValidateProblem(VALIDATE_URL, 'datestamp', datestamp)
