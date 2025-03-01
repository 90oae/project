import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, classification_report

# Step 1: إعداد البيانات
def load_data():
    data = {
        'text': [
            "I love this product!",
            "This is the worst service I've ever had.",
            "Absolutely fantastic experience.",
            "I'm very disappointed with the quality.",
            "This is okay, but not great.",
            "The food was amazing and the service was excellent.",
            "I hate how slow this device is.",
            "Very satisfied with my purchase.",
            "Terrible experience, I want a refund.",
            "This is just what I needed!"
        ],
        'sentiment': [
            "positive", "negative", "positive", "negative", "neutral",
            "positive", "negative", "positive", "negative", "positive"
        ]
    }
    return pd.DataFrame(data)

# Step 2: تحويل النصوص إلى متجهات
def vectorize_data(df):
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(df['text'])
    y = df['sentiment']
    return X, y, vectorizer

# Step 3: تقسيم البيانات وتدريب النموذج
def train_model(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
    classifier = MultinomialNB()
    classifier.fit(X_train, y_train)
    return classifier, X_test, y_test

# Step 4: تقييم النموذج
def evaluate_model(classifier, X_test, y_test):
    y_pred = classifier.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy:.2f}\\n")
    print("Classification Report:")
    print(classification_report(y_test, y_pred))

# Step 5: تحليل المشاعر لنص جديد
def analyze_sentiment(text, classifier, vectorizer):
    text_vector = vectorizer.transform([text])
    sentiment = classifier.predict(text_vector)[0]
    return sentiment

# Main function
if __name__ == "__main__":
    df = load_data()
    X, y, vectorizer = vectorize_data(df)
    classifier, X_test, y_test = train_model(X, y)
    evaluate_model(classifier, X_test, y_test)

    # Example usage
    new_text = "The product quality is superb!"
    result = analyze_sentiment(new_text, classifier, vectorizer)
    print(f"Sentiment for '{new_text}': {result}")