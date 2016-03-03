import maya.cmds as cmds
import math
import random
import time
import maya.mel as mel


cmds.select(all=True)
cmds.delete()


cube=cmds.polyCube()

for i in range(0,361,10):
    posX=2*math.cos(i*(math.pi/180.0))
    posZ=2*math.sin(i*(math.pi/180.0))
    cmds.xform(cube, translation=[posX,0,0])
    cmds.xform(cube, translation=[0,0,posZ])
    cmds.xform(cube,  rotation=[0,i,0])
    cmds.setKeyframe( v=posX, at='translateX', t = i)
    cmds.setKeyframe( v=posZ, at='translateZ', t = i)
    cmds.setKeyframe( v=-i, at='rotateY', t = i)