"""This file does the main processing"""

import datetime
from getitems import GetItems
from initializenewtrack import NewTrack

class ProcessSeminars:
    """This Class has function to process and schedule seminars
    """
    def processnewlist(self, filelist):
        """ This function processes the file
        """
        #Initialize
        datalist = []
        objtrack = NewTrack()

        for index, i in enumerate(filelist):
            #get every item to be printed (title and time)
            objgetitems = GetItems()
            newtime, item = objgetitems.getitemstring(i)

            #For the Morning Session within 180 mins
            if objtrack.max1 >= (objtrack.mrngsession+newtime):
                objtrack.mrngsession += newtime
                totime = datetime.datetime.strftime(objtrack.mrngtime, '%H:%M')
                objtrack.data1.append(str(totime)+" "+str(item))
                objtrack.mrngtime = objtrack.mrngtime+datetime.timedelta(minutes=newtime)
                if index == len(filelist)-1:
                    datalist.append(objtrack.data1+ objtrack.data2)

            #For the Evening Session within 180 mins
            elif objtrack.max2 > (objtrack.eveningsession+newtime):
                if objtrack.flag == 0:
                    objtrack.data2.append("12:00 Lunch")
                    objtrack.flag = 1
                objtrack.eveningsession += newtime
                totime = datetime.datetime.strftime(objtrack.evngtime, '%H:%M')
                objtrack.data2.append(str(totime)+" "+str(item))
                objtrack.evngtime = objtrack.evngtime+datetime.timedelta(minutes=newtime)
                if index == len(filelist)-1:
                    if objtrack.eveningsession <= 240 and objtrack.eveningsession >= 180:
                        totime = datetime.datetime.strftime(objtrack.evngtime, '%H:%M')
                        objtrack.data2.append(str(totime)+" Networking Event")
                    datalist.append(objtrack.data1+ objtrack.data2)

            #If No more conferences can be scheduled for the day
            else:
                if objtrack.eveningsession <= 240 and objtrack.eveningsession >= 180:
                    totime = datetime.datetime.strftime(objtrack.evngtime, '%H:%M')
                    objtrack.data2.append(str(totime)+" Networking Event")
                if newtime <= 240:
                    datalist.append(objtrack.data1+ objtrack.data2)
                    objtrack = NewTrack()
                    #if conference fits in the first session new track
                    if objtrack.max1 >= (objtrack.mrngsession+newtime):
                        objtrack.mrngsession += newtime
                        totime = datetime.datetime.strftime(objtrack.mrngtime, '%H:%M')
                        objtrack.data1.append(str(totime)+" "+str(item))
                        objtrack.mrngtime = objtrack.mrngtime+datetime.timedelta(minutes=newtime)
                        if index == len(filelist)-1:
                            datalist.append(objtrack.data1+ objtrack.data2)

                    #if conference fits in the second session new track
                    elif objtrack.max2 > (objtrack.eveningsession+newtime):
                        if objtrack.flag == 0:
                            objtrack.data2.append("12:00 Lunch")
                            objtrack.flag = 1
                        objtrack.eveningsession += newtime
                        totime = datetime.datetime.strftime(objtrack.evngtime, '%H:%M')
                        objtrack.data2.append(str(totime)+" "+str(item))
                        objtrack.evngtime = objtrack.evngtime+datetime.timedelta(minutes=newtime)
                        if index == len(filelist)-1:
                            if objtrack.eveningsession <= 240 and objtrack.eveningsession >= 180:
                                totime = datetime.datetime.strftime(objtrack.evngtime, '%H:%M')
                                objtrack.data2.append(str(totime)+" Networking Event")
                            datalist.append(objtrack.data1+ objtrack.data2)
        return datalist
