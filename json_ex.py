from oop.class_ex import *
import os
import json
from typing import List

def test_json():
    master = Master('')
    try:
        path = os.path.dirname(os.path.abspath(__file__))
        json_file = os.path.join(path,'oop/data.json')
        with open(json_file) as dump_f:        
            data = json.load(dump_f)       
            print(data)
            master.__dict__ = data
            print(master)
            # print(master.dogs[0]["heigh"])     
  
        for dog_dict in master.dogs:
            dog = Dog.fromdict(dog_dict)
            print(dog.heigh)

    except Exception as e:
        print(e)    

test_json()    