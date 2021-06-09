#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  8 14:51:34 2021

@author: Pontus Nordqvist
@email: p.nordq@gmail.com
"""

import os
import pandas as pd

filename = 'CleanHolidayData2016-2022'
data_path = os.path.join(os.getcwd(),f'../Data/CleanedData/{filename}.csv')
holiday_df = pd.read_csv(data_path)

summary_table = holiday_df.groupby(['Alpha-3 code','Year'])

summary_table.head()

summary_table = summary_table['Holiday'].nunique()

summary_table.head(20)

summary_table = summary_table.unstack(level=-1)