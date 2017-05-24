import urllib, StringIO
from math import log, exp, tan, atan, pi, ceil
from PIL import Image
import googlemaps

EARTH_RADIUS = 6378137
EQUATOR_CIRCUMFERENCE = 2 * pi * EARTH_RADIUS
INITIAL_RESOLUTION = EQUATOR_CIRCUMFERENCE / 256.0
ORIGIN_SHIFT = EQUATOR_CIRCUMFERENCE / 2.0
key='AIzaSyDAw6syBJ_LLYa0EyidcNBGeqbAeZjhn-k'

#GOOGLE API
gmaps = googlemaps.Client(key=key)

# Geocoding an address
geocode_result = gmaps.geocode('edinburgh, airport')


def latlontopixels(lat, lon, zoom):
    mx = (lon * ORIGIN_SHIFT) / 180.0
    my = log(tan((90 + lat) * pi/360.0))/(pi/180.0)
    my = (my * ORIGIN_SHIFT) /180.0
    res = INITIAL_RESOLUTION / (2**zoom)
    px = (mx + ORIGIN_SHIFT) / res
    py = (my + ORIGIN_SHIFT) / res
    return px, py

def pixelstolatlon(px, py, zoom):
    res = INITIAL_RESOLUTION / (2**zoom)
    mx = px * res - ORIGIN_SHIFT
    my = py * res - ORIGIN_SHIFT
    lat = (my / ORIGIN_SHIFT) * 180.0
    lat = 180 / pi * (2*atan(exp(lat*pi/180.0)) - pi/2.0)
    lon = (mx / ORIGIN_SHIFT) * 180.0
    return lat, lon

############################################


# ullat = geocode_result[0]['geometry']['viewport']['northeast']['lat']
# ulllng = geocode_result[0]['geometry']['viewport']['northeast']['lng']
# brlat = geocode_result[0]['geometry']['viewport']['southwest']['lat']
# brllng = geocode_result[0]['geometry']['viewport']['southwest']['lng']
#
# upperleft = str(ullat)+','+str(brllng) #'8.622135, -70.222482'#'-29.44,-52.0'
# lowerright = str(brlat)+','+str(ulllng)#'8.617694, -70.216141'#'-29.45,-51.98'


#upperleft =  '-29.44,-52.0'
#lowerright = '-29.45,-51.98'

upperleft = '55.945097, -3.380004'
lowerright = '55.941330, -3.370404'

print 'UPPERLEFT IS {}'.format(upperleft)
print 'LOWERRIGHT IS {}'.format(lowerright)

zoom = 22   # be careful not to get too many images!

############################################

ullat, ullon = map(float, upperleft.split(','))
lrlat, lrlon = map(float, lowerright.split(','))

# Set some important parameters
scale = 1
maxsize = 640

# convert all these coordinates to pixels
ulx, uly = latlontopixels(ullat, ullon, zoom)
lrx, lry = latlontopixels(lrlat, lrlon, zoom)

# calculate total pixel dimensions of final image
dx, dy = abs(lrx - ulx), uly - lry

# calculate rows and columns
cols, rows = int(ceil(dx/maxsize)), int(ceil(dy/maxsize))
print cols
print rows
# calculate pixel dimensions of each small image
bottom = 120
largura = int(ceil(dx/cols))
altura = int(ceil(dy/rows))
alturaplus = altura + bottom


final = Image.new("RGB", (int(dx), int(dy)))
for x in range(cols):
    for y in range(rows):
        dxn = largura * (0.5 + x)
        dyn = altura * (0.5 + y)
        latn, lonn = pixelstolatlon(ulx + dxn, uly - dyn - bottom/2, zoom)
        position = ','.join((str(latn), str(lonn)))
        print(x, y, position)
        urlparams = urllib.urlencode({'center': position,
                                      'zoom': str(zoom),
                                      'size': '%dx%d' % (largura, alturaplus),
                                      'maptype': 'satellite',
                                      'sensor': 'false',
                                      'scale': scale,
                                      'key': key})
        url = 'http://maps.googleapis.com/maps/api/staticmap?' + urlparams
        f=urllib.urlopen(url)
        print url
        im=Image.open(StringIO.StringIO(f.read()))
        final.paste(im, (int(x*largura), int(y*altura)))
final.show()

#final.save('c:/')
