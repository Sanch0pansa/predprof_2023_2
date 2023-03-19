from math import *


#pointeses = [[[44, 56]], [[28, 4088], [43, 504], [20, 120]], [[10, 6], [19, 3]]]
#for points in pointeses:
points = [[28, 4088], [43, 504], [20, 120]]
days = 0
credits = 0
raspisanie = [{'SH_end': 8}]
for s, c in points:
    for w in [80, 30, 5]:
        t = s * (200 + c) / (5 * w)
        if t >= log(1 + (c / 8), 2):
            break
    t = ceil(t)
    days += t

    credits += 10 * w
    if 11 * w >= 465:
        oxi = 20
        temp = 30
        e = 465 / 11
    elif 11 * w >= 325:
        oxi = 30
        temp = 25
        e = 325 / 11
    else:
        oxi = 60
        temp = 10
        e = 55 / 11
    credits += 7 * oxi * t

    for i in range(t):
        sh = 8 + 8 * (i + 1)
        raspisanie.append({'fuel_consumption': w,
                            'engine_consumption': w - e,
                            'elecricity_consumption': e,
                            'elecricity': 11 * e,
                            'ship_mass': 192 + sh,
                            'oxygen_consumption': oxi * sh,
                            'SH_start': raspisanie[-1]['SH_end'],
                            'SH_end': sh,
                            'temperature': temp})

print(*[i for i in raspisanie], sep='\n')
