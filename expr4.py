from PIL import Image
import stepic

image = Image.open('img1.png')

encoded = stepic.encode(image, b'This is a secret message!')

encoded.save('img2.png')

encoded_image = Image.open('img2.png')

encoded_image.show()

decoded = stepic.decode(encoded_image)

print(decoded)
"""
pip install pillow
pip install stepic
"""