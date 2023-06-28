from pdf2image import convert_from_path

images = convert_from_path('D:/read_pdf.pdf')

for i, image in enumerate(images):
    image.save("D:/img/read_pdf"+str(i)+".jpg", "JPEG")

print('conversion complete')