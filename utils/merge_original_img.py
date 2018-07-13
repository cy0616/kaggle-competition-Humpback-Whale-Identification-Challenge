import os


src_file = open("0.04sub_0.38_aug_triplet_loss.csv","r")
dst_file = open("./submit_0.38.csv","w")
original_img_file = open("./original_image.csv","r")
_ = original_img_file.readline()
ori_dic = {}
for line in original_img_file:
    id = line.split(",")[0]
    img = line.split(",")[1].strip()
    ori_dic[img] = id

for line in src_file:
    id = line.split(",")[0]
    img = line.split(",")[1].strip()
    if(img not in ori_dic.keys()):
        dst_file.write(line)
    else:
        id= ori_dic[img]+" "+id
        id_list = id.split(" ")
        if(len(id_list) <=5 ):
            content = id +","+img+"\n"
            dst_file.write(content)
        else:
            content=""
            for i in range(5):
                content = content+" "+id_list[i]
            content = content[1:] +","+img+"\n"
            dst_file.write(content)

