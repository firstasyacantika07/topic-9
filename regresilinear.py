import numpy as np  # Library untuk operasi numerik, terutama array
import matplotlib.pyplot as plt  # Library untuk membuat visualisasi data (plot, grafik)
from sklearn.linear_model import LinearRegression  # Model regresi linier dari scikit-learn

# =============================================================================
# Soal 1: Regresi Linier Sederhana
# =============================================================================
X1 = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)  # Data fitur (variabel independen), diubah menjadi matriks kolom
y1 = np.array([200, 400, 600, 800, 1000])  # Data target (variabel dependen)

model1 = LinearRegression().fit(X1, y1)  # Membuat dan melatih model regresi linier
y1_pred = model1.predict(X1)  # Memprediksi nilai target menggunakan model yang telah dilatih

# =============================================================================
# Soal 2: Regresi Linier Sederhana
# =============================================================================
X2 = np.array([1, 2, 3, 4]).reshape(-1, 1)  # Data fitur
y2 = np.array([60, 65, 70, 74])  # Data target

model2 = LinearRegression().fit(X2, y2)  # Membuat dan melatih model
y2_pred = model2.predict(X2)  # Memprediksi nilai target

# =============================================================================
# Soal 3: Regresi Linier Sederhana
# =============================================================================
X3 = np.array([1, 3, 5, 7, 9]).reshape(-1, 1)  # Data fitur
y3 = np.array([150, 120, 90, 60, 30])  # Data target

model3 = LinearRegression().fit(X3, y3)  # Membuat dan melatih model
y3_pred = model3.predict(X3)  # Memprediksi nilai target

# =============================================================================
# Soal 4: Regresi Linier Sederhana
# =============================================================================
X4 = np.array([5, 10, 15, 20]).reshape(-1, 1)  # Data fitur
y4 = np.array([25000, 50000, 75000, 100000])  # Data target

model4 = LinearRegression().fit(X4, y4)  # Membuat dan melatih model
y4_pred = model4.predict(X4)  # Memprediksi nilai target

# =============================================================================
# Soal 5: Regresi Linier Berganda
# =============================================================================
X5 = np.array([[50, 2], [60, 3], [70, 4], [80, 5], [90, 6]])  # Data fitur (dua variabel independen)
y5 = np.array([400, 480, 560, 640, 720])  # Data target

model5 = LinearRegression().fit(X5, y5)  # Membuat dan melatih model regresi linier berganda
prediksi5 = model5.predict([[75, 4]])  # Memprediksi nilai target untuk data baru [[75, 4]]

# =============================================================================
# Visualisasi Soal 1 - 4: Regresi Linier Sederhana
# =============================================================================
fig, axs = plt.subplots(2, 2, figsize=(14, 10))  # Membuat figure dan axes untuk subplot (2x2)
axs = axs.flatten()  # Mengubah array 2D axes menjadi array 1D untuk iterasi yang lebih mudah

# Daftar dataset untuk iterasi dan visualisasi
datasets = [
    (X1, y1, y1_pred, "No.1: Y = {:.2f}X + {:.2f}".format(model1.coef_[0], model1.intercept_), "Jumlah Pelanggan", "Pendapatan"),
    (X2, y2, y2_pred, "No.2: Y = {:.2f}X + {:.2f}".format(model2.coef_[0], model2.intercept_), "Jam Belajar", "Nilai"),
    (X3, y3, y3_pred, "No.3: Y = {:.2f}X + {:.2f}".format(model3.coef_[0], model3.intercept_), "Umur Kendaraan", "Harga Jual"),
    (X4, y4, y4_pred, "No.4: Y = {:.2f}X + {:.2f}".format(model4.coef_[0], model4.intercept_), "Jam Internet", "Pulsa")
]

# Iterasi melalui dataset dan membuat plot untuk setiap soal
for i, (X, y, y_pred, title, xlabel, ylabel) in enumerate(datasets):
    axs[i].scatter(X, y, color='blue', label='Data')  # Scatter plot data aktual
    axs[i].plot(X, y_pred, color='red', linewidth=2, label='Regresi Linier')  # Garis regresi
    axs[i].set_title(title, fontsize=14)  # Judul plot
    axs[i].set_xlabel(xlabel, fontsize=12)  # Label sumbu x
    axs[i].set_ylabel(ylabel, fontsize=12)  # Label sumbu y
    axs[i].grid(True)  # Menambahkan grid untuk kemudahan pembacaan
    axs[i].legend()  # Menampilkan legenda

plt.tight_layout()  # Menyesuaikan tata letak subplot agar tidak tumpang tindih

# =============================================================================
# Visualisasi Soal 5: Regresi Linier Berganda (2D)
# =============================================================================
fig2, ax5 = plt.subplots(figsize=(10, 8))  # Membuat figure dan axes untuk plot
x5_1 = X5[:, 0]  # Fitur 1 (Waktu Layanan)
x5_2 = X5[:, 1]  # Fitur 2 (Jumlah Komplain)

# Scatter plot dengan warna berdasarkan Jumlah Komplain
scatter = ax5.scatter(x5_1, y5, c=x5_2, cmap='cool', s=100, edgecolor='black', label='Data')
plt.colorbar(scatter, label='X2: Jumlah Komplain')  # Menambahkan colorbar untuk interpretasi warna

ax5.set_title("No.5: Visualisasi Regresi Linier Berganda (2D)", fontsize=14)  # Judul plot
ax5.set_xlabel("X1: Waktu Layanan", fontsize=12)  # Label sumbu x
ax5.set_ylabel("Y: Tingkat Kepuasan", fontsize=12)  # Label sumbu y
ax5.grid(True)  # Menambahkan grid
ax5.legend()  # Menampilkan legenda

# Menambahkan persamaan regresi pada plot
equation = "Y = {:.2f} + {:.2f}*X1 + {:.2f}*X2".format(model5.intercept_, model5.coef_[0], model5.coef_[1])
ax5.text(0.05, 0.95, equation, transform=ax5.transAxes, fontsize=12, verticalalignment='top', bbox=dict(facecolor='white', alpha=0.8))

plt.tight_layout()  # Menyesuaikan tata letak

# Menyimpan plot ke file gambar (opsional)
image_path = "/mnt/data/regresi_linier_ppt_style.png"
plt.savefig(image_path)

print("Plot disimpan di:", image_path)
print("Prediksi untuk [75, 4]:", prediksi5[0])

plt.show()  # Menampilkan semua plot
