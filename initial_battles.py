from troops import *


def load_battle(pattern):
    """ For specified pattern 1-3 return array containing two arrays: [POLISH_TROOPS, OSMAN_TROOPS] """
    if pattern == 1:
        return [
            # Jednostki polskie
            [
                Infantry(600, 300, 5000),
                SpearMan(630, 230, 5000),
                Hussar(900, 275, 5000)
            ],
            # Jednostki tatarskie
            [
                TatarInfantry(475, 170, 5000),
                TatarInfantry(450, 210, 4000),
                TatarCavalry(425, 250, 5000),
                SpearMan(400, 290, 4000)
            ]
        ]
    if pattern == 2:
        return [
            # Jednostki polskie
            [
                Cossack(800, 435, 3600),
                SpearMan(720, 455, 3500),
                LightCavalry(640, 385, 3600),
                SpearMan(610, 350, 4900),
                Infantry(635, 250, 3200),
                Hussar(705, 230, 3900),
                Cossack(620, 290, 2800),
            ],
            # Jednostki tatarskie
            [
                TatarInfantry(690, 140, 3800),
                SpearMan(630, 170, 2500),
                SpearMan(550, 200, 3700),
                TatarInfantry(500, 240, 3600),
                TatarCavalry(510, 340, 2600),
                TatarInfantry(550, 410, 2900),
                TatarInfantry(630, 490, 3100),
                TatarCavalry(690, 520, 2600),
                TatarInfantry(790, 550, 3800),
            ]
        ]
    if pattern == 3:
        return [
            # Jednostki polskie
            [
                Hussar(690, 140, 3800),
                SpearMan(630, 170, 2500),
                SpearMan(550, 200, 3700),
                Infantry(500, 240, 3600),
                LightCavalry(510, 340, 2600),
                Infantry(550, 410, 2900),
                Infantry(630, 490, 3100),
                Hussar(690, 520, 2600),
                SpearMan(790, 550, 3800),
                #symulacja osobna
                Cossack(900, 550, 4000)
            ],
            # Jednostki tatarskie
            [
                TatarInfantry(800, 435, 3600),
                SpearMan(720, 455, 3500),
                LightCavalry(640, 385, 3300),
                SpearMan(610, 350, 4900),
                TatarInfantry(635, 250, 3200),
                TatarCavalry(705, 230, 3600),
                TatarInfantry(620, 290, 2800),
                TatarInfantry(750, 390, 2600),
                TatarCavalry(796, 380, 3200),
                #symulacja osobna
                Infantry(770, 310, 2700),
            ]
        ]
    else:
        return None
