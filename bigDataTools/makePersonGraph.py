#!/usr/bin/env python


import sys
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as md
import numpy as np
from datetime import datetime
import time

# based on the result of "mrWebPersonalReport.py" make graphic
def datetimeToStamp(day):
    dt = datetime.strptime(day,'%d/%b/%Y:%H:%M:%S')
    print dt.hour
    timestamp = ( dt - datetime(1970, 1, 1)).total_seconds()
    return timestamp

def dateToStamp(day):
    dt = datetime.strptime(day,'%d/%b/%Y')
    print dt.hour
    timestamp = ( dt - datetime(1970, 1, 1)).total_seconds()
    return timestamp


def genGraphic(graphic_data):
    filename = graphic_data['username']+".png"
    startdate = graphic_data['startdate']
    enddate = graphic_data['enddate']
 
    plt.xticks( rotation=25 )
    ax=plt.gca()
    plt.xticks( rotation=25 )
    xfmt = md.DateFormatter('%m-%d')
    ax.xaxis.set_major_formatter(xfmt)
    #ax.set_xlim(startdate, enddate)
    ax.set_xlim(datetime(2015, 5, 1,), datetime(2015, 5, 27))
    ax.set_ylim(0,24)
    for aplot in graphic_data['plot'] :
        msize = float(aplot[2])
        marker = "o"
        if msize >= 15:
            msize = 15
            marker = "8"
        if msize <= 2:
            msize =2
        plt.plot(aplot[0],aplot[1],marker,markersize=msize,mfc='none')

    plt.title("tbox:"+graphic_data['username'])
    plt.savefig("tboxp/"+filename)   # save the figure to file
    plt.close() 

if __name__ == '__main__':
    mrResultFile = sys.argv[1]
    print mrResultFile

    with open(mrResultFile, 'r') as infile:
        current_name = "###"
        graphic_data = {}
        tmpCnt = 0
        for line in infile:
            line.replace("[","").replace("]","")
            parts = line.split(",")
            username = parts[0].replace('"',"")
            if username != current_name : 
                if current_name != '###':
                    tmpCnt +=1
                    print "flush out "+current_name
                    genGraphic(graphic_data)
                  #  if tmpCnt >= 10:
                  #      break 

                print "handle user:"+username
                graphic_data ={}
                graphic_data['username'] = username
                graphic_data['plot'] = []
                graphic_data['startdate'] = None
                graphic_data['enddate'] = None
                current_name = username
                 #"22/May/2015:06:00:28"        0.109002
            dateString = parts[1].split(":")[0].replace(' "','')
            dateDT = datetime.strptime(dateString,'%d/%b/%Y')
            
            if dateDT < datetime(2015, 5, 1,):
                continue 

            if graphic_data['startdate'] == None or dateDT < graphic_data['startdate'] :
                graphic_data['startdate'] = dateDT
            if graphic_data['enddate'] == None or dateDT > graphic_data['enddate'] :
                graphic_data['enddate'] = dateDT
        
            hour = float(parts[1].split(":")[1])
            minutes = float(parts[1].split(":")[2])/60.0
            seconds = float(parts[1].split(":")[3][:2])/3600
            hour = hour + minutes + seconds
            waitSecond = parts[1].split('"')[2].replace(" ","").replace("\t","")
            aplot = [dateDT, hour, waitSecond]
    #        print aplot
            graphic_data['plot'].append(aplot)




