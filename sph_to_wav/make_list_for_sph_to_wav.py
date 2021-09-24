#!/usr/bin/env python
# encoding:utf-8
import os
import os.path
import argparse     
 
#in_dir = "/root/utils/test"
#out_path = "/root/utils/output"
# 文件保存路径
sph2pipe_path = "/root/kaldi/tools/sph2pipe_v2.5/sph2pipe"
# sph2pipe工具所在路径
def make_list_for_sph_to_wav(in_dir,out_path):
    f= open("/root/utils/make_sph2pipe_file.txt", 'w')
    for root, dirs, files in os.walk(in_dir):
        for fn in files:
            if fn[len(fn)-3:len(fn)]=='sph':
                sourcefile = in_dir+root[len(in_dir):]+"/"+fn
                targetfile = out_path+"/"+fn[0:(len(fn)-4)]
                s = sph2pipe_path + " -f wav " + sourcefile+" "+targetfile+".wav"+"\n"
                f.write(s.replace('\\','/'))
                
    f.close()
if __name__ == "__main__":
    parser = argparse.ArgumentParser("sph to wav")
    parser.add_argument('--in_dir', help='the address of inputfile')
    parser.add_argument('--out_path', help='the address of outputfile')
    args = parser.parse_args()
    print(args)
    make_list_for_sph_to_wav(args.in_dir,args.out_path)
    