import joblib
import pandas as pd

# Load model
rf = joblib.load('../data/rf_model.joblib')

# Nhập dữ liệu mới
humidity = float(input('Nhập độ ẩm (%): '))
wind_speed = float(input('Nhập tốc độ gió (m/s): '))
dayofyear = int(input('Nhập số thứ tự ngày trong năm (1-366): '))
year = int(input('Nhập năm: '))

# Tạo dataFrame cho model
x_new = pd.DataFrame([[humidity, wind_speed, dayofyear, year]],
                     columns=['humidity', 'wind_speed', 'dayofyear', 'year'])

# Dự đoán
y_pred = rf.predict(x_new)
print(f"Nhiệt độ dự đoán: {y_pred[0]:.2f} °C")