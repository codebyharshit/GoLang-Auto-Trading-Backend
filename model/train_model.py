# model/train_model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load data
df = pd.read_csv('data/AAPL_historical_data.csv', index_col=0)
df.index = pd.to_datetime(df.index)

# Feature engineering
df['SMA_50'] = df['close'].rolling(window=50).mean()
df['SMA_200'] = df['close'].rolling(window=200).mean()
df['Signal'] = 0
df.loc[df['SMA_50'] > df['SMA_200'], 'Signal'] = 1

# Drop rows with NaN values
df = df.dropna()

# Preprocess data
X = df[['SMA_50', 'SMA_200']]
y = df['Signal']

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluate model
predictions = model.predict(X_test)
accuracy = accuracy_score(y_test, predictions)
print(f'Accuracy: {accuracy}')

# Save model
joblib.dump(model, 'model/model.pkl')
print('Model saved to model/model.pkl')
