import streamlit as st
import pandas as pd

# Menu sidebar
selected = st.sidebar.radio("Menu",["Perkenalan Kelompok", "Pengetahuan", "Perhitungan", "Rekomendasi Makanan", "Tabel Protein"])

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
if selected == "Pengetahuan":
    st.title("Pengetahuan Tentang Kadar Protein 🧠🥦💪")
    st.write("Di sini Anda dapat menemukan informasi tentang kadar protein dan pentingnya asupan protein dalam makanan.")

    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    st.header("Pentingnya Kadar Protein dalam Berbagai Tingkat Aktivitas")

    st.write("Kadar protein yang dibutuhkan tubuh sehari-hari dapat berbeda-beda tergantung pada usia, jenis kelamin, tinggi dan berat badan, serta berbagai faktor pendukung lainnya. Pedoman yang diterbitkan oleh Food and Nutrition Board of the National Academy of Sciences merekomendasikan bahwa orang dewasa membutuhkan sekitar 50 gram protein per hari yang dapat diperoleh dari makanan berprotein. Namun, kebutuhan protein dapat berbeda untuk individu yang memiliki tingkat aktivitas fisik yang lebih tinggi atau memiliki kebutuhan gizi yang lebih besar, seperti ibu hamil yang membutuhkan peningkatan asupan nutrisi selama kehamilan.")

    st.write("Kalkulator kadar protein kami dapat membantu Anda menghitung kadar protein dalam berbagai produk pangan dan membandingkannya dengan kebutuhan harian Anda.")
    st.header("Kadar Protein dan Tingkat Aktivitas")
    st.write("Aktivitas fisik seseorang juga memengaruhi kebutuhan protein harian. Berikut adalah rekomendasi kebutuhan protein berdasarkan tingkat aktivitas:")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.subheader("Aktivitas Rendah:")
    st.write("Orang yang memiliki aktivitas fisik rendah membutuhkan asupan protein yang lebih sedikit dari pada orang yang memiliki tingkat aktivitas fisik yang lebih tinggi.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas rendah adalah sekitar 0,8 gram protein per kilogram berat badan.")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)

    st.subheader("Aktivitas Sedang:")
    st.write("Orang yang memiliki tingkat aktivitas fisik sedang membutuhkan lebih banyak protein dari pada orang dengan aktivitas fisik yang rendah.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas sedang adalah sekitar 1,0 - 1,2 gram protein per kilogram berat badan.")
    # Garis pembatas berwarna-warni
    st.markdown(
    '<hr style="border: none; height: 5px; background: linear-gradient(to right, red, orange, yellow, green, blue, indigo, violet);"/>',
    unsafe_allow_html=True
)
    st.subheader("Aktivitas Tinggi:")
    st.write("Orang yang memiliki aktivitas fisik yang tinggi, seperti atlet atau pekerja fisik, membutuhkan lebih banyak protein untuk memperbaiki dan membangun otot yang rusak selama latihan.")
    st.write("Kebutuhan protein harian untuk orang dengan aktivitas tinggi adalah sekitar 1,2 - 1,5 gram protein per kilogram berat badan.")

# Halaman Pengantar
elif selected == "Perkenalan Kelompok":
    st.title("🌟 Aplikasi Perhitungan Kadar Protein 🍏🥩")
    st.write("Selamat datang di aplikasi perhitungan kadar protein dalam produk pangan!")
    st.write("Kami hadir untuk membantu Anda menghitung kadar protein dalam berbagai jenis makanan.")
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

# Halaman Perhitungan
elif selected == "Perhitungan":
    st.title("Perhitungan Kadar Protein dalam Produk Pangan 🥩🍳🌽")
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

# Halaman Opsi Makanan
elif selected == "Rekomendasi Makanan":
    st.title("🍽 Rekomendasi Makanan Berdasarkan Kebutuhan Protein Harian 🍗🥦🍳")

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
