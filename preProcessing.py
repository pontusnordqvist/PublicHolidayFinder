#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 18:41:20 2021

@author: Pontus Nordqvist
@email: p.nordq@gmail.com
"""
import os
import pandas as pd

filename = 'HolidayData2016-2022'
data_path = os.path.join(os.getcwd(),f'Data/MinedData/{filename}.csv')
holiday_df = pd.read_csv(data_path)


holiday_df['Year'] = pd.DatetimeIndex(holiday_df['Date']).year
#summary_table = holiday_df.groupby(['Alpha-3 code','Year']).size()
#Grooping
summary_table = holiday_df.groupby(['Alpha-3 code','Year'])
#Obtain unique holidays
summary_table = summary_table['Holiday'].nunique()

#Norway and Sweden is wrong, involves Sunday :O 
#Clean the data
holiday_df = holiday_df[~holiday_df['Holiday'].isin(['Söndag', 'Søndag'])]
#Still isreal is way off, let's just drop it for now 
holiday_df = holiday_df[holiday_df['Alpha-3 code'] != 'ISR']

save_name = 'CleanHolidayData2016-2022'
output_path = os.path.join(os.getcwd(),
                            f'Data/CleanedData/{save_name}.csv')
holiday_df.to_csv(output_path)

