
import streamlit as st
import json
import os
from datetime import date

# ==========================================
# KONFIGURASI
# ==========================================

st.set_page_config(
    page_title="Mountain Adventure",
    page_icon="⛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

FILE_DATA = "pendaftaran.json"

# ==========================================
# DATA GUNUNG INDONESIA
# ==========================================

GUNUNG = {
    "Gunung Lawu": {
        "provinsi": "Jawa Timur / Jawa Tengah",
        "wilayah": "Perbatasan Magetan, Karanganyar",
        "deskripsi": "Gunung Lawu dikenal dengan suasana alamnya yang sejuk, kawasan hutan, serta panorama pegunungan yang indah.",
        "daya_tarik": "Pemandangan alam, hutan pegunungan, dan kawasan budaya di sekitar Lawu.",
        "kategori": "Pegunungan"
    },
    "Gunung Semeru": {
        "provinsi": "Jawa Timur",
        "wilayah": "Kabupaten Lumajang dan Malang",
        "deskripsi": "Semeru merupakan gunung tertinggi di Pulau Jawa dan bagian dari kawasan Taman Nasional Bromo Tengger Semeru.",
        "daya_tarik": "Lanskap pegunungan, kawasan hutan, dan panorama alam.",
        "kategori": "Gunung api"
    },
    "Gunung Bromo": {
        "provinsi": "Jawa Timur",
        "wilayah": "Probolinggo, Pasuruan, Lumajang, Malang",
        "deskripsi": "Bromo terkenal dengan lautan pasir, kaldera luas, dan pemandangan matahari terbit.",
        "daya_tarik": "Lautan pasir, kawah, dan panorama matahari terbit.",
        "kategori": "Gunung api"
    },
    "Gunung Arjuno": {
        "provinsi": "Jawa Timur",
        "wilayah": "Malang, Pasuruan, Batu",
        "deskripsi": "Gunung Arjuno merupakan bagian dari kompleks pegunungan Arjuno-Welirang dengan kawasan hutan yang luas.",
        "daya_tarik": "Hutan pegunungan dan pemandangan alam.",
        "kategori": "Pegunungan"
    },
    "Gunung Welirang": {
        "provinsi": "Jawa Timur",
        "wilayah": "Pasuruan dan Mojokerto",
        "deskripsi": "Welirang merupakan gunung api yang berada dalam satu kompleks dengan Gunung Arjuno.",
        "daya_tarik": "Lanskap pegunungan dan kawasan vulkanik.",
        "kategori": "Gunung api"
    },
    "Gunung Ijen": {
        "provinsi": "Jawa Timur",
        "wilayah": "Banyuwangi dan Bondowoso",
        "deskripsi": "Ijen dikenal dengan kawah asam berwarna hijau kebiruan dan fenomena api biru yang dapat terlihat dalam kondisi tertentu.",
        "daya_tarik": "Kawah Ijen dan fenomena api biru.",
        "kategori": "Gunung api"
    },
    "Gunung Raung": {
        "provinsi": "Jawa Timur",
        "wilayah": "Banyuwangi, Bondowoso, Jember",
        "deskripsi": "Raung dikenal memiliki kaldera besar dan karakter bentang alam vulkanik yang khas.",
        "daya_tarik": "Kaldera dan panorama pegunungan.",
        "kategori": "Gunung api"
    },
    "Gunung Argopuro": {
        "provinsi": "Jawa Timur",
        "wilayah": "Probolinggo, Situbondo, Jember",
        "deskripsi": "Argopuro dikenal memiliki kawasan hutan yang luas serta peninggalan sejarah di sekitar jalurnya.",
        "daya_tarik": "Hutan, padang savana, dan situs bersejarah.",
        "kategori": "Pegunungan"
    },
    "Gunung Penanggungan": {
        "provinsi": "Jawa Timur",
        "wilayah": "Mojokerto dan Pasuruan",
        "deskripsi": "Penanggungan memiliki banyak situs peninggalan sejarah dan budaya di kawasan lerengnya.",
        "daya_tarik": "Pemandangan alam dan situs sejarah.",
        "kategori": "Pegunungan"
    },
    "Gunung Kelud": {
        "provinsi": "Jawa Timur",
        "wilayah": "Kediri, Blitar, Malang",
        "deskripsi": "Kelud merupakan gunung api yang terkenal dengan sejarah aktivitas vulkaniknya.",
        "daya_tarik": "Bentang alam vulkanik dan kawasan wisata sekitar.",
        "kategori": "Gunung api"
    },
    "Gunung Merapi": {
        "provinsi": "Jawa Tengah / DIY",
        "wilayah": "Yogyakarta dan Jawa Tengah",
        "deskripsi": "Merapi merupakan salah satu gunung api paling aktif di Indonesia dan memiliki kawasan konservasi.",
        "daya_tarik": "Lanskap vulkanik dan pemandangan pegunungan.",
        "kategori": "Gunung api"
    },
    "Gunung Merbabu": {
        "provinsi": "Jawa Tengah",
        "wilayah": "Magelang, Boyolali, Semarang",
        "deskripsi": "Merbabu terkenal dengan padang sabana dan panorama pegunungan di sekitarnya.",
        "daya_tarik": "Sabana dan pemandangan gunung-gunung Jawa.",
        "kategori": "Pegunungan"
    },
    "Gunung Sindoro": {
        "provinsi": "Jawa Tengah",
        "wilayah": "Temanggung dan Wonosobo",
        "deskripsi": "Sindoro merupakan gunung api yang berdekatan dengan Gunung Sumbing.",
        "daya_tarik": "Panorama alam dan perkebunan di lereng gunung.",
        "kategori": "Gunung api"
    },
    "Gunung Sumbing": {
        "provinsi": "Jawa Tengah",
        "wilayah": "Magelang, Temanggung, Wonosobo",
        "deskripsi": "Sumbing memiliki pemandangan alam yang luas dan merupakan salah satu gunung besar di Jawa Tengah.",
        "daya_tarik": "Lanskap pegunungan dan panorama alam.",
        "kategori": "Gunung api"
    },
    "Gunung Slamet": {
        "provinsi": "Jawa Tengah",
        "wilayah": "Banyumas, Purbalingga, Tegal",
        "deskripsi": "Slamet merupakan gunung tertinggi di Jawa Tengah dan memiliki kawasan hutan pegunungan.",
        "daya_tarik": "Hutan pegunungan dan panorama alam.",
        "kategori": "Gunung api"
    },
    "Gunung Prau": {
        "provinsi": "Jawa Tengah",
        "wilayah": "Dieng, Wonosobo",
        "deskripsi": "Prau terkenal dengan pemandangan matahari terbit dan hamparan perbukitan.",
        "daya_tarik": "Padang rumput dan panorama pegunungan.",
        "kategori": "Pegunungan"
    },
    "Gunung Ungaran": {
        "provinsi": "Jawa Tengah",
        "wilayah": "Kabupaten Semarang",
        "deskripsi": "Ungaran merupakan kawasan pegunungan yang memiliki hutan dan sejumlah tempat wisata alam.",
        "daya_tarik": "Hutan dan pemandangan alam.",
        "kategori": "Pegunungan"
    },
    "Gunung Ciremai": {
        "provinsi": "Jawa Barat",
        "wilayah": "Kuningan dan Majalengka",
        "deskripsi": "Ciremai merupakan gunung tertinggi di Jawa Barat dan berada dalam kawasan taman nasional.",
        "daya_tarik": "Hutan konservasi dan panorama alam.",
        "kategori": "Gunung api"
    },
    "Gunung Gede": {
        "provinsi": "Jawa Barat",
        "wilayah": "Bogor, Cianjur, Sukabumi",
        "deskripsi": "Gede merupakan bagian dari Taman Nasional Gunung Gede Pangrango yang memiliki keanekaragaman hayati.",
        "daya_tarik": "Hutan hujan, air terjun, dan kawasan konservasi.",
        "kategori": "Gunung api"
    },
    "Gunung Pangrango": {
        "provinsi": "Jawa Barat",
        "wilayah": "Bogor, Cianjur, Sukabumi",
        "deskripsi": "Pangrango berada dalam kawasan taman nasional yang sama dengan Gunung Gede.",
        "daya_tarik": "Hutan pegunungan dan padang edelweiss.",
        "kategori": "Pegunungan"
    },
    "Gunung Papandayan": {
        "provinsi": "Jawa Barat",
        "wilayah": "Garut",
        "deskripsi": "Papandayan terkenal dengan kawasan kawah, hutan mati, dan padang edelweiss.",
        "daya_tarik": "Kawah, hutan mati, dan padang edelweiss.",
        "kategori": "Gunung api"
    },
    "Gunung Tangkuban Perahu": {
        "provinsi": "Jawa Barat",
        "wilayah": "Bandung Barat dan Subang",
        "deskripsi": "Tangkuban Perahu terkenal dengan bentuk kawahnya yang khas dan kawasan wisata alam.",
        "daya_tarik": "Kawah dan panorama alam.",
        "kategori": "Gunung api"
    },
    "Gunung Rinjani": {
        "provinsi": "Nusa Tenggara Barat",
        "wilayah": "Pulau Lombok",
        "deskripsi": "Rinjani merupakan gunung tertinggi kedua di Indonesia dan terkenal dengan Danau Segara Anak.",
        "daya_tarik": "Danau Segara Anak dan panorama kaldera.",
        "kategori": "Gunung api"
    },
    "Gunung Tambora": {
        "provinsi": "Nusa Tenggara Barat",
        "wilayah": "Pulau Sumbawa",
        "deskripsi": "Tambora terkenal karena letusan besar pada tahun 1815 dan memiliki kaldera yang sangat luas.",
        "daya_tarik": "Kaldera dan sejarah geologi.",
        "kategori": "Gunung api"
    },
    "Gunung Agung": {
        "provinsi": "Bali",
        "wilayah": "Kabupaten Karangasem",
        "deskripsi": "Agung merupakan gunung tertinggi di Bali dan memiliki nilai budaya serta spiritual bagi masyarakat setempat.",
        "daya_tarik": "Panorama Bali dan kawasan budaya.",
        "kategori": "Gunung api"
    },
    "Gunung Batur": {
        "provinsi": "Bali",
        "wilayah": "Kintamani, Bangli",
        "deskripsi": "Batur dikenal dengan kaldera luas dan Danau Batur yang berada di kawasan Kintamani.",
        "daya_tarik": "Kaldera dan Danau Batur.",
        "kategori": "Gunung api"
    },
    "Gunung Kerinci": {
        "provinsi": "Jambi / Sumatera Barat",
        "wilayah": "Kawasan Taman Nasional Kerinci Seblat",
        "deskripsi": "Kerinci merupakan gunung api tertinggi di Indonesia dan berada di kawasan hutan konservasi.",
        "daya_tarik": "Hutan tropis dan panorama pegunungan.",
        "kategori": "Gunung api"
    },
    "Gunung Marapi": {
        "provinsi": "Sumatera Barat",
        "wilayah": "Kabupaten Agam dan Tanah Datar",
        "deskripsi": "Marapi merupakan gunung api aktif di Sumatera Barat.",
        "daya_tarik": "Lanskap pegunungan dan kawasan vulkanik.",
        "kategori": "Gunung api"
    },
    "Gunung Singgalang": {
        "provinsi": "Sumatera Barat",
        "wilayah": "Agam dan Padang Pariaman",
        "deskripsi": "Singgalang dikenal dengan kawasan hutan pegunungan dan Telaga Dewi.",
        "daya_tarik": "Hutan dan telaga pegunungan.",
        "kategori": "Pegunungan"
    },
    "Gunung Dempo": {
        "provinsi": "Sumatera Selatan",
        "wilayah": "Kota Pagar Alam",
        "deskripsi": "Dempo merupakan gunung tertinggi di Sumatera Selatan dan berada di kawasan perkebunan teh.",
        "daya_tarik": "Perkebunan teh dan panorama alam.",
        "kategori": "Gunung api"
    },
    "Gunung Sibayak": {
        "provinsi": "Sumatera Utara",
        "wilayah": "Kabupaten Karo",
        "deskripsi": "Sibayak merupakan gunung api yang terkenal di kawasan wisata Berastagi.",
        "daya_tarik": "Kawah dan pemandangan dataran tinggi Karo.",
        "kategori": "Gunung api"
    },
    "Gunung Leuser": {
        "provinsi": "Aceh / Sumatera Utara",
        "wilayah": "Kawasan Taman Nasional Gunung Leuser",
        "deskripsi": "Leuser merupakan kawasan pegunungan luas yang menjadi habitat berbagai satwa dan tumbuhan langka.",
        "daya_tarik": "Hutan hujan tropis dan keanekaragaman hayati.",
        "kategori": "Pegunungan"
    },
    "Puncak Jaya": {
        "provinsi": "Papua",
        "wilayah": "Pegunungan Sudirman",
        "deskripsi": "Puncak Jaya merupakan puncak tertinggi di Indonesia dan memiliki lingkungan pegunungan yang sangat khusus.",
        "daya_tarik": "Pemandangan pegunungan tinggi dan formasi es.",
        "kategori": "Pegunungan tinggi"
    }
}

# ==========================================
# PENYIMPANAN DATA
# ==========================================

def baca_data():
    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, "r", encoding="utf-8") as file:
                return json.load(file)
        except (json.JSONDecodeError, OSError):
            return []
    return []

def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

if "data" not in st.session_state:
    st.session_state.data = baca_data()

if "hasil" not in st.session_state:
    st.session_state.hasil = None

# ==========================================
# DESAIN
# ==========================================

st.markdown("""
<style>
.stApp {
    background-color: #F3F7F2;
}

section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #103D2C, #216044);
}

section[data-testid="stSidebar"] * {
    color: white !important;
}

.hero {
    background: linear-gradient(120deg, #103D2C, #3D8058);
    padding: 45px 35px;
    border-radius: 20px;
    color: white;
    margin-bottom: 25px;
}

.hero h1 {
    font-size: 43px;
    font-weight: 800;
}

.hero p {
    font-size: 18px;
    color: #E2F0E4;
}

.kartu {
    background: white;
    padding: 22px;
    border-radius: 15px;
    border: 1px solid #DDE9DD;
    margin-bottom: 15px;
}

.kartu h3 {
    color: #174B35;
}

.info {
    background: #E4F0E5;
    padding: 18px;
    border-radius: 12px;
    color: #174B35;
}

.stButton button {
    border-radius: 10px;
    font-weight: bold;
}

footer {
    text-align: center;
    color: #718075;
    padding: 25px;
}
</style>
""", unsafe_allow_html=True)

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.markdown("# ⛰️ MOUNTAIN")
st.sidebar.markdown("## ADVENTURE")
st.sidebar.caption("EXPLORE THE BEAUTY OF INDONESIA")
st.sidebar.divider()

halaman = st.sidebar.radio(
    "NAVIGASI",
    [
        "Beranda",
        "Jelajah Gunung",
        "Pendaftaran",
        "Hasil Registrasi",
        "Riwayat"
    ]
)

st.sidebar.divider()
st.sidebar.write("🌿 Jelajahi alam dengan bijak.")
st.sidebar.caption("Mountain Adventure © 2026")

# ==========================================
# BERANDA
# ==========================================

if halaman == "Beranda":

    st.markdown("""
    <div class="hero">
        <h1>⛰️ MOUNTAIN ADVENTURE</h1>
        <h2>Discover The Beauty of Indonesia</h2>
        <p>
        Temukan keindahan pegunungan Indonesia
        melalui satu platform informasi dan pendaftaran.
        </p>
    </div>
    """, unsafe_allow_html=True)

    st.title("Selamat Datang, Petualang!")

    st.write("""
    Mountain Adventure adalah platform informasi gunung
    dan pendaftaran pendakian. Temukan informasi mengenai
    berbagai gunung di Indonesia sebelum merencanakan perjalanan.
    """)

    col1, col2, col3 = st.columns(3)

    col1.metric("Daftar Gunung", len(GUNUNG))
    col2.metric("Total Pendaftaran", len(st.session_state.data))
    col3.metric("Wilayah", "Indonesia")

    st.divider()
    st.subheader("🌄 Gunung Pilihan")

    pilihan = [
        "Gunung Lawu",
        "Gunung Bromo",
        "Gunung Rinjani"
    ]

    c1, c2, c3 = st.columns(3)

    for kolom, nama in zip([c1, c2, c3], pilihan):
        with kolom:
            info = GUNUNG[nama]
            st.markdown(
                f"""
                <div class="kartu">
                    <h3>⛰️ {nama}</h3>
                    <p><b>Lokasi:</b> {info['provinsi']}</p>
                    <p>{info['deskripsi']}</p>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("""
    <div class="info">
        <b>⚠️ Utamakan keselamatan!</b><br>
        Periksa status gunung, cuaca, aturan pengelola,
        izin pendakian, dan kondisi kesehatan sebelum bepergian.
        Jangan memasuki jalur yang ditutup atau zona berbahaya.
    </div>
    """, unsafe_allow_html=True)

# ==========================================
# JELAJAH GUNUNG
# ==========================================

elif halaman == "Jelajah Gunung":

    st.title("🌄 Jelajah Gunung Indonesia")
    st.write("Temukan informasi berbagai gunung di Indonesia.")

    daftar_provinsi = sorted(set(
        info["provinsi"] for info in GUNUNG.values()
    ))

    filter_daerah = st.selectbox(
        "Filter berdasarkan wilayah",
        ["Semua Wilayah"] + daftar_provinsi
    )

    pencarian = st.text_input(
        "🔎 Cari nama gunung",
        placeholder="Contoh: Lawu, Rinjani, Bromo..."
    )

    daftar_tampil = []

    for nama, info in GUNUNG.items():

        cocok_daerah = (
            filter_daerah == "Semua Wilayah"
            or filter_daerah == info["provinsi"]
        )

        cocok_nama = pencarian.lower() in nama.lower()

        if cocok_daerah and cocok_nama:
            daftar_tampil.append((nama, info))

    st.write(f"Menampilkan {len(daftar_tampil)} gunung")

    if daftar_tampil:

        for mulai in range(0, len(daftar_tampil), 2):

            kolom = st.columns(2)

            for i, (nama, info) in enumerate(
                daftar_tampil[mulai:mulai + 2]
            ):

                with kolom[i]:

                    with st.container(border=True):

                        st.subheader("⛰️ " + nama)
                        st.caption(info["provinsi"])

                        st.write(info["deskripsi"])

                        st.write(
                            "**Daya tarik:**",
                            info["daya_tarik"]
                        )

                        with st.expander("Lihat informasi lengkap"):

                            st.write("**Lokasi:**", info["wilayah"])
                            st.write("**Kategori:**", info["kategori"])
                            st.write("**Provinsi:**", info["provinsi"])

                            st.info(
                                "Informasi ini merupakan pengenalan umum. "
                                "Status jalur dan izin harus diperiksa "
                                "langsung melalui pengelola resmi."
                            )

    else:
        st.warning("Gunung tidak ditemukan.")

# ==========================================
# PENDAFTARAN
# ==========================================

elif halaman == "Pendaftaran":

    st.title("📝 Pendaftaran Pendakian")
    st.write("Isi formulir berikut dengan data yang benar.")

    with st.form("form_pendaftaran"):

        st.subheader("A. Identitas Pendaki")

        nama = st.text_input("Nama lengkap")
        umur = st.number_input(
            "Umur",
            min_value=13,
            max_value=100,
            value=18
        )

        alamat = st.text_area("Alamat")
        hp = st.text_input("Nomor HP")

        st.divider()
        st.subheader("B. Informasi Pendakian")

        gunung = st.selectbox(
            "Pilih gunung",
            list(GUNUNG.keys())
        )

        tanggal = st.date_input(
            "Tanggal pendakian",
            min_value=date.today()
        )

        jumlah = st.number_input(
            "Jumlah pendaki",
            min_value=1,
            max_value=50,
            value=1
        )

        darurat = st.text_input("Nomor kontak darurat")

        persetujuan_wali = False

        if umur < 18:
            persetujuan_wali = st.checkbox(
                "Saya akan melakukan pendakian dengan persetujuan "
                "dan pendampingan orang tua/wali sesuai aturan pengelola."
            )

        setuju = st.checkbox(
            "Saya memastikan data yang dimasukkan benar."
        )

        kirim = st.form_submit_button(
            "KIRIM PENDAFTARAN",
            use_container_width=True
        )

    if kirim:

        if not all([
            nama.strip(),
            alamat.strip(),
            hp.strip(),
            darurat.strip()
        ]):
            st.error("Lengkapi semua data terlebih dahulu.")

        elif umur < 18 and not persetujuan_wali:
            st.warning("Persetujuan orang tua/wali diperlukan.")

        elif not setuju:
            st.warning("Silakan centang pernyataan data.")

        else:

            data_baru = {
                "id": max(
                    [d["id"] for d in st.session_state.data],
                    default=0
                ) + 1,
                "nama": nama,
                "umur": umur,
                "alamat": alamat,
                "hp": hp,
                "gunung": gunung,
                "tanggal": str(tanggal),
                "jumlah": jumlah,
                "darurat": darurat
            }

            st.session_state.data.append(data_baru)
            simpan_data(st.session_state.data)

            st.session_state.hasil = data_baru

            st.success("Pendaftaran berhasil dicatat!")

            st.subheader(
                f"Nomor Registrasi: MA-{data_baru['id']:04d}"
            )

            st.json(data_baru)

            st.info(
                "Bukti ini bukan izin resmi pendakian. "
                "Pastikan pendaftaran resmi kepada pengelola gunung."
            )

# ==========================================
# HASIL REGISTRASI
# ==========================================

elif halaman == "Hasil Registrasi":

    st.title("✅ Hasil Registrasi")

    if st.session_state.hasil:

        data = st.session_state.hasil

        st.success("Data pendaftaran berhasil dicatat.")

        st.markdown(
            f"""
            <div class="hero">
                <h2>BUKTI REGISTRASI</h2>
                <h1>MA-{data['id']:04d}</h1>
                <p>Mountain Adventure</p>
            </div>
            """,
            unsafe_allow_html=True
        )

        for k, v in data.items():
            st.write(f"**{k.title()}:** {v}")

    else:
        st.info(
            "Belum ada hasil registrasi pada sesi ini. "
            "Silakan melakukan pendaftaran terlebih dahulu."
        )

# ==========================================
# RIWAYAT
# ==========================================

elif halaman == "Riwayat":

    st.title("📋 Riwayat Pendaftaran")

    if st.session_state.data:

        for data in reversed(st.session_state.data):

            with st.expander(
                f"MA-{data['id']:04d} | "
                f"{data['nama']} | {data['gunung']}"
            ):

                for k, v in data.items():
                    st.write(f"**{k.title()}:** {v}")

    else:
        st.info("Belum ada data pendaftaran.")

# ==========================================
# FOOTER
# ==========================================

st.divider()

st.markdown(
    """
    <div style="text-align:center; padding:20px; color:#718075;">
        <h3>⛰️ MOUNTAIN ADVENTURE</h3>
        Explore Indonesia, Respect Nature.<br>
        © 2026 Mountain Adventure
    </div>
    """,
    unsafe_allow_html=True
)
