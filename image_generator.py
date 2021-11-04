import numpy as np
from PIL import Image

IMAGE_SIZE = 1000

if __name__ == '__main__':
    # Два изображения одинаковой яркости, но полностью разного цвета
    img_1_1_data = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
    img_1_1_data[..., 0] = 255
    img_1_1 = Image.fromarray(img_1_1_data)
    img_1_1.save('images/img_1_1.jpg', format='jpeg')

    img_1_2_data = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
    img_1_2_data[..., 2] = 255
    img_1_2 = Image.fromarray(img_1_2_data)
    img_1_2.save('images/img_1_2.jpg', format='jpeg')

    # Два изображения одинаковой яркости, но почти одного цвета
    img_2_1_data = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
    img_2_1_data[..., 0] = 120
    img_2_1_data[..., 1] = 121
    img_2_1_data[..., 2] = 120
    img_2_1 = Image.fromarray(img_2_1_data)
    img_2_1.save('images/img_2_1.jpg', format='jpeg')

    img_2_2_data = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
    img_2_2_data[..., 0] = 120
    img_2_2_data[..., 1] = 120
    img_2_2_data[..., 2] = 121
    img_2_2 = Image.fromarray(img_2_2_data)
    img_2_2.save('images/img_2_2.jpg', format='jpeg')

    # Два изображения. Одна - шахматная доска, вторая - инвертированная первая
    img_3_1_data = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
    for i in range(IMAGE_SIZE):
        for j in range(IMAGE_SIZE):
            if (i + j) % 2:
                img_3_1_data[i, j, ...] = 255
    img_3_1 = Image.fromarray(img_3_1_data)
    img_3_1.save('images/img_3_1.jpg', format='jpeg')

    img_3_2_data = 255 - img_3_1_data
    img_3_2 = Image.fromarray(img_3_2_data)
    img_3_2.save('images/img_3_2.jpg', format='jpeg')

    # Два изображения. Исходное (1024 на 544), и увеличенное в 1.00098 раз изображение (1025 на 544)
    s = 1.00098
    img_4_1 = Image.open('images/img_4_1.jpg', formats=['jpeg'])
    img_4_2 = img_4_1.resize((int(img_4_1.width * s), int(img_4_1.height * s)))
    img_4_2.save('images/img_4_2.jpg', format='jpeg')

    # Два изображения. Исходное (1024 на 544), и изображение (1024 на 544) цвета, как исходное в среднем
    s = 1.00098
    img_5_1 = Image.open('images/img_5_1.jpg', formats=['jpeg'])

    img_5_2_data = np.array(img_5_1)
    img_5_2_data[...] = int(img_5_2_data.mean())
    img_5_2 = Image.fromarray(img_5_2_data)
    img_5_2.save('images/img_5_2.jpg', format='jpeg')

    # Два изображения разной яркости, но одного цвета
    img_6_1_data = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
    img_6_1_data[..., 0] = 50
    img_6_1_data[..., 1] = 50
    img_6_1_data[..., 2] = 25
    img_6_1 = Image.fromarray(img_6_1_data)
    img_6_1.save('images/img_6_1.jpg', format='jpeg')

    img_6_2_data = np.zeros((IMAGE_SIZE, IMAGE_SIZE, 3), dtype=np.uint8)
    img_6_2_data[..., 0] = 100
    img_6_2_data[..., 1] = 100
    img_6_2_data[..., 2] = 50
    img_6_2 = Image.fromarray(img_6_2_data)
    img_6_2.save('images/img_6_2.jpg', format='jpeg')
