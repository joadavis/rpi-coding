import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

mc = minecraft.Minecraft.create()
#mc.postToChat("Heat Vision!")

pos = mc.player.getTilePos()

#mc.postToChat(pos)

#rot = mc.player.getRotation()
#pitch = mc.player.getPitch()
#direct = mc.player.getDirection()

#mc.postToChat(rot)
#mc.postToChat(pitch)
#mc.postToChat(direct)

# those dont work on Pi



# activate any tnt around

mc.postToChat("Oliver's boom!")

while True:

    x,y,z = mc.player.getPos()

    for xi in range(-4, 4):
        for zi in range (-4, 4):
            for yi in range (-1, 3):
                thisblock = mc.getBlock(x + xi, y + yi, z + zi)
                #print thisblock
                if thisblock == 46:
                    mc.setBlock(x + xi, y + yi, z+zi, 46, 1)
                    print "setting on"
                #mc.setBlock(x + xi, y + 1, z+zi, 46, 1)
    time.sleep(1)
