#Analysis of Accidents in North American Mountineering
Analysis and visual summary of accident data collected in [Accidents in North American Mountaineering](https://www.americanalpineclub.org/p/anam) (ANAM) from 1951 to 2014. ANAM is published annualy by the [American Alpine Club](https://www.americanalpineclub.org/). The data is included here in three Excel spreadsheets. Have fun and come up with your own analysis!

###Included:
Three Excel spreadsheet containing the data. 
A Jupyter notebook for running the analysis. (You can also see it here.)
Shapefiles for drawing state and country boundaries.
`pretty_breaks.py` for calculating non-linear binning. This comes from the `class_intervals.py` script of [Carson Farmer](https://github.com/carsonfarmer/blog/tree/source/content/uploads)
 
###Dependencies:
```
Python 3
```
Python libraries:
```
math
pandas
matplotlib
numpy
shapefile
shapely
squarify
windrose
```