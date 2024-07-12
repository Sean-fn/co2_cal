import random

class Calculator:
    def __init__(self, data):
        self.data = data
        self.co2data = {}

    def calculation(self):
        methods = [
            self.gas, self.water, self.food_ware, self.distance, 
            self.electricity, self.bottle, self.paper_box, 
            self.garbage, self.paperless, self.invoice,
            self.staff
        ]
        
        for method in methods:
            result = method()
            if result is not None:
                self.co2data[method.__name__] = result

        self.co2data['total'] = sum(value for value in self.co2data.values() if value is not None)
        
        return self.co2data

    def gas(self):
        if 'gas' in self.data:
            return 2.63 * int(self.data['gas'])
        return None

    def water(self):
        if 'water' in self.data:
            return 0.156 * self.data['water']
        return None

    def food_ware(self):
        if 'food_ware' in self.data:
            return 0.11 * self.data['food_ware']
        return None

    def staff(self):
        return 1.41333333

    def distance(self):
        if 'origin' in self.data and 'destination' in self.data:
            cities = {
                '基隆': 25, '新北': 10, '台北': 15, '桃園': 35, '新竹': 85,
                '苗栗': 110, '台中': 165, '彰化': 180, '台南': 310, '高雄': 350,
                '宜蘭': 80, '花蓮': 190, '南投': 200, '雲林': 250, '嘉義': 280,
                '屏東': 320, '台東': 335
            }
            origin = self.data['origin']
            destination = self.data['destination']
            if origin == destination:
                return (random.uniform(8, 10)) * 0.22
            else:
                return (abs(cities[origin] - cities[destination]) + random.uniform(0, 10)) * 0.22
        return None

    def electricity(self):
        if 'electricity' in self.data:
            return 0.495 * self.data['electricity']
        return None

    def bottle(self):
        if 'bottle' in self.data:
            return 0.121 * self.data['bottle']
        return None

    def paper_box(self):
        if 'paper_box' in self.data:
            return 0.48 * self.data['paper_box']
        return None

    def garbage(self):
        if 'garbage' in self.data:
            return 2.06 * self.data['garbage']
        return None

    def paperless(self):
        if 'paperless' in self.data:
            return 0.0064 * self.data['paperless']
        return None

    def invoice(self):
        cloud_invoice = self.cloud_invoice()
        e_invoice = self.e_invoice()
        total_invoice = (cloud_invoice or 0) + (e_invoice or 0)
        return total_invoice if total_invoice > 0 else None

    def cloud_invoice(self):
        if 'cloud_invoice' in self.data:
            return 0.0076 * self.data['cloud_invoice']
        return None

    def e_invoice(self):
        if 'cloud_invoice' in self.data:
            return 0.0038 * self.data['cloud_invoice']
        return None