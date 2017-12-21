# Read Input Fileprint(finallist[0][2]) 

import time
import datetime
from getitems import GetItems

class ProcessSeminars:
    
    def processnewlist(self,ls):
        max1 = 180
        max2 = 180 
        mrngtime = datetime.datetime.strptime("9:00", '%H:%M')
        evngtime = datetime.datetime.strptime("2:00", '%H:%M')
       
          
        mrngsession=0
        eveningsession=0
        flag=0
        data=[]
        datalist=[]

        for index,i in enumerate(ls):
            objgetitems=GetItems()
            newtime,item=objgetitems.getitemstring(i)

            if max1>=(mrngsession+newtime):
                mrngsession+=newtime
                totime=datetime.datetime.strftime(mrngtime, '%H:%M')
                data.append(str(totime)+" "+str(item))
                mrngtime = mrngtime+datetime.timedelta(minutes=newtime)
                if index==len(ls)-1:
                    datalist.append(data)
            elif max2>(eveningsession+newtime):
                if flag==0:
                   data.append("01:00 Lunch")
                   flag=1     
                eveningsession+=newtime 
                totime=datetime.datetime.strftime(evngtime, '%H:%M')
                data.append(str(totime)+" "+str(item))
                evngtime = evngtime+datetime.timedelta(minutes=newtime)
                if index==len(ls)-1:
                    datalist.append(data)   
            else:
                if eveningsession<240:
                    totime=datetime.datetime.strftime(evngtime, '%H:%M')
                    data.append(str(totime)+" Networking Event")
                datalist.append(data)
                mrngsession=0
                eveningsession=0 
                data=[]
                mrngtime = datetime.datetime.strptime("9:00", '%H:%M')
                evngtime = datetime.datetime.strptime("2:00", '%H:%M')
                if max1>=(mrngsession+newtime):
                    mrngsession+=newtime
                    totime=datetime.datetime.strftime(mrngtime, '%H:%M')
                    data.append(str(totime)+" "+str(item))
                    mrngtime = mrngtime+datetime.timedelta(minutes=newtime)
                    if index==len(ls)-1:
                        datalist.append(data)
                elif max2>=(eveningsession+newtime):
                    if evngtime=="02:00":
                       data.append("01:00 Lunch")
                    eveningsession+=newtime 
                    totime=datetime.datetime.strftime(evngtime, '%H:%M')
                    data.append(str(totime)+" "+str(item))
                    evngtime = evngtime+datetime.timedelta(minutes=newtime)
                    if index==len(ls)-1:
                        datalist.append(data)        
       
        return datalist