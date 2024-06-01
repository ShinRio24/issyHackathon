#
#READ ME
#
#this file is to output and format all collected data that swift uses
#
#

#importing googlemaps module
import googlemaps
#api key for google maps
gmaps = googlemaps.Client(key='AIzaSyD2p98heOeXL-5zigusil-niJ5Z-Rmc43Y')

#used to store final array of prices, distance, and gas station locations
final=[]

#calculate the google maps distance from point at to b
def getdist(here,loc):
    return gmaps.distance_matrix(here,loc)['rows'][0]['elements'][0]

#main function to import all of the data
def main():
    #current location of user
    currLoc = '301 Rainier Blvd S, Issaquah, WA 98027'

    #collect data from data.txt file
    tot=[]
    file = open('data.txt', 'r')
    while True:
        line = file.readline()
        if not line:
            break
        tot.append(line)

    #used to disect data (seperating adress from prices of all the pumps)
    n=[]
    for i,x in enumerate(tot):
        n.append(list(x.split(";")))
    for y in range(len(n)):
        for i,x in enumerate(n[y]):
            n[y][i]=(list(n[y][i].split("^")))


    finalList=[]
    #get the individual prices of each pump and get the cheapest one (regular is usually the chepest)
    for y in range(len(n)):
        minn=999999999
        for i,x in enumerate(n[y][0]):
            c=list(n[y][0][i].split("*"))
            for xx in c:
                if xx.isdigit():
                    minn=min(minn,int(xx))

        #convert gas price to under 10 (some locations dont use decimals on their signs)
        loc =n[y][1][0]
        while(True):
            if(minn>10): minn/=10
            else: break
        
        #find distance to pump and format and add all info to final list
        a=getdist(currLoc,loc)
        final.append([float(a['duration']['text'].split(' ')[0]),float(a['distance']['text'].split(' ')[0]), float(minn), loc])
    #format duration(mins) distance(miles), cost at pump, adress


#actual function that returns the code that will be used in swift
#return in order of clostest gas stations
def getSpeed():
    main()
    final.sort(key=lambda final: final[0])
    return final
#return based on cheapest gas stations
def getCost():
    main()
    final.sort(key=lambda final: final[2])
    return final

if __name__ == '__main__':
    print(getCost())
    print(getSpeed())

