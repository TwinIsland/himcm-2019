import populartimes as pt
import numpy as np

sum_data = np.zeros(24)

api_key = ''
place_id = ''


data = pt.get_id(api_key,place_id)

times = data['data']

for i in times:
    sum_data += times['time']

print(sum_data)
print([int(i/7) for i in sum_data])