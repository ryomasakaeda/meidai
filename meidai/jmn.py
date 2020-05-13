#形態素ごとに分かち書き

import os 
from pyknp import Juman
from tqdm import tqdm #本当はプログレスバーを出したい
juman=Juman()
src_path="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/replace/inputr.txt" #replaceの出力のうち、元データのinputのほうの
tgt_path="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/replace/outputr.txt" #replaceの出力のうち、元データのoutputのほう

output_src_path="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/src/src.txt"
output_tgt_path="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/tgt/tgt.txt"

with open(src_path,mode="r") as i:
    with open(output_src_path,mode="w") as j:
        for line in tqdm(i):
            result=juman.analysis(line)
            for mrph in result.mrph_list():
                if "。" in mrph.midasi or "、" in mrph.midasi or "「" in mrph.midasi or "」" in mrph.midasi or "？" in mrph.midasi or "?" in mrph.midasi:
                    j.write("")
                else: 
                    j.write(mrph.midasi+" ")
            j.write("\n")

with open(tgt_path,mode="r") as i:
    with open(output_tgt_path,mode="w") as j:
        for line in tqdm(i):
            result=juman.analysis(line)
            for mrph in result.mrph_list():
                if "。" in mrph.midasi or "、" in mrph.midasi or "「" in mrph.midasi or "」" in mrph.midasi or "？" in mrph.midasi or "?" in mrph.midasi:
                    j.write("")
                else: 
                    j.write(mrph.midasi+" ")
            j.write("\n")



    