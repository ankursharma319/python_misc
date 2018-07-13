# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:10:05 2015

@author: Akhil
"""

import urllib


def line_averages(filename):
    """open file by filename. compute the average value for every line,
    and return the average values in a list"""
    fr = open(filename, 'r')
    rawData = fr.read()
    fr.close()

    averagesList = []
    lines = rawData.strip().split("\n")

    for eachLine in lines:
        numbers = eachLine.strip().split(',')
        print("---___---")
        print(numbers)
        print("---___---")
        sum = 0.0
        n = 0.0
        for number in numbers:
            if(number.strip() != ""):
                try:
                    sum += float(number)
                    n += 1
                except ValueError:
                    print("Error encountered")
        if(n > 0):
            averagesList.append(sum/n)
    return averagesList


def noaa_string():
    """Returns the content of the txt file containing
    current conditions in Southampton as string"""
    url = "http://weather.noaa.gov/pub/data" +\
        "/observations/metar/decoded/EGHI.TXT"
    noaa_data_string = urllib.urlopen(url).read()
    return noaa_data_string


def noaa_temperature(s):
    """Returns the temperature at Southampton in degrees Celsiuis"""
    temp = 0
    lines = s.split("\n")

    for line in lines:
        if line.startswith("Temperature"):
            tempString = line.split("(")[1].split(")")[0].split("C")[0].strip()
            temp = int(tempString)
    return temp
