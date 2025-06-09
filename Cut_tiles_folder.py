from PIL import Image
import os


def split_image(input_path, output_folder, tile_size=512):
    """
    Разрезает изображение на тайлы заданного размера с возможным перекрытием.

    :param input_path: Путь к исходному изображению
    :param output_folder: Папка для сохранения тайлов
    :param tile_size: Размер тайла (квадратный)
    :param overlap: Перекрытие между тайлами (в пикселях)
    """

    # Открываем изображение
    img = Image.open(input_path)
    width, height = img.size

    # Итерируемся по изображению и вырезаем тайлы
    tile_num = 0
    for y in range(0, height, 480):
        for x in range(0, width, 512):
            # Определяем границы тайла
            left = x
            upper = y
            right = min(x + tile_size, width)
            lower = min(y + tile_size, height)

            # Вырезаем тайл
            tile = img.crop((left, upper, right, lower))

            # Если тайл меньше заданного размера, дополняем его
            if tile.size != (tile_size, tile_size):
                new_tile = Image.new('L', (tile_size, tile_size), 0)
                new_tile.paste(tile, (0, 0))
                tile = new_tile

            # Формируем имя файла с координатами
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            tile_name = f"{base_name}_{tile_num}.tif"
            tile_path = os.path.join(output_folder, tile_name)

            # Сохраняем тайл
            tile.save(tile_path)
            tile_num += 1

    return tile_num


def process_folder(input_folder, output_folder, tile_size=512):
    """
    Обрабатывает все .tif файлы в папке

    :param input_folder: Папка с исходными изображениями
    :param output_folder: Папка для сохранения всех тайлов
    :param tile_size: Размер тайла
    :param overlap: Перекрытие между тайлами
    """

    # Получаем список .tif файлов
    tif_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.tif') and 'topo' not in f.lower()]

    total_tiles = 0
    for file_name in tif_files:
        # Обрабатываем файл
        input_path = os.path.join(input_folder, file_name)
        tiles_count = split_image(input_path, output_folder, tile_size)

        print(f"Файл {file_name} разделен на {tiles_count} тайлов")
        total_tiles += tiles_count

    print(f"\nВсего создано {total_tiles} тайлов из {len(tif_files)} изображений")
    print(f"Все тайлы сохранены в папку: {os.path.abspath(output_folder)}")


# Пример использования
input_folder = r"C:\Users\malys\Desktop\MSU_AI\_images_CRN_Stofan2\1"  # Папка с исходными изображениями
output_folder = r"C:\Users\malys\Desktop\MSU_AI\_images_CRN_Stofan2\tyles_images_Stofan_2"  # Единая папка для всех тайлов

process_folder(input_folder, output_folder)
