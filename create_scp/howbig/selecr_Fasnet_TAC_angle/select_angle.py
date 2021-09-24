#!/usr/bin/env python
# Created on 2021/8/12
# Author: Zhenyu Wang

import json
import os
import pickle

path = '/root/GitHub/TAC-master/data/configs/MC_Libri_fixed_test.pkl'
with open(path, 'rb') as f:
    configs = pickle.load(f)
    
angle_15 = []
angle_45 = []
angle_90 = []
angle_180 = []
for i in range(len(configs)):
    angle=configs[i]
    #print(overlap['overlap_ratio'])
    #print(type(overlap['overlap_ratio']))
    if angle['spk_angle'] <= 15:
        str_15 = str('sample{}'.format(i+1))
        angle_15.append(str_15)
    elif angle['spk_angle'] <= 45:
        str_45 = str('sample{}'.format(i+1))
        angle_45.append(str_45)
    elif angle['spk_angle'] <= 90:
        str_90 = str('sample{}'.format(i+1))
        angle_90.append(str_90)
    else:
        str_180 = str('sample{}'.format(i+1))
        angle_180.append(str_180)

angle_15.append(len(angle_15))
angle_45.append(len(angle_45))
angle_90.append(len(angle_90))
angle_180.append(len(angle_180))
out_dir = '/root/utils/create_scp/howbig/selecr_Fasnet_TAC_angle'
out_filename1 = 'angle_15'
with open(os.path.join(out_dir, out_filename1 + '.json'), 'w') as f:
    json.dump(angle_15, f, indent=4)
    
out_filename2 = 'angle_45'
with open(os.path.join(out_dir, out_filename2 + '.json'), 'w') as f:
    json.dump(angle_45, f, indent=4)

out_filename3 = 'angle_90'
with open(os.path.join(out_dir, out_filename3 + '.json'), 'w') as f:
        json.dump(angle_90, f, indent=4)
        
out_filename4 = 'angle_180'
with open(os.path.join(out_dir, out_filename4 + '.json'), 'w') as f:
        json.dump(angle_180, f, indent=4)
