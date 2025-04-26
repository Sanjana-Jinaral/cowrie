import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import classification_report

# Load the dataset
df = pd.read_csv("cowrie_login_events.csv")

# Label the event: 1 for failed login, 0 for success
df['label'] = df['event'].apply(lambda x: 1 if x == "cowrie.login.failed" else 0)

# Encode the username
le = LabelEncoder()
df['user_encoded'] = le.fit_transform(df['username'].astype(str))

# Feature and label
X = df[['user_encoded']]
y = df['label']

# 🔒 Check if there's enough data
if len(df) < 2:
    print("[-] Not enough login events to train the model. Try more fake SSH attempts.")
    exit()

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Train and evaluate model
model = RandomForestClassifier()
model.fit(X_train, y_train)

preds = model.predict(X_test)
print(classification_report(y_test, preds))


