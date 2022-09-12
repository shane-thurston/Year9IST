import qrcode

data = "Hello! Welcome to the world of programming"
link = "www.stannies.com"

img = qrcode.make(data)
print(type(img))
img_link = qrcode.make(link)

img.save("test1.jpg")
img_link.save("link.jpg")
