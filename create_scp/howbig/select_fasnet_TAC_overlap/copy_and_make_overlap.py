#!/usr/bin/env python
# Created on 2021/8/13
# Author: Zhenyu Wang

import json
import os
import pickle
import shutil

dir = '/root/utils/create_scp/howbig/select_fasnet_TAC_overlap/overlap_100.json'
with open(dir,'r') as json_file:
    data = json.load(json_file)
file_path = '/root/Datasets/Librimix_fasnet/MC_Libri_fixed/test/6mic'
target_path = '/root/Datasets/Librimix_fasnet/MC_Libri_fixed/test/6mic_overlap_100'
print(type(data))
for sample in data:
    if not sample.startswith('sample'):
        continue
    target = os.path.join(target_path,sample)
    file = os.path.join(file_path,sample)
    shutil.copytree(file, target)

    