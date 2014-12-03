inFile = open("julyTemps.txt")

lines = inFile.readlines()

highTemps = ()
lowTemps = ()
diffTemps = ()

for line in lines:
    fields = line.rstrip().split(" ")
    if len(fields) == 3 and fields[0].isdigit():
        highTemps += (fields[1],)
        lowTemps += (fields[2],)
        diffTemps += (int(fields[1]) - int(fields[2]),)

print highTemps
print lowTemps
print diffTemps

import pylab

pylab.figure(1)

pylab.title('Day by Day Ranges in Temperature in Boston in July 2012')
pylab.xlabel('Days')
pylab.ylabel('Temperature Ranges')

pylab.plot(range(1, 32), diffTemps)
pylab.show()
