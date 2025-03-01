import json
import os

# функциة للقراءة من ملف JSON
def read_json(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# функциة للبحث في الملفات النصية
def search_in_files(keywords, directory):
    results = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            with open(os.path.join(directory, file), 'r') as f:
                text = f.read()
                for keyword in keywords:
                    if keyword in text:
                        results.append({
                            'file': file,
                            'text': text
                        })
    return results

# функциة للبحث في الملفات JSON
def search_in_json(keywords, directory):
    results = []
    for file in os.listdir(directory):
        if file.endswith(".json"):
            data = read_json(os.path.join(directory, file))
            for keyword in keywords:
                if keyword in data['text']:
                    results.append({
                        'file': file,
                        'text': data['text']
                    })
    return results

# اختيار الملفات للبحث فيها
directory = input("أدخل مسار الملفات: ")
keywords = input("أدخل الكلمات المفتاحية: ").split()

# البحث في الملفات النصية
results_txt = search_in_files(keywords, directory)

# البحث في الملفات JSON
results_json = search_in_json(keywords, directory)

# عرض النتائج
print("نتائج البحث:")
for result in results_txt + results_json:
    print(f"ملف: {result['file']}")
    print(f"نص: {result['text']}")
    print("---------")