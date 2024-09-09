from PIL import Image

# meningkatkan brightness image lalu hasilnya di printoutkn
def increase_brightness(image, value):
    width, height = image.size
    result = Image.new('L', (width, height)) 
    
    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            new_value = pixel + value
            result.putpixel((i, j), min(max(new_value, 0), 255))  # Batas antara 0-255
    return result

# Fungsi increase contrast
def increase_contrast(image, factor):
    width, height = image.size
    result = Image.new('L', (width, height))  # Buat gambar baru untuk hasil
    
    for i in range(width):
        for j in range(height):
            pixel = image.getpixel((i, j))
            new_value = int((pixel - 128) * factor + 128)
            result.putpixel((i, j), min(max(new_value, 0), 255))  # Batas antara 0-255
    return result

# Fungsi mencetak citra (array)
def print_image(image):
    width, height = image.size
    for j in range(height):
        row = [f"{image.getpixel((i, j)):3}" for i in range(width)]
        print(" ".join(row))

# read file dari filepath
input_image = Image.open('d:/Kuliah/Semester 7 Bismillah YaAllah/Pengolahan Citra Digital dan Visi Komputer/Tugas 1/input_image.jpeg').convert('L')  # Mengubah menjadi grayscale

# Increase kecerahan dan kontras
brightness_value = 30
contrast_factor = 1.5

bright_image = increase_brightness(input_image, brightness_value)
contrast_image = increase_contrast(bright_image, contrast_factor)

# Menyimpan result
bright_image.save('d:/Kuliah/Semester 7 Bismillah YaAllah/Pengolahan Citra Digital dan Visi Komputer/Tugas 1/bright_image.jpeg')
contrast_image.save('d:/Kuliah/Semester 7 Bismillah YaAllah/Pengolahan Citra Digital dan Visi Komputer/Tugas 1/contrast_image.jpeg')

# Menampilkan hasil perbaikan citra
print("Citra Asli:")
print_image(input_image)

print("\nCitra Setelah Peningkatan Kecerahan:")
print_image(bright_image)

print("\nCitra Setelah Peningkatan Kontras:")
print_image(contrast_image)
