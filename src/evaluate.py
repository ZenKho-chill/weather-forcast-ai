import pandas as pd
import joblib
from sklearn.metrics import mean_absolute_error, mean_squared_error
import matplotlib.pyplot as plt
import numpy as np

# Load model và data test
rf = joblib.load('data/rf_model.joblib')
X_test = pd.read_csv('data/X_test.csv')
y_test = pd.read_csv('data/y_test.csv').squeeze()

y_pred = rf.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f'MAE: {mae:.2f}')
print(f'RMSE: {rmse:.2f}')

# Vẽ biểu đồ so sánh thực tế và dự đoán
plt.figure(figsize=(10,4))
plt.plot(y_test.values, label='Thực tế')
plt.plot(y_pred, label='Dự đoán')
plt.legend()
plt.title('So sánh nhiệt độ thực tế và dự đoán')
plt.xlabel('Sample')
plt.ylabel('Temperature')
plt.tight_layout()
plt.show()