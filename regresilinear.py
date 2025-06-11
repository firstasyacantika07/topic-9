import matplotlib.pyplot as plt  # Mengimpor library matplotlib untuk membuat plot
import numpy as np  # Mengimpor library numpy untuk operasi numerik

# Soal No.1: Linear Regression
x1 = np.array([10, 20, 30, 40, 50])  # Data variabel independen (misal: jumlah pelanggan)
y1 = np.array([200, 400, 600, 800, 1000])  # Data variabel dependen (misal: pendapatan)
m1, b1 = 20, 0  # Slope (m) dan intercept (b) untuk persamaan garis y = 20x

# Soal No.2: Linear Regression
x2 = np.array([1, 2, 3, 4])  # Data variabel independen (misal: jam belajar)
y2 = np.array([60, 65, 70, 74])  # Data variabel dependen (misal: nilai)
m2, b2 = 5, 55  # Slope (m) dan intercept (b) untuk persamaan garis y = 5x + 55

# Soal No.3: Linear Regression
x3 = np.array([1, 3, 5, 7, 9])  # Data variabel independen (misal: umur kendaraan)
y3 = np.array([150, 120, 90, 60, 30])  # Data variabel dependen (misal: nilai kendaraan)
m3, b3 = -15, 165  # Slope (m) dan intercept (b) untuk persamaan garis y = -15x + 165

# Soal No.4: Linear Regression
x4 = np.array([5, 10, 15, 20])  # Data variabel independen (misal: jam kerja)
y4 = np.array([25000, 50000, 75000, 100000])  # Data variabel dependen (misal: pendapatan)
m4, b4 = 5000, 0  # Slope (m) dan intercept (b) untuk persamaan garis y = 5000x

# Soal No.5: Multiple Linear Regression Visualization (Basic 2D)
x5_1 = np.array([50, 60, 70, 80, 90])   # Feature 1: Waktu Layanan
x5_2 = np.array([2, 3, 4, 5, 6])        # Feature 2: Jumlah Komplain
y5 = np.array([400, 480, 560, 640, 720])# Target: Tingkat Kepuasan
a5, b5_1, b5_2 = -320, 8, 80  # Regression equation: Y = -320 + 8X1 + 80X2

# Membuat subplot 2x2 untuk empat soal pertama
fig, axs = plt.subplots(2, 2, figsize=(14, 10))

# Plot Soal 1: Regresi linier sederhana
axs[0, 0].scatter(x1, y1, color='blue')  # Membuat scatter plot dari data
axs[0, 0].plot(x1, m1 * x1 + b1, color='red')  # Membuat garis regresi
axs[0, 0].set_title("No.1 : Y = 20X")  # Menetapkan judul plot
axs[0, 0].set_xlabel("Pelanggan")  # Menetapkan label sumbu x
axs[0, 0].set_ylabel("Pendapatan (ribu)")  # Menetapkan label sumbu y

# Plot Soal 2: Regresi linier sederhana dengan intercept
axs[0, 1].scatter(x2, y2, color='green')  # Membuat scatter plot dari data
axs[0, 1].plot(x2, m2 * x2 + b2, color='red')  # Membuat garis regresi
axs[0, 1].set_title("No.2 : Y = 5X + 55")  # Menetapkan judul plot
axs[0, 1].set_xlabel("Jam Belajar")  # Menetapkan label sumbu x
axs[0, 1].set_ylabel("Nilai")  # Menetapkan label sumbu y

# Plot Soal 3: Regresi linier dengan slope negatif
axs[1, 0].scatter(x3, y3, color='purple')  # Membuat scatter plot dari data
axs[1, 0].plot(x3, m3 * x3 + b3, color='red')  # Membuat garis regresi
axs[1, 0].set_title("No.3 : Y = -15X + 165")  # Menetapkan judul plot
axs[1, 0].set_xlabel("Umur Kendaraan (tahun)")  # Menetapkan label sumbu x
axs[1, 0].set_ylabel("Nilai Kendaraan (juta)")  # Menetapkan label sumbu y

# Plot Soal 4: Regresi linier dengan skala besar
axs[1, 1].scatter(x4, y4, color='orange')  # Membuat scatter plot dari data
axs[1, 1].plot(x4, m4 * x4 + b4, color='red')  # Membuat garis regresi
axs[1, 1].set_title("No.4 : Y = 5000X")  # Menetapkan judul plot
axs[1, 1].set_xlabel("Jam Kerja")  # Menetapkan label sumbu x
axs[1, 1].set_ylabel("Pendapatan (rupiah)")  # Menetapkan label sumbu y

# Menampilkan semua subplot dengan tata letak yang rapi
plt.tight_layout()

# Visualisasi 2D dasar untuk Soal 5:
# Plot x5_1 (Waktu Layanan) vs y5 (Tingkat Kepuasan)
# Gunakan warna untuk merepresentasikan x5_2 (Jumlah Komplain) - fitur kedua
plt.figure(figsize=(8, 6))  # Membuat figure baru
scatter = plt.scatter(x5_1, y5, c=x5_2, cmap='winter', s=100, edgecolor='black')  # Membuat scatter plot dengan warna berdasarkan x5_2
plt.colorbar(scatter, label='X2: Jumlah Komplain')  # Menambahkan colorbar untuk interpretasi warna
plt.title("No.5 : Visualisasi Regresi Linier Berganda (2D Basic)")  # Menetapkan judul plot
plt.xlabel("X1: Waktu Layanan")  # Menetapkan label sumbu x
plt.ylabel("Tingkat Kepuasan")  # Menetapkan label sumbu y
plt.grid(True)  # Menambahkan grid ke plot

# Teks penjelasan yang dicetak ke konsol untuk pemahaman pengguna
explanation = """
Penjelasan Visualisasi No.5:
- Ini adalah visualisasi regresi linier berganda dengan dua variabel bebas (X1 dan X2).
- Sumbu X1 (Waktu Layanan) diplot pada sumbu horizontal.
- Sumbu Y (Tingkat Kepuasan) diplot pada sumbu vertikal.
- Warna titik mewakili nilai X2 (Jumlah Komplain) menggunakan skala warna.
- Dengan cara ini, kita dapat melihat bagaimana Tingkat Kepuasan dipengaruhi oleh kombinasi Waktu Layanan dan Jumlah Komplain.
- Titik dengan warna berbeda menunjukkan variasi variabel kedua (X2).
"""

print(explanation)  # Mencetak penjelasan

plt.show()  # Menampilkan semua plot