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

#TODO: Error handling, check string first, fix better print_out country
class PublicHolidayChecker():
    
    def __init__(self, file = 'CleanHolidayData2016-2022.csv'):
        #self.cwd = os.getcwd()
        self.data_path = os.path.join(os.getcwd(),
                        f'Data/CleanedData/{file}')
        #self.data = None
        
    def run(self):
        print('-'*70)
        print(' '*15+"""Welcome to PN public holiday checker.
               To quit, type: exit.\n""")
        print('-'*70)
        running = True
        
        print('Please specify a data path. Press "Enter" to use the default.')
        data_path = input('Data path: ')
        
        #valid_path = os.path.exists(self.data_path)
        #while(valid_path):
        if data_path == '':
            #self.data_path = os.path.join(self.cwd,
             #           'Data/CleanedData/CleanHolidayData2016-2022.csv')
            print(f'No path specified. Using: {self.data_path}')
        elif data_path.lower() == 'exit':
                print('Bye bye!')
                running = False 
        else:
            self.data_path = data_path
          #  else: broken
          #      print('Path does not exist! Try again.')
          #      self.data_path = input('Data path: ')
          #      valid_path = not os.path.exists(self.data_path)
            
    
        while(running):     
            print("""Please specify a date (from 2016 to 2022) to query public
                  holiday. Type "exit"  to quit.""")
            date = input('Date: ')
            date = date.lower()
            if date == 'exit':
                print('Bye bye!')
                running = False
                break
            
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
        
        print(f'Date: {date}')
        print(f'Country: {country}')
        date, country, validity, country_type = self.__inputHandler(date,
                                                                    country)
        invalid_input = False
        #validity = self.__checkValidInput(date, country)
        
        
        for k,v in validity.items():
            if v == True:
                invalid_input = True
                print('Invalid input detected! The error is:')
                print(k)
                
        #date, country = self.__convertInput(date, country)
        
        if date == None:
            invalid_input = True
            print('Invalid input detected! The error is: multiple dates input')
            
        if not invalid_input:
            data = pd.read_csv(self.data_path)
            if not (data[country_type] == country).any():
                print(f'The Country "{country}" is not yet supported!')
                invalid_input = True 
            
        if invalid_input:
            print('Please retry with an valid input!')
        else:
                
            query = data[(data['Date']==date) & 
                         (data[country_type]==country)]
             #            (data['Alpha-3 code'].str.lower()==country)]
        
            #if len(query) == 0:
            if country_type == 'Country':
                country = country.capitalize()
                
            if query.empty:
                print(f"""No public holiday exists for the date {date} in the
                      country {country}.""")
            else:
                print( f"""The holiday "{query["Holiday"].iat[0]}" exists for
                      the date {date} and country {country}.""")

    #def __checkValidInput(self, date, country):
    def __inputHandler(self,date, country):
        empty_input = False
        validity = {'Date input empty' : False,
                    'Country input empty' : False,
                    'Multiple dates detected' : False,
                    'Year smaller than 2016' : False,
                    'Year bigger than 2022' : False,
                    'Invalid country name' : False,
                    'Invalid day' : False,
                    'Invalid month' : False}
        if date == '':
            validity['Date input empty'] = True
            empty_input = True
            
        if country == '':
            validity['Country input empty'] = True
            empty_input = True
    
    #def __convertInput(self, date, country):
        if not empty_input:
            dates = datefinder.find_dates(date)
            try:
                date = next(dates)
                year = int(date.year)
                day = int(date.day)
                month = int(date.month)
                date = str(date.date())
                
                if year < 2016:
                    validity['Year smaller than 2016'] = True
                elif year > 2022:
                    validity['Year bigger than 2022'] = True
                if day not in [i for i in range(1,32)]:
                    validity['Invalid day'] = True
                if month not in [i for i in range(1,13)]:
                    validity['Invalid month'] = True
                
            except StopIteration:
                #print(f""""Multiple dates entered!}""")
                validity['Multiple dates detected'] = True
        
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
    #print(f'WD: {os.getcwd()}')
    #publicHolidayChecker('2016-01-01','ABW')
    #publicHolidayChecker('2016-04-01','ABW')
    #ABW, 2016-01-01
    #main()
    phf = PublicHolidayChecker()
    phf.run()
