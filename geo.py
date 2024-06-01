#a importing googlemaps module
import googlemaps
  
def getdist(here,loc):
    return gmaps.distance_matrix(here,loc)['rows'][0]['elements'][0]
# Requires API key
gmaps = googlemaps.Client(key='AIzaSyD2p98heOeXL-5zigusil-niJ5Z-Rmc43Y')
  
currLoc = '301 Rainier Blvd S, Issaquah, WA 98027'


tot=[]
file = open('data.txt', 'r')
while True:
    line = file.readline()
    if not line:
        break
    tot.append(line)


n=[]
for i,x in enumerate(tot):
    n.append(list(x.split(";")))
for y in range(len(n)):
    for i,x in enumerate(n[y]):
        n[y][i]=(list(n[y][i].split("^")))


finalList=[]
#print(n)
for y in range(len(n)):
    minn=999999999
    for i,x in enumerate(n[y][0]):
        #print(n[y][0][i])
        c=list(n[y][0][i].split("*"))
        for xx in c:
            if xx.isdigit():
                minn=min(minn,int(xx))

    loc =n[y][1][0]
    while(True):
        if(minn>10): minn/=10
        else: break
    
    a=getdist(currLoc,loc)
    print(a['duration']['text'],a['distance']['text'], minn, loc)