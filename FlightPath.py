flighttable = loadStrings(
    "https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat")
#table = loadTable("http://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.csv", "header")
Airports = loadStrings(
    "https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat")

angle = 0
r = 150
vel = 0.02
points = []
mags = []
coor = []
myDic = {}
flightPts = []

def setup():
    
    size(500, 500, P3D)
    smooth()
    """
    for row in table.rows():
        lat = row.getFloat("latitude")
        lon = row.getFloat("longitude")
        mag = row.getFloat("mag")

        # print lon,lat
        pt = Coor2Pt(lon, lat)
        # print pt
        points.append(pt)
        mags.append(mag)
    """        
    for i, line in enumerate(Airports):
        nl = line.split(',')
        IATA, lon , lat  = nl[4].strip('"'), nl[6], nl[7]
        myDic[IATA] = (lon , lat)
        #print(str(i) + " code is {} lon is {}".format(IATA, lon))
        
    for i, line in enumerate(flighttable):
        nls = split(line, ',')
        dep = nls[2]
        arr = nls[4]
        flight = (dep,arr)
        #print  str(i) + " departure is {} arrival is {}".format(dep,arr)
        if dep in myDic:
            depCo = myDic[dep]
        if arr in myDic:
            arrCo = myDic[arr]
        depPt = Coor2Pt(float(depCo[0]),float(depCo[1]))
        arrPt = Coor2Pt(float(arrCo[0]),float(arrCo[1]))
        flightPts.append([depPt,arrPt])
        

def draw():
    global angle
    global table
    background(51)

    translate(height * 0.5, width * 0.5)
    lights()
    rotateY(angle)
    #noStroke()
    #fill(255, 0, 0)
    noFill()
    strokeWeight(1)
    stroke(0,0,0)

    sphereDetail(25)
    sphere(r + 2)
    angle += vel
    
    """
    for i, pt in enumerate(points[:100]):
        pushMatrix()
        translate(pt[0], pt[1], pt[2])
        fill(255, 255, 255)
        sphereDetail(5)
        sphere(mags[i])
        popMatrix()
    """
    
    for i, pt in enumerate(flightPts[:250]):
        
        x1,y1,z1 = pt[0][0],pt[0][1],pt[0][2]
        x2,y2,z2 = pt[1][0],pt[1][1],pt[1][2]
        
        strokeWeight(5)
        stroke(255,0,0,50)
        point(x1, y1, z1)
        stroke(0,0,255,50)
        point(x2, y2, z2)
        
        flightArc(pt[0],pt[1])
        
        """
        pushMatrix()
        translate(x1,y1,z1)
        fill(255, 255, 255)
        box(5)
        popMatrix()
        #line(x1,y1,z1,x2,y2,z2)
        """
    
    
def Coor2Pt(lon, lat):
    theta = radians(lat) + PI / 2
    phi = radians(lon) + PI

    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)

    return (x, y, z)

def flightArc(pt1,pt2):
    
    d = dist(pt1[0],pt1[1],pt1[2],pt2[0],pt2[1],pt2[2])
    d = map(d,0,100,10,50)
    
    midpt = ((pt1[0]+pt2[0])/2,(pt1[1]+pt2[1])/2,(pt1[2]+pt2[2])/2)
    
    vectorMid = PVector(midpt[0], midpt[1],midpt[2])
    vectorMid.normalize()
    vectorMid.mult(r+d)
    """
    strokeWeight(1)
    stroke(0,255,0)
    point(midpt[0], midpt[1],midpt[2])
    strokeWeight(3)
    stroke(255,255,0)
    point(vectorMid.x, vectorMid.y,vectorMid.z)
    """
    strokeWeight(1)
    stroke(255,255,0)
    beginShape()
    vertex(pt1[0],pt1[1],pt1[2])
    #quadraticVertex(vectorMid.x, vectorMid.y,vectorMid.z)
    quadraticVertex(vectorMid.x,vectorMid.y,vectorMid.z,pt2[0],pt2[1],pt2[2])
    endShape()
    


        
