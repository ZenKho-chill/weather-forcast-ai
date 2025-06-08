import os
import requests
import pandas as pd
from datetime import datetime, timedelta

def fetch_weather_data(lat, lon, start_date, end_date):
    url = (
        "https://archive-api.open-meteo.com/v1/archive"
        f"?latitude={lat}&longitude={lon}"
        f"&start_date={start_date}&end_date={end_date}"
        "&hourly=temperature_2m,relative_humidity_2m,windspeed_10m"
        "&timezone=Asia%2FBangkok"
    )
    print("Đang lấy dữ liệu từ:", url)
    response = requests.get(url)
    data = response.json()
    print("Kết quả trả về từ API:", data.keys())
    if "hourly" not in data or len(data["hourly"].get("time", [])) == 0:
        print("Không có dữ liệu thời tiết trả về! Kiểm tra lại tham số hoặc API.")
        return pd.DataFrame()
    df = pd.DataFrame({
        "date": [d.split("T")[0] for d in data["hourly"]["time"]],
        "temperature": data["hourly"]["temperature_2m"],
        "humidity": data["hourly"]["relative_humidity_2m"],
        "wind_speed": data["hourly"]["windspeed_10m"]
    })
    print("Số dòng dữ liệu thô:", len(df))
    df = df.groupby("date").agg({
        "temperature": "mean",
        "humidity": "mean",
        "wind_speed": "mean"
    }).reset_index()
    print("Số dòng dữ liệu sau groupby:", len(df))
    print(df.head())
    print(df.shape)
    return df

if __name__ == "__main__":
    os.makedirs("../data", exist_ok=True)
    lat, lon = 21.0285, 105.8542  # Hà Nội
    today = datetime.today()
    start = (today - timedelta(days=365)).strftime("%Y-%m-%d")
    end = today.strftime("%Y-%m-%d")
    df = fetch_weather_data(lat, lon, start, end)
    if df.empty:
        print("Không lấy được dữ liệu. File sẽ không được lưu.")
    else:
        # Đảm bảo file không bị mở bởi chương trình khác trước khi ghi!
        df.to_csv(r"C:\Users\heruh\Downloads\Train AI\data\weather.csv", index=False)
        print("Dữ liệu đã được lưu vào data/weather.csv")