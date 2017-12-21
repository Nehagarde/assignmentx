"""This is to take the input through a file
    """
import re
import os
class ClassFileReader:
    """This Class has function to process and format the input
    """
    def readinputfile(self, fname):
        """This function processes the input file and formats it into a list
        """
        finallist = []
        if os.path.isfile(fname):
            with open(fname) as file:
                for eachline in file:
                    if eachline not in ['\n', '\r\n']:
                        newline = eachline.replace('lightning', '5min')
                        talk = re.match(r'([a-zA-Z]+.*?\s)(\d+)', newline)

                        if talk:
                            data = []
                            data = [talk.group(1).strip(), int(talk.group(2))]
                            finallist.append(data)
        #finallist = sorted(finallist,key=lambda x: x[1],reverse=True)
        return finallist
