# Analysis of Accidents in North American Mountineering
Analysis and visual summary of accident data collected in [Accidents in North American Mountaineering](https://www.americanalpineclub.org/p/anam) (ANAM) from 1951 to 2014 (and 2015! - see NOTE). ANAM is published annualy by the [American Alpine Club](https://www.americanalpineclub.org/). The data is included here in three Excel spreadsheets (2 new spreadsheets are available - see NOTE). Have fun and come up with your own analysis!

### Included:
* Three Excel spreadsheet containing the data. 
* A Jupyter notebook for running the analysis. (You can also see it [here](http://nbviewer.jupyter.org/gist/mikeskaug/8984e8110c9dd7fcc84c).)
* Shapefiles for drawing state and country boundaries.
* `pretty_breaks.py` for calculating non-linear binning. This comes from the `class_intervals.py` script of [Carson Farmer](https://github.com/carsonfarmer/blog/tree/source/content/uploads)
 
### Dependencies:
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

### NOTE 2017-06-11
I added updated spreadsheets that include data for 2015. Unfortunately, the format of the spreadsheets changed, so some changes need to be made in the notebook in order for it to use the new data. I may commit those changes here at some point, but in the meantime I thought it was important to make the new data available.
