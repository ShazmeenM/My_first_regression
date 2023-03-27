# importing required libararies and dataset
import numpy as np
import pandas as pd
housing_sale_price = pd.read_excel("D:\\git_demo\\Data/Housing_data.xlsx", sheet_name="mean_sale_price")

# Assumption: House price should always be a positive number.
# Quality: RED
# Impact: AMBER
# Detailed description: We assume that no house is sold for a negative amount or for no value.

# Function testing the above assumption. It will return true if the assumptions holds and false otherwise.
test_neg = ((housing_sale_price['Detached' or 'Semi-detached' or 'Terraced' or 'Flats']) < 0).any()
print (test_neg)
print("Status description: A true means there is no negative values (Pass). A false means there is a negative value (Fail).")

# Assumption: Current trends in price will continue.
# Quality: RED
# Impact: AMBER
# Detailed description: We assume that the mean sale price of each dwelling type in a local authority in time 't' should be less than time 't+1'.

# Function testing the above assumption. It will return true if the assumptions holds and false otherwise.

# Assumption: There is no change in average house prices by local authority.
# Quality: RED
# Impact: AMBER
# Detailed description: We assume that there is no regional variation in house prices. 

# Function testing the above assumption. It will return true if the assumptions holds and false otherwise.