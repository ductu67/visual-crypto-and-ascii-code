# encode
from PIL import Image, ImageFont
import random
from PIL import Image
from PIL import ImageDraw
"""
Ý tưởng ở đây. từ password của mình mã hóa thành một đoạn text dựa trên dictionary cho trước, và từ đoạn text đó
nhúng vào ảnh  rồi sau đó từ ảnh đó tạo ra 2 shares 
"""
# text cần mã hóa
names = "sarita"
# dictionary
keys = {"0": "hi", "1": "dear", "2": "how", "3": "dog", "4": "prince", "5": "plan", "6": "to", "7": "my", "8": "are",
        "9": "you", "a": "happy", "b": "son", "c": "cat", "d": "go", "e": "hell", "f": "god", }
# chuyen sang nhi phan
binary = ''.join(format(ord(name), 'b').zfill(8) for name in names)
list_all_bit = []
# chuyen sang he hex
for i in range(0, len(binary), 4):
    four_bit = binary[i:i + 4]
    decimal_bit = int(four_bit, 2)
    hex_bits = hex(decimal_bit)[2:]
    # lay ra các cặp key và value tương ứng
    for hex_bit in hex_bits:
        list_all_bit.append(keys[hex_bits])
        result = ' '.join(list_all_bit)
print(result)
# font chữ và kích thước chữ
font = ImageFont.truetype("arial.ttf", 20)
# tạo ra ảnh nền trắng và kích thước
img = Image.new("RGB", (600, 250), (255, 255, 255))
draw = ImageDraw.Draw(img)
# tạo ra text màu đen và nội dung mã hóa
draw.text((0, 0), result, (0, 0, 0), font=font)
draw = ImageDraw.Draw(img)
# chuyen sang rg 1 bit
img = img.convert('1')
img.save("test.png")
# tao ra 2 file ảnh mới "L" 8 bit
outfile1 = Image.new("L", [kichthuoc * 2 for kichthuoc in img.size])
outfile2 = Image.new("L", [kichthuoc * 2 for kichthuoc in img.size])
# create 2 shares image with xor operator
for x in range(0, img.size[0], 2):
    for y in range(0, img.size[1], 2):
        sourcepixel = img.getpixel((x, y))
        assert sourcepixel in (0, 255)
        coinflip = random.random()
        if sourcepixel == 255:
            if coinflip < .5:
                outfile1.putpixel((x * 2, y * 2), 255)
                outfile1.putpixel((x * 2 + 1, y * 2), 0)
                outfile1.putpixel((x * 2, y * 2 + 1), 0)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                outfile2.putpixel((x * 2, y * 2), 0)
                outfile2.putpixel((x * 2 + 1, y * 2), 255)
                outfile2.putpixel((x * 2, y * 2 + 1), 255)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), 0)
            else:
                outfile1.putpixel((x * 2, y * 2), 0)
                outfile1.putpixel((x * 2 + 1, y * 2), 255)
                outfile1.putpixel((x * 2, y * 2 + 1), 255)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                outfile2.putpixel((x * 2, y * 2), 255)
                outfile2.putpixel((x * 2 + 1, y * 2), 0)
                outfile2.putpixel((x * 2, y * 2 + 1), 0)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), 255)
        elif sourcepixel == 0:
            if coinflip < .5:
                outfile1.putpixel((x * 2, y * 2), 255)
                outfile1.putpixel((x * 2 + 1, y * 2), 0)
                outfile1.putpixel((x * 2, y * 2 + 1), 0)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), 255)

                outfile2.putpixel((x * 2, y * 2), 255)
                outfile2.putpixel((x * 2 + 1, y * 2), 0)
                outfile2.putpixel((x * 2, y * 2 + 1), 0)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), 255)
            else:
                outfile1.putpixel((x * 2, y * 2), 0)
                outfile1.putpixel((x * 2 + 1, y * 2), 255)
                outfile1.putpixel((x * 2, y * 2 + 1), 255)
                outfile1.putpixel((x * 2 + 1, y * 2 + 1), 0)

                outfile2.putpixel((x * 2, y * 2), 0)
                outfile2.putpixel((x * 2 + 1, y * 2), 255)
                outfile2.putpixel((x * 2, y * 2 + 1), 255)
                outfile2.putpixel((x * 2 + 1, y * 2 + 1), 0)

# save 2 shares image
outfile1.save('out1.jpg')
outfile2.save('out2.jpg')
