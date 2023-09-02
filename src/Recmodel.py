from keras.applications import vgg16
from keras.preprocessing.image import load_img, img_to_array
from keras.models import Model
from keras.applications.imagenet_utils import preprocess_input
import pickle
from PIL import Image
import os
import matplotlib.pyplot as plt
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import pandas as pd

'''This File is a script of the content based reccomendation model which we are using to get similar
     available products available on our catalog of the IMAGINARY PRODUCT the user is wanting '''
     
'''The model used is VGG-16(computer vision) which is used to get the embeddings and finally based on 
     cosine similariy we suggest the user most similar product the user is seeing(image) himself into the imaginary
     product'''


def getSimilar(name):
    imgs_path = "/home/btech/nityanand.mathur/aman/grid/images/"
    imgs_model_width, imgs_model_height = 224, 224

    nb_closest_images = 20  # number of most similar images to retrieve

    # In[19]:

    vgg_model = vgg16.VGG16(weights='imagenet')

    # remove the last layers in order to get features instead of predictions
    feat_extractor = Model(inputs=vgg_model.input, outputs=vgg_model.get_layer("fc2").output)

    # print the layers of the CNN
    feat_extractor.summary()
    files = [imgs_path + x for x in os.listdir(imgs_path) if "jpg" in x or "jpeg" in x or "png" in x]

    files.append(name)
    importedImages = []
    print("wip")
    for f in files:
        try:
            filename = f
            original = load_img(filename, target_size=(224, 224))
            numpy_image = img_to_array(original)
            image_batch = np.expand_dims(numpy_image, axis=0)
            importedImages.append(image_batch)
        except Exception as e:
            print(f"Error loading {filename}: {e}")

    images = np.vstack(importedImages)

    processed_imgs = preprocess_input(images.copy())
    imgs_features = feat_extractor.predict(processed_imgs)

    print("features successfully extracted!")
    cosSimilarities = cosine_similarity(imgs_features)
    cos_similarities_df = pd.DataFrame(cosSimilarities, columns=files, index=files)
    cos_similarities_df.head()

    def retrieve_most_similar_products(given_img):
        closest_imgs = cos_similarities_df[given_img].sort_values(ascending=False)[1:nb_closest_images + 1].index
        closest_imgs_scores = cos_similarities_df[given_img].sort_values(ascending=False)[1:nb_closest_images + 1]
        ci = []
        for i in range(0, len(closest_imgs)):
            ci.append(os.path.basename(closest_imgs[i]))
            ci.append(str(closest_imgs_scores[i]))
            print("similarity score : ", closest_imgs_scores[i])
        return ci
    files.remove(name)
    l = retrieve_most_similar_products(name)
    return l


