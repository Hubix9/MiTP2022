# This module works with PPM (P6) format with max channel value of 255 (0 -> 255)
class Image():
    def __init__(self, path: str):
        self.path = path
        f = open(path, "rb")
        code = f.readline()[:-1]
        self.width = int(f.readline()[:-1])
        self.height = int(f.readline()[:-1])
        maxValue = f.readline()[:-1]
        pixels = []
        #print(f"{code}, {width}, {height}, {maxValue}")
        for y in range(self.height):
            row = []
            for x in range(self.width):
                r = int.from_bytes(f.read(1), "little")
                g = int.from_bytes(f.read(1), "little")
                b = int.from_bytes(f.read(1), "little")
                pixel = [r, g, b]
                row.append(pixel)
            pixels.append(row)
        #print(pixels)
        self.pixels = pixels

    @property
    def dimensions(self):
        return (self.width, self.height)


if __name__ == '__main__':
    image = Image("")
