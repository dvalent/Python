add_library('peasycam')

nflights = 50000
angle = 0
r = 150
vel = 0.02

points = []
mags = []
coor = []
myDic = {}
flightPts = []
newMid = []

def setup():
    flighttable = loadStrings("https://raw.githubusercontent.com/jpatokal/openflights/master/data/routes.dat")
    Airports = loadStrings("https://raw.githubusercontent.com/jpatokal/openflights/master/data/airports.dat")
    size(500, 500, P3D)
    cam = PeasyCam(this,height * 0.5, width * 0.5,0, 500)
    #cam.lookAt(height * 0.5, width * 0.5,0)
    cam.setActive(True)
    cam.setMinimumDistance(300)
    cam.setMaximumDistance(800)
    smooth()

    for i, line in enumerate(Airports):
        nl = line.split(',')
        IATA, lon , lat  = nl[4].strip('"'), nl[6], nl[7]
        myDic[IATA] = (lon , lat)
        #print(str(i) + " code is {} lon is {}".format(IATA, lon))

    for i, line in enumerate(flighttable[:nflights]):
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

        d = dist(depPt[0],depPt[1],depPt[2],arrPt[0],arrPt[1],arrPt[2])
        d = map(d,0,100,10,50)

        midpt = ((depPt[0]+arrPt[0])/2,(depPt[1]+arrPt[1])/2,(depPt[2]+arrPt[2])/2)

        vectorMid = PVector(midpt[0], midpt[1],midpt[2])
        vectorMid.normalize()
        vectorMid.mult(r+d)

        newMid.append(vectorMid)

def draw():
    global angle
    global table

    #frameRate(1)
    background(51)

    translate(height * 0.5, width * 0.5)
    lights()
    rotateY(angle)
    #noStroke()
    fill(25)
    #noFill()
    strokeWeight(1)
    stroke(0,0,0)

    sphereDetail(25)
    sphere(r)
    noFill()


    for i, pt in enumerate(flightPts):


        #Draw paths:
        strokeWeight(1)
        stroke(255,255,0,30)
        beginShape()
        vertex(pt[0][0],pt[0][1],pt[0][2])
        quadraticVertex(newMid[i].x,newMid[i].y,newMid[i].z,pt[1][0],pt[1][1],pt[1][2])
        endShape()

    angle += vel
    """
    print frameCount
    print degrees(angle)
    if degrees(angle) < 360:
        saveFrame("earth{}.png".format(frameCount))
    else: pass
    """
def Coor2Pt(lon, lat):
    theta = radians(lat) + PI / 2
    phi = radians(lon) + PI

    x = r * sin(theta) * cos(phi)
    y = r * sin(theta) * sin(phi)
    z = r * cos(theta)

    return (x, y, z)
