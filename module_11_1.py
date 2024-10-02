import matplotlib.pyplot as plt
import numpy as np
from PIL import Image, ImageDraw, ImageFont


## Использование numpy
# Генерация двумерной матрицы с заданным интервалом значений
matrix1 = np.arange(1, 31).reshape(6, 5)
print(matrix1, '\n')

# Генерация двумерной матрицы случайных значений
rng = np.random.default_rng()
matrix2 = rng.integers(100, size=(6, 5))
print(matrix2, '\n')

# Сложение двух матриц в итоговую
data = matrix1 + matrix2
print(data, '\n')

# Суммы итоговой матрицы по столбцам
data_sum = data.sum(axis=0)
print(data_sum)


## Использование matplotlib
# Построение графика
fig, ax = plt.subplots(figsize=(7, 5), label='График к заданию 11_1')
ax.set_title('Итоги по столбцам', fontsize=11, fontweight=600, pad=12)
categories = []
for i in range(data.shape[1]):
    i += 1
    categories.append(f'Столбец {i}')
ax.bar(categories, data_sum, color='#726eb2')
filename = 'gr_11_1.png'
fig.savefig(filename)
plt.show()

## Использование pillow
# Наложение водяного знака на сохраненное изображение
with Image.open(filename).convert('RGBA') as img:
    wm = Image.new('RGBA', img.size, (0, 0, 0, 0))
    fnt = ImageFont.load_default(200)
    d = ImageDraw.Draw(wm)
    d.text((100, 100), 'TEST', font=fnt, fill=(102, 102, 102, 128))
    new_img = Image.alpha_composite(img, wm)
    new_img.show()
