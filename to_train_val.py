 
import os
import shutil
 
# 【一】、读取train.txt文件
with open('./ImageSets/train.txt', 'r') as file:
    # 逐行读取train.txt文件中的文件名ID
    file_ids = [line.strip() for line in file]
 
# 【1】calib
# 指定路径A和路径B
path_A = './training/calib'
path_B = './train/calib'
 
# 如果路径B不存在，创建它
if not os.path.exists(path_B):
    os.makedirs(path_B)
 
# 遍历文件名ID并复制文件到路径B
for file_id in file_ids:
    source_file = os.path.join(path_A, f"{file_id}.txt")
    destination_file = os.path.join(path_B, f"{file_id}.txt")
    
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"文件未找到：{file_id}.txt")
 
 
# 【2】image_2
# 指定路径A和路径B
path_A = './training/image_2'
path_B = './train/image_2'
 
# 如果路径B不存在，创建它
if not os.path.exists(path_B):
    os.makedirs(path_B)
 
# 遍历文件名ID并复制文件到路径B
for file_id in file_ids:
    source_file = os.path.join(path_A, f"{file_id}.png")
    destination_file = os.path.join(path_B, f"{file_id}.png")
    
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"文件未找到：{file_id}.txt")
 
 
# 【3】label_2
# 指定路径A和路径B
path_A = './training/label_2'
path_B = './train/label_2'
 
# 如果路径B不存在，创建它
if not os.path.exists(path_B):
    os.makedirs(path_B)
 
# 遍历文件名ID并复制文件到路径B
for file_id in file_ids:
    source_file = os.path.join(path_A, f"{file_id}.txt")
    destination_file = os.path.join(path_B, f"{file_id}.txt")
    
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"文件未找到：{file_id}.txt")
 
# 【二】、读取valtxt文件
with open('./ImageSets/val.txt', 'r') as file:
    # 逐行读取val.txt文件中的文件名ID
    file_ids = [line.strip() for line in file]
 
# 【1】calib
# 指定路径A和路径B
path_A = './training/calib'
path_B = './val/calib'
 
# 如果路径B不存在，创建它
if not os.path.exists(path_B):
    os.makedirs(path_B)
 
# 遍历文件名ID并复制文件到路径B
for file_id in file_ids:
    source_file = os.path.join(path_A, f"{file_id}.txt")
    destination_file = os.path.join(path_B, f"{file_id}.txt")
    
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"文件未找到：{file_id}.txt")
 
 
# 【2】image_2
# 指定路径A和路径B
path_A = './training/image_2'
path_B = './val/image_2'
 
# 如果路径B不存在，创建它
if not os.path.exists(path_B):
    os.makedirs(path_B)
 
# 遍历文件名ID并复制文件到路径B
for file_id in file_ids:
    source_file = os.path.join(path_A, f"{file_id}.png")
    destination_file = os.path.join(path_B, f"{file_id}.png")
    
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"文件未找到：{file_id}.txt")
 
 
# 【3】label_2
# 指定路径A和路径B
path_A = './training/label_2'
path_B = './val/label_2'
 
# 如果路径B不存在，创建它
if not os.path.exists(path_B):
    os.makedirs(path_B)
 
# 遍历文件名ID并复制文件到路径B
for file_id in file_ids:
    source_file = os.path.join(path_A, f"{file_id}.txt")
    destination_file = os.path.join(path_B, f"{file_id}.txt")
    
    if os.path.exists(source_file):
        shutil.copy(source_file, destination_file)
    else:
        print(f"文件未找到：{file_id}.txt")
