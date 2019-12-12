import json
import os
from glob import glob

from apng import APNG

with open('./Resources/metadata.json') as f:
    data = json.load(f)

try:
    os.mkdir('./Resources/apng')
except FileExistsError:
    pass

for key in data.keys():
    files = glob('./Resources/png/{}/*.png'.format(key))
    files.sort(key=lambda x: int(os.path.split(x)[1][:-4]))

    APNG.from_files(files, delay=1, delay_den=int(data[key]['FrameRate'])).save("./Resources/apng/{}.png".format(key))
