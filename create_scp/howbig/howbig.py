#!/usr/bin/env python
# Created on 2021/8/12
# Author: Zhenyu Wang

import argparse
import json
import os
import librosa

def preprocess_one_dir(in_dir, out_dir, out_filename):
    file_infos = []
    in_dir = os.path.abspath(in_dir)
    wav_list = os.listdir(in_dir)
    sample_all_number = 0
    sample_all_length = 0
    for wav_file in wav_list:
        if not wav_file.endswith('.wav'):
            continue
        wav_path = os.path.join(in_dir, wav_file)
        samples, sr = librosa.load(wav_path, sr=None)
        length = len(samples)
        sample_all_length = sample_all_length + length
        sample_all_number = sample_all_number+1
        
    seconds = sample_all_length / sr
    hours = seconds / 3600
    sample_all_length_str = str('sample_all_length: {}'.format(sample_all_length))
    sample_all_number_str = str('sample_all_number: {}'.format(sample_all_number))
    hours_str = str('data_time_length_hours: {}'.format(hours))
    file_infos.append(sample_all_length_str)
    file_infos.append(sample_all_number_str)
    file_infos.append(hours_str)
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
    with open(os.path.join(out_dir, out_filename + '.json'), 'w') as f:
        json.dump(file_infos, f, indent=4)


def preprocess(args):
    for data_type in ['tr', 'cv', 'tt']:
        for speaker in ['mix']:
            preprocess_one_dir(os.path.join(args.in_dir, data_type, speaker),
                               os.path.join(args.out_dir, data_type),
                               speaker)


if __name__ == "__main__":
    parser = argparse.ArgumentParser("WSJ0 data preprocessing")
    parser.add_argument('--in-dir', type=str, default='/root/Datasets/wsj0_2mix/wsj0-mix/2speakers/wav16k/min',
                        help='Directory path of wsj0 including tr, cv and tt')
    parser.add_argument('--out-dir', type=str, default='/root/utils/create_scp/WSJ0all/16KHZ',
                        help='Directory path to put output files')
    parser.add_argument('--sample-rate', type=int, default=8000,
                        help='Sample rate of audio file')
    args = parser.parse_args()
    print(args)
    preprocess(args)
