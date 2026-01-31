# задание 1


# import re

# def is_palindrome(text):
#     cleaned = re.sub(r'[^а-яa-z0-9]', '', text.lower())
#     return cleaned == cleaned[::-1]

# user_input = input("Введите строку: ")

# if is_palindrome(user_input):
#     print("Строка является палиндромом.")
# else:
#     print("Строка не является палиндромом.")




# задание 2


# def main():
#     text = input("Введите текст: ")
#     reserved_words_input = input("Введите зарезервированные слова, разделенные пробелами: ")
#     reserved_words = reserved_words_input.split()
#     for word in reserved_words:
#         text = text.replace(word, word.upper())

#     print("Измененный текст:")
#     print(text)

# if __name__ == "__main__":
#     main()



# задание 3



def count_sentences(text):
    sentences = text.split('.')
    count = 0
    
    for sentence in sentences:

        sentence = sentence.strip()
        if sentence.endswith('?') or sentence.endswith('!'):
            count += 1
        if sentence and not (sentence.endswith('?') or sentence.endswith('!')):
            count += 1

    return count

def main():
    text = input("Введите текст: ")
    sentence_count = count_sentences(text)
    print(f"Количество предложений в тексте: {sentence_count}")

if __name__ == "__main__":
    main()