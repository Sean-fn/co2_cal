import random

class Calculator:
    def __init__(self, data):
        self.data = data
        self.co2data = {
            'gas': self.data['gas'],
            'water': self.data['water'],
            'food_ware': self.data['food_ware'],
            'distance': 30,
            'staff': None,
            'invoice': None,
        }

    def calculation(self):
        self.co2data['gas'] = self.gas()
        self.co2data['water'] = self.water()
        self.co2data['food_ware'] = self.food_ware()
        self.co2data['distance'] = self.distance()
        self.co2data['staff'] = 1.41
        self.co2data['invoice'] = 0.0076

        self.co2data['total'] = sum(self.co2data.values())
        return self.co2data

    def gas(self):
        return 2.63 * self.data['gas']

    def water(self):
        return 0.156 * self.data['water']

    def food_ware(self):
        return 0.11 * self.data['food_ware']
        
    def distance(self):
        cities = {
            '基隆': 25,
            '新北': 10,
            '台北': 15,
            '桃園': 35,
            '新竹': 85,
            '苗栗': 110,
            '台中': 165,
            '彰化': 180,
            '台南': 310,
            '高雄': 350,
            '宜蘭': 80,
            '花蓮': 190,
            '南投': 200,
            '雲林': 250,
            '嘉義': 280,
            '屏東': 320,
            '台東': 335
        }
        origin = self.data['origin']
        destination = self.data['destination']
        if origin == destination:
            return (random.uniform(8, 10)) * 0.22
        else:
            return (abs(cities[origin] - cities[destination]) + random.uniform(0, 10)) * 0.22