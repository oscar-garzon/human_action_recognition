import cv2

def dibujar_rect_clas(img, coordenadas, clasificacion):
    """Dibuja el rectangulo definido por coordenadas en img.
       Pone la clasificación del objeto.
       
       img es un numpy array
       coordenadas es una lista con dos puntos opuestos del rectángulo
       clasificación es la clase del objeto
       
       Regresa un numpy array con el rectangulo dibujado"""
    poner_clasificacion(img, 
                        (coordenadas[0], coordenadas[1]),
                        clasificacion)
    cv2.rectangle(img, 
                 (coordenadas[0], coordenadas[1]),
                 (coordenadas[2], coordenadas[3]),
                 255,                  #color de la linea
                 2)                    #grosor 
    return img

def poner_clasificacion(img, coord, clasificacion):
    """Escribe la clasificación en la imagen.
    
    coord: una tupla con las coordenadas
    clasificacion: el texto que se va poner"""
    cv2.putText(
         img, #numpy array on which text is written
         clasificacion, #text
         coord, #position at which writing has to start
         cv2.FONT_HERSHEY_SIMPLEX, #font family
         1, #font size
         (209, 80, 0, 255), #font color
         3) #font stroke
    return img

































""" para cada imagen en el directorio necesito:
    -arreglo
    -nombre, bndbox coord

No se si tengan el mismo orden. Entonces las consigo por separado y aqui las pego.

imagenes: un diccionario con key filename y value arreglo {filename: img_arr}
anotaciones: un diccionario con key filename y value una lista con el object_name, bndbox_values.
            solo el primero y principal objeto en el directorio.  {filename: [name, x, y, z, w]}

imagenes = obtener_imagenes(IMG_PATH)
anotaciones = obtener_anotaciones(ANOTACIONES_PATH)


train_pctg = 0.8
x_train = dataset()


imagenes = np.array([[[0,0,0]]])

for PATH_IMG in listdir(filepath):
    img_arr = np.asarray(resize(PATH_IMG))



    img = np.arra
    img_array = image.imread(filepath + '/' + img) 
    print(img_array.ndim)
    print(imagenes.ndim)    
    imagenes = np.append(imagenes, img_array, 0)

return imagenes

def resize(PATH_IMG):
    with Image.open(PATH_IMG) as img:
        img = img.resize((448, 448))
    
    return img 



img = load_data('test') 
print(img.shape)

 """