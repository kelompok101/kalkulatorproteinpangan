import streamlit as st
import time
import pandas as pd

# Fungsi untuk mengatur warna background
def set_background_color(color):
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# Fungsi utama aplikasi
def main():
    # Pemilihan warna background
    color = st.color_picker("Pilih warna untuk background:", "#FFFFFF")
    set_background_color(color)

if __name__ == "__main__":
    main()


# Fungsi untuk menghasilkan animasi teks
def animate_text():
    st.markdown('<span style="color: fuchsia; font-size: 24px; font-family: Algerian;">Hay, Selamat datang</span>', unsafe_allow_html=True)
    for i in range(1):
        st.markdown('<span style="color: red; font-size: 24px; font-family: Agency FB;">Terimakasih telah mengunjungi WebApps </span>', unsafe_allow_html=True)
        time.sleep(1)
    for i in range(1):
        st.markdown('<span style="color: navy; font-size: 24px; font-family: Agency FB;">  🧮 Kalkulator Perhitungan Kadar Protein ini 🍏🥩 </span>', unsafe_allow_html=True)
        time.sleep(1)
    for i in range(1):
        st.markdown('<span style="color: green; font-size: 24px; font-family: Agency FB;"> 👩🏼‍💻 🖥 Web Apps Kalkulator Perhitungan Kadar Protein ini dipersembahkan untuk kalian , </span>', unsafe_allow_html=True)
        time.sleep(1)
    for i in range(1):
        st.markdown('<span style="color: orange; font-size: 24px; font-family:Agency FB;">Agar membantu dalam menghitung dan memantau asupan protein harian kalian 🍽🍽 <3 <3 <3  </span>', unsafe_allow_html=True)
        time.sleep(1)
    for i in range(1):
        st.markdown('<span style="color: brown; font-size: 30px; font-family: Agency FB;">Enjoy xixixixixi, Salam dari kami Kelompok 10  </span>', unsafe_allow_html=True)
        time.sleep(3)
    st.title("")
    st.text("")
    
# Menampilkan animasi teks jika aplikasi dijalankan untuk pertama kalinya
if "animation_started" not in st.session_state:
    st.session_state["animation_started"] = True
    animate_text()
    
# Menu sidebar
selected = st.sidebar.radio("Menu",["Perkenalan Kelompok", "Informasi Mengenai WebApps", "Pengetahuan Kebutuhan Harian", "Perhitungan", "Informasi Nutrisi pada Makanan", "Rekomendasi Makanan", "Tabel Protein"])

# Opsi untuk mengubah gaya teks atau warna pada sidebar
opsi = st.sidebar.selectbox("Opsi", ["Normal", "Teks Tebal", "Warna Merah", "Warna Hijau", "Warna Biru", "Warna Pelangi"])

# Modifikasi gaya teks atau warna berdasarkan opsi yang dipilih
if opsi == "Teks Tebal":
    st.markdown("<style>h1 {font-weight: bold;}</style>", unsafe_allow_html=True)
elif opsi == "Warna Merah":
    st.markdown("<style>h1 {color: red;}</style>", unsafe_allow_html=True)
elif opsi == "Warna Hijau":
    st.markdown("<style>h1 {color: green;}</style>", unsafe_allow_html=True)
elif opsi == "Warna Biru":
    st.markdown("<style>h1 {color: blue;}</style>", unsafe_allow_html=True)
elif opsi == "Warna Pelangi":
    st.markdown("""
    <style>
    @keyframes animateRainbow {
        0% {color: red;}
        14% {color: orange;}
        28% {color: yellow;}
        42% {color: green;}
        56% {color: blue;}
        70% {color: indigo;}
        84% {color: violet;}
        100% {color: red;}
    }
    h1 {animation: animateRainbow 7s infinite;}
    </style>
    """, unsafe_allow_html=True)

# Halaman Pengetahuan
if selected == "Informasi Mengenai WebApps":
    st.title("Informasi Mengenai WebApps Kalkulator Kadar Protein 🧠🥦💪")
    st.write("Di sini pengguna dapat menemukan informasi mengenai webapps kalkulator kadar protein")
    image_path = 'protein_image.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='Protein dalam Berbagai Makanan')
    
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.write("Pembuatan web app kalkulator kadar protein dimulai dengan identifikasi kebutuhan dan tujuan aplikasi, seperti apakah itu akan digunakan untuk menghitung kadar protein dalam makanan atau untuk rencana diet. Selanjutnya, desainer antarmuka pengguna bekerja untuk membuat tata letak yang menarik dan mudah dinavigasi, sementara pengembang backend merancang algoritma untuk menghitung kadar protein berdasarkan informasi yang dimasukkan pengguna.")
    st.write("Selanjutnya, kalkulator ini dilakukan banyak pengujian untuk memastikan bahwa kalkulator memberikan hasil yang akurat. Ini seperti menguji sebuah kalkulator fisik untuk memastikan angka yang ditampilkan benar. Setelah itu, kalkulator diluncurkan secara resmi untuk digunakan oleh semua orang.Kami juga terus memperbarui kalkulator dan memperbaiki masalah jika ada. Tujuan kami adalah membuat kalkulator yang mudah digunakan dan membantu pengguna dalam menjaga asupan protein mereka. Semua ini kami lakukan agar Anda bisa menggunakan kalkulator dengan percaya diri dan mendapatkan hasil yang akurat setiap kali menggunakannya.")
    
if selected == "Pengetahuan Kebutuhan Harian":
    st.header("Pentingnya Memenuhi Kebutuhan Harian Protein dalam Berbagai Tingkatan Aktivitas")
    image_path = 'pro.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path)
    st.write("Kadar protein yang dibutuhkan tubuh sehari-hari dapat berbeda-beda tergantung pada usia, jenis kelamin, tinggi dan berat badan, serta berbagai faktor pendukung lainnya. Pedoman yang diterbitkan oleh Food and Nutrition Board of the National Academy of Sciences merekomendasikan bahwa orang dewasa membutuhkan sekitar 50 gram protein per hari yang dapat diperoleh dari makanan berprotein. Namun, kebutuhan protein dapat berbeda untuk individu yang memiliki tingkat aktivitas fisik yang lebih tinggi atau memiliki kebutuhan gizi yang lebih besar, seperti ibu hamil yang membutuhkan peningkatan asupan nutrisi selama kehamilan.")
    
    st.header("Tingkatan Aktivitas dalam Sehari-hari")
    st.write("Aktivitas fisik seseorang juga memengaruhi kebutuhan protein harian. Berikut adalah rekomendasi kebutuhan protein berdasarkan tingkat aktivitas:")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.subheader("Aktivitas Rendah:")
    image_path = 'ringan.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='Ilustrasi aktivitas rendah dalam sehari-hari')
    st.write("Orang yang memiliki aktivitas fisik rendah membutuhkan asupan protein yang lebih sedikit dari pada orang yang memiliki tingkat aktivitas fisik yang lebih tinggi.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas rendah adalah sekitar 0,8 gram protein per kilogram berat badan.")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    st.subheader("Aktivitas Sedang:")
    image_path = 'sedang.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='Ilustrasi aktivitas sedang dalam sehari-hari')
    st.write("Orang yang memiliki tingkat aktivitas fisik sedang membutuhkan lebih banyak protein dari pada orang dengan aktivitas fisik yang rendah.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas sedang adalah sekitar 1,0 - 1,2 gram protein per kilogram berat badan.")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.subheader("Aktivitas Tinggi:")
    image_path = 'berat.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='Ilustrasi aktivitas tinggi dalam sehari-hari')
    st.write("Orang yang memiliki aktivitas fisik yang tinggi, seperti atlet atau pekerja fisik, membutuhkan lebih banyak protein untuk memperbaiki dan membangun otot yang rusak selama latihan.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas tinggi adalah sekitar 1,2 - 1,5 gram protein per kilogram berat badan.")
    pass

# Halaman Pengantar
elif selected == "Perkenalan Kelompok":
    st.title("🌟 Aplikasi Perhitungan Kadar Protein 🍏🥩")
    st.write("Selamat datang di aplikasi perhitungan kadar protein dalam produk pangan!")
    st.write("Kami hadir untuk membantu Anda menghitung kadar protein dalam berbagai jenis makanan.")
    image_path = 'kerkom3 .jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path, caption='Dokumentasi Kelompok 10')
    st.write("Dibuat oleh Kelompok 10 Kelas PMIP Mata Kuliah Logika dan Pemrograman Komputer.")

    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    nama_kelompok = "Kelompok 10"
    anggota_tim = (
        "1. Adinda Rahmadani (2320501)\n"
        "2. Ajeng Maulida Aprilia (2320503)\n"
        "3. Amalia Syfa Zahra (2320505)\n"
        "4. Anjani Rahmawati (2320508)\n"
        "5. Harits Dzaki Firdani (2320527)"
    )

    st.info(f"👥 Kelompok: {nama_kelompok}")
    st.write("Anggota tim:")
    st.write(anggota_tim.replace("\n", "\n"))
    pass

# Halaman Perhitungan
elif selected == "Perhitungan":
    st.title("Perhitungan Kadar Protein dalam Produk Pangan 🥩🍳🌽")
    image_path = 'kalku.jpg'  # Ganti dengan path yang sesuai ke file gambar Anda
    st.image(image_path)
    st.write("Aplikasi ini menghitung kadar protein dalam produk pangan berdasarkan berbagai parameter.")

    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    daftar_produk = {
        "Daging": ["Daging Sapi", "Daging Ayam", "Daging Kambing", "Daging Babi", "Daging Ikan", 
                   "Daging Domba", "Daging Rusa"],
        "Susu": ["Susu Sapi", "Susu Kambing"],
        "Telur": ["Telur Ayam", "Telur Bebek", "Telur Puyuh"],
        "Kacang-kacangan": ["Kacang Merah", "Kacang Hijau", "Kacang Kedelai"],
        "Sereal": ["Oat", "Beras", "Gandum"],
        "Sayuran": ["Brokoli", "Bayam", "Kangkung"],
        "Buah-buahan": ["Pisang", "Apel", "Jeruk"],
        "Tahu": ["Tahu Putih", "Tahu Kuning"],
        "Tempe": ["Tempe Mendoan", "Tempe Goreng"],
        "Keju": ["Keju Cheddar", "Keju Mozzarella"],
        "Yoghurt": ["Yoghurt Plain", "Yoghurt Buah"],
        "Roti": ["Roti Gandum", "Roti Tawar"],
        "Kentang": ["Kentang Rebus", "Kentang Goreng"],
        "Sosis": ["Sosis Ayam", "Sosis Sapi"],
        "Biskuit": ["Biskuit Gandum", "Biskuit Cokelat"],
        "Nasi": ["Nasi Putih", "Nasi Merah"],
        "Pasta": ["Spaghetti", "Penne"]
    }

    kategori_produk = st.selectbox("Pilih kategori produk:", list(daftar_produk.keys()))

    if daftar_produk[kategori_produk]:
        produk_pilihan = st.selectbox(f"Pilih jenis {kategori_produk.lower()}: ", daftar_produk[kategori_produk])
    else:
        produk_pilihan = kategori_produk
    
    berat_produk = st.number_input(
        "Masukkan berat produk (gram):",
        min_value=0.0,
        step=0.1,
        format="%.1f"
    )

    berat_badan = st.number_input(
        "Masukkan berat badan Anda (kg):",
        min_value=0.0,
        step=0.1,
        format="%.1f"
    )

    usia = st.number_input("Masukkan usia Anda (tahun):", min_value=0, step=1, format="%d")

    kategori_aktivitas = st.selectbox("Pilih kategori aktivitas Anda:", ["Rendah", "Sedang", "Tinggi"])

    jenis_kelamin = st.radio("Pilih jenis kelamin Anda:", ["Pria", "Wanita"])

    default_protein = {
        "Daging Sapi": 26.0,
        "Daging Ayam": 25.0,
        "Daging Kambing": 27.0,
        "Daging Babi": 25.0,
        "Daging Ikan": 20.0,
        "Susu Sapi": 3.5,
        "Telur Ayam": 12.0,
        "Kacang Merah": 22.0,
        "Tempe": 19.0,
        "Roti Gandum": 8.0,
        "Kedelai": 35.0,
        "Biskuit Gandum": 6.0,
    }

    konsentrasi_protein = st.number_input(
        f"Konsentrasi protein dalam {produk_pilihan} (persentase):",
        min_value=0.0,
        max_value=100.0,
        step=0.1,
        format="%.1f",
        value=float(default_protein.get(produk_pilihan, 0))
    )

    st.write("Konsentrasi protein diukur dalam persentase dari berat total produk.")

    if st.button("Hitung Kadar Protein"):
        if berat_produk <= 0 or konsentrasi_protein < 0 or konsentrasi_protein > 100:
            st.error("Pastikan berat produk lebih dari 0 dan konsentrasi protein antara 0 dan 100.")

        kadar_protein = (berat_produk * konsentrasi_protein) / 100

        st.success(f"Kadar protein dalam {produk_pilihan} adalah {kadar_protein:.2f} gram.")

        # Hitung kebutuhan protein harian dengan batas bawah dan batas atas
        if kategori_aktivitas == "Rendah":
            kebutuhan_protein_bawah = 0.8 * berat_badan
            kebutuhan_protein_atas = 1.0 * berat_badan
        elif kategori_aktivitas == "Sedang":
            kebutuhan_protein_bawah = 1.0 * berat_badan
            kebutuhan_protein_atas = 1.2 * berat_badan
        elif kategori_aktivitas == "Tinggi":
            kebutuhan_protein_bawah = 1.2 * berat_badan
            kebutuhan_protein_atas = 1.5 * berat_badan

        st.info(f"Kebutuhan protein harian Anda berkisar antara {kebutuhan_protein_bawah:.2f} dan {kebutuhan_protein_atas:.2f} gram.")

        if kadar_protein < kebutuhan_protein_bawah:
            st.warning("Kadar protein dalam produk ini kurang dari batas bawah kebutuhan harian Anda.")
        elif kadar_protein > kebutuhan_protein_atas:
            st.warning("Kadar protein dalam produk ini melebihi batas atas kebutuhan harian Anda.")
        pass

# Halaman untuk informasi terkait nutrisi makanan
elif selected == "Informasi Nutrisi pada Makanan":
    st.title("Menu Informasi Nutrisi")
    st.markdown(
        '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
        unsafe_allow_html=True
    )
    st.write("Menu ini memberikan informasi tentang nutrisi dari berbagai jenis makanan.")
    st.write("Pilih makanan dari opsi di sebelah kiri untuk melihat informasi nutrisinya.")
    def display_nutrition_info(food_item):
        # Informasi nutrisi untuk makanan tertentu
        nutrition_info = {
            "Daging Sapi": {"Protein": 26.0, "Karbohidrat": 0.0, "Lemak": 17.0, "Kalori": 250},
            "Daging Ayam": {"Protein": 25.0, "Karbohidrat": 0.0, "Lemak": 3.6, "Kalori": 137},
            "Daging Kambing": {"Protein": 27.0, "Karbohidrat": 0.0, "Lemak": 21.0, "Kalori": 294},
            "Daging Babi": {"Protein": 25.0, "Karbohidrat": 0.0, "Lemak": 20.0, "Kalori": 271},
            "Daging Ikan": {"Protein": 20.0, "Karbohidrat": 0.0, "Lemak": 8.0, "Kalori": 165},
            "Daging Domba": {"Protein": 23.0, "Karbohidrat": 0.0, "Lemak": 18.0, "Kalori": 235},
            "Daging Rusa": {"Protein": 22.0, "Karbohidrat": 0.0, "Lemak": 2.0, "Kalori": 120},
            "Susu Sapi": {"Protein": 3.5, "Karbohidrat": 4.7, "Lemak": 3.2, "Kalori": 42},
            "Susu Kambing": {"Protein": 4.0, "Karbohidrat": 4.6, "Lemak": 3.8, "Kalori": 60},
            "Telur Ayam": {"Protein": 12.0, "Karbohidrat": 0.7, "Lemak": 9.5, "Kalori": 140},
            "Telur Bebek": {"Protein": 13.0, "Karbohidrat": 1.1, "Lemak": 10.0, "Kalori": 155},
            "Telur Puyuh": {"Protein": 11.0, "Karbohidrat": 0.6, "Lemak": 8.0, "Kalori": 115},
            "Kacang Merah": {"Protein": 22.0, "Karbohidrat": 62.0, "Lemak": 0.6, "Kalori": 333},
            "Kacang Hijau": {"Protein": 24.0, "Karbohidrat": 63.0, "Lemak": 0.8, "Kalori": 336},
            "Kacang Kedelai": {"Protein": 35.0, "Karbohidrat": 30.0, "Lemak": 17.0, "Kalori": 415},
            "Oat": {"Protein": 17.0, "Karbohidrat": 66.0, "Lemak": 7.0, "Kalori": 389},
            "Beras": {"Protein": 7.0, "Karbohidrat": 77.0, "Lemak": 0.8, "Kalori": 123},
            "Gandum": {"Protein": 13.0, "Karbohidrat": 71.0, "Lemak": 1.4, "Kalori": 329},
            "Brokoli": {"Protein": 3.7, "Karbohidrat": 7.0, "Lemak": 0.4, "Kalori": 34},
            "Bayam": {"Protein": 2.9, "Karbohidrat": 3.6, "Lemak": 0.6, "Kalori": 23},
            "Kangkung": {"Protein": 2.9, "Karbohidrat": 1.2, "Lemak": 0.2, "Kalori": 20},
            "Pisang": {"Protein": 1.3, "Karbohidrat": 27.0, "Lemak": 0.4, "Kalori": 105},
            "Apel": {"Protein": 0.3, "Karbohidrat": 14.0, "Lemak": 0.3, "Kalori": 52},
            "Jeruk": {"Protein": 0.9, "Karbohidrat": 9.0, "Lemak": 0.3, "Kalori": 43},
            "Tahu Putih": {"Protein": 19.9, "Karbohidrat": 2.4, "Lemak": 3.3, "Kalori": 121},
            "Tahu Kuning": {"Protein": 20.5, "Karbohidrat": 6.4, "Lemak": 7.4, "Kalori": 152},
            "Tempe Mendoan": {"Protein": 20.3, "Karbohidrat": 10.4, "Lemak": 16.0, "Kalori": 215},
            "Tempe Goreng": {"Protein": 19.0, "Karbohidrat": 10.1, "Lemak": 17.7, "Kalori": 198},
            "Keju Cheddar": {"Protein": 25.0, "Karbohidrat": 1.3, "Lemak": 33.1, "Kalori": 403},
            "Keju Mozzarella": {"Protein": 22.0, "Karbohidrat": 2.2, "Lemak": 22.0, "Kalori": 318},
            "Yoghurt Plain": {"Protein": 3.5, "Karbohidrat": 4.7, "Lemak": 3.0, "Kalori": 61},
            "Yoghurt Buah": {"Protein": 3.8, "Karbohidrat": 15.9, "Lemak": 0.4, "Kalori": 95},
            "Roti Gandum": {"Protein": 8.0, "Karbohidrat": 48.0, "Lemak": 1.5, "Kalori": 241},
            "Roti Tawar": {"Protein": 7.5, "Karbohidrat": 45.0, "Lemak": 1.0, "Kalori": 223},
            "Kentang Rebus": {"Protein": 2.0, "Karbohidrat": 17.5, "Lemak": 0.1, "Kalori": 82},
            "Kentang Goreng": {"Protein": 3.3, "Karbohidrat": 31.3, "Lemak": 15.4, "Kalori": 312},
            "Sosis Ayam": {"Protein": 13.0, "Karbohidrat": 1.9, "Lemak": 16.0, "Kalori": 185},
            "Sosis Sapi": {"Protein": 15.0, "Karbohidrat": 3.0, "Lemak": 22.3, "Kalori": 260},
            "Biskuit Gandum": {"Protein": 6.0, "Karbohidrat": 70.0, "Lemak": 15.0, "Kalori": 417},
            "Biskuit Cokelat": {"Protein": 4.0, "Karbohidrat": 65.0, "Lemak": 21.0, "Kalori": 450},
            "Nasi Putih": {"Protein": 2.6, "Karbohidrat": 28.0, "Lemak": 0.3, "Kalori": 130}, 
            "Nasi Merah": {"Protein": 2.9, "Karbohidrat": 28.2, "Lemak": 0.6, "Kalori": 136}, 
            "Spaghetti": {"Protein": 5.0, "Karbohidrat": 25.0, "Lemak": 1.3, "Kalori": 131}, 
            "Penne": {"Protein": 5.1, "Karbohidrat": 25.0, "Lemak": 1.2, "Kalori": 130} 
            # Tambahkan makanan lainnya di sini
        }
        if food_item in nutrition_info:
            st.write(f"Informasi Nutrisi untuk {food_item}:")
            with st.container():
                col1, col2 = st.columns([1, 1])
                with col1:
                    st.write("Nutrisi")
                    st.write("Protein")
                    st.write("Karbohidrat")
                    st.write("Lemak")
                    st.write("Kalori")
                with col2:
                    st.write("Nilai")
                    st.write(nutrition_info[food_item]["Protein"])
                    st.write(nutrition_info[food_item]["Karbohidrat"])
                    st.write(nutrition_info[food_item]["Lemak"])
                    st.write(nutrition_info[food_item]["Kalori"])
        else:
            st.write("Maaf, informasi nutrisi untuk makanan tersebut tidak tersedia.")

    # Pilihan makanan
    food_item = st.selectbox("Pilih Makanan", ["Daging Sapi","Daging Ayam","Daging Kambing","Daging Babi","Daging Ikan","Daging Domba", " Daging Rusa", "Susu Sapi", " Susu Kambing", "Telur Ayam", " Telur Bebek", "Telur Puyuh", " Kacang Merah", "Kacang Hijau", "Kacang Kedelai", " Oat", "Beras", " Gandum ", " Brokoli", "Kangkung", " Pisang", "Apel", " Jeruk", "Tahu Putih", " Tahu Kuning", "Tempe Mendoan", " Tempe Goreng", "Keju Cheddar", " Keju Mozzarella", "Yogurt Plain", " Yogurt Buah", "Roti Gandum", " Roti Tawar", "Kentang Rebus", " Kentang Goreng", "Sosis Ayam", " Sosis Sapi", "Biskuit Gandum", "Biskuit Cokelat", "Nasi Putih", " Nasi Merah", "Spaghetti", " Penne"])

    # Tombol untuk mendapatkan informasi nutrisi
    if st.button("Dapatkan Informasi Nutrisi"):
        display_nutrition_info(food_item)

# Halaman Opsi Makanan
elif selected == "Rekomendasi Makanan":
    st.title("🍽 Rekomendasi Makanan Berdasarkan Kebutuhan Protein Harian 🍗🥦🍳")

    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    
    st.write("Masukkan informasi tentang diri Anda untuk mendapatkan rekomendasi makanan berdasarkan kebutuhan protein harian Anda.")

    berat_badan = st.number_input("Masukkan berat badan Anda (kg):", min_value=0.0, step=0.1, format="%.1f")
    usia = st.number_input("Masukkan usia Anda (tahun):", min_value=0, step=1, format="%d")
    kategori_aktivitas = st.selectbox("Pilih kategori aktivitas Anda:", ["Rendah", "Sedang", "Tinggi"])
    jenis_kelamin = st.radio("Pilih jenis kelamin Anda:", ["Pria", "Wanita"])

    # Logika rekomendasi makanan berdasarkan kebutuhan protein harian pengguna
    if st.button("Dapatkan Rekomendasi"):
        if jenis_kelamin == "Pria":
            faktor = 1.0
        else:
            faktor = 0.9

        if kategori_aktivitas == "Rendah":
            faktor_aktivitas = 0.8
        elif kategori_aktivitas == "Sedang":
            faktor_aktivitas = 1.0
        else:
            faktor_aktivitas = 1.2

        kebutuhan_protein_harian = faktor * faktor_aktivitas * berat_badan

        # Menambahkan rekomendasi makanan berdasarkan kebutuhan protein harian pengguna
        rekomendasi_makanan = []
        if kebutuhan_protein_harian >= 50:
            rekomendasi_makanan.append("Daging Ayam Panggang")
            rekomendasi_makanan.append("Salad Sayuran dengan Telur Rebus")
            rekomendasi_makanan.append("Tahu Goreng dengan Sambal Kacang")
            rekomendasi_makanan.append("Kacang-kacangan Panggang")
            rekomendasi_makanan.append("Smoothie Buah dengan Yoghurt")
        elif kebutuhan_protein_harian >= 30:
            rekomendasi_makanan.append("Telur Dadar dengan Sayuran")
            rekomendasi_makanan.append("Sup Kacang Merah")
            rekomendasi_makanan.append("Roti Gandum dengan Keju")
            rekomendasi_makanan.append("Pasta dengan Saus Tomat dan Daging Cincang")
        else:
            rekomendasi_makanan.append("Bubur Oat dengan Buah-buahan")
            rekomendasi_makanan.append("Yoghurt dengan Alpukat dan Madu")
            rekomendasi_makanan.append("Sandwich Alpukat dan Telur Rebus")
            rekomendasi_makanan.append("Smoothie Bayam dengan Pisang dan Whey Protein")

        st.success(f"Kebutuhan protein harian Anda adalah {kebutuhan_protein_harian:.2f} gram.")

        st.write("Berikut adalah beberapa rekomendasi makanan yang bisa Anda pertimbangkan:")
        for makanan in rekomendasi_makanan:
            st.write(f"- {makanan}")
        pass

# Halaman Tabel Protein
elif selected == "Tabel Protein":
    st.title("🍖🥚🧀 Tabel Konsentrasi Protein Berdasarkan Produk 🥜🥛🍗")
# Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    default_protein = {
        "Daging Sapi": 26.0,
        "Daging Ayam": 25.0,
        "Daging Kambing": 27.0,
        "Daging Babi": 25.0,
        "Daging Ikan": 20.0,
        "Daging Domba": 23.0,
        "Daging Rusa": 22.0,
        "Susu Sapi": 3.5,
        "Susu Kambing": 4.0,
        "Telur Ayam": 12.0,
        "Telur Bebek": 13.0,
        "Telur Puyuh": 11.0,
        "Kacang Merah": 22.0,
        "Kacang Hijau": 24.0,
        "Kacang Kedelai": 35.0,
        "Oat": 17.0,
        "Beras": 7.0,
        "Gandum": 13.0,
        "Brokoli": 3.7,
        "Bayam": 2.9,
        "Kangkung": 2.7,
        "Pisang": 1.3,
        "Apel": 0.3,
        "Jeruk": 0.9,
        "Tahu Putih": 19.9,
        "Tahu Kuning": 20.5,
        "Tempe Mendoan": 20.3,
        "Tempe Goreng": 19.0,
        "Keju Cheddar": 25.0,
        "Keju Mozzarella": 22.0,
        "Yoghurt Plain": 3.5,
        "Yoghurt Buah": 3.8,
        "Roti Gandum": 8.0,
        "Roti Tawar": 7.5,
        "Kentang Rebus": 2.0,
        "Kentang Goreng": 3.3,
        "Sosis Ayam": 13.0,
        "Sosis Sapi": 15.0,
        "Biskuit Gandum": 6.0,
        "Biskuit Cokelat": 4.0,
        "Nasi Putih": 2.6,
        "Nasi Merah": 2.9,
        "Spaghetti": 5.0,
        "Penne": 5.1
    }

    df = pd.DataFrame({
        "Produk": list(default_protein.keys()),
        "Konsentrasi Protein (per 100 gram)": list(default_protein.values())
    })

    st.write("Berikut adalah tabel konsentrasi protein untuk beberapa produk makanan umum:")
    st.dataframe(df)
    pass
