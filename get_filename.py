import os

folder_list = {
    "user_study/BIWI/codetalker",
    "user_study/BIWI/faceformer",
    "user_study/BIWI/gt",
    "user_study/BIWI/meshtalk",
    "user_study/BIWI/voca",
    "user_study/BIWI/selftalk",
    "user_study/VOCASET/codetalker",
    "user_study/VOCASET/faceformer",
    "user_study/VOCASET/gt",
    "user_study/VOCASET/meshtalk",
    "user_study/VOCASET/voca",
    "user_study/VOCASET/selftalk",
}


for folder_path in folder_list:
    # 获取文件夹中的文件名列表
    file_names = os.listdir(folder_path)
    # 确定文本文件的路径：如BIWI_codetalker
    txt_file_name = "_".join(folder_path.split("/")[1:])
    # txt文件路径
    txt_file_path = fr"filename/{txt_file_name}.txt"
    # 打开txt文件并写入文件名
    with open(txt_file_path, 'w') as txt_file:
        for file_name in file_names:
            txt_file.write(folder_path + '/' + file_name + '\n')

# folder_list = {
#     "user_study/BIWI/voca",
#     "user_study/BIWI/meshtalk",
#     "user_study/BIWI/faceformer",
#     "user_study/BIWI/codetalker",
#     "user_study/BIWI/gt",
#     "user_study/VOCASET/voca",
#     "user_study/VOCASET/meshtalk",
#     "user_study/VOCASET/faceformer",
#     "user_study/VOCASET/codetalker",
#     "user_study/VOCASET/gt",
# }


# Ours vs. VOCA 
# Ours vs. MeshTalk 
# Ours vs. FaceFormer 
# Ours vs. codetalker
# Ours vs. GT
# folder_list = [
#     "BIWI_voca.txt",
#     "BIWI_meshtalk.txt",
#     "BIWI_faceformer.txt",
#     "BIWI_codetalker.txt",
#     "BIWI_gt.txt",
#     "VOCASET_voca.txt",
#     "VOCASET_meshtalk.txt",
#     "VOCASET_faceformer.txt",
#     "VOCASET_codetalker.txt",
#     "VOCASET_gt.txt"
# ]