from mcpi import minecraft

'''block.DIRT. should work, but idle is lame and doesnt tab complete'''

dirt = 3
wool = 35
stone = 1
air = 0
tnt = 46
flower = 38


mc = minecraft.Minecraft.create()

mc.postToChat("Hello world")


pos = mc.player.getPos()

x, y, z = mc.player.getPos()
mc.player.setPos(x, y+10, z)

x, y, z = mc.player.getPos()
mc.setBlock(x+1, y, z, wool)


mc.setBlocks(x+12, y+1, z+1, x+21, y+11, z+11, tnt, 1)
mc.setBlocks(x+13, y+2, z+2, x+20, y+10, z + 10, air)

for i in range(10):
    mc.setBlock(x+18, y+i+9, z+8, dirt)

mc.player.setPos(x+18, y+8, z + 8)


mc.postToChat("boom!")
print('done')
