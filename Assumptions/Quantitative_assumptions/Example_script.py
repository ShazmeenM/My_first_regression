# importing required libararies and dataset
import numpy as np
import pandas as pd
housing_sale_price = pd.read_excel("D:\\git_demo\\Data/Housing_data.xlsx", sheet_name="median_sale_price")
housing_sale_price_regions = pd.read_excel("D:\\git_demo\\Data/Housing_data.xlsx", sheet_name="median_sale_price_regions")

# Assumption: House price should always be a positive number.
# Quality: RED
# Impact: AMBER
# Detailed description: We assume that no house is sold for a negative amount or for no value.

# testing the above assumption. It will return true if the assumptions holds and false otherwise.
test_neg = ((housing_sale_price['Detached' or 'Semi-detached' or 'Terraced' or 'Flats']) < 0).any()
print (test_neg)
print("Status description: A true means there is a negative value(Fail). A false means there is no negative value (Pass).")

# printing location of failures
housing_sale_price_neg = housing_sale_price[(housing_sale_price['Detached']<0) | (housing_sale_price['Semi-detached']<0) | (housing_sale_price['Terraced']<0) | (housing_sale_price['Flats']<0)]
print(housing_sale_price_neg)

# Assumption: Current trends in price will continue.
# Quality: RED
# Impact: AMBER
# Detailed description: We assume that the median sale price of each dwelling type in a local authority in time 't' should be less than time 't+1'.

# testing the above assumption.

# grouping rows (LA_Name) by columns (Year)
group = housing_sale_price.groupby(['LA_Name', 'Year'], as_index=False)[['Detached', 'Semi-detached', 'Terraced', 'Flats']].first()

# computing row differences across groups
group['Detached_trend'] = group['Detached'].diff()
group['Semi-detached_trend'] = group['Semi-detached'].diff()
group['Terraced_trend'] = group['Terraced'].diff()
group['Flats_trend'] = group['Flats'].diff()

# Using drop() to delete rows in which Year < 2001
group.drop(group[group['Year'] < 2001].index, inplace = True)

# printing location of failures
house_price_trend_neg = group[(group['Detached_trend']<0) | (group['Semi-detached_trend']<0) | (group['Terraced_trend']<0) | (group['Flats_trend']<0)]
print(house_price_trend_neg)

# Assumption: There is regional variation in house prices.
# Quality: RED
# Impact: AMBER
# Detailed description: We assume that median house prices of all dwelling types in London exceeds median house prices for every other region in England and Wales each year. 

# function testing the above assumption. It will return true if the assumptions holds and false otherwise.
def comparing_rows_columns():
    for x in housing_sale_price_regions[housing_sale_price_regions['LA_Name'] == 'London']['Detached']:
      for y in housing_sale_price_regions[housing_sale_price_regions['LA_Name'] != 'London']['Detached']:
          return x > y

comparing_rows_columns()

