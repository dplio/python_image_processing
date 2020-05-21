from PIL import Image, ImageFilter

img = Image.open('./sneakers/nike.jpeg')

# print(img, img.size, img.format, img.mode)
# print(dir(img))

filtered_img = img.filter(ImageFilter.BLUR)

filtered_img.save("./sneakers/blur.png")

smooth_img = img.filter(ImageFilter.SMOOTH)

smooth_img.save("./sneakers/smooth.png")

converted_img = img.convert("L")

converted_img.save("./sneakers/greyscale.png")

converted_img.show()
