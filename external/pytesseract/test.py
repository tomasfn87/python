from PIL import Image as Im
import pytesseract
# import cv2


'''img_cv = cv2.imread(r'numbers_from_1_to_60_in_6_10-element_lines.jpg')
img_rgb = cv2.cvtColor(img_cv, cv2.COLOR_BGR2RGB)
print(pytesseract.image_to_string(img_rgb))'''

def print_image_list(img_list):
    for i in range(0, len(img_list)):
        if i != 0:
            print()
        print(f'{i+1}', end='')
        print(r')', end=' ')
        print(f'{img_list[i]}')
        print(pytesseract.image_to_string(f'{img_list[i]}').strip())
        



images = [
    'test1.jpg',
    'test2_url_1.jpg',
    'test3_url_2.jpg',
    'test4_url_3.jpg',
    'test5_url_4.jpg',
    'test6_url_4.png',
    'test7_numbers_from_1_to_60_in_6_10-element_lines.jpg',
    'test8_numbers_from_1_to_60_in_6_10-element_lines_box.jpg',
    'test9_numbers_from_1_to_60_in_6_10-element_lines_v2.jpg',
    'test10_numbers_from_1_to_60_in_6_10-element_lines_v3.jpg',
    'test11_times_new_roman_phrases.jpg',
    'test12_arial_phrases.jpg'
]


# export as pdf
'''pdf = pytesseract.image_to_pdf_or_hocr('numbers_from_1_to_60_in_6_10-element_lines.jpg', extension='pdf')
with open('test.pdf', 'w+b') as f:
    f.write(pdf)'''

print_image_list(images)
# print(pytesseract.get_languages(config=''))
