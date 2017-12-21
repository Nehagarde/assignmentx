# Main File.

"""Run Application from here"""
from filereader import ClassFileReader
from processtracks import ProcessSeminars
from printtracks import TrackPrinter

# Get Input
formatinput = ClassFileReader()
newformattedinput = formatinput.readinputfile('test/bin/assignment/inputfileninputs.txt')
noofconferences = len(newformattedinput)

#If list of conferences generated from file is empty
if  noofconferences == 0:
    print("Empty Input File or File does not exists")

else:
    # Use Processed Input File to Schedule Conference
    process = ProcessSeminars()
    objprocess1 = process.processnewlist(newformattedinput)
    # Print the Schedule
    printer = TrackPrinter()
    objprinter = printer.printtracks(objprocess1)
