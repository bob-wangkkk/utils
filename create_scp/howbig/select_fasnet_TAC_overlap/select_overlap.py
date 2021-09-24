#!/usr/bin/env python
# Created on 2021/8/12
# Author: Zhenyu Wang

import argparse
import json
import os
import librosa
import pickle

path = '/root/GitHub/TAC-master/data/configs/MC_Libri_fixed_test.pkl'
with open(path, 'rb') as f:
    configs = pickle.load(f)
    
overlap_25 = []
overlap_50 = []
overlap_75 = []
overlap_100 = []
for i in range(len(configs)):
    overlap=configs[i]
    #print(overlap['overlap_ratio'])
    #print(type(overlap['overlap_ratio']))
    if overlap['overlap_ratio'] <= 0.25:
        str_25 = str('sample{}'.format(i+1))
        overlap_25.append(str_25)
    elif overlap['overlap_ratio'] <= 0.50:
        str_50 = str('sample{}'.format(i+1))
        overlap_50.append(str_50)
    elif overlap['overlap_ratio'] <= 0.75:
        str_75 = str('sample{}'.format(i+1))
        overlap_75.append(str_75)
    else:
        str_100 = str('sample{}'.format(i+1))
        overlap_100.append(str_100)

overlap_25.append(len(overlap_25))
overlap_50.append(len(overlap_50))
overlap_75.append(len(overlap_75))
overlap_100.append(len(overlap_100))
out_dir = '/root/utils/create_scp/howbig/select_fasnet_TAC_overlap'
out_filename1 = 'overlap_25'
with open(os.path.join(out_dir, out_filename1 + '.json'), 'w') as f:
    json.dump(overlap_25, f, indent=4)
    
out_filename2 = 'overlap_50'
with open(os.path.join(out_dir, out_filename2 + '.json'), 'w') as f:
    json.dump(overlap_50, f, indent=4)

out_filename3 = 'overlap_75'
with open(os.path.join(out_dir, out_filename3 + '.json'), 'w') as f:
        json.dump(overlap_75, f, indent=4)
        
out_filename4 = 'overlap_100'
with open(os.path.join(out_dir, out_filename4 + '.json'), 'w') as f:
        json.dump(overlap_100, f, indent=4)
