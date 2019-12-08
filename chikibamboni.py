import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
mc.player.setTilePos(0,170,0)
pos=mc.player.getTilePos()
def chikibamboni():
    mc.setBlocks(0,170,0,20,180,20,35)
    mc.player.getTilePos()
chikibamboni()
#2 postroika
def nogibamboni():
    mc.player.getTilePos()
    mc.setBlocks(0,169,16,5,163,20,35)
    mc.setBlocks(20,169,20,15,163,16,35)
    mc.setBlocks(20,169,0,15,163,4,35)
    mc.setBlocks(0,169,0,5,163,4,35)
nogibamboni()

