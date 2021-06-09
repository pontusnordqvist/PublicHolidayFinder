#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 13:12:01 2021

@author: Pontus Nordqvist
@email: p.nordq@gmail.com
"""
import os
import pandas as pd
from holidays.utils import list_supported_countries, CountryHoliday

def dataMiner(year_intervall, save_name):
    supported_countries = list_supported_countries()
    supported_countries = pd.DataFrame({'Alpha-3 code':supported_countries})
    
    iso_path = os.path.join(os.getcwd(),
                            '../Data/ISOCodes/wikipedia-iso-country-codes.csv')
    iso_country = pd.read_csv(iso_path)
    
    
    common_countries = pd.merge(supported_countries, iso_country,
                                how ='inner',
                                on = 'Alpha-3 code')
    
    years = [year for year in range(year_intervall[0],year_intervall[1])]
    output_df = pd.DataFrame(columns=['Country code','Date','Holiday'])
    
    for country in common_countries['Alpha-3 code']:
        holiday_obj = CountryHoliday(country, years=years)
        country_list = [country] * len(holiday_obj)
        add_df = pd.DataFrame({'Country code' : country_list,
                               'Date' : list(holiday_obj.keys()),
                          'Holiday' : list(holiday_obj.values())})
        output_df = pd.concat([output_df,add_df])
    
    output_df = pd.merge(output_df, iso_country,
                         how='left',
                         left_on='Country code',
                         right_on='Alpha-3 code')
    
    output_df = output_df.drop(columns = 'Country code',axis=1)
    output_df.rename({'English short name lower case': 'Country'}, axis=1,
                     inplace=True)
    output_df['Country'] = output_df['Country'].map(lambda name: name.lower())
    
    output_path = os.path.join(os.getcwd(),
                            f'../Data/MinedData/{save_name}.csv')
    output_df.to_csv(output_path)

dataMiner((2016,2023),'HolidayData2016-2022')
