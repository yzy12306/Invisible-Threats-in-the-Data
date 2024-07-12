import  os
def  batch_rename_images(input_folder,  output_folder):
     a = 1
     for  img_name  in  os.listdir(input_folder):
            img_path  =  os.path.join(input_folder,  img_name)
            #split_name =img_name.split('.')
            #n= split_name[1]
            new_img_name  =  'rest'+str(a)+ '.png'
            #new_img_name = str(a) + n
            os.rename(img_path,  os.path.join(output_folder,  new_img_name))
            a += 1
            print(f"{img_name}  重命名为  {new_img_name}")
#  示例用法：
input_folder  =  '/home/wayne/PycharmProjects/project/bd-image/r1'
output_folder  = '/home/wayne/PycharmProjects/project/bd-image/out-rest'
batch_rename_images(input_folder,  output_folder)