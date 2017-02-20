data = loadStrings("https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat")
table = loadTable("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv" , "header")
lonC = 10.4806
latC = 66.9036
r = 100
angle = 0
points = []

def setup():
    size(500,500,P3D)
    smooth()

    for i,line in enumerate(data[:100]):
        nl = split(line, ',')
        #print  str(i) + " departure is {} arrival is {}".format(nl[2],nl[4])
        
    for row in table.rows():
        lat = row.getFloat("latitude")
        lon = row.getFloat("longitude") 
        #print lon,lat
        pt = Coor2Pt(lon, lat)
        #print pt
        points.append(pt)
    
def draw():
    global angle
    global table
    background(51)
    
    translate(height*0.5,width*0.5)
    lights()
    rotateY(angle)
    noStroke()
    fill(255,0,0)
    sphere(r)
    angle += 0.05
    
    
    for pt in points:
        pushMatrix()
        translate(pt[0],pt[1],pt[2])
        fill(0,0,255)
        box(5)
        popMatrix()

def Coor2Pt(lon,lat):
    theta = radians(lat) + PI/2;
    phi = radians(lon) + PI;
    
    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)
    
    return (x,y,z)
    
