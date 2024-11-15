from PIL import Image

brightness_list = " `.:-,';_~\\/\"^><i=!*r+I)(lj?t1}{vf7z|LJcx][TsYyoFa2#nuZVek3XC4A5PhESU0pbqdK69HORwG8D&gmQ%B$NWM@"

image = Image.open("nagisa.jpg").convert("RGB")

image.thumbnail((100, 100))

width, height = image.size

brightness_map = []
for y in range(height):
    row = []
    for x in range(width):
        red, green, blue = image.getpixel((x, y))
        row.append(0.2989 * red + 0.5870 * green + 0.1140 * blue)
    brightness_map.append(row)

ascii_map = []
for y in range(height):
    row = []
    for x in range(width):
        row.append(
            brightness_list[
                int(brightness_map[y][x] / 255 * (len(brightness_list) - 1))
            ]
        )
    ascii_map.append(row)

for y in range(height):
    for x in range(width):
        for i in range(3):
            print(ascii_map[y][x], end="")
    print()
