import os
import pandas as pd

# Đảm bảo thư mục data tồn tại
os.makedirs("../data", exist_ok=True)

# Đọc file weather.csv
df = pd.read_csv('../data/weather.csv')

df = df.dropna()
df['date'] = pd.to_datetime(df['date'])
df['dayofyear'] = df['date'].dt.dayofyear
df['year'] = df['date'].dt.year

# Ghi file vào đúng vị trí dự án (gốc Train AI/data)
output_path = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data/weather_processed.csv'))
print("Đang ghi file vào:", output_path)
df.to_csv(output_path, index=False)
print("Đã lưu weather_processed.csv, shape:", df.shape)
print(df.head())