# BigDive
### notebooks collections for analyzing car sharing data

 --- 
 
##### visualize the demo notebooks:
+ [first analysis](http://nbviewer.jupyter.org/github/CityChrone/BigDive/blob/master/first_analysis.ipynb)
+ [fluxes](http://nbviewer.jupyter.org/github/CityChrone/BigDive/blob/master/fluxes.ipynb)
+ [parkings](http://nbviewer.jupyter.org/github/CityChrone/BigDive/blob/master/parking_time.ipynb)

*on chrome maps not working, use firefox/safari or other browsers*

## Guide
### prerequesites
1. MongoDB database with readWrite & create_index permissions
1. python 3
1. Jupyter Notebook
1. python library listed at the beginning of the notebooks.

### Notebooks sequence
1. ```import_csv_mongodb.ipynb``` -> import csv file inside mongoDB database.
1. ```generate_hexagons_city.ipynb``` -> generate hexagons tessellation for cities.
1. ```first_analysis.ipynb``` -> first simple analysis of data, qith interactive maps.
1. ```Fluxes.ipynb``` -> visualizing fluxes on maps.
1. ```parking_time.ipynb``` -> visualizing parking times.

