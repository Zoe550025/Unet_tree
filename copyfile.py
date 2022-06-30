import os
import shutil
import re

#dir = "0-5"

# Destination path
#destination = "E:/tzuwen/tree_segmentation2/Unet_tree_2/data/HSV6_test/test"

def deletefile(dest="E:/tzuwen/tree_segmentation2/Unet_tree_2/data/HSV6_test/test"):
    for root, dirs, files in os.walk(dest):
        for f in files:
            try:
                os.remove(os.path.join(root, f))
            except:
                pass

def cpfile(addr,dest="E:/tzuwen/tree_segmentation2/Unet_tree_2/data/HSV6_test/test"):
    pic_name = addr.split("/")[-1]
    #print("copyfile:",addr)
    #print("copyfile：",pic_name)
    if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.jpg|.jpeg|.png)$', pic_name):
        try:
            destination_full_addr = dest + "/" + pic_name
            #print("copyfile：",destination_full_addr)
            shutil.copyfile(addr, destination_full_addr)
            #print("File copied successfully.")
        # If source and destination are same
        except shutil.SameFileError:
            pass
            print("Source and destination represents the same file.")

        # If destination is a directory.
        except IsADirectoryError:
            pass
            print("Destination is a directory.")

        # If there is any permission issue
        except PermissionError:
            pass
            print("Permission denied.")

        # For other errors
        except:
            pass
            print("Error occurred while copying file.")
    else:
        pass
    return destination_full_addr
#cpfile("E:\\tzuwen\\tree_segmentation2\\resize_test\\640_1115\\0\\0-0\\crop\\256x256\\2021-01-27_1552_0.png")

# Copy the content of
# source to destination
#files = os.listdir(destination)
# for dir in files:
#     source = #"E:/tzuwen/tree_segmentation2/resize_test/640_1125/0/"+ dir + "/crop/256x256"
#     try:
#         pics = os.listdir(source)
#     except FileNotFoundError:
#         pass
#     #print(pics)
#     for pic in pics:
#         if re.search(r'([a-zA-Z0-9\s_\\.\-\(\):])+(.jpg|.jpeg|.png)$', pic):
#             try:
#                 source_full_addr = source + "/" + pic
#                 destination_full_addr = destination+ "/"+ dir + "/" + pic
#                 shutil.copyfile(source_full_addr, destination_full_addr)
#                 #print("File copied successfully.")
#
#             # If source and destination are same
#             except shutil.SameFileError:
#                 pass
#                 print("Source and destination represents the same file.")
#
#             # If destination is a directory.
#             except IsADirectoryError:
#                 pass
#                 print("Destination is a directory.")
#
#             # If there is any permission issue
#             except PermissionError:
#                 pass
#                 print("Permission denied.")
#
#             # For other errors
#             except:
#                 pass
#                 print("Error occurred while copying file.")
#         else:
#             pass
#     print(dir,"OK")