#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 10:44:35 2021

@author: Pontus Nordqvist
@email: p.nordq@gmail.com
"""
from holidays.utils import list_supported_countries, CountryHoliday

import os
import pandas as pd

supported_countries = list_supported_countries()
supported_countries = pd.DataFrame({'Holidays countries':supported_countries})

output_df = pd.DataFrame(columns=['Country code','Date','Holiday'])
years = [year for year in range(2016,2023)]

for country in supported_countries['Holidays countries']:
    holiday_obj = CountryHoliday(country, years=years)
    country_list = [country] * len(holiday_obj)
    add_df = pd.DataFrame({'Country code' : country_list,
                           'Date' : list(holiday_obj.keys()),
                      'Holiday' : list(holiday_obj.values())})
    output_df = pd.concat([output_df,add_df])
    
output_df.head()

file_name = 'HolidayData2016-2022'
output_path = os.path.join(os.getcwd(),f'../Data/MinedData/{file_name}.csv')
output_df.to_csv(output_path)

iso_path = os.path.join(os.getcwd(),
                        '../Data/ISOCodes/wikipedia-iso-country-codes.csv')
iso_country = pd.read_csv(iso_path)