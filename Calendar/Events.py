#!/usr/bin/env python3
"""
---------------------------------------------------
Events.py
---------------------------------------------------
This program is responsible for the following:
1.) Providing the Event template to be used in
    processing by P.A.P.A.;
2.) Retrieving previously generated calendar events
    housed in Calendar.json, then turning those
    json objects into class instances;
3.) Saving new events;
4.) <Coming Soon>
----------------------------------------------------
Special Thanks to Ian Walton for continued Python 
skill development and Python tutelage.
"""
import json
import time
PATH = "/Your/Path/To/Calendar.json"

# (Probably bad) way to grab the number of json objects
# For upstream __init__ logic
with open(PATH, 'r') as f:
    myList = json.load(f)
for thing in myList:
    allEvents = [dict(thing) for thing in myList]

class Event:
    number_Of_Events = 0
    def __init__(self, event_Date, title, starts_At, 
            ends_At, reminder_Set_For, created_On=time.ctime()):
        self.event_Date = event_Date
        self.title = title
        self.starts_At = starts_At
        self.ends_At = ends_At
        self.reminder_Set_For = reminder_Set_For
        self.created_On = created_On
        Event.number_Of_Events += 1
        """
        Every time a new Event instance is generated,
        __init__ checks whether the number of JSON objects is
        less than the number class members, to see if we  
        need to update the json file with our newest instance.
        """
        if Event.number_Of_Events > len(allEvents):
            EVENTS.append(self)
            with open(PATH,'w') as f:
                f.write(toJSON(EVENTS))

    def as_dict(self):
        return self.__dict__

    def __repr__(self):
        return 'Event(%s)' % ", ".join(k+"="+repr(v) for k,v in self.__dict__.items())

    def out_File(self):
        pass
    # Type <instance>.__str__() at the interpreter for info
    def __str__(self):
        return f"""event_Date: {self.event_Date}, 
            title: {self.title}, 
            starts_At: {self.starts_At},
            ends_at = {self.ends_At},
            reminder_set_For = {self.reminder_Set_For}, 
            created_On = {self.created_On})"""

def toJSON(capitalized_events_list_object):
    i = 0
    jsonList = []
    while i < len(capitalized_events_list_object):
        jsonList.append(capitalized_events_list_object[i].__dict__)
        i += 1
    return json.dumps(jsonList, indent=4)

"""
Observe how we use the same programmic logic as earlier
but now for actually pulling those values into the Event class
"""
with open(PATH, 'r') as f:
    myList = json.load(f)
for thing in myList:
    allEvents = [dict(thing) for thing in myList]
EVENTS = [Event(**kwargs) for kwargs in allEvents]
"""
Usage:
        >>> from Events import *
        # Access all events by entering:
        >>> EVENTS
        [Event(event_Date='12/07/2018', title='Super Smash Bros. Ultimate Releases', starts_At= ...
        # Access individual events by entering:
        >>> EVENTS[2].__dict__
        {'event_Date': '01/01/2019', 'title': 'New Years Day', 'starts_At': ...
"""
