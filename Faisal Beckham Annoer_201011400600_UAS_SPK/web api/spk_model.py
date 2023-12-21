from settings import BRAND_SCALE,PROCESSOR_SCALE,KAMERA_SCALE

class BaseMethod():

    def __init__(self, data_dict, **setWeight):
        self.database_iphone = data_dict
        # 1-6
        self.raw_weight = {
            'brand': 6,
            'ram': 2,
            'battery': 1,
            'processor': 3,
            'kamera': 5,
            'harga': 4
        }

        if setWeight:
            for item in setWeight.items():
                temp1 = setWeight[item[0]]
                temp2 = {v: k for k, v in setWeight.items()}[item[1]]
                setWeight[item[0]] = item[1]
                setWeight[temp2] = temp1

    @property
    def weight(self):
        total_weight = sum(self.raw_weight.values())
        return {c: round(w/total_weight, 2) for c,w in self.raw_weight.items()}

    @property
    def data(self):
        return [{
            'id': iphone['brand'],
            'brand': BRAND_SCALE[iphone['brand']],
            'ram': int(iphone['ram'].replace(" GB", "")),
            'battery': int(iphone['battery'].replace(" mAh", "")),
            'processor': PROCESSOR_SCALE[iphone['processor']],
            'kamera': KAMERA_SCALE[iphone['kamera']],
            'harga': iphone['harga'] 
        } for iphone in self.database_iphone]

    @property
    def normalized_data(self):
        # x/max [benefit]
        # min/x [cost]
        brand = [] # max
        ram = [] # max
        battery = [] # max
        processor = [] # max
        kamera = [] # max
        harga = [] # min

        for data in self.data:
            brand.append(data['brand'])
            ram.append(data['ram'])
            battery.append(data['battery'])
            processor.append(data['processor'])
            kamera.append(data['kamera'])
            harga.append(data['harga'])

        max_brand = max(brand)
        max_ram = max(ram)
        max_battery = max(battery)
        max_processor = max(processor)
        max_kamera = max(kamera)
        min_harga = min(harga)

        return [{
            'id': data['id'],
            'brand': data['brand']/max_brand, # benefit
            'ram': data['ram']/max_ram, # benefit
            'battery': data['battery']/max_battery, # benefit
            'processor': data['processor']/max_processor, # benefit
            'kamera': data['kamera']/max_kamera, # benefit
            'harga': min_harga/data['harga'], # cost
        } for data in self.data]
 

class WeightedProduct(BaseMethod):
    def __init__(self, database_iphone, setWeight:dict):
        super().__init__(data_dict=database_iphone, **setWeight)

    @property
    def calculate(self):
        weight = self.weight
        # calculate data and weight[WP]
        result = {row['id']:
            round(
                row['brand'] ** weight['brand'] *
                row['ram'] ** weight['ram'] *
                row['battery'] ** weight['battery'] *
                row['processor'] ** weight['processor'] *
                row['kamera'] ** weight['kamera'] *
                row['harga'] ** (-weight['harga'])
                , 2
            )

            for row in self.normalized_data}
        #sorting
        # return result
        return dict(sorted(result.items(), key=lambda x:x[1]))
