import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.probability import FreqDist
from nltk.stem import WordNetLemmatizer

# تحميل المكتبة
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# نص للتخزين
text = "هذا هو مثال على نص لتحليله، يتميز بوجود كلمات شائعة والتكرار في الكلمات"

# تحويل النص إلى قائمة كلمات
words = word_tokenize(text)

# إزالة الكلمات الشائعة
stop_words = set(stopwords.words('arabic'))
words = [word for word in words if word not in stop_words]

# تحويل الكلمات إلى شکلها الأساسية
lemmatizer = WordNetLemmatizer()
words = [lemmatizer.lemmatize(word) for word in words]

# حساب الترددات
freq_dist = FreqDist(words)

# عرض الترددات
print(freq_dist.most_common(10))