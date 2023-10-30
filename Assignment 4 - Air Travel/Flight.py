"""
Name: James Wong
    Date: Dec 7 2022
    Professor: Brian Sarlo
    Class: 1026A - 002
    Python Ver: 3.9
    Program: The Flight file must contain a class called Flight. Note that this file must import from Airport as
            it makes use of Airport objects; add the line from Airport import * to the top of the Flight
            file. Other than this import line, everything in this file must be in the Flight class. Do not have
            any other code in the file that isn't part of this class. As suggested by its name, this class
            represents a Flight from one Airport to another Airport in the program. Each Flight object must
            have a flightNo (a unique 6-character code containing 3 letters followed by 3 digits), an origin,
            and a destination.
"""
from Airport import *   # import Airport File

class Flight:

    #  initialize the instance variables _flightNo, _origin, and _destination
    def __init__(self, flightNo, origin, destination):

        # check that both origin and destination are Airport object
        if isinstance(origin, Airport) and isinstance(destination, Airport):
            self._flightNo = flightNo
            self._flightOrigin = origin
            self._flightDestination = destination
        # If either or both are not Airport objects, raise a TypeError
        else:
            raise TypeError("The origin and destination must be Airport objects")

    # return a flight statement that classifies each flight as domestic or international
    def __repr__(self):
        if self.isDomesticFlight() == True:     # if the flight is domestic
            return "Flight: " + str(self._flightNo) + " from " + str(self._flightOrigin.getCity()) + " to " + str(self._flightDestination.getCity()) + " {domestic}"
        else:       # if the flight is international
            return "Flight: " + str(self._flightNo) + " from " + str(self._flightOrigin.getCity().title()) + " to " + str(self._flightDestination.getCity().title()) + " {international}"

    # returns True if self and other are considered the same Flight:
    def __eq__(self, other):
        if isinstance(other, Flight):       # check if other is a flight object

            # returns True if the flight origin and destination code of both self and other
            if self._flightOrigin.getCode() == other._flightOrigin.getCode() and self._flightOrigin.getCity() == other._flightOrigin.getCity() and self._flightOrigin.getCountry() == other._flightOrigin.getCountry():
                return True
            elif self._flightDestination.getCode() == other._flightDestination.getCode() and self._flightDestination.getCity() == other._flightDestination.getCity() and self._flightDestination.getCountry() == other._flightDestination:
                return True
            else:
                return False
        else:   # returns False if variable is not a Flight object
            return False

    # Getter that returns the Flight number code
    def getFlightNumber(self):
        return self._flightNo

    # Getter that returns the Flight origin
    def getOrigin(self):
        return self._flightOrigin

    # Getter that returns the Flight destination
    def getDestination(self):
        return self._flightDestination

    # returns True if the flight's origin country is the same as the flight's destination country
    def isDomesticFlight(self):
        return self._flightOrigin.getCountry() == self._flightDestination.getCountry()

    # Setter that sets (updates) the Flight origin
    def setOrigin(self, origin):
        self._flightOrigin = origin

    # Setter that sets (updates) the Flight destination
    def setDestination(self, destination):
        self._flightDestination = destination