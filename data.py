from os import listdir
from math import sqrt

import numpy as np 
from sklearn.model_selection import train_test_split
from PIL import Image 
import xmltodict 

def load_data(filepath):
    """Regresa dos tuplas, cada una con un np.array de las imágenes y otro np.array
        con la clasificación y las coordenads del bounding box normalizadas """

    filenames = listdir(filepath + '/Annotations')
    filenames = [ fn.replace('.xml', '') for fn in filenames]

    dataset = {}
    total_files = len(filenames)

    for i, filename in enumerate(filenames):
        if i == 500:
            break
        dataset[filename] = [get_img(filename, filepath), get_label(filename, filepath)]  
        print(i, '/', total_files)
    
    x = np.asarray([valores[0] for valores in dataset.values()])[:]   #FALTA PONER PORCENTAJE
    y = np.asarray([valores[1] for valores in dataset.values()])  #FALTA PONER PORCENTAJE

    x_train, x_test = train_test_split(x, test_size=0.1)
    y_train, y_test = train_test_split(y, test_size=0.1)

    print('Descarga Completa')

    return (x_train, y_train), (x_test, y_test)


def get_img(filename, filepath):
    """Regresa el numpy array que representa a la imagen filename
    con un resize a 448x448"""
    IMAGE_PATH = filepath + '/JPEGImages/' + filename + '.jpg'
    
    with Image.open(IMAGE_PATH) as img:
        img_rs = img.resize((100,100))
    
    return np.asarray(img_rs)/255


def get_label(filename, filepath):
    """Regresa la clasificación en hot-one encoding y las coordenadas
    del bound box x,y, sqrt(height) y sqrt(width) normalizadas(448)"""

    #Leer el xml
    xml_file_path = filepath + '/Annotations/' + filename + '.xml'
    with open(xml_file_path, 'r', encoding='utf-8') as file:
        my_xml = file.read()
    
    #parser el xml
    annotations = xmltodict.parse(my_xml)

    object_ = annotations['annotation']['object']

    if type(object_) == list:
        object_ = object_[0]
    
    name = object_['name']
    xmin = float(object_['bndbox']['xmin']) / 448.0
    ymin = float(object_['bndbox']['ymin']) / 448.0 
    xmax = float(object_['bndbox']['xmax']) / 448.0
    ymax = float(object_['bndbox']['ymax']) / 448.0

    label = obtener_onehotencoding(name)
    bndbox_coord = obtener_centro_width_height_coord(xmin, ymin, xmax, ymax)
    for coord in bndbox_coord:
        label.append(coord)
        
    return label


def obtener_onehotencoding(name):
    """Toma el nombre de una clasificación y regresa su one
    hot encoding. """

    clasificaciones = { 'person': 0.0, 
                        'bird': 1.0,
                        'cat': 2.0,
                        'cow': 3.0,
                        'dog': 4.0, 
                        'horse': 5.0,
                        'sheep': 6.0,
                        'aeroplane': 7.0,
                        'bicycle': 8.0,
                        'boat': 9.0,
                        'bus': 10.0,
                        'car': 11.0,
                        'motorbike': 12.0,
                        'train': 13.0, 
                        'bottle': 14.0,
                        'chair': 15.0,
                        'diningtable': 16.0,
                        'pottedplant': 17.0,
                        'sofa': 18.0,
                        'tvmonitor': 19.0 }

    onehotencoding = [ 
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        0.0, 0.0, 0.0, 0.0, 0.0,
        ]
    onehotencoding[ int(clasificaciones[name]) ] = 1.0

    return onehotencoding                  

def obtener_centro_width_height_coord(xmin, ymin, xmax, ymax):
    """Toma coordenadas de dos puntos opuestos de un rectángulo y
    regresa las coordenadas de ese mismo rectángulo pero definido
    por su punto en el centro y la sqrt(altura) y sqrt(ancho)."""
    x_center = (xmax + xmin)/2
    y_center = (ymax + ymin)/2
    width_root = xmax - xmin
    height_root = ymax - ymin
    
    return [x_center, y_center, sqrt(width_root), sqrt(height_root)]


