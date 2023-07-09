import pickle
import json
import numpy as np
import config


class DiamondPrice():
    def __init__(self, carat,cut,color,clarity,depth,table,x,y,z):
        print("****** INIT Function *********")
        self.carat=carat
        self.cut = cut
        self.color= color
        self.clarity = clarity
        self.depth = depth
        self.table = table
        self.x = x
        self.y = y
        self.z = z

    def __load_saved_data(self):

        with open(config.MODEL_FILE_PATH,'rb') as f:
            self.model = pickle.load(f)

        with open(config.JSON_FILE_PATH,'r') as f:
            self.json_data = json.load(f)

    def get_predicted_price(self):
        self.__load_saved_data()

        cut = self.json_data['cut'][self.cut]
        color = self.json_data['color'][self.color]
        clarity = self.json_data['clarity'][self.clarity]
        
        test_array = np.zeros([1,self.model.n_features_in_])
        test_array[0,0] = self.carat
        test_array[0,1] = cut
        test_array[0,2] = color
        test_array[0,3] = clarity
        test_array[0,4] = self.depth
        test_array[0,5] = self.table
        test_array[0,6] = self.x
        test_array[0,7] = self.y
        test_array[0,8] = self.z
  
        predicted_charges = np.around(self.model.predict(test_array)[0],3)
        return predicted_charges


