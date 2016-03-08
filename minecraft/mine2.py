from mcpi import minecraft
import math

'''block.DIRT. should work, but idle is lame and doesnt tab complete'''

dirt = 3
wool = 35
stone = 1
air = 0
tnt = 46
flower = 38
water = 8
yellowore = 14


mc = minecraft.Minecraft.create()

mc.postToChat("Hello world, time for art")


pos = mc.player.getPos()
#if pos[2] < 0:
#    mc.player.setPos(pos[0], pos[1], 10)

x, y, z = mc.player.getPos()
if z < 1:
    z = 10
mc.player.setPos(x, y+10, z)

x, y, z = mc.player.getPos()
#mc.setBlock(x+1, y, z, wool)


def boombox():
    mc.setBlocks(x+12, y+1, z+1, x+21, y+11, z+11, tnt, 1)
    mc.setBlocks(x+13, y+2, z+2, x+20, y+10, z + 10, air)

    for i in range(10):
        mc.setBlock(x+8, y+i+9, z, dirt)

    mc.player.setPos(x, y+7, z)


    mc.postToChat("boom!")


def blockline():
    print("lots of differnt blocks")
    for b in range(80):
        mc.setBlocks(x, y+20, z+b,  x+3, y+20, z+b,  b)
        mc.setBlocks(x, y+19, z+b,  x+3, y+19, z+b,  dirt)



def artpiece1():
    print("piece 1")

    for wi in range(6):
        mc.setBlocks(x-wi, y+2+wi, z-wi, x+wi, y+2+wi, z+wi, yellowore)
        mc.setBlocks(x-wi, y+12-wi, z-wi, x+wi, y+2+wi, z+wi, wool, wi)


def artpiece2():
    mc.postToChat("art piece 2..")

    for xish in range(20):
        yval = math.sin(xish) * 2 + 10
        otheryval = math.cos(xish) * 2 + 10
        mc.setBlock(x + xish, y + yval + 4, z + 4, yellowore)
        mc.setBlock(x + xish, y + otheryval + 4, z + 4, wool)
        print(yval)
    
def artpiece3():
    mc.postToChat("art piece 3")

    for xish in range(20):
        for yish in range(20):
            for zish in range(20):
                if (xish * yish * zish > 800 and xish * yish * zish < 1100) \
                or (xish * yish * zish > 1500 and xish * yish * zish < 1800) \
                or (xish * yish * zish > 3000 and xish * yish * zish < 4000):
                    mc.setBlock(x + xish, y + yish, z - 30 + zish, xish % 4 + 1)



#artpiece1()
#artpiece2()
artpiece3()


print('done')
