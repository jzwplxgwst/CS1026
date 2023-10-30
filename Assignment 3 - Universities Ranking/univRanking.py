"""
Name: James Wong
    Date: Nov 17 2022
    Professor: Brian Sarlo
    Class: 1026A - 002
    Python Ver: 3.9
    Program: Read the files and find the,
                1. Total number of universities     (TopUni.csv)
                2. List all available countries     (TopUni.csv)
                3. List all available continents    (capitals.csv)
                4. The university with top international rank
                5. The university with top national rank
                6. The average score of all universities
                7. The continents relative score
                8.  The capital city
                9. The universities that hold the capital name
    TopUni.csv: This file contains data about the universities ranking nationally and internationally. The data is stored in a comma
                separated file (.CSV).
    capitals.csv: This file contains geographical data for several countries around the world. The data is stored in a comma separated
                  file (.CSV).
"""
def getInformation(sCountry, topuni,capital):
    import csv
    with open(topuni, newline='') as TopUni:        #opens and saves the file topuni
        TOPUNI = csv.reader(TopUni)
        inFile1 = list(TOPUNI)                      #stores the file in a list
    with open(capital, newline='') as capital:      #opens and saves the file capital
        CAPITAL = csv.reader(capital)
        inFile2 = list(CAPITAL)                     #stores the file in a list
    output = open("output.txt", 'w')

    #1.
    Countries = []
    universities = []
    for i in range(1,len(inFile1)):                     #loop that runs to append all countries and universities.
        universities.append(inFile1[i][1].upper())      #appends all universities. This will be used for #2.
        if inFile1[i][2].upper() not in Countries:      #append only unique values
            Countries.append(inFile1[i][2].upper())


    output.write("Total number of universities is => " + str(len(universities)) + '\n')
    #2.
    allCOuntries = "Available countries ==> "               #seting up output
    for i in Countries:                                     #loops to look through the Countries array.
        allCOuntries = allCOuntries + i.upper() + ', '      #setting up the output
    allCOuntries = allCOuntries.rstrip(", ")                #removes ', ' at the end.
    output.write(allCOuntries)                              #outputs it.
    #3.
    Continents = []
    for i in Countries:
        for j in range(1,len(inFile2)):                                                 #checks each continent in capitals.csv
            if inFile2[j][0].upper() == i and inFile2[j][5].upper() not in Continents:  #compares if the value is in the array cpuntries and if the input has already been registered
                Continents.append(inFile2[j][5].upper())                                #if the value is in array and it's not a;ready been added to Continents, then it will be added
    ContinentsOutput = "\nAvailable Continents => "
    for i in Continents:
        ContinentsOutput = ContinentsOutput + i + ', '      #defining the final input
    ContinentsOutput = ContinentsOutput.rstrip(', ')        #strips the last comma and space
    output.write(ContinentsOutput)                          #writes it to the files
    #4.
    sCountry = sCountry.upper()                 #This is here to make everything user inputs into upper case. Its basically here to make cases not matter from here on out.
    selectedUniversities = []
    nationalRanks = []                          #used in number 5.
    WorldRank = []
    for i in range(1,len(inFile1)):
        if inFile1[i][2].upper() == sCountry:                   #checking if the country in inFile1 is the selected country
            WorldRank.append(inFile1[i][0])                     #add the world rank
            selectedUniversities.append(inFile1[i][1].upper())  #add the institution name
            nationalRanks.append(inFile1[i][3].upper())         #Add the national Rank. used in number 5.
    TopUniversity = selectedUniversities[0]                     #first index in topUniversity should be the highest rank.
    TopUniversityRank = WorldRank[0]                            #same with this.
    output.write("\nAt International Rank => " + TopUniversityRank + " the university name is => " + TopUniversity)

    #5.
    highestNationalRank = min(nationalRanks)                #min() gives the lowest value, which is the highest national rank
    # setting TopNationalUni to the selectedUniversities which should be the same as selectedUniversities
    TopNationalUni = selectedUniversities[nationalRanks.index(highestNationalRank)]
    output.write("\nAt national Rank => " + str(highestNationalRank) + " the university name is => " + TopNationalUni)

    #6.
    Scores = []
    for i in range(1, len(inFile1)):                #runs through all the data
        if inFile1[i][2].upper() == sCountry:       #compares the data to match selectedCountry
            Scores.append(float(inFile1[i][8]))     #adds the score
    total = 0                                       #defining total
    for i in Scores:
        total = total + i                           #find the number of scores
    Average = total/len(Scores)                     #find the average of the score.
    output.write('\nThe average score => {:0.2f}.'.format(Average) + ' %')

    #7.
    selectedContinent = ''
    CountinentCountries = []
    CountryScores = []
    for i in range(1, len(inFile2)):                        #run through all the code
        if inFile2[i][0].upper() == sCountry:               #compares the values with the input
            selectedContinent = inFile2[i][5].upper()       #adds the continent of the selected country
    for i in range(1, len(inFile2)):                        #run through all the code
        if inFile2[i][5].upper() == selectedContinent:      #compares the values with the input
            CountinentCountries.append(inFile2[i][0])       #puts all the countries of the selectedContinent into a list of countries
    for i in range(1,len(inFile1)):                         #run through all the code
        for country in CountinentCountries:                 #runs through all the data in the list of selected countries
            if inFile1[i][2] == country:                    #compares the values with the input
                CountryScores.append(float(inFile1[i][8]))  #put the scores of CountinentCountries in a list
    RelBottom = max(CountryScores)                          #max() is the largest value.
    Relscore = (Average/RelBottom)*100                      #use the average from question 6, and calculate the relative score
    output.write("\nThe relative score to the top university in " + selectedContinent + " is => ("+str(Average)+"/"+str(RelBottom)+" x 100% = {:0.2f}".format(Relscore))

    #8.
    capital = ''
    for i in range(1, len(inFile2)):                #runs through all the data
        if inFile2[i][0].upper() == sCountry:       #compares the countries
            capital = inFile2[i][1].upper()         #add the capital
    output.write("\nThe capital is => " + capital)  #write to output.txt file

    #9.
    CapitalUnis = []
    for i in range(1,len(inFile1)):     # runs through all the data
        if inFile1[i][2].upper() == sCountry and capital in inFile1[i][1].upper():  #compares the values
            CapitalUnis.append(inFile1[i][1].upper())                               #add the value to the list
    output.write("\nThe universities that contain the capital name => ")
    count = 0
    for i in CapitalUnis:       #add the number of universities
        count = count + 1
        output.write("\n#"+str(count)+ " " + i)

    output.close()

getInformation("china", "TopUni.csv", "capitals.csv")