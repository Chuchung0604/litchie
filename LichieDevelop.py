# -*- coding: utf-8 -*-
"""
Created on Fri Mar 25 15:34:12 2022

@author: ccchen
"""
import csv
from datetime import datetime
from datetime import timedelta



def DOY2DATE(year2,jday):
    if jday > 365:
        year = int(year2)
        DOY = jday - 365

    else:
        year = int(year2)-1
        DOY = jday 

    nonLeap = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,
               10:273,11:304,12:334}
    for i in range(1,12+1):
        if DOY > nonLeap[i]:
            month = i
            day = DOY-nonLeap[i]

    toReturn = "%d/%d/%d"%(year,month,day)
    return toReturn

def DOY2DATE2(jday):
    if jday > 365:
        DOY = jday - 365
    else:
        DOY = jday 

    nonLeap = {1:0,2:31,3:59,4:90,5:120,6:151,7:181,8:212,9:243,
               10:273,11:304,12:334}
    for i in range(1,12+1):
        if DOY > nonLeap[i]:
            month = i
            day = DOY-nonLeap[i]

    toReturn = "%02d%02d"%(month,day)
    return toReturn


def beta_fn(t, t_b, t_o, t_c):


    if (t <= t_b or t >= t_c):
        return 0
    f = (t - t_b) / (t_o - t_b)
    g = (t_c - t) / (t_c - t_o)
    alpha = (t_o - t_b) / (t_c - t_o)
    Rmax = t_c - t_o
    
    return g*pow(f,alpha)*Rmax
        

def dayNumbers(year):
    if year%4 == 0:
        return 366
    else:
        return 365


def read2YrWea(RCP, modelName, year2no,lon,lat,site,weatype):

    value = []    
    # path of first year
    if year2no > 2025:
        filename = "G:/TCCIP WEA/TCCIP統計降尺度日資料_AR5/AR5_統計降尺度_日資料_%s_%s/AR5_統計降尺度_日資料_%s_%s_%s_%s_%d.csv" %(
            site,weatype,site,weatype,RCP,modelName,year2no-1)
        #print(filename)
    else:
        filename = "G:/TCCIP WEA/臺灣歷史氣候重建資料_5km/TReAD_日資料_%s_%s/TReAD_日資料_%s_%s_%d.csv" %(
            site,weatype,site,weatype,year2no-1)
    # read weather of first year
    with open(filename, newline='') as csvfile:
        wea = csv.reader(csvfile, delimiter = ',')
        next(wea) # skip header
        for row in wea:
            if float(row[0]) == lon and float(row[1]) == lat:                
                for d in range(365 + 2):
                    if d < 2: 
                        continue
                    value.append(float(row[d]))
                            #print(row[d])
    # read year 2
    filename = "G:/TCCIP WEA/TCCIP統計降尺度日資料_AR5/AR5_統計降尺度_日資料_%s_%s/AR5_統計降尺度_日資料_%s_%s_%s_%s_%d.csv" %(
        site,weatype,site,weatype,RCP,modelName,year2no)

    with open(filename, newline='') as csvfile:
        wea = csv.reader(csvfile, delimiter = ',')
        next(wea) # skip header
        for row in wea:
            if float(row[0]) == lon and float(row[1]) == lat:
                for d in range(365 + 2):
                    if d < 2:
                        continue
                    value.append(float(row[d]))
    return value
                             

def read2YrWeaHist(year2no,lon,lat,site,weatype):
    value = []    
    # path of first year
    filename = "G:/TCCIP WEA/臺灣歷史氣候重建資料_5km/TReAD_日資料_%s_%s/TReAD_日資料_%s_%s_%d.csv" %(
        site,weatype,site,weatype,year2no-1)
    # read weather of first year
    with open(filename, newline='') as csvfile:
        wea = csv.reader(csvfile, delimiter = ',')
        next(wea) # skip header
        for row in wea:
            if float(row[0]) == lon and float(row[1]) == lat:            
                for d in range(dayNumbers(year2no-1) + 2):
                    if d < 2: 
                        continue
                    value.append(float(row[d]))
                            #print(row[d])
    # read year 2
    filename = "G:/TCCIP WEA/臺灣歷史氣候重建資料_5km/TReAD_日資料_%s_%s/TReAD_日資料_%s_%s_%d.csv" %(
        site,site,year2no)

    with open(filename, newline='') as csvfile:
        wea = csv.reader(csvfile, delimiter = ',')
        next(wea) # skip header
        for row in wea:
            if float(row[0]) == lon and float(row[1]) == lat:
                for d in range(dayNumbers(year2no) + 2):
                    if d < 2:
                        continue
                    value.append(float(row[d]))
    return value

def selectTemp(year1no,wealist):
    # select temperature    
    nonLeap = [0,1,32,60,91,121,152,182,213,244,274,305,335]
    Leap = [0,1,32,61,92,122,153,183,214,245,275,306,336]
       
    value = []
    # select start day
    if year1no%4 == 0:
        start = Leap[10] # 從10月DOY 275 開始讀氣象
        year1days = 366
    else:
        start = nonLeap[10] # 從DOY 274 開始讀氣象
        year1days = 365
    
    # select end day
    if (year1no+1)%4 == 0:
        end = year1days + Leap[3] # 隔年3月前的氣象全讀
    else:
        end = year1days + nonLeap[3] 
    
    DOY = 1
    for tmp in wealist:
        if DOY < (start -1):
            continue
        value.append(tmp)
        if DOY > end:
            break
        DOY += 1
        #print(DOY)
    return value # end of the function
        

if __name__ == "__main__" : 
    
    year = 2028
    # delta = timedelta(days =1)
    
    tempLst = read2YrWea("rcp26","canESM2",year,120.85,24.35,"北部")

    # dayStart = datetime.strptime("%d/10/01" %(year-1),"%Y/%m/%d")
    # dayEnd = datetime.strptime("%d/03/01" %year,"%Y/%m/%d")
    # Date0 = datetime.strptime("%d/01/01" %(year-1),"%Y/%m/%d")

    counter = 0
    # 玉荷包的積溫
    endGDD = 60.37
    Tbase = 0
    Topt = 19.8
    Tmax = 21.9
    
    DOY = 0
    GDD = 0
    for tmp in tempLst:
        DOY += 1

        if DOY < 274 or DOY > 424:
            # DOY 274  十月1日
            # DOY 424  二月28日
            continue
 
        #print (date, tmp)
        GDD += beta_fn(tmp,Tbase,Topt,Tmax)
        if GDD >= endGDD:
            print(DOY2DATE(year,DOY),GDD)
            break
        
        print(DOY2DATE(year,DOY),GDD)

        
    # print(DOY2DATE(2018,415))

   

    
