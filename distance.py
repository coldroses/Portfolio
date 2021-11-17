#paul clear status: complete

#d (dist) #g 9.8m/s ** 2 (gravit constant)  #t time in seconds object falling
#d = 1/2 (g)(t**2)

gravConst = 9.8

#calculate and return distance in meters
def falling_distance(timeSec):
    fallDist = timeSec**2 * 9.8 * .5
    return fallDist
