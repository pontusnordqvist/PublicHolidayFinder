#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 15:42:10 2021

@author: Pontus Nordqvist
@email: p.nordq@gmail.com
"""
import os
import pandas as pd

iso_path = os.path.join(os.getcwd(),
                        '../Data/ISOCodes/wikipedia-iso-country-codes.csv')
iso_country = pd.read_csv(iso_path)

filename = 'HolidayData2016-2022'
data_path = os.path.join(os.getcwd(),f'../Data/MinedData/{filename}.csv')
holiday_df = pd.read_csv(data_path)

output_df = pd.merge(holiday_df, iso_country,
                            how ='inner',
                            left_on = 'Country code',
                            right_on = 'Alpha-3 code')

output_df.head()

output_df = output_df.drop(columns = ['Unnamed: 0', 'Country code'], axis=1)

output_df.rename({'English short name lower case': 'Country'}, axis=1,
                 inplace=True)

output_df['Country'] = output_df['Country'].map(lambda name: name.lower())

output_df['Year'] = pd.DatetimeIndex(output_df['Date']).year

output_df.head()

output_df = output_df[~output_df['Holiday'].isin(['Söndag', 'Søndag'])]

output_df = output_df[output_df['Alpha-3 code'] != 'ISR']

save_name = 'CleanHolidayData2016-2022'
output_path = os.path.join(os.getcwd(),
                            f'../Data/CleanedData/{save_name}.csv')
output_df.to_csv(output_path)