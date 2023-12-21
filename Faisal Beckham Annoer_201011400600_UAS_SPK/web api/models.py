import numpy as np
import pandas as pd
from spk_model import WeightedProduct

class Iphone():

    def __init__(self) -> None:
        self.iphone = pd.read_csv('iphone_202310311540.csv')
        self.iphone_array = np.array(self.iphone)
        print(self.iphone_array)

    @property
    def iphone_data_dict(self):
        data = {}
        for iphone in self.iphone_array:
            data[iphone[0]] = iphone[0] 
        return data

    def get_recs(self, kriteria):
        wp = WeightedProduct(self.iphone.to_dict(orient="records"), kriteria)
        return wp.calculate

