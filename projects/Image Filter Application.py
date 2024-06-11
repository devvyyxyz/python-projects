from PIL import Image, ImageOps

def apply_filter(image_path, filter_type, output_image_path):
    img = Image.open(image_path)

    if filter_type == 'grayscale':
        filtered_img = ImageOps.grayscale(img)
    elif filter_type == 'sepia':
        sepia = [(r // 2 + 100, g // 2 + 50, b // 2) for (r, g, b) in img.getdata()]
        filtered_img = Image.new('RGB', img.size)
        filtered_img.putdata(sepia)
    elif filter_type == 'invert':
        filtered_img = ImageOps.invert(img.convert('RGB'))
    else:
        print('Unknown filter type')
        return

    filtered_img.save(output_image_path)

# Example usage
apply_filter('input_image.jpg', 'grayscale', 'output_image.jpg')
