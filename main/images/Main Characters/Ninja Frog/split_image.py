from PIL import Image

def split_tileset(image_path, tile_width, tile_height, output_folder):
    img = Image.open(image_path)
    name = image_path.replace(".png", "")
    width, height = img.size
    i = 0
    for y in range(0, height, tile_height):
        for x in range(0, width, tile_width):
            tile = img.crop((x, y, x + tile_width, y + tile_height))
            tile.save(f"{output_folder}/{name}_{i}.png")
            i = i + 1

split_tileset("Wall Jump.png", 32, 32, "Wall_jump")