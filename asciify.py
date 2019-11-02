from PIL import Image

ASCII_CHARS = ['.',',',':',';','+','*','?','%','S','#','@']
ASCII_CHARS = ASCII_CHARS[::-1]

def _resize(image, new_width):
    (old_width, old_height) = image.size
    aspect_ratio = float(old_height)/float(old_width)
    new_height = int(aspect_ratio * new_width)
    new_dim = (new_width, new_height)
    new_image = image.resize(new_dim)
    return new_image

def _modify(image, buckets):
    initial_pixels = list(image.getdata())
    new_pixels = [ASCII_CHARS[pixel_value//buckets] for pixel_value in initial_pixels]
    return ''.join(new_pixels)

def _do(image, new_width, buckets):
    image = _resize(image, new_width)
    image = image.convert("L")

    pixels = _modify(image, buckets)
    len_pixels = len(pixels)

    # Construct the image from the character list
    new_image = [pixels[index:index+new_width] for index in range(0, len_pixels, new_width)]

    return '\n'.join(new_image)

def convert(path, new_width=100, buckets=25):
    image = None
    try:
        image = Image.open(path)
    except Exception:
        raise Exception("Cannot find image from " + path)
    image = _do(image, new_width, buckets)
    return image