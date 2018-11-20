import os

dir_in_str = "/home/kabir/data/road_damage_datset_no_annotations"
img_directory = os.fsencode(dir_in_str)
for file in os.listdir(img_directory):
    filename = os.fsdecode(file)
    if filename.endswith(".jpg"):
        print(os.path.join(img_directory, filename))
        continue
    else:
        continue
