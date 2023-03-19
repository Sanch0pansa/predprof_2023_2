from math import *

import requests

headers = {'X-Auth-Token': '7vt3qmhc'}
Import = requests.get('https://dt.miet.ru/ppo_it_final', headers=headers)
Import: list = Import.json()

class Ship:
    def __init__(self, count_SH=8, count_fuel=0, count_Oxi=0):
        self.Mass = 192 + count_SH
        self.count_SH = count_SH
        self.count_fuel = count_fuel
        self.count_Oxi = count_Oxi
        self.sum_fuel = 0
        self.sum_Oxi = 0

    def calculate_SH_new_day(self, G0, Kp):
        Gn = G0 + G0 * Kp
        self.Mass = self.Mass - G0 + Gn
        if Gn < 8:
            raise Exception(f'Critical count SH ({Gn})')

        return Gn

    def calculate_Kp(self, T, Oxi):
        self.sum_Oxi += Oxi
        self.count_Oxi -= Oxi
        return sin((-pi) / 2 + (pi * (T + 0.5 * Oxi)) / 40)

    def calculate_Enegry(self, T):
        E = 0
        for t in range(0, T + 1):
            E += t
        return E

    def calculate_V_to_new_day(self, W, M):
        if W > 80:
            raise Exception(f'No W > 80 ({W})')
        Vmax = 2
        return Vmax * (W / 80) * (200 / M)

    def calculate_sum_fuel(self, W, T):
        E = self.calculate_Enegry(T)
        fuel_of_day = W + E * 11
        self.count_fuel -= fuel_of_day
        self.sum_fuel += fuel_of_day
        return fuel_of_day


SHIP = Ship()
# days = 0
# for point in Import:
#     S, C = point
#     if S * (200 + C) / 400 >= log(1 + C / 8, 2):
#         days += S * (200 + C) / 400
#
#     elif S * (200 + C) / 150 > log(1 + C / 8, 2):
#         days += S * (200 + C) / 150


for Oxi in range(60):
    if SHIP.calculate_Kp(30, Oxi) == 1:
        print(Oxi)
