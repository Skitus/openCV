import cv2
import numpy as np
import sys

# Этот код использует BFMatcher для сопоставления особенностей, обнаруженных алгоритмом SIFT, и применяет тест отношения для фильтрации хороших совпадений.
#  Затем он вычисляет гомографию с использованием метода RANSAC и преобразует координаты краев первого изображения во второе пространство изображения. 
# Наконец, он отрисовывает преобразованные границы на втором изображении и сохраняет результат. Пожалуйста, проверьте, что это соответствует
#  вашим требованиям.

# Этот скрипт выполняет процесс "склейки" изображений, используя SIFT (Scale-Invariant Feature Transform) для обнаружения и описания особенностей каждого изображения, BFMatcher для сопоставления этих особенностей, и RANSAC для вычисления гомографии и применения перспективных преобразований. Вот что делает каждый блок кода:

# Чтение изображений: Загрузка изображений по указанным путям файлов. Затем проверяет, успешно ли загружены все изображения.

# Обнаружение и описание особенностей: Используется SIFT для обнаружения и описания особенностей каждого изображения. Результаты сохраняются в списки keypoints и descriptors.

# Сопоставление особенностей: Используется BFMatcher для сопоставления особенностей между первым и вторым изображением. Сопоставления затем фильтруются с использованием теста отношения, предложенного в статье Лоу, чтобы отобрать "хорошие" совпадения.

# Вычисление гомографии: Если хороших совпадений достаточно (более 10), то гомография вычисляется с использованием метода RANSAC. Гомография – это матрица преобразования, которая описывает, как перейти от координат в одном изображении к координатам в другом.

# Применение перспективных преобразований: Используя вычисленную гомографию, код преобразует координаты границ первого изображения в пространство второго изображения.

# Отображение результатов: Результаты затем отображаются на втором изображении, а конечное изображение сохраняется в файл.

# Этот код служит для совмещения двух изображений на основе общих особенностей. Он может быть полезным для создания панорамных изображений или выполнения других задач, где необходимо объединить несколько изображений в одно.

# Этот код попытается выполнить процесс "склейки" изображений сначала в заданном порядке, а затем в обратном порядке, если первоначально не найдено достаточно "хороших" совпадений.
#Склейка изображений в данном скрипте реализована с учётом возможности свободного перемещения и поворота изображений. Однако, в большинстве случаев, метод SIFT (Scale-Invariant Feature Transform), используемый для обнаружения и сопоставления особенностей изображения, эффективно работает для панорамных изображений, которые обычно создаются путем горизонтальной или вертикальной склейки.

#Тем не менее, общий алгоритм не ограничивается только горизонтальной или вертикальной склейкой. Он может найти и сопоставить особенности между двумя изображениями, независимо от того, как они расположены относительно друг друга. Важно, чтобы между изображениями было достаточно общих особенностей для успешного сопоставления.

#В общем, если вы хотите склеить изображения сверху вниз, этот код должен работать без изменений. Однако, результат может варьироваться в зависимости от конкретных изображений и наличия на них уникальных особенностей для сопоставления.

#Текущий код может обрабатывать только два изображения за раз, поскольку он использует подход "pairwise" (попарный) для склейки изображений. Однако, вы можете расширить этот подход, чтобы обрабатывать более двух изображений.

#Один из подходов - это использовать цикл, чтобы последовательно склеивать изображения по два. Сначала первое и второе изображения склеиваются вместе, затем результат склеивается с третьим изображением, затем этот результат склеивается с четвертым изображением, и так далее.

#Однако, учтите, что качество конечного изображения может ухудшаться с увеличением количества изображений из-за накопления ошибок преобразования и искажения из-за многократного применения преобразований.

#Если у вас есть большое количество изображений для склейки, рекомендуется использовать более сложные алгоритмы, такие как алгоритмы глобального сопоставления, которые учитывают все изображения сразу, чтобы минимизировать общую ошибку.

def stitch_images(file_paths):
    print('start')
    # Read the images
    images = [cv2.imread(file) for file in file_paths]
    
    # Check if images are loaded
    for i in range(len(images)):
        if images[i] is None:
            print('ERROR: Image ', file_paths[i], ' could not be read')
            exit()

    # Detect and describe features
    sift = cv2.SIFT_create()
    keypoints = []
    descriptors = []
    for image in images:
        kp, des = sift.detectAndCompute(image, None)
        keypoints.append(kp)
        descriptors.append(des)
    print('key end')
    # Function to find good matches and stitch images
    def find_matches_and_stitch(images, descriptors, keypoints):
        # Match features using BFMatcher
        bf = cv2.BFMatcher()
        matches = bf.knnMatch(descriptors[0], descriptors[1], k=2)

        # Apply ratio test as per Lowe's paper
        good = []
        for m,n in matches:
            if m.distance < 0.75*n.distance:
                good.append(m)

        return good, matches
    print('mau')
    # Check good matches in both orders
    good_normal, matches_normal = find_matches_and_stitch(images, descriptors, keypoints)
    good_reversed, matches_reversed = find_matches_and_stitch(images[::-1], descriptors[::-1], keypoints[::-1])

    # Determine the better order
    if len(good_normal) >= len(good_reversed):
        good_matches, matches = good_normal, matches_normal
    else:
        good_matches, matches = good_reversed, matches_reversed
        images = images[::-1]
        keypoints = keypoints[::-1]

    # Stitch images
    if len(good_matches)>10:
        src_pts = np.float32([ keypoints[0][m.queryIdx].pt for m in good_matches ]).reshape(-1,1,2)
        dst_pts = np.float32([ keypoints[1][m.trainIdx].pt for m in good_matches ]).reshape(-1,1,2)

        M, mask = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC,5.0)
        matchesMask = mask.ravel().tolist()

        h,w,d = images[0].shape
        pts = np.float32([ [0,0],[0,h-1],[w-1,h-1],[w-1,0] ]).reshape(-1,1,2)
        dst = cv2.perspectiveTransform(pts,M)

        img2 = cv2.polylines(images[1],[np.int32(dst)],True,255,3, cv2.LINE_AA)
        draw_params = dict(matchColor = (0,255,0), # draw matches in green color
                           singlePointColor = None,
                           matchesMask = matchesMask, # draw only inliers
                           flags = 2)

        img3 = cv2.drawMatches(images[0],keypoints[0],img2,keypoints[1],good_matches,None,**draw_params)
        cv2.imwrite('./result2certical.jpg', img3)
    else:
        print("Not enough good matches found in both orders of images")

if __name__ == "__main__":
    # List of image file paths
    # image_paths = ['/home/artur/Downloads/5/4.JPG','/home/artur/Downloads/5/6.JPG']
    image_paths = ['/home/artur/Downloads/2/1.jpg','/home/artur/Downloads/2/2.jpg']
    
    # Call the function
    stitch_images(image_paths)



# GEO DATA
# import os
# import cv2
# import gdal
# import piexif
# from PIL import Image
# from pyproj import Proj, transform

# def stitch_images_with_gdal(file_paths):
#     # Получение геоданных из EXIF
#     def get_geodata(image_path):
#         img = Image.open(image_path)
#         exif_data = piexif.load(img.info['exif'])

#         lat = exif_data['GPS'][piexif.GPSIFD.GPSLatitude]
#         lon = exif_data['GPS'][piexif.GPSIFD.GPSLongitude]

#         # Преобразование координат в градусы
#         lat = lat[0] + lat[1]/60 + lat[2]/3600
#         lon = lon[0] + lon[1]/60 + lon[2]/3600

#         return lat, lon

#     # Преобразование изображений в геотифы
#     def convert_to_geotiff(image_path, lat, lon):
#         # Преобразование координат в проекцию UTM
#         in_proj = Proj(init='epsg:4326')
#         out_proj = Proj(init='epsg:32632')  # пример кода для зоны UTM 32N, измените это в соответствии с вашим регионом
#         utm_x, utm_y = transform(in_proj, out_proj, lon, lat)

#         # Создание геотрансформации
#         geotransform = (utm_x, 1, 0, utm_y, 0, -1)

#         # Открытие изображения с помощью GDAL
#         image_ds = gdal.Open(image_path, gdal.GA_ReadOnly)

#         # Создание нового GeoTIFF файла
#         driver = gdal.GetDriverByName('GTiff')
#         file_name, file_extension = os.path.splitext(image_path)
#         output_file = f"{file_name}_geo.tif"

#         out_ds = driver.CreateCopy(output_file, image_ds, 0)

#         # Установка новой геотрансформации в выходной файл
#         out_ds.SetGeoTransform(geotransform)

#         out_ds = None
#         image_ds = None

#         return output_file

#     geotiff_files = []
#     for file in file_paths:
#         lat, lon = get_geodata(file)
#         geotiff_file = convert_to_geotiff(file, lat, lon)
#         geotiff_files.append(geotiff_file)

#     # Объединение GeoTIFF файлов с помощью GDAL
#     output_file = 'orthophoto.tif'
#     files_string = " ".join(geotiff_files)
#     os.system(f'gdal_merge.py -o {output_file} {files_string}')

#     # Удаление временных GeoTIFF файлов
#     for file in geotiff_files:
#         os.remove(file)

# if __name__ == "__main__":
#     image_paths = ['/home/artur/Downloads/2/1.jpg','/home/artur/Downloads/2/2.jpg']
#     stitch_images_with_gdal(image_paths)
