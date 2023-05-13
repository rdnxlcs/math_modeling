from random import uniform

LY = 9.4 * 10**15
SM = 2 * 10**30
def genstar():
    size = 0.1
    x = uniform(-size, size) * LY
    y = uniform(-size, size) * LY
    z = uniform(-size, size) * LY
    vx = uniform(-10000, 10000)
    vy = uniform(-10000, 10000)
    vz = uniform(-10000, 10000)
    return list((x, vx, y, vy, z, vz))

def generate(count):
    res = []
    for i in range(count):
        res.extend(genstar())
    return tuple(res)

def genmass(count):
    res = []
    for i in range(count):
        res.append(uniform(0.1 * SM, 40 * SM))
    return res