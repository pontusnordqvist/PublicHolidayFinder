#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  8 17:03:49 2021

@author: Pontus Nordqvist
@email: p.nordq@gmail.com
"""
import os
import pandas as pd

filename = 'CleanHolidayData2016-2022'
data_path = os.path.join(os.getcwd(),f'Data/CleanedData/{filename}.csv')
holiday_df = pd.read_csv(data_path)


holiday_df['Year'] = pd.DatetimeIndex(holiday_df['Date']).year
#summary_table = holiday_df.groupby(['Alpha-3 code','Year']).size()
summary_table = holiday_df.groupby(['Alpha-3 code','Year'])['Holiday'].nunique()
#summary_table = holiday_df.groupby(['Alpha-3 code','Year']).unique()
#summary_table.plot.bar(x='Alpha-3 code', y='val')

#Norway and Sweden is wrong, involves Sunday :O 
#Clean the data
holiday_df = holiday_df[~holiday_df['Holiday'].isin(['Söndag', 'Søndag'])]

summary_table = holiday_df.groupby(['Alpha-3 code','Year']).size()
#Better! :) 
#Need to pivot
summary_table = summary_table.unstack(level=-1)
 

