from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL.GL import *
import sys

def main():
    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(400,400)
    glutCreateWindow('Earthquakes')

    glShadeModel(GL_SMOOTH)
    #glShadeModel(GL_FLAT)
    """
    glEnable(GL_LIGHTING)
    lightZeroPosition = [10.,4.,10.,1.]
    glLightfv(GL_LIGHT0, GL_POSITION, lightZeroPosition)
    glLightf(GL_LIGHT0, GL_CONSTANT_ATTENUATION, 0.1)
    glLightf(GL_LIGHT0, GL_LINEAR_ATTENUATION, 0.05)
    glEnable(GL_LIGHT0)
    """
    glutDisplayFunc(display)

    gluPerspective(40,1,1,40)
    gluLookAt( 0,  0, 10,
               0,  0,  0,
               0,  1,  0 )

    glutMainLoop()
    return


def display():

    glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
    glutDisplayFunc( )
    #glPushMatrix()
    color = [0.1,0.5,0.5]
    glMaterialfv(GL_FRONT,GL_DIFFUSE,color)
    glRotatef(1, 3, 1, 1)
    # glutWireSphere(2,50,50)
    # glutSolidSphere(2,50,50)
    glutSolidTorus(1,3,50,50)
    #glPopMatrix()

    glutSwapBuffers()
    return

if __name__ == "__main__": main()
