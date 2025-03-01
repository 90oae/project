def count_words_in_file(file_name):
    try:
        with open(file_name, 'r') as file:
            text = file.read()
            words = text.split()
            count = len(words)
            return count
    except FileNotFoundError:
        print(f"الملف {file_name} غير موجود")
        return None

file_name = input("ادخل اسم الملف: ")
count = count_words_in_file(file_name)

if count is not None:
    print(f"عدد الكلمات في الملف {file_name} هو: {count}")