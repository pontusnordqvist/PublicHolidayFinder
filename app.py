#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 10:30:34 2021

@author: Pontus Nordqvist
@email: p.nordq@gmail.com
"""
import os
#import datefinder
import pandas as pd

#TODO: Error handling, check string first, fix better print_out country
def publicHolidayChecker(date, country):

    #date = datefinder(date)

    print(f'Date: {date}')
    print(f'Country: {country}')
    data_type = 'MinedData/CleanedHolidayData2016-2022.csv'
    #data_path = os.path.join(os.getcwd(), f'/Data/{data_type}') #Not working? :O
    data_path = os.getcwd() + f'/Data/{data_type}'
    
    print(f'Path: {data_path}')
    print(f'Root: {os.getcwd()}')
    data = pd.read_csv(data_path)

    query = data[(data['Date']==date) & (data['Alpha-3 code']==country)]

    #if len(query) == 0:
    if query.empty:
        print(f'No public holiday exists for the date {date} in the country {country}.')
    else:
        print( f"""The holiday "{query["Holiday"].iat[0]}" exists for the date {date}
              and country {country}.""")

def main():
    print("""Welcome to PN public holiday checker. Follow the instrution.
          To quit, type: exit.""")
    while(True):
        date = input("""Please specify a date to query public holiday.\n
                     Date: """)
        if date == 'exit':
            break

        country = input("""Please specify a country to query public holiday.\n
                        Country: """)
        if country == 'exit':
            break

        publicHolidayChecker(date, country)
    
if __name__ == "__main__":
    #print(f'WD: {os.getcwd()}')
    #publicHolidayChecker('2016-01-01','ABW')
    #publicHolidayChecker('2016-04-01','ABW')
    #ABW, 2016-01-01
    main()
