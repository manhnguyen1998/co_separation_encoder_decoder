import subprocess
# iimpomport random
import os
list_file = []
# with open('test_duet_duet.txt') as f:
#     lines = f.readlines()
#     for line in lines:
#         line = line.split(" ")
#         video_name1 = line[0]
#         video_name2 = line[1].split('\n')[0]
#         # line = line[0:-4]
#         # print(line)
#         # list_file.append(line)
#         cmd = ["python", "test.py", "--video1_name", video_name1,"--video2_name", video_name2,"--visual_pool", "conv1x1","--unet_num_layers", "7","--data_path", "/ext_data2/manhnh/MUSIC_dataset","--weights_visual", "/home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/visual_best.pth","--weights_unet", "/home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/unet_best.pth","--weights_classifier", "/home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/classifier_best.pth","--num_of_object_detections_to_use", "5","--scene_path", "/home/manhnguyen/new/co-separation/iccv2019_co_separation/iccv2019_co_separation/ADE.h5","--output_dir_root", "resultsD3/duet_duet"]
#         subprocess.run(cmd)

# video_name1 = "duet/top_detections_two_classes/tHvLBLCBHyU_1"
# video_name2 = "duet/top_detections_two_classes/nTMJTm6tqoY_18"
# cmd = ["python", "test.py", "--video1_name", video_name1,"--video2_name", video_name2,"--visual_pool", "conv1x1","--unet_num_layers", "7","--data_path", "/ext_data2/manhnh/MUSIC_dataset","--weights_visual", "/home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/visual_best.pth","--weights_unet", "/home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/unet_best.pth","--weights_classifier", "/home/manhnguyen/new/co-separation/8_500000_checkpoint_dataD3/audioVisual/classifier_best.pth","--num_of_object_detections_to_use", "5","--scene_path", "/home/manhnguyen/new/co-separation/iccv2019_co_separation/iccv2019_co_separation/ADE.h5","--output_dir_root", "results2/"]
# subprocess.run(cmd)

arr = os.listdir('./resultsD3/solo_mul_2v1')
# print(arr)
list_file = []
for dir in arr:
    # list_file.append(dir)
    print(dir)
    list_file.append("./resultsD3/solo_mul_2v1/" + dir)
    # sub = os.listdir("./results/mixed/" + dir)
    cmd = ["python", "evaluateSeparation.py", "--results_dir","./resultsD3/solo_mul_2v1/" + dir]
    subprocess.run(cmd)


# sdr = []
# sdr_mixed = []
# sdr_sdr_mixed  = []
# sir = []
# sar = []
# with open('results2/mixed.txt','a') as f:
#     for folder in list_file:
#         output_file = open(os.path.join(folder, 'eval.txt'),'r')
#         line = output_file.readlines()
#         arr = line[0].split(" ")
#         sdr.append(float(arr[0]))
#         sdr_mixed.append(float(arr[1]))
#         sdr_sdr_mixed.append(float(arr[2]))
#         sir.append(float(arr[3]))
#         sar.append(float(arr[4]))
#         # print(line[0].split(" ")[0])
#         f.write(folder.split('/')[2]+" | "+line[0]+'\n')
#         output_file.close()
#     f.write(str(sum(sdr)/len(sdr))+" "+str(sum(sdr_mixed)/len(sdr_mixed))+" "+str(sum(sdr_sdr_mixed)/len(sdr_sdr_mixed))+" "+str(sum(sir)/len(sir))+" "+str(sum(sar)/len(sar)))
#     f.close()
# # print(sum(sdr)/len(sdr))