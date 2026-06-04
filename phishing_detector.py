import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix

# Load dataset
data = pd.read_csv("emails.csv")

# Features and labels
X = data["text"]
y = data["label"]

# Convert text into numerical form
vectorizer = TfidfVectorizer()
X_vectorized = vectorizer.fit_transform(X)

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X_vectorized,
    y,
    test_size=0.2,
    random_state=42
)

# Train model
model = MultinomialNB()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", round(accuracy * 100, 2), "%")

# Confusion Matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))

# Test custom email
email = input("\nEnter email text: ")

email_vector = vectorizer.transform([email])

prediction = model.predict(email_vector)

if prediction[0] == "phishing":
    print("Result: PHISHING EMAIL")
else:
    print("Result: SAFE EMAIL")
    # Test custom email
email = input("\nEnter email text: ")

# URL detection
if "http" in email or "www" in email:
    print("⚠ Warning: URL detected in email")

# Suspicious keywords
suspicious_keywords = [
    "click", "urgent", "verify", "login",
    "bank", "password", "free", "winner", "reward"
]

print("\nKeyword Analysis:")
for word in suspicious_keywords:
    if word.lower() in email.lower():
        print(f"- Suspicious keyword found: {word}")

# Prediction
email_vector = vectorizer.transform([email])
prediction = model.predict(email_vector)

print("\nFinal Result:")
if prediction[0] == "phishing":
    print("🚨 PHISHING EMAIL")
else:
    print("✅ SAFE EMAIL")