# from www.raspberrypi.org/learning/minecraft-whac-a-block-game/worksheet

import mcpi.minecraft as minecraft
import mcpi.block as block
import random
import time

mc = minecraft.Minecraft.create()
mc.postToChat("Minecraft Whac-a-Block")

pos = mc.player.getTilePos()

mc.setBlocks(pos.x-1, pos.y, pos.z+3,
             pos.x+1, pos.y + 2, pos.z + 3,
             block.STONE.id)
mc.setBlocks(pos.x-3, pos.y, pos.z+2,
             pos.x+3, pos.y + 2, pos.z + 1,
             block.AIR.id)

pos_start = (pos.x + 3, pos.y + 1, pos.z + 2)
pos_end = (pos.x - 3, pos.y + 1, pos.z + 2)

#mc.setBlock(pos_start[0], pos_start[1], pos_start[2],
#            block.WOOL.id, 7)
#mc.setBlock(pos_end[0], pos_end[1], pos_end[2],
#            block.WOOL.id, 3)

    
game_running=False
blocksLit = 0
points = 0
new_block_cycle = 0

# run script forever
while True:
    print("polling...")
    new_block_cycle += 1

    hitzz = mc.events.pollBlockHits()

    for hitBlock in hitzz:
        if game_running \
             and hitBlock.pos.x == pos_end[0] \
             and hitBlock.pos.y == pos_end[1] \
             and hitBlock.pos.z == pos_end[2]:
            mc.postToChat("STOOOP!!!")
            mc.postToChat("Game Over - points = " + str(points))
            game_running = False
            points = 0
                                                                            
        elif not game_running \
             and hitBlock.pos.x == pos_start[0] \
             and hitBlock.pos.y == pos_start[1] \
             and hitBlock.pos.z == pos_start[2]:
            game_running = True
            mc.postToChat("Get ready...")
            time.sleep(2)
            mc.postToChat("Go")

            blocksLit = 0
            points = 0
            
        elif game_running:
            print("got a hit" + str(hitBlock.pos.x))
            print(hitBlock)
            if mc.getBlock(hitBlock.pos.x, hitBlock.pos.y, hitBlock.pos.z) == block.GLOWSTONE_BLOCK.id:
                mc.setBlock(hitBlock.pos, block.DIRT.id)
                blocksLit = blocksLit - 1
                points = points + 1

    # generate blocks if gaming
    if game_running and new_block_cycle > 1:
        new_block_cycle = 0
        if blocksLit < 9:
            print("blocksLit: " + str(blocksLit))
            blocksLit = blocksLit + 1
            lightCreated = False
            while not lightCreated:
                xPos = pos.x + random.randint(-1,1)
                yPos = pos.y + random.randint(0,2)
                zPos = pos.z + 3
                if mc.getBlock(xPos, yPos, zPos) == block.STONE.id \
                or mc.getBlock(xPos, yPos, zPos) == block.DIRT.id \
                or mc.getBlock(xPos, yPos, zPos) == block.AIR.id:
                    mc.setBlock(xPos, yPos, zPos, block.GLOWSTONE_BLOCK.id)
                    lightCreated = True
        else:
            mc.postToChat("The End! points= " + str(points))
            game_running = False



    time.sleep(.5)
    mc.setBlock(pos_start[0], pos_start[1], pos_start[2],
            block.WOOL.id, 5)
    mc.setBlock(pos_start[0], pos_start[1] + 1, pos_start[2],
            block.WOOL.id, 4 + new_block_cycle)
    mc.setBlock(pos_end[0], pos_end[1], pos_end[2],
            block.WOOL.id, 6)
    for resetx in range(-1,2):
        for resety in range(0,3):
            if mc.getBlock(pos.x + resetx, pos.y + resety, pos.z + 3) == block.DIRT.id:
                print("dirt to stone")
                mc.setBlock(pos.x + resetx, pos.y + resety, pos.z + 3,
                            block.STONE.id)
            print("update " + str(resetx) + str(resety))
    print("looping")
    # one more check
    if new_block_cycle > 50:
        new_block_cycle = 0
    


mc.postToChat("Game Over - points = " + str(points))
