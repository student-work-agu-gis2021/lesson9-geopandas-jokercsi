#!/usr/bin/env python
# coding: utf-8

# ## Problem 3: How long distance individuals have travelled? 
# 
# In this problem the aim is to calculate the "distance" in meters that the individuals have travelled according the social media posts (Euclidean distances between points). In this problem, we will need the `userid` -column an the points created in the previous problem. You will need the shapefile `Kruger_posts.shp` generated in Problem 2 as input file.
# 

# YOUR CODE HERE 1 to read data
import geopandas as gpd
from pyproj import CRS

#Read in the shapefile as a geodataframe called data
fp = "Kruger_posts.shp"
data = gpd.read_file(fp)


# - Check the crs of the input data. If this information is missing, set it as epsg:4326 (WGS84).
# - Reproject the data from WGS84 to `EPSG:32735` -projection which stands for UTM Zone 35S (UTM zone for South Africa) to transform the data into metric system. (don't create a new variable, update the existing variable `data`!)"

# YOUR CODE HERE 2 to set crs

#Reproject the data from WGS84 projection into EPSG:32735 -projection which stands for UTM Zone 35S (UTM zone for South Africa) to transform the data into metric system.
data = data.to_crs(epsg=32735)

# CODE FOR TESTING YOUR SOLUTION

# Check the data
print(data.head())

# CODE FOR TESTING YOUR SOLUTION

# Check that the crs is correct after re-projecting (should be epsg:32735)
print(data.crs)


#  - Group the data by userid

#  YOUR CODE HERE 3 to group 

#Group the data by userid
grouped = data.groupby('userid')

# CODE FOR TESTING YOUR SOLUTION

#Check the number of groups:
assert len(grouped.groups) == data["userid"].nunique(), "Number of groups should match number of unique users!"


# **Create LineString objects for each user connecting the points from oldest to latest:**
# 

# YOUR CODE HERE 4 to set movements
import pandas as pd
from shapely.geometry import LineString, Point

#Create an empty DataFrame called movements. #Create an empty column "geometry"
movements = pd.DataFrame({'geometry':[]})

#for i, row in grouped:
  


# create a LineString object based on the user's points
# for i, row in data.iterrows():
#   # sort the rows by timestamp
#   data = data.sort_values('timestamp')
#   line = (LineString(row["lat"], row["lon"]))
#   movements.at[i, 'userid'] = i
#   movements.at[i, 'geometry'] = line


# Add the LineString to the geometry column of the movements dataframe. You can also add the userid in a separate column (or use the userid as index).

# CODE FOR TESTING YOUR SOLUTION

#Check the result
print(type(movements))
print(movements.crs)
print(movements["geometry"].head())


# **Finally:**
# - Check once more the crs definition of your dataframe (should be epsg:32735, define the correct crs if this information is missing)
# - Calculate the lenghts of the lines into a new column called ``distance`` in ``movements`` GeoDataFrame.

# YOUR CODE HERE 5 to calculate distance

# CODE FOR TESTING YOUR SOLUTION

#Check the output
movements.head()


# You should now be able to print answers to the following questions: 
# 
#  - What was the shortest distance travelled in meters?
#  - What was the mean distance travelled in meters?
#  - What was the maximum distance travelled in meters?

# YOUR CODE HERE 6 to find max, min,mean of the distance.

# - Finally, save the movements of into a Shapefile called ``some_movements.shp``

# YOUR CODE HERE 7 to save as Shapefile

# CODE FOR TESTING YOUR SOLUTION

import os

#Check if output file exists
assert os.path.isfile(fp), "Output file does not exits."


# That's all for this week!
#check length
def func7():
    return data

#check type
def func8():
    return grouped 

#check crs
def func9():
    return movements

#check movements['distance']
def func10():
    return movements