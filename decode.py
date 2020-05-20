# dictionary
from PIL import Image
from pytesseract import pytesseract

'''
ý tưởng ở đây là : khi mà có ảnh giải mã rồi. thì sẽ convert text trong ảnh giải mã ra text thật và sử dụng
code trong file decode.py để tiến hành giải mã
'''
keys = {"0": "hi", "1": "dear", "2": "how", "3": "dog", "4": "prince", "5": "plan", "6": "to", "7": "my", "8": "are",
        "9": "you", "a": "happy", "b": "son", "c": "cat", "d": "go", "e": "hell", "f": "god", }
# thong diep da ma hoa
mess = "to hell to my to prince my plan to dog my prince my plan"
# hai file ảnh
infile1 = Image.open('out1.jpg')
infile2 = Image.open('out2.jpg')
# tạo file ảnh mới với "L"(8 bit)
outfile = Image.new('L', infile1.size)
# xếp chồng 2 ảnh với nhau để tạo ra ảnh giải mã
for x in range(infile1.size[0]):
    for y in range(infile1.size[1]):
        outfile.putpixel((x, y), max(infile1.getpixel((x, y)), infile2.getpixel((x, y))))
# sử dụng thư viện pytesseract để chuyển từ image sang text
"""
Việc sử dung pytesseract có thể chuyển ảnh nền trắng chữ đen sang text được, còn ảnh đã mã hóa thì không thành công
Do bị nhiễu quá
"""
pytesseract.pytesseract.tesseract_cmd = 'C:/Program Files/Tesseract-OCR/tesseract.exe'
# outfile.save('outfile.jpg')
# chuyển từ image to string
result = pytesseract.image_to_string(outfile)
# in ra kết quả text
print(result)
# show image ra màn hình
outfile.show()

# Xu ly doan text lấy được ra
# phan tach tung chu dua vao trong list
string_split = mess.split(" ")


# ham chuyen tu binary sang string
def decode_binary_string(s):
    return ''.join(chr(int(s[i * 8:i * 8 + 8], 2)) for i in range(len(s) // 8))


# dua ve chuoi nhi phan
list_bin = []
for i in string_split:
    for key, value in keys.items():
        if i.lower() == value:
            binary = bin(int(key, 16))[2:].zfill(4)
            list_bin.append(binary)
            all_bin = ''.join(list_bin)

# dua ve thong diep da duoc giai ma
list_word = []
for i in range(0, len(all_bin), 8):
    eight_bit = all_bin[i:i + 8]
    a = decode_binary_string(eight_bit)
    list_word.append(a)
    result = ''.join(list_word)
print(result)
