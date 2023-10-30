"""
Name: James Wong
    Date: Dec 7 2022
    Professor: Brian Sarlo
    Class: 1026A - 002
    Python Ver: 3.9
    Program: This file is meant to be the core of the program from which the Airport and Flight objects
            should be created as their corresponding text files are loaded in; and several functions must be
            implemented to analyze the data and retrieve results about specific queries.
"""

from Flight import *        # imported Flight file
from Airport import *       # imported Airport file

allAirports = []    # container to hold all the Airports
allFlights = {}     # container to hold all the Flights

# read in all the data from the airports file and flights file
def loadData(airportFile, flightFile):

    try:    # try reading in the database with the airports
        inAirportFile = open(airportFile, "r")  # open airport reader

        # removing all whitespace
        for line in inAirportFile:
            newAirport = line.replace("\n", "")
            newAirport = newAirport.replace("\t", "")
            newAirport = newAirport.replace(" ", "")
            newAirport = newAirport.split(",")

            allAirports.append(Airport(newAirport[0], newAirport[2], newAirport[1]))    # appending each airport to a list of all airports

        inAirportFile.close()       # close airport reader
    except IOError:     # catch if the file was unreadable or does not exist
        print("could not read or find airport file")
        return False
    except:     # catch for all other possible errors
        print("Error in Airport")
        return False

    try:        # try reading in the database with the airports
        inFlightFile = open(flightFile, "r")    # open flight reader

        # removing all whitespace
        for line in inFlightFile:
            newFlight = line.replace('\n', "")
            newFlight = newFlight.replace("\t", "")
            newFlight = newFlight.replace(" ", "")
            newFlight = newFlight.split(",")

            # turn the airport codes into airport objects
            holdOrig = getAirportByCode(newFlight[1])
            holdDest = getAirportByCode(newFlight[2])

            # hold the line of code as a flight object
            holdFlights = Flight(newFlight[0], holdOrig, holdDest)

            # if the origin is already in the list of all the flights
            if holdOrig.getCode() not in allFlights:
                allFlights[holdOrig.getCode()] = [holdFlights]  # add the line of code to the all flights list with the key as the origin code
            else:   # if the origin is not in the list of all Flights
                allFlights[holdOrig.getCode()].append(holdFlights)  # append the line of code to the all flights list using the key code

        inFlightFile.close()    # close the flight reader
    except IOError:     # catch if the file was unreadable or does not exist
        print("could not read or find flight file")
        return False
    except:     # catch for all other possible errors
        print("Error in Flight")
        return False

    return True     # returns the function successfully read the files

# Return the Airport object that has the given code
def getAirportByCode(code):

    # checking all airports in the airports list
    for airport in allAirports:
        if airport.getCode() == code:   # if any of the airports' code matches the user inputted code
            return airport
    # If there is no Airport found for the given code, just return -1
    return -1

# Return a list that contains all Flight objects that involve the given city either as the origin or the destination
def findAllCityFlights(city):

    allCityFlights = []     # create a list to holds all city flights

    # checking all flight values from the flights list
    for flights in allFlights.values():
        for i in flights:
            # if the origin city or destination city is the same as the user inputted city
            if i.getOrigin().getCity().upper() == city.upper() or i.getDestination().getCity().upper() == city.upper():
                allCityFlights.append(i)        # append the flight to the all city flights list
    return allCityFlights       # return the all city flights list

# Return a list that contains all Flight objects that involve the given country either as the origin or the destination
def findAllCountryFlights(country):

    allCountryFlights = []      # create a list that holds all country flights

    # checking all flight values from the flights list
    for flights in allFlights.values():
        for i in flights:
            # if the origin country and destination country is the same as the user inputted country
            if i.getOrigin().getCountry().upper() == country.upper() or i.getDestination().getCountry().upper() == country.upper():
                allCountryFlights.append(i)     # append the flight to the all country flights list
    return allCountryFlights        # return the all country flights list

# function that finds all flights inbetween two locations
def findFlightBetween(origAirport, destAirport):

    singleHop = set()   # create a set for singleHop

    # running through all the flights
    for i in range(len(allFlights[origAirport.getCode()])):
        # Check if there is a direct flight from origAirport to destAirport
        if allFlights[origAirport.getCode()][i].getDestination().getCode() == destAirport.getCode():
            return "Direct Flight: " + origAirport.getCode() + " to " + destAirport.getCode()   # return a string format
        else: # if there is no direct flight from origAirport to destAirport
            hold = allFlights[origAirport.getCode()][i].getDestination()    # hold the flight's destination of the leaving original city

            # running through all the flights with the original flight's destination
            for j in range(len(allFlights[hold.getCode()])):
                # if there is a direct flight from the original flight's destination to destAirport
                if allFlights[hold.getCode()][j].getDestination().getCode() == destAirport.getCode():
                    singleHop.add(allFlights[hold.getCode()][j].getOrigin().getCode())      # add the flight

    if len(singleHop) == 0:     # if single hop holds something
        return -1   # return -1
    else:       # if single hop doesn't hold anything
        return singleHop    # return the single hop

# find the Flight object that departs from origin B and arrives in destination A
def findReturnFlight(firstFlight):

    # running through all the flights code of the user input
    for i in allFlights[firstFlight.getDestination().getCode()]:
        # if a flight's destination code is equal to the user inputted origin's code
        if i.getDestination().getCode() == firstFlight.getOrigin().getCode():
            return i    # return the flight of the destination code
    return -1   # If there is no such Flight object that goes in the opposite direction as firstFlight, just return -1.