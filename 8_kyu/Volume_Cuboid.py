"""Bob needs a fast way to calculate the volume of a cuboid with three values: the length, width and height 
of the cuboid. Write a function to help Bob with this calculation."""

# Calculate the volume of a cuboid
def volume_cuboid(cuboid):
    return cuboid[0] * cuboid[1] * cuboid[2] 

# MAIN

print(volume_cuboid(cuboid=[3,4,5]))