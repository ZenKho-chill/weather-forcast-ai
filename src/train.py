import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import joblib

# Đảm bảo thư mục data tồn tại
os.makedirs("data", exist_ok=True)

# Đọc dữ liệu đã tiền xử lý
df = pd.read_csv('data/weather_processed.csv')

# Chọn feature và target
features = ['humidity', 'wind_speed', 'dayofyear', 'year']
X = df[features]
y = df['temperature']

# Chia train/test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train Random Forest
rf = RandomForestRegressor(n_estimators=100, random_state=42)
rf.fit(X_train, y_train)

# Lưu model và dữ liệu test
joblib.dump(rf, 'data/rf_model.joblib')
X_test.to_csv('data/X_test.csv', index=False)
y_test.to_csv('data/y_test.csv', index=False)

print("Đã train xong mô hình và lưu tại data/rf_model.joblib")