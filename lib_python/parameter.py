#parameters for CSA-Algortihms
from urllib.parse import quote_plus

urlMongoDb = "mongodb://%s:%s@%s" % (
    quote_plus('indaco'), quote_plus('Capocotta2008'), '130.192.68.192:5555/')

urlMongoDbUniroma = "mongodb://%s:%s@%s" % (
    quote_plus('cityadmin'), quote_plus('m0ng0l01d3'), 'infodyn.phys.uniroma1.it:44444/')


#urlServerOsrm = 'http://socdyn.phys.uniroma1.it:3000/table/v1/foot/';
#urlMongoDb = 'mongodb://130.192.68.192:5555/'
nameDB = 'citychrone'
gridEdge = 0.4
#parameters of walking distance
#tS = distanceS/(5./3.6)
timeWalk = 900
distanceS = timeWalk * (5./3.6);

def UrlOsrmServer(city):        
    urlBaseServer = "http://130.192.68.192:3000/"
    if(city == 'Paris'):
        urlBaseServer = 'http://130.192.68.192:3001/'
    if(city == 'New York'):
        urlBaseServer = 'http://130.192.68.192:3002/'
    if(city == 'Berlin'):
        urlBaseServer = 'http://130.192.68.192:3003/'
    if(city == 'Madrid'):
        urlBaseServer = 'http://130.192.68.192:3004/'
    if(city == 'Vienna'):
        urlBaseServer = 'http://130.192.68.192:3005/'
    if(city == 'London'):
        urlBaseServer = 'http://130.192.68.192:3006/'
    if(city == 'Mexico City'):
        urlBaseServer = 'http://130.192.68.192:3007/'
    if(city == 'Manchester'):
        urlBaseServer = 'http://130.192.68.192:3008/'
    if(city == 'San Francisco'):
        urlBaseServer = 'http://130.192.68.192:3009/'
    if(city == 'Athens'):
        urlBaseServer = 'http://130.192.68.192:3020/'
    if(city == 'Helsinki'):
        urlBaseServer = 'http://130.192.68.192:3021/'
    if(city == 'Oslo'):
        urlBaseServer = 'http://130.192.68.192:3022/'
    if(city == 'Boston'):
        urlBaseServer = 'http://130.192.68.192:3023/'
    if(city == 'Budapest'):
        urlBaseServer = 'http://130.192.68.192:3024/'
    if(city == 'Chicago'):
        urlBaseServer = 'http://130.192.68.192:3025/'
    if(city == 'Los Angeles'):
        urlBaseServer = 'http://130.192.68.192:3026/'
    if(city == 'Toulouse'):
        urlBaseServer = 'http://130.192.68.192:3027/'
    if(city == 'Prague'):
        urlBaseServer = 'http://130.192.68.192:3028/'

    return urlBaseServer

def UrlOsrmServerContinent(continent):    
    urlBaseServer = "http://130.192.68.192:3010/"
    if(continent == 'europe'):
        urlBaseServer = "http://130.192.68.192:3010/"
    if(continent == 'north-america'):
        urlBaseServer = "http://130.192.68.192:3011/"
    if(continent == 'australia'):
        urlBaseServer = "http://130.192.68.192:3012/"
    return urlBaseServer

  

