from PIL import Image
import os


def split_image(input_path, output_folder, tile_size=512):
    """
    Cuts the image into tiles of the specified size with possible overlap.

    :param input_path: Path to the original image
    :param output_folder: Folder for saving tiles
    :param tile_size: Tile size (square)
    :param overlap: Overlap between tiles (in pixels)
    """

    # Opening the image
    img = Image.open(input_path)
    width, height = img.size

    # Iterate through the image and cut out tiles
    tile_num = 0
    for y in range(0, height, 480):
        for x in range(0, width, 512):
            # Defining the tile borders
            left = x
            upper = y
            right = min(x + tile_size, width)
            lower = min(y + tile_size, height)

            # Cutting out a tile
            tile = img.crop((left, upper, right, lower))

            # If the tile is smaller than the specified size, we add additional elements to it
            if tile.size != (tile_size, tile_size):
                new_tile = Image.new('L', (tile_size, tile_size), 0)
                new_tile.paste(tile, (0, 0))
                tile = new_tile

            # Forming a file name with coordinates
            base_name = os.path.splitext(os.path.basename(input_path))[0]
            tile_name = f"{base_name}_{tile_num}.tif"
            tile_path = os.path.join(output_folder, tile_name)

            # Saving the tile
            tile.save(tile_path)
            tile_num += 1

    return tile_num


def process_folder(input_folder, output_folder, tile_size=512):
    """
    Processes everything .tif files in the folder

    :param input_folder: Folder with source images
    :param output_folder: Folder for saving all tiles
    :param tile_size: Tile size
    :param overlap: Overlap between tiles
    """

    # Getting the list .tif files
    tif_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.tif') and 'topo' not in f.lower()]

    total_tiles = 0
    for file_name in tif_files:
        # Processing the file
        input_path = os.path.join(input_folder, file_name)
        tiles_count = split_image(input_path, output_folder, tile_size)

        print(f"Файл {file_name} разделен на {tiles_count} тайлов")
        total_tiles += tiles_count

    print(f"\nВсего создано {total_tiles} тайлов из {len(tif_files)} изображений")
    print(f"Все тайлы сохранены в папку: {os.path.abspath(output_folder)}")


# Usage example
input_folder = r"\path_to_the_input_folder"  # Folder with source images
output_folder = r"\path_to_the_output_folder"  # Single folder for all tiles

process_folder(input_folder, output_folder)
