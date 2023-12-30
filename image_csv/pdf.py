from PIL import Image

img = Image.open(r'img2.jpg')
img_rgb = img.convert('RGB')
img_rgb.save('pdf/img2.pdf')