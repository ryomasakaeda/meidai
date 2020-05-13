#元データのinputとoutputを分ける

input_file="/mnt/c/Users/ryomasakaeda/dialogue_research/corpus/meidai/sequence.txt"#https://qiita.com/knok/items/df7a155d17e3c9a12e94の出力
output_path="/mnt/c/Users/ryomasakaeda/dialogue_research/dataset/meidai/"
with open (input_file,mode="r") as i:
    with open(output_path+"input.txt",mode="w") as oi:
        with open(output_path+"output.txt",mode="w") as oo:
            for line in i:
                if line.split()[0]=="input:":
                    oi.write(line.replace("input: ",""))
                else:
                    oo.write(line.replace("output: ",""))
                
