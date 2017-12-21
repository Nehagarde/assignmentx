"""This file gets the description of current conference"""

class GetItems:
    """This Class has function to process and schedule seminars
    """
    def getitemstring(self, i):
        """This method sorts out the time and title of the event
        """
        for index1, eachitem in enumerate(i):
            if index1 == 0:
                title = eachitem
            elif index1 == 1:
                newtime = eachitem

        if newtime == 5:
            newstring = title+" Lightning"
        else:
            newstring = title+" "+str(newtime)+"min"
        return newtime, newstring
