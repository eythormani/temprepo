from mcpi.minecraft import Minecraft

mc = Minecraft.create()

hnit = mc.player.getTilePos()
print(hnit)

x = hnit.x
y = hnit.y
z = hnit.z

print(x, y, z)
