import os

import random



# 定义文件路径

calib_dir = '/APP/dataset/training/calib'

train_txt_path = '/APP/dataset/ImageSets/train.txt'

val_txt_path = '/APP/dataset/ImageSets/val.txt'



# 获取所有txt文件名（去掉后缀）

txt_files = [f[:-4] for f in os.listdir(calib_dir) if f.endswith('.txt')]



# 随机选择3712个文件名用于train.txt，3769个用于val.txt

random.shuffle(txt_files)  # 打乱文件列表

train_files = txt_files[:3712]

val_files = txt_files[3712:3712+3769]



# 对文件名进行排序

train_files.sort()

val_files.sort()



# 写入train.txt（如果文件不存在，会自动创建）

with open(train_txt_path, 'w') as train_file:

    for file in train_files:

        train_file.write(file + '\n')



# 写入val.txt（如果文件不存在，会自动创建）

with open(val_txt_path, 'w') as val_file:

    for file in val_files:

        val_file.write(file + '\n')



print("文件分配完成，train.txt和val.txt已创建并排序！")


