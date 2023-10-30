"""
Name: James Wong
    Date: Dec 7 2022
    Professor: Brian Sarlo
    Class: 1026A - 002
    Python Ver: 3.9
    Program:The Airport file must contain a class called Airport. Everything in this file must be in the Airport
            class. Do not have any code in the file that isn't part of this class. As suggested by its name, this
            class represents an Airport in the program. Each Airport object must have a unique 3-letter
            code which serves as an ID, a city, and a country which are strings representing its geographical
            location.
"""
class Airport:

    # Initialize the instance variables _code, _city, and _country based on the corresponding parameters in the constructor
    def __init__(self, code, city, country):
        self._airportCode = code
        self._airportCity = city
        self._airportCountry = country

    # Return the representation of this Airport
    def __repr__(self):
        return self._airportCode + " (" + self._airportCity + ", " + self._airportCountry + ")"

    #  Getter that returns the Airport code
    def getCode(self):
        return self._airportCode

    # Getter that returns the Airport city
    def getCity(self):
        return self._airportCity

    # Getter that returns the Airport country
    def getCountry(self):
        return self._airportCountry

    # Setter that sets (updates) the Airport city
    def setCity(self, city):
        self._airportCity = city

    # Setter that sets (updates) the Airport country
    def setCountry(self, country):
        self._airportCountry = country

"""a = Airport("YVR", "Vancouver", "Canada")
print(a)"""