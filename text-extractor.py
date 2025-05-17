import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk, ImageDraw, ImageFont
import cv2
import numpy as np
import easyocr
import arabic_reshaper
from bidi.algorithm import get_display

# فونت فارسی (مسیر را به فونت مناسب در سیستم خود تغییر دهید)
FONT_PATH = r"C:\Users\PC\AppData\Local\Microsoft\Windows\Fonts\Vazirmatn-Regular.ttf"

reader = easyocr.Reader(['fa', 'en'])

def process_image():
    path = filedialog.askopenfilename(title="انتخاب تصویر", filetypes=[("Image files", "*.png *.jpg *.jpeg")])
    if not path:
        return

    image = cv2.imread(path)
    if image is None:
        messagebox.showerror("خطا", "❌ تصویر بارگذاری نشد.")
        return

    image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    height, width, _ = image_rgb.shape

    results = reader.readtext(image_rgb)

    # ساختن کادر جدید برای افزودن متن‌ها در کنار عکس
    padding = 350
    canvas = Image.new('RGB', (width + padding, height), (255, 255, 255))
    canvas.paste(Image.fromarray(image_rgb), (0, 0))
    draw = ImageDraw.Draw(canvas)

    try:
        font = ImageFont.truetype(FONT_PATH, 20)
    except:
        font = ImageFont.load_default()

    x_text = width + 20
    y_offset = 20
    reshaped_title = get_display(arabic_reshaper.reshape("متن‌های شناسایی‌شده:"))
    draw.text((x_text, y_offset), reshaped_title, font=font, fill=(0, 0, 0))
    y_offset += 30

    extracted_texts.clear()
    for (_, text, _) in results:
        reshaped = arabic_reshaper.reshape(text)
        bidi_text = get_display(reshaped)
        extracted_texts.append(text)
        draw.text((x_text, y_offset), bidi_text, font=font, fill=(0, 0, 0))
        y_offset += 25

    # نمایش تصویر نهایی
    final_image = ImageTk.PhotoImage(canvas.resize((800, int(canvas.height * (800 / canvas.width)))))
    image_label.config(image=final_image)
    image_label.image = final_image
    save_button.pack(pady=10)

def save_texts():
    if not extracted_texts:
        messagebox.showwarning("هشدار", "متنی برای ذخیره وجود ندارد.")
        return

    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if not filepath:
        return

    with open(filepath, "w", encoding="utf-8") as f:
        for text in extracted_texts:
            f.write(text + "\n")

    messagebox.showinfo("ذخیره شد", "✅ فایل با موفقیت ذخیره شد.")

# ---------- رابط کاربری tkinter ----------
root = tk.Tk()
root.title("تشخیص متن از تصویر")
root.geometry("850x700")

btn = tk.Button(root, text="انتخاب تصویر و شناسایی متن", font=("Vazirmatn", 14), command=process_image)
btn.pack(pady=15)

image_label = tk.Label(root)
image_label.pack()

save_button = tk.Button(root, text="📄 ذخیره متن‌ها در فایل متنی", font=("Vazirmatn", 12), command=save_texts)

extracted_texts = []

root.mainloop()