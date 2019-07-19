#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Raphaël LEBER"

from datetime import datetime
import unittest

class CalendarSlot:

    def __init__(self, start_datetime, ModuleName = "", SlotText = "",timeLength=(2, 0), ClassRoom = ""  ):
        self.start_datetime = start_datetime
        self.ModuleName = ModuleName
        self.SlotText = SlotText
        self.timeLength = timeLength
        self.ClassRoom = ClassRoom


    def TimeOfSlot(self, x):
        return [
            (0, 0),
            (8, 0),     # 8 hours and 00 minutes
            (10, 15),   # 10 hours and 15 minutes
            (13, 30),
            (15, 45),
        ][x]

    def isNeighour(self, firstSlot, secondSlot):
        #print("### " + str(secondSlot.datetime.timetuple()[0]) )

        if (firstSlot.start_datetime.year == secondSlot.start_datetime.year
            and firstSlot.start_datetime.month == secondSlot.start_datetime.month
            and firstSlot.start_datetime.day == secondSlot.start_datetime.day ) :

            #print("### " +  str(firstSlot.datetime.hour) + " " + str(secondSlot.datetime.hour) )

            if firstSlot.start_datetime.hour == self.TimeOfSlot(1)[0] and secondSlot.start_datetime.hour == self.TimeOfSlot(2)[0] :
                return True
            if firstSlot.start_datetime.hour == self.TimeOfSlot(2)[0] and secondSlot.start_datetime.hour == self.TimeOfSlot(1)[0] :
                return True
            if firstSlot.start_datetime.hour == self.TimeOfSlot(3)[0] and secondSlot.start_datetime.hour == self.TimeOfSlot(4)[0] :
                return True
            if firstSlot.start_datetime.hour == self.TimeOfSlot(4)[0] and secondSlot.start_datetime.hour == self.TimeOfSlot(3)[0] :
                return True

        return False


    def isSameNeighour(self, firstSlot, secondSlot):
        if self.isNeighour(firstSlot, secondSlot) :
            if firstSlot.SlotText == secondSlot.SlotText :
                return True

        return False


    def trySlotFusion(self, firstSlot, secondSlot):
        if self.isSameNeighour(firstSlot, secondSlot) :
            firstSlot.timeLength = (4, 15)
            return True
        return False





class CalendarSlotTest(unittest.TestCase):

    def test_isNeighour(self):
        CS = CalendarSlot(datetime.now())
        slots = []
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=8), ModuleName='Motor', SlotText='Motor blabla'))
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=10), ModuleName='Motor', SlotText='Motor blabla'))
        #print("### " + str(slots[0].datetime) + " " + str(slots[1].datetime) )
        self.assertTrue( CS.isNeighour(slots[0], slots[1] ) )

        slots.clear()
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=8), ModuleName='Motor', SlotText='Motor blabla'))
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 18, hour=10), ModuleName='Motor', SlotText='Motor blabla'))
        self.assertFalse(CS.isNeighour(slots[0], slots[1]))

        slots.clear()
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=10), ModuleName='Motor', SlotText='Motor blabla'))
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=15), ModuleName='Motor', SlotText='Motor blabla'))
        self.assertFalse(CS.isNeighour(slots[0], slots[1]))



    def test_isSameNeighour(self):
        CS = CalendarSlot(datetime.now())
        slots = []
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=8), ModuleName='Motor', SlotText='Motor blabla'))
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=10), ModuleName='Motor', SlotText='Motor blabla'))
        self.assertTrue( CS.isSameNeighour(slots[0], slots[1] ) )

        slots.clear()
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=8), ModuleName='Motor', SlotText='Motor blabla'))
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=10), ModuleName='Motor', SlotText='Motor hum hum'))
        self.assertFalse( CS.isSameNeighour(slots[0], slots[1] ) )



    def test_trySlotFusion(self):
        CS = CalendarSlot(datetime.now())
        slots = []
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=8), ModuleName='Motor', SlotText='Motor blabla'))
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=10), ModuleName='Motor', SlotText='Motor blabla'))
        fusionStatus = CS.trySlotFusion( slots[0], slots[1] )
        self.assertEqual( slots[0].timeLength, (4, 15) )

        slots.clear()
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=8), ModuleName='Motor', SlotText='Motor blabla'))
        slots.append(CalendarSlot(start_datetime=datetime(2018, 6, 17, hour=10), ModuleName='Motor', SlotText='Motor hum hum'))
        fusionStatus = CS.trySlotFusion( slots[0], slots[1] )
        self.assertEqual(slots[0].timeLength, (2, 0))



if __name__ == '__main__':
    unittest.main()