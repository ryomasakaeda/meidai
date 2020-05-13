#いらない部分を取り除くプログラム。BTSJのコーパス用に作ったのをもとにしてるので、余計なものが多い
import re
import os

reg_jinmei=r"「人名(\d+)」"
reg_chimei=r"「地名(\d+)」"
reg_square=r"\[[^\[\]]*\]"
reg_tri=r"<[^<>]*笑いながら|軽い笑い|若干笑い気味(に)?|(大きな)?笑い|笑>"
reg_tri2=r"＜[^＜＞]*笑いながら|軽い笑い|若干笑い気味(に)?|(大きな)?笑い|笑＞"
reg_wave=r"{[^{}]*}"
reg_bra=r"\([^\(\)]*\)"
reg_double="《[^《》]*》"
reg_list=[reg_jinmei,reg_chimei]

no=1

input_file="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/input.txt"
output_file="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/replace/inputr.txt"

with open(input_file,mode="r") as ifn:
    with open(output_file,mode="w") as ofn:
        for line in ifn:
            # print(line)
            # if re.search(reg_jinmei,line):
            #     line=re.sub(reg_jinmei,"＜人名＞",line)
            # if re.search(reg_chimei,line):
            #     line=re.sub(reg_chimei,"＜地名＞",line)
            if "【" in line:
                line=line.replace("【","")
            if "＊" in line:
                line=line.replace("＊","")
            if "】" in line:
                line=line.replace("】","")
            if "=" in line:
                line=line.replace("=","")
            if "#" in line:
                line=line.replace("#","")
            if re.search(reg_square,line):
                line=re.sub(reg_square,"",line)
            if re.search(reg_tri,line):
                line=re.sub(reg_tri,"",line)
            if re.search(reg_wave,line):
                line=re.sub(reg_wave,"",line)
            if "＞" in line:
                line=line.replace("＞","")
            if "＜" in line:
                line=line.replace("＜","")
            if re.search(reg_bra,line):
                line=re.sub(reg_bra,"",line)
            if re.search(reg_double,line):
                line=re.sub(reg_double,"",line)
            if line=="。\n":
                line="\n"
                
            ofn.write(line)
    no+=1

input_file="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/output.txt"
output_file="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/replace/outputr.txt"
no=1
with open(input_file,mode="r") as ifn:
    with open(output_file,mode="w") as ofn:
        for line in ifn:
            # print(line)
            # if re.search(reg_jinmei,line):
            #     line=re.sub(reg_jinmei,"＜人名＞",line)
            # if re.search(reg_chimei,line):
            #     line=re.sub(reg_chimei,"＜地名＞",line)
            if "【" in line:
                line=line.replace("【","")
            if "＊" in line:
                line=line.replace("＊","")
            if "】" in line:
                line=line.replace("】","")
            if "=" in line:
                line=line.replace("=","")
            if "#" in line:
                line=line.replace("#","")
            if re.search(reg_square,line):
                line=re.sub(reg_square,"",line)
            if re.search(reg_tri,line):
                line=re.sub(reg_tri,"",line)
            if re.search(reg_wave,line):
                line=re.sub(reg_wave,"",line)
            if "＞" in line:
                line=line.replace("＞","")
            if "＜" in line:
                line=line.replace("＜","")
            if re.search(reg_bra,line):
                line=re.sub(reg_bra,"",line)
            if re.search(reg_double,line):
                line=re.sub(reg_double,"",line)
            if line=="。\n":
                line="\n"
                
            ofn.write(line)
    no+=1
    