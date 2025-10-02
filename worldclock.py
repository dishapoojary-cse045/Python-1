import datetime

CITIES_OFFSETS = {
    "UTC": 0, "San Francisco": -7.0, "New York": -4.0,
    "London": 1.0, "Dubai": 4.0, "Bangalore": 5.5,
    "Singapore": 8.0, "Tokyo": 9.0, "Sydney": 10.0, "Wellington": 12.0
}

utc_now = datetime.datetime.utcnow() 
print("Time Display by Static Offsets:")

for city, offset_float in CITIES_OFFSETS.items():
    total_minutes_offset = int(offset_float * 60)
    city_time = utc_now + datetime.timedelta(minutes=total_minutes_offset)
    offset_sign = "+" if offset_float >= 0 else ""
    abs_hours = int(abs(offset_float))
    abs_minutes = int(abs(offset_float * 60) % 60)
    offset_str = f"{offset_sign}{abs_hours}:{abs_minutes:02d}"
    formatted_time = city_time.strftime("%Y-%m-%d %H:%M:%S")
    print(f"{city:<15} (UTC {offset_str:<6}): {formatted_time}")
  
