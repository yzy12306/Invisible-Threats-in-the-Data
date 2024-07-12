from PIL import Image
import os

# 需要转换的图片所在的文件夹路径
folder_path = '/home/wayne/PycharmProjects/project/1'
# 需要保存图片的位置路径
save_path = '/home/wayne/PycharmProjects/project/2'
# 遍历文件夹中的所有文件
for file in os.listdir(folder_path):
    # 如果文件是 JPG 格式的
    if file.endswith('.JPEG'):
        # 打开文件
        img = Image.open(os.path.join(folder_path, file))
        # 获取文件名（不包含扩展名）
        file_name = os.path.splitext(file)[0]
        # 保存为 PNG 格式
        img.save(os.path.join(save_path, file_name + '.png'))

