import os
import shutil

images_path = "app/dataset/fireDetectVOCfinal/JPEGImages/"
labels_path = "app/dataset/fireDetectVOCfinal/Annotations/"

destination_path = "app/dataset/"
folder_name = "split_data/"

new_path = destination_path + folder_name

#make dir
if not(os.path.exists(new_path)):
    print('creating directories')
else :
    print ('directories already exists, removing old dirs and creating new one.')
    shutil.rmtree(destination_path+folder_name, ignore_errors=True)  # remove folder if it exist

os.mkdir(new_path)

for i in ["train", "test", "valid"]:
    os.mkdir(new_path + i)
    os.mkdir(new_path + i + "/images")
    os.mkdir(new_path + i + "/labels")

print("done creating all required dirs")

train, test, valid = 0.7, 0.2, 0.1

print(os.getcwd())

original_list = os.listdir(images_path)

total_length = len(original_list)
first_length = int(total_length * train)
second_length = int(total_length * test)
third_length = total_length - first_length - second_length

first_list = original_list[:first_length]
second_list = original_list[first_length:first_length + second_length]
third_list = original_list[first_length + second_length:]

for i in first_list:
    shutil.copyfile(images_path + i, new_path+'train/'+'images/' + ''.join(i.split('.')[:-1])+'.'+i.split('.')[-1])
    shutil.copyfile(labels_path + i.split('.')[0]+'.xml', new_path+'train/'+'labels/' + i.split('.')[0]+'.xml')
    # break

for i in second_list:
    shutil.copyfile(images_path + i, new_path+'test/'+'images/' + ''.join(i.split('.')[:-1])+'.'+i.split('.')[-1])
    shutil.copyfile(labels_path + i.split('.')[0]+'.xml', new_path+'test/'+'labels/' + i.split('.')[0]+'.xml')
    # break

for i in third_list:
    shutil.copyfile(images_path + i, new_path+'valid/'+'images/' + ''.join(i.split('.')[:-1])+'.'+i.split('.')[-1])
    shutil.copyfile(labels_path + i.split('.')[0]+'.xml', new_path+'valid/'+'labels/' + i.split('.')[0]+'.xml')
    # break


print()