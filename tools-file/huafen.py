import os
import numpy as np
import random
import shutil  # 导入移动模块

data_path = "/home/wayne/PycharmProjects/project/datasets/sub-imagenet-200/train"
sub_path = ['train4']

fileNames = os.listdir(data_path)  # 获取当前路径下的文件名，返回List
num_plt = len(fileNames)
test_path = '/home/wayne/PycharmProjects/project/datasets/sub-imagenet-200-bd/inject_a/org-train'
#train_path ='/home/wayne/PycharmProjects/project/datasets/sub-imagenet-200/test/train'

for folder in sub_path:
    # test = []
    file_path = data_path + '/' + folder  # 进入类型文件夹
    fileNames = os.listdir(file_path)  # 读取文件夹中的所有文件名
    num_plt = len(fileNames)  # 得到文件夹中图片的总数
    num_test = num_plt //8  # 计算测试集的总数
    index_test = random.sample(range(num_plt), num_test)  # 从num_plt个文件中随机选出num_test个作为索引,random.sample用于生成不重复的随机数
    index_test.sort(reverse=True)  # 对索引进行排序，使其从后往前删除
    # print(index_test)
    for i in index_test:
        plt_test = fileNames.pop(i)
        shutil.copy(file_path + '/' + plt_test, test_path)
#    for i in fileNames:
#        shutil.copy(file_path + '/' + i, train_path)


