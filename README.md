# Austin-Crash-Analytics

The project idea is to use publicly available data to investigate crash patterns on a city or county level. This is performed by sourcing data from the TXDoT Crash Records Information System (CRIS) as tables for the years 2010-2017, converting to GIS and pandas dataframes, and analyzing spatial and temporal patterns. 


# CRIS:

This database contains all crash data reported by local and state agencies that have occurred. The database includes data such as contributing factors, XY coordinates (WGS84), time of day, day of week, and year of the each crash, daily average traffic flows (for major roads), among others. XY data seems to be of high quality from the analysis that I have done so far, and can be attributed to individual streets and intersections. Unfortunately the records do not have mm/dd/yy values, presenting a challenge for regression analysis.


Intersections give us a useful way to aggregate crash incidents on a county or city scale.  Crashes often occur at intersections because these are the locations where two or more roads cross each other and activities such as turning left, crossing over, and turning right have the potential for conflicts resulting in crashes (1). Identifying intersections where a high volume of crashes occur for specific reasons can give civic planners clear problems to investigate and solve.


# GIS:

Patterns can be drawn from the CRIS data by converting records to points and aggregating spatially. This is also how the data can be applied to a web map for public consumption. So far I have been doing this by using the ESRI python arcpy site package (requires ArcGIS) and pandas for prep and analysis, with carto for web mapping, but I am open to other solutions.


# Machine Learning:

The big idea is to apply machine learning to the crash data, by combing it with 311 data and whatever other public data makes sense to do some predictive analytics. This can be done using python libraries such as scikit-learn or  CRIS crash data includes location, daily traffic volume(for major roads), time, and day which could be used along with intersections to train a neural network to predict chance of accident at any given intersection at a certain day/time


# Prototypes:

These maps show prototypes of the sort of spatial analysis that is possible for the CRIS data. 

San Antonio Crash Map:
This map focuses on alcohol and drug related crashes in San Antonio by finding the intersections where the most of these crashes occur. Data was prepped from CRIS 2010-2017 with drugs and alcohol flagged as contributing factors.

https://tom-montgomery.carto.com/builder/57d7b3e1-37d5-4a17-a83f-2f2d727fca5a/embed

Bexar Crash Map:
This map shows intersections with the highest counts of crashes of any type. Also of interest is the calculation of mean (most common) crash times, days, and years to help elucidate patterns.

https://tom-montgomery.carto.com/builder/74bbff05-75b9-40c2-9ec2-190c64bb4818/embed

# Links:
CRIS:
Example of machine learning for similar application:
https://github.com/jgdodson/DerbyHacks17

https://cris.dot.state.tx.us/public/Query/#/app/public/welcome


Sources:
1 https://crashstats.nhtsa.dot.gov/Api/Public/ViewPublication/811366
