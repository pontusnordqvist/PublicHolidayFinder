#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 12:30:34 2021

@author: Pontus Nordqvist
@email: p.nordq@gmail.com
"""
import os
import datefinder
import pandas as pd

#TODO: Add path if they don't exist
class PublicHolidayChecker():
    """
    Class for the inference of the cleaned data. 
    """
    
    def __init__(self, file = 'CleanHolidayData2016-2022.csv'):
        """
        Constructor for the class.

        Parameters
        ----------
        file : str, optional
            DESCRIPTION. Dataset to load, in .csv format. 
                         The default is 'CleanHolidayData2016-2022.csv'.

        Returns
        -------
        None.

        """
        #Defaults to the cleaned dataset
        self.data_path = os.path.join(os.getcwd(),
                        f'Data/CleanedData/{file}')
        
    def run(self):
        """
        Method to run the API for the inference of the cleaned data.

        Returns
        -------
        None.

        """
        #Initial welcome prints
        print('-'*70)
        print(' '*15+"""Welcome to PN public holiday checker.
               To quit, type: exit.\n""")
        print('-'*70)
        running = True
        
        #Enables custom input
        print('Please specify a data path. Press "Enter" to use the default.')
        data_path = input('Data path: ')
        
        #Enter = blankspace = dafualt dataset
        if data_path == '':
            print(f'No path specified. Using: {self.data_path}')
        elif data_path.lower() == 'exit':
                print('Bye bye!')
                running = False 
        else:
            self.data_path = data_path          
    
        while(running):   #While(True) is a sinn 
            #Data input
            print("""Please specify a date (from 2016 to 2022) to query public
                  holiday. Type "exit"  to quit.""")
            date = input('Date: ')
            date = date.lower()
            if date == 'exit':
                print('Bye bye!')
                running = False
                break
            
            #Country input
            print(""""Please specify a country to query public holiday. Type 
                  "exit" to quit.""")
            country = input('Country: ')
            country = country.lower()
            if country == 'exit':
                print('Bye bye!')
                running = False
                break
    
            self.checker(date, country)
            print('-'*70)

    def checker(self, date, country):
        """
        Method to check if date and country exist in the dataset.

        Parameters
        ----------
        date : str
            DESCRIPTION. Input date to infer. Can only handle singel dates.
                         Will identify the date using the package datefinder.
                        
        country : str
            DESCRIPTION. Country to infer. Can handle case insensitive inputs
                         of Three and two digit ISO and normal name.

        Returns
        -------
        None.

        """
        #Check and fix the inputs
        date, country, validity, country_type = self.__inputHandler(date,
                                                                    country)
        
        #Flag to keep track of invalid inputs
        invalid_input = False
        
        #Prints out error if any
        for k,v in validity.items():
            if v == True:
                invalid_input = True
                print('Invalid input detected! The error is:')
                print(k)
            
        #Check if the country exist
        if not invalid_input:
            data = pd.read_csv(self.data_path)
            if not (data[country_type] == country).any():
                print(f'The Country "{country}" is not yet supported!')
                invalid_input = True 
            
        if invalid_input:
            print('Please retry with an valid input!')
        else: #here we go if no errors are found
            
            #Probably what you're looking for ;) 
            query = data[(data['Date']==date) & 
                         (data[country_type]==country)]
            
            #Make nicer printout
            if country_type == 'Country':
                country = country.capitalize()
                
            if query.empty:
                print(f"""No public holiday exists for the date {date} in the
                      country {country}.""")
            else:
                print( f"""The holiday "{query["Holiday"].iat[0]}" exists for
                      the date {date} and country {country}.""")


    def __inputHandler(self,date, country):
        """
        Help method to check if the inputs are valid and will identify the 
        typ of the inputed country query. 

        Parameters
        ----------
        date : str
            DESCRIPTION. Date to check.
        country : str
            DESCRIPTION. Country to check and get country type from.

        Returns
        -------
        date : str
            DESCRIPTION. Correctly formated date for inference.
        country : str
            DESCRIPTION. Country input
        validity : dict
            DESCRIPTION. Error dictionary
        country_type : str
            DESCRIPTION. Type of the country, i.e the format of it.

        """
        #Flag, to stop the rest from activatiing if found
        empty_input = False
        #Error dict
        validity = {'Date input empty' : False,
                    'Country input empty' : False,
                    'Multiple dates detected' : False,
                    'Year smaller than 2016' : False,
                    'Year bigger than 2022' : False,
                    'Invalid country name' : False,
                    'Invalid day' : False,
                    'Invalid month' : False}
        
        #Checs for empty input
        if date == '':
            validity['Date input empty'] = True
            empty_input = True
            
        if country == '':
            validity['Country input empty'] = True
            empty_input = True
    
        if not empty_input:
            #Package to find date
            dates = datefinder.find_dates(date)
            try:
                date = next(dates) #dates is a generator object
                year = int(date.year)
                day = int(date.day)
                month = int(date.month)
                date = str(date.date())
                
                #Sanity checks for the dates
                if year < 2016:
                    validity['Year smaller than 2016'] = True
                elif year > 2022:
                    validity['Year bigger than 2022'] = True
                if day not in [i for i in range(1,32)]:
                    validity['Invalid day'] = True
                if month not in [i for i in range(1,13)]:
                    validity['Invalid month'] = True
                
            except StopIteration:
                #Goes here if multiple dates are found
                validity['Multiple dates detected'] = True
        
        #Get the country type by looking at length of country.
        #P.s there is no country with 3 or less letter
        country_type = None
        if len(country) > 3:
            country_type = 'Country'
            country = country.lower()
        elif len(country) == 3:
            country_type = 'Alpha-3 code'
            country = country.upper()
        elif len(country) == 2:
            country_type = 'Alpha-2 code'
            country = country.upper()
        else:
            validity['Invalid country name'] = True
            
        return date, country, validity, country_type
            
        
if __name__ == "__main__":
    phf = PublicHolidayChecker()
    phf.run()
