import random
list_file = []
with open('duet.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split('\n')[0]
        line = line[0:-4]
        # print(name)
        list_file.append(line)
    f.close()
list_path = []
with open('solo_list.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.split('\n')[0]
        line = line[0:-4]
        # print(name)
        # print(line)
        list_path.append(line)
    f.close()

count = 0
list_pair = []
while count<100:
    pair = random.sample(list_file, 2)
    namefile1 = pair[0].split('/')[2]
    namefile2 = pair[1].split('/')[2]
    # print(namefile2)
    part1 = ""
    part2 = ""
    for s in list_path:
        if namefile1 == s.split('/')[3]:
            # print(namefile1,s)
            part1 = s 
        if namefile2 == s.split('/')[3]:
            # print(namefile2,s)
            part2 = s
    # print(part1)
    # print(part2)
    if part1 != "" and part2 != "":
        print(part1,part2)
        if part1.split('/')[2] != part2.split('/')[2]:
            # print(part1.split('/')[6],part2.split('/')[6])
            list_pair.append(pair[0]+" "+pair[1])
            print(count)
            count += 1
    # if any("abc" in s for s in list_path):
    # if namefile1 != namefile2:
        # print(namefile1)
        # print(namefile2)
        # print(count)

with open('duet_pairs.txt', 'a') as the_file:
    for pair in list_pair:
        the_file.write(pair+'\n')
the_file.close()







# import os
# from os import walk
# import glob
# arr = os.listdir('top_detections/duet')
# # print(arr)
# list_file = []
# with open('duet_list.txt', 'a') as the_file:
#     # for pair in list_pair:
#     for dir in arr:
#         # list_file.append(dir)
#         print(dir)
#         sub = os.listdir("top_detections/duet/" + dir)
#         for subdir in sub:
#             print("top_detections/duet/" + dir+'/'+subdir)
#             the_file.write("top_detections/duet/" + dir+'/'+subdir+'\n')
# the_file.close()