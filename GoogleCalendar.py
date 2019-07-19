#!/usr/bin/env python
# -*- coding: utf-8 -*-



from __future__ import print_function

from httplib2 import Http
from oauth2client import file, client, tools
import datetime
from apiclient.discovery import build

import unittest

class GoogleCalendar:

    def __init__(self):

        # Setup the Calendar API
        SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('calendar', 'v3', http=creds.authorize(Http()))



    def getEvents(self):

        # Call the Calendar API
        now = datetime.datetime.utcnow().isoformat() + 'Z' # 'Z' indicates UTC time
        print('Getting the upcoming 10 events')
        events_result = self.service.events().list(calendarId='primary', timeMin=now,
                                              maxResults=10, singleEvents=True,
                                              orderBy='startTime').execute()
        events = events_result.get('items', [])

        if not events:
            print('No upcoming events found.')
        for event in events:
            start = event['start'].get('dateTime', event['start'].get('date'))
            print(start, event['summary'])






# class GoogleCalendarTest(unittest.TestCase):
#
#     def __init__(self):
#         self.toto = 0


if __name__ == '__main__':
    #unittest.main()

    GC = GoogleCalendar()

    GC.getEvents()
