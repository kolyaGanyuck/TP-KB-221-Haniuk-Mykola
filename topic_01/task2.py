#   Додавання рядків:
text1 = "Hello, "
text2 = "world!"
result = text1 + text2
print(result)

#   Розділення рядка на слова:
text = "split word pala laalla all"
words = text.split()
print(words)

#   Перевірка, чи починається рядок з певного слова:
text = "Start with some word"
starts_with_word = text.startswith("Start")
print(starts_with_word)

#   Перетворення на великі літери
text = "upPer caSe"
uppercase_text = text.upper()
print(uppercase_text)

#   Перетворення на маленькі літери:
text = "SMAL cAse"
lowercase_text = text.lower()
print(lowercase_text)

#   Перевірка, чи закінчується рядок певним словом:
text = "end word"
ends_with_word = text.endswith("word")
print(ends_with_word)

#   Пошук підрядка у тексті:
text = "some word in the text"
substring = "some"
found = substring in text
print(found)

#   Визначення довжини рядка:
text = "length of the row is"
length = len(text)
print(length)

#   Вилучення пробілів з початку і кінця рядка:
text = "   strip spase   "
trimmed_text = text.strip()
print(trimmed_text)

#   Заміна тексту
text = "change word"
new_text = text.replace("change", "hello")
print(new_text)

#   Повторення рядка:
text = "repeat the row "
repeated_text = text * 3
print(repeated_text)

#   Переведення першої літери у велику:
text = "capitalize"
capitalized_text = text.capitalize()
print(capitalized_text)

#   Перетворення числа в рядок:
number = 20
text = str(number)
print(text)

#   Визначення позиції підрядка у тексті:
text = "find order in string"
substring = "order"
position = text.find(substring)
print(position)

#   Перетворення рядка у список символів:
text = "charrr"
char_list = list(text)
print(char_list)

#   Розділення рядка на підрядки за роздільником:
text = "try/split/method"
substrings = text.split("/")
print(substrings)


#   Перевірка, чи складається рядок лише з цифр:
text = "12345678"
is_digit = text.isdigit()
print(is_digit)

#   Визначення, чи є рядок числом з плаваючою точкою:
text = "20.09"
is_float = text.replace(".", "", 1).isdigit()
print(is_float)

#   Перевірка, чи складається рядок лише з пробілів:
text = "   "
text2 = " sf  "
is_whitespace = text.isspace()
is_whitespace2 = text2.isspace()
print(is_whitespace)
print(is_whitespace2)

#   Перевірка, чи починається рядок цифрою:
text = "20.09"
starts_with_digit = text[0].isdigit()
print(starts_with_digit)

#   Перевірка, чи складається рядок лише з букв:
text = "onlu alpha"
is_alpha = text.isalpha()
print(is_alpha)

#   Визначення кількості входжень підрядка в рядок:
text = "how much word in the world "
substring = "word"
count = text.count(substring)
print(count)