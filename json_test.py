import json
import numpy as np
import codecs

# with open('test.json') as json_file:
#     data = json.load(json_file)

# tmp = np.array(data['double_array'])



data = {}
data['list'] = ['fdsfd','dsfdsf',25]


a = np.random.randn(3,4,5);
data['array'] = a.tolist()



with open('test2.json', 'w') as json_file:
    json.dump(data, json_file)
    
    
    


with open('test2.json') as json_file:
    data2 = json.load(json_file)
    
b = np.array(data2['array'])


print(np.sum(np.abs(a-b)))











