import random
line_num=33361 #ペア数
rand_list=random.sample(range(line_num),k=int(line_num/5)) #20%のペアをランダムにvalidationデータとする
print(len(rand_list))
with open("/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/src/src.txt",mode="r") as s:
    with open("/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/src/src_train.txt",mode="w") as st:
        with open("/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/src/src_val.txt",mode="w") as sv:
            i=0
            for line in s:
                if len(line)==1:
                    print("aaa")
                    line="＜空行＞\n"
                if i in rand_list:
                   sv.write(line)
                else:
                    st.write(line) 
                i+=1
                

with open("/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/tgt/tgt.txt",mode="r") as t:
    with open("/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/tgt/tgt_train.txt",mode="w") as tt:
        with open("/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/tgt/tgt_val.txt",mode="w") as tv:
            i=0
            for line in t:
                if len(line)==1:
                    print("aaa")
                    line="＜空行＞\n"
                if i in rand_list:
                   tv.write(line)
                else:
                    tt.write(line) 
                i+=1