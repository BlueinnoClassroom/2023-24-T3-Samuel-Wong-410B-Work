import pytesseract as tesc

file_path = 'number_of_cookies 1716620754.529679.png'
text: str = tesc.image_to_string(file_path)
print(f'text: {text}')

text = int(text.replace(',', ''))
print(f'new text: {text}')

number_text = int(text)
print(f'number text: {number_text}')