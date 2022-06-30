from data import *
from model import IOU, dice_metric, jaccard_distance_loss
from keras.models import load_model
from keras.callbacks import Callback
from show import *
import os
# path = "E:/tzuwen/tree_segmentation2/Unet_tree_2/data/HSV6_test/test"

def count_file(addr):
    return len([name for name in os.listdir(addr) if os.path.isfile(os.path.join(addr, name))])

def test_folder(folderpath):
    try:
        os.makedirs(folderpath)
        return folderpath
    # 檔案已存在的例外處理
    except FileExistsError:
        print("檔案已存在。")
        return folderpath


def predict_GUIv3(Pbar, path="E:/tzuwen/tree_segmentation2/Unet_tree_2/data/HSV6_test/test"):
    print("YOYOYO")
    num = count_file(path)
    model = load_model('unet_membrane_HSV6.hdf5')
    save_path = path + "/results"
    testGene = testGenerator(path, num)
    results = model.predict_generator(testGene, steps=num, verbose=0)
    test_folder(save_path)

    saveResult(save_path, results, Pbar)
    print("heyheyhey")
    #print("done")
    # show_train_history(train_history, 'loss', 'accuracy')

def predict_GUIv2(path="E:\\tzuwen\\tree_segmentation2\\Unet_tree_2\\data\\HSV6_test\\test"):
    num = count_file(path)
    model = load_model('unet_membrane_HSV6.hdf5')
    save_path = path + "/results"
    testGene = testGenerator(path, num)
    results = model.predict_generator(testGene, steps=num, verbose=0)
    saveResult2(save_path, results)

def predict(path="E:\\tzuwen\\tree_segmentation2\\Unet_tree_2\\data\\HSV6_test\\test_0523_30ings-model"):
    num = count_file(path)
    print(num)
    model = load_model('unet_membrane_77_compile_version.hdf5', custom_objects={'dice_metric':dice_metric, 'IOU':IOU, "jaccard_distance_loss":jaccard_distance_loss})
    save_path = test_folder(path + "/results")
    print(save_path)
    testGene = testGenerator(path, num)
    results = model.predict_generator(testGene, steps=num, verbose=0)
    #test_folder(save_path)
    saveResult2(save_path, results)

#predict()
# root_addr = "E:/tzuwen/tree_segmentation2/Unet_tree_2/data/HSV6/test/test_2-19"
# for dir in os.listdir(root_addr):
#     print("Now is ",dir)
#     count_file_addr = os.path.join(root_addr,dir)
#     pic_num = count_file(count_file_addr)
#     testGene = testGenerator("data/HSV6/test/test_2-19"+dir,pic_num)
#     results = model.predict_generator(testGene, steps=pic_num, verbose=1)
#     create_results_dir_addr = count_file_addr + "/results"
#     if not os.path.isdir(count_file_addr+"results"):
#         os.makedirs(count_file_addr)
#     saveResult("data/HSV6/test/test_2-19"+dir+"/results", results)        #remenber to build results dir
# #show_train_history(train_history, 'loss', 'accuracy')
