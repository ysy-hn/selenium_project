from PIL import Image
import pytesseract


image = Image.open('./data/captcha_1.png')
code = pytesseract.image_to_string(image)
print(code)