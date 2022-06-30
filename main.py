from model import *
from data import *
from show import *
import keras.backend as K
from tensorflow import keras

#os.environ["CUDA_VISIBLE_DEVICES"] = "0"


data_gen_args = dict(rotation_range=0.2,
                     width_shift_range=0.05,
                     height_shift_range=0.05,
                     shear_range=0.05,
                     zoom_range=0.05,
                     horizontal_flip=True,
                     fill_mode='nearest')
#E:\tzuwen\tree_segmentation2\Unet_tree_2\data\membrane\train\image
#data/HSV20/train
myGene = trainGenerator(2,'data\\membrane\\train_30','image','label',data_gen_args,save_to_dir = None)

model = unet()
model_checkpoint = ModelCheckpoint('unet_membrane_77_compile_version.hdf5', monitor='loss',verbose=1, save_best_only=True)
train_history = model.fit(myGene,steps_per_epoch=300,epochs=500,callbacks=[model_checkpoint])

show_train_history(train_history, 'loss', 'accuracy','./acc_loss/77imgs_step-300_epochs-500_compile_version')

# testGene = testGenerator("data/membrane/test")
# results = model.predict_generator(testGene,30,verbose=1)
# saveResult("data/membrane/test/results",results)