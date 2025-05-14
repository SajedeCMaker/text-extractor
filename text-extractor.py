import easyocr
import cv2
from PIL import Image
import matplotlib.pyplot as plt

# مسیر تصویر را وارد کنید
image_path = 'image.jpg'

# بارگذاری تصویر با OpenCV
image = cv2.imread(image_path)
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# ساخت OCR Reader با زبان فارسی و انگلیسی
reader = easyocr.Reader(['fa', 'en'])  # زبان‌ها: فارسی و انگلیسی

# اجرای OCR روی تصویر
results = reader.readtext(image_rgb)

# نمایش تصویر و رسم کادر دور متن‌ها
for (bbox, text, prob) in results:
    (top_left, top_right, bottom_right, bottom_left) = bbox
    top_left = tuple(map(int, top_left))
    bottom_right = tuple(map(int, bottom_right))
    cv2.rectangle(image_rgb, top_left, bottom_right, (0, 255, 0), 2)
    cv2.putText(image_rgb, text, (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 0, 0), 2)

# نمایش تصویر با متن‌های شناسایی‌شده
plt.figure(figsize=(10, 10))
plt.imshow(image_rgb)
plt.axis('off')
plt.title('متن‌های شناسایی‌شده')
plt.show()

# چاپ تمام متن‌های شناسایی‌شده
print("\n📄 متن‌های استخراج‌شده:")
for (_, text, _) in results:
    print(f"- {text}")
