from moviepy.editor import *
import os

# file = open(fr"filenames_BIWI.txt", "r", encoding='utf-8') 
# file_list_biwi = file.readlines()
# file.close()

file = open(fr"filenames_VOCASET.txt", "r", encoding='utf-8') 
file_list_vocaset = file.readlines()
file.close()

type = {
    'codetalker',
    'faceformer',
    'gt',
    'meshtalk',
    'selftalk',
    'voca'
}


# # BIWI
# for t in type:
#     for file in file_list_biwi:
#         pro = 'BIWI'
#         # 去掉每行末尾的换行符
#         file = file.strip()
#         video_path1 = f'{pro}/ours/{file}'
#         video_path2 = f'{pro}/{t}/{file}'

#         # 加载两个视频文件
#         video1 = VideoFileClip(video_path1)
#         if os.path.exists(video_path2):
#             video2 = VideoFileClip(video_path2)
#         else:
#             index = video_path2.index('_', video_path2.index('_') + 1)
#             path = video_path2[:index]
#             files = os.listdir(f'{pro}/{t}')
#             for f in files:
#                 f = f'{pro}/{t}/' + f
#                 if f.startswith(path):
#                     video2 = VideoFileClip(f)

#         # 确保视频时长相同
#         min_duration = min(video1.duration, video2.duration)
#         video1 = video1.set_duration(min_duration)
#         video2 = video2.set_duration(min_duration)

#         # 合并两个视频
#         final_clip = clips_array([[video1, video2]])

#         # 保存最终合并后的视频
#         final_clip.write_videofile(f"user_study/{pro}/{t}/{file}", codec='libx264')

# VOCASET
for t in type:
    for file in file_list_vocaset:
        pro = 'VOCASET'
        # 去掉每行末尾的换行符
        file = file.strip()
        video_path1 = f'{pro}/ours/{file}'
        video_path2 = f'{pro}/{t}/{file}'

        # 加载两个视频文件
        video1 = VideoFileClip(video_path1)
        if os.path.exists(video_path2):
            video2 = VideoFileClip(video_path2)
        else:
            path = video_path2.split("_condition")[0]
            files = os.listdir(f'{pro}/{t}')
            for f in files:
                f = f'{pro}/{t}/' + f
                if f.startswith(path):
                    video2 = VideoFileClip(f)

        # 确保视频时长相同
        min_duration = min(video1.duration, video2.duration)
        video1 = video1.set_duration(min_duration)
        video2 = video2.set_duration(min_duration)

        # 合并两个视频
        final_clip = clips_array([[video1, video2]])

        # 保存最终合并后的视频
        final_clip.write_videofile(f"user_study/{pro}/{t}/{file}", codec='libx264')