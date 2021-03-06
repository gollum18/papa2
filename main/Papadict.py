import math
import cmath
# Papadict.py
# is a dictionary body for looking up a function name
# to perform by passing it a single lookup string,
# called the "lookupKey".
# The lookupKey is passed from a P.A.P.A. module,
# called parsingArrays, with its "command_Parsing" function.

# import Commands
# import ParsingArrays

# Need priority-ranking system for steering most-likely or 
# most-sense-making selection for word that trumps one func"s
# execution over another
important_Words = {
    "who's": "default_Interpreter",
    "who": "default_Interpeter",
    "what's": "default_Interpreter",
    "what": "default_Interpreter",
    "when's": "Schedule.Calendar",   
    "when": "Schedule.Calendar",
    "where's": "default_Interpreter",
    "where": "default_Interpreter",
    "why's": "default_Interpreter",
    "why": "default_Interpreter",
    "how many": "default_Interpreter",
    "how's": "default_Interpreter",
    "how": "default_Interpreter",
    "answer": "default_Interpreter",
    "start": "default_Interpreter",
    "play": "Internet_Youtube",
    "on": "default_Interpreter",
    "off": "default_Interpreter",
    "shut": "default_Interpreter",
    "tell": "default_Interpreter",
    "text": "Phone.TextMessage",
    "search": "Internet_Search",
    "wake": "Schedule_Alarm",
    "turn": "default_Interpreter"}

command_Words = {
    "bash": "Bashing",
    "open": "default_Interpreter",
    "lookup": "Internet_Search",
    "google": "Internet_Search",
    "go": "Internet_Search",
    "web": "Internet_Search",
    "youtube": "Internet_YouTube",
    "calculate": "Internet_Wolfram",
    "wikipedia": "Internet_Search",
    "timer": "Schedule_Timer",
    "to-do": "Schedule_Calendar",
    "planner": "Schedule_Calendar",
    "homework": "Schedule_Calendar",
    "alarm": "Schedule_Alarm",
    "message": "Email.Send_Message",
    "answer": "Phone.Phone_Call_Answer",
    "call": "Phone.Phone_Call",
    "text-message": "Phone.Text_Message",
    "remind": "Schedule_Calendar",
    "power": "default_Interpreter",
    "text": "Phone.Text_Message",
    "day": "Schedule.Date",
    'date': "Schedule.Date",
    "today": "Schedule.Date",
    "appointment": "Schedule.Calendar"}

number_Words = {
    "zero": 0,
    "0": 0,
    "point": ".",
    "one": 1,
    "1": 1,
    "two": 2,
    "2": 2,
    "three": 3,
    "3": 3,
    "four": 4,
    "4": 4,
    "five": 5,
    "5": 5,
    "six": 6,
    "6": 6,
    "seven": 7,
    "7": 7,
    "eight": 8,
    "8": 8,    
    "nine": 9,
    "9": 9,
    "ten": 10,
    "10": 10,
    "eleven": 11,
    "11":11,
    "twelve": 12,
    "12":12,
    "thirteen": 13,
    "13":13,
    "fourteen": 14,
    "14":14,
    "fifteen": 15,
    "15": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "20": 20,
    "twenty-one": 21,
    "twenty-two": 22,
    "twenty-three": 23,
    "twenty-four": 24,
    "twenty-five": 25,
    "25":25,
    "twenty-six": 26,
    "twenty-seven": 27,
    "twenty-eight": 28,
    "twenty-nine": 29,
    "thirty": 30,
    "30": 30,
    "thirty-one": 31,
    "thirty-two": 32,
    "thirty-three": 33,
    "thirty-four": 34,
    "thirty-five": 35,
    "thirty-six": 36,
    "thirty-seven": 37,
    "thirty-eight": 38,
    "thirty-nine": 39,
    "forty": 40,
    "forty-one": 41,
    "forty-two": 42,
    "forty-three": 43,
    "forty-four": 44,
    "forty-five": 45,
    "45": 45,
    "forty-six": 46,
    "forty-seven": 47,
    "forty-eight": 48,
    "forty-nine": 49,
    "fifty": 50,
    "fifty-one": 51,
    "fifty-two": 52,
    "fifty-three": 53,
    "fifty-four": 54,
    "fifty-five": 55,
    "fifty-six": 56,
    "fifty-seven": 57,
    "fifty-eight": 58,
    "fifty-nine": 59,
    "sixty": 60,
    "sixty-one": 61,
    "sixty-two": 62,
    "sixty-three": 63,
    "sixty-four": 64,
    "sixty-five": 65,
    "sixty-six": 66,
    "sixty-seven": 67,
    "sixty-eight": 68,
    "sixty-nine": 69,
    "seventy": 70,
    "seventy-one": 71,
    "seventy-two": 72,
    "seventy-three": 73,
    "seventy-four": 74,
    "seventy-five": 75,
    "seventy-six": 76,
    "seventy-seven": 77,
    "seventy-eight": 78,
    "seventy-nine": 79,
    "eighty": 80,
    "eighty-one": 81,
    "eighty-two": 82,
    "eighty-three": 83,
    "eighty-four": 84,
    "eighty-five": 85,
    "eighty-six": 86,
    "eighty-seven": 87,
    "eighty-eight": 88,
    "eighty-nine": 89,
    "ninety": 90,
    "ninety-one": 91,
    "ninety-two": 92,
    "ninety-three": 93,
    "ninety-four": 94,
    "ninety-five": 95,
    "ninety-six": 96,
    "ninety-seven": 97,
    "ninety-eight": 98,
    "ninety-nine": 99,
    "one-hundred": 100,
    "two-hundred": 200,
    "three-hundred": 300,
    "four-hundred": 400,
    "five-hundred": 500,
    "six-hundred": 600,
    "seven-hundred": 700,
    "eight-hundred": 800,
    "nine-hundred": 900,
    "one-thousand": 1000,
    "ten-thousand": 10000,
    "one-hundred-thousand": 100000,
    "one-million": 1000000,
    "ten-million": 10000000,
    "one-hundred-million": 100000000,
    "one-billion": 1000000000,
    "j": 1j,
    "pi": cmath.pi,
    "e": cmath.e,
    "negative-one": -1,
    #"complex-negative-one": 1j**2,
    "infinity": math.inf}

time_Units = {
    "seconds": 1,
    "second":1,
    "minutes": 60.0,
    "minute": 60.0,
    "hours": 3600.0,
    "hour": 3600.0,
    "AM": 0.0,
    "PM": 12.0,
    "week": "7 days",
    "month": "28 days",
    "year": "365 days",
    "today": ""}
