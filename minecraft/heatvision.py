import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

mc = minecraft.Minecraft.create()
mc.postToChat("Heat Vision!")

pos = mc.player.getTilePos()

mc.postToChat(pos)

#rot = mc.player.getRotation()
#pitch = mc.player.getPitch()
#direct = mc.player.getDirection()

#mc.postToChat(rot)
#mc.postToChat(pitch)
#mc.postToChat(direct)

# those dont work on Pi

## Unfortunately, while this was a fun idea it didn't work
## with the version of Minecraft on the Pi in 2015
