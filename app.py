from pathlib import Path

code = r'''import streamlit as st
import json
import os
from datetime import date

# =========================================================
# MOUNTAIN ADVENTURE - versi tampilan diperbarui
# =========================================================
st.set_page_config(
    page_title="Mountain Adventure",
    page_icon="⛰️",
    layout="wide",
    initial_sidebar_state="expanded"
)

FILE_DATA = "pendaftaran.json"

# Data gunung: informasi pengenalan umum. Selalu cek pengelola resmi
# untuk status jalur, izin, cuaca, dan aturan terbaru.
GUNUNG = {
    "Gunung Lawu": {
        "provinsi": "Jawa Timur / Jawa Tengah",
        "wilayah": "Perbatasan Kabupaten Magetan dan Karanganyar",
        "kategori": "Pegunungan",
        "daya_tarik": "Hutan pegunungan, panorama puncak, serta kawasan budaya di lerengnya.",
        "deskripsi": "Gunung Lawu berada di perbatasan Jawa Timur dan Jawa Tengah. Kawasan ini dikenal dengan udara pegunungan yang sejuk, hutan, serta pemandangan luas dari kawasan puncaknya. Di sekitar lereng Lawu juga terdapat sejumlah tempat bersejarah dan tujuan wisata alam.",
        "detail": "Lawu memiliki hubungan erat dengan kehidupan masyarakat di sekitar Magetan dan Karanganyar. Bentang alamnya berubah dari kawasan permukiman dan kebun di kaki gunung menjadi hutan pegunungan pada bagian lebih tinggi. Pengunjung dapat mengenal panorama alam sekaligus budaya lokal. Kondisi jalur dan fasilitas dapat berubah, jadi informasi resmi perlu diperiksa sebelum berangkat."
    },
    "Gunung Semeru": {
        "provinsi": "Jawa Timur", "wilayah": "Kabupaten Lumajang dan Malang",
        "kategori": "Gunung api", "daya_tarik": "Lanskap Taman Nasional Bromo Tengger Semeru dan ekosistem pegunungan.",
        "deskripsi": "Semeru merupakan gunung tertinggi di Pulau Jawa dan berada di kawasan Taman Nasional Bromo Tengger Semeru. Kawasannya memiliki hutan, lereng vulkanik, dan bentang alam yang khas.",
        "detail": "Gunung Semeru merupakan gunung api aktif. Kawasan taman nasionalnya memiliki nilai konservasi tinggi dan menjadi habitat beragam flora serta fauna. Aktivitas vulkanik dapat memengaruhi keselamatan dan menyebabkan penutupan kawasan. Jangan menjadikan informasi wisata umum sebagai izin untuk mendekati kawah atau memasuki zona yang dibatasi."
    },
    "Gunung Bromo": {
        "provinsi": "Jawa Timur", "wilayah": "Probolinggo, Pasuruan, Lumajang, dan Malang",
        "kategori": "Gunung api", "daya_tarik": "Lautan pasir, kaldera Tengger, dan panorama matahari terbit.",
        "deskripsi": "Bromo terkenal dengan lautan pasir yang luas, kaldera Tengger, serta pemandangan matahari terbit. Kawasan ini juga memiliki hubungan budaya yang penting bagi masyarakat Tengger.",
        "detail": "Gunung Bromo berada di dalam kawasan Taman Nasional Bromo Tengger Semeru. Bentang alamnya terbentuk dari aktivitas vulkanik dan menawarkan pemandangan kaldera yang luas. Selain keindahan alam, kawasan ini merupakan ruang hidup masyarakat Tengger. Pengunjung perlu menghormati adat setempat, mengikuti arahan petugas, dan mematuhi pembatasan kawasan."
    },
    "Gunung Arjuno": {
        "provinsi": "Jawa Timur", "wilayah": "Malang, Pasuruan, dan Kota Batu",
        "kategori": "Pegunungan", "daya_tarik": "Hutan pegunungan dan panorama kompleks Arjuno-Welirang.",
        "deskripsi": "Arjuno merupakan bagian dari kompleks pegunungan Arjuno-Welirang. Kawasannya memiliki hutan pegunungan, punggungan, dan pemandangan alam Jawa Timur.",
        "detail": "Gunung Arjuno memiliki bentang alam yang beragam dari kaki hingga kawasan puncak. Area ini juga dikenal dengan sejumlah situs sejarah di lerengnya. Perjalanan di kawasan pegunungan memerlukan persiapan dan pendampingan yang sesuai. Periksa pengumuman resmi pengelola karena cuaca dan kondisi jalur dapat berubah."
    },
    "Gunung Welirang": {
        "provinsi": "Jawa Timur", "wilayah": "Kabupaten Pasuruan dan Mojokerto",
        "kategori": "Gunung api", "daya_tarik": "Bentang alam vulkanik dan kawasan pegunungan Arjuno-Welirang.",
        "deskripsi": "Welirang berada dalam satu kompleks pegunungan dengan Arjuno. Gunung ini dikenal dengan karakter vulkanik dan kawasan hutan pegunungan.",
        "detail": "Kawasan Welirang memiliki lingkungan vulkanik yang khas. Aktivitas alam di gunung api dapat menimbulkan bahaya, sehingga pengunjung wajib mematuhi batas aman dan arahan petugas. Informasi pada halaman ini hanya pengenalan, bukan panduan untuk mendekati area aktivitas vulkanik."
    },
    "Gunung Ijen": {
        "provinsi": "Jawa Timur", "wilayah": "Kabupaten Banyuwangi dan Bondowoso",
        "kategori": "Gunung api", "daya_tarik": "Kawah Ijen dan danau kawah berwarna hijau kebiruan.",
        "deskripsi": "Ijen dikenal karena danau kawah berwarna hijau kebiruan dan lanskap vulkaniknya. Kawasan ini juga menjadi tempat kegiatan masyarakat, termasuk pertambangan belerang.",
        "detail": "Kawah Ijen merupakan kawasan vulkanik dengan kondisi gas dan cuaca yang dapat berubah. Fenomena api biru hanya muncul pada kondisi tertentu dan bukan atraksi yang selalu dapat dilihat. Keselamatan harus menjadi prioritas: ikuti pembatasan, pengumuman resmi, dan arahan petugas; jangan memasuki area yang ditutup."
    },
    "Gunung Raung": {
        "provinsi": "Jawa Timur", "wilayah": "Banyuwangi, Bondowoso, dan Jember",
        "kategori": "Gunung api", "daya_tarik": "Kaldera besar dan panorama pegunungan.",
        "deskripsi": "Raung dikenal memiliki kaldera besar dan bentang alam vulkanik yang menonjol di kawasan timur Jawa.",
        "detail": "Gunung Raung merupakan gunung api aktif dengan karakter medan pegunungan yang perlu dihormati. Aktivitas vulkanik, cuaca, dan kondisi jalur dapat berubah. Informasi kunjungan harus selalu mengikuti pemberitahuan lembaga resmi dan pengelola kawasan."
    },
    "Gunung Argopuro": {
        "provinsi": "Jawa Timur", "wilayah": "Probolinggo, Situbondo, dan Jember",
        "kategori": "Pegunungan", "daya_tarik": "Hutan, padang savana, dan peninggalan sejarah.",
        "deskripsi": "Argopuro dikenal dengan kawasan hutan yang luas, padang savana, serta situs-situs sejarah di sekitar kawasan pegunungannya.",
        "detail": "Pegunungan Argopuro memiliki bentang alam yang panjang dan beragam. Kawasan hutannya penting bagi lingkungan dan keanekaragaman hayati. Karena jarak antarkawasan dapat jauh, perencanaan dan pendampingan yang bertanggung jawab sangat penting. Pastikan aturan dan akses resmi sebelum mengunjungi kawasan."
    },
    "Gunung Penanggungan": {
        "provinsi": "Jawa Timur", "wilayah": "Kabupaten Mojokerto dan Pasuruan",
        "kategori": "Pegunungan", "daya_tarik": "Situs peninggalan sejarah dan panorama alam.",
        "deskripsi": "Penanggungan memiliki banyak peninggalan arkeologi dan budaya di lerengnya. Bentuk gunungnya tampak khas di antara wilayah Mojokerto dan Pasuruan.",
        "detail": "Gunung Penanggungan sering dikaitkan dengan sejarah dan kebudayaan Jawa kuno. Sejumlah situs berupa bangunan dan struktur bersejarah tersebar di kawasan lereng. Pengunjung perlu menjaga kelestarian situs, tidak merusak atau memindahkan benda, dan mematuhi ketentuan pengelola."
    },
    "Gunung Kelud": {
        "provinsi": "Jawa Timur", "wilayah": "Kediri, Blitar, dan Malang",
        "kategori": "Gunung api", "daya_tarik": "Bentang alam vulkanik dan sejarah letusan.",
        "deskripsi": "Kelud merupakan gunung api yang memiliki sejarah aktivitas vulkanik penting di Jawa Timur. Kawasan sekitarnya memperlihatkan pengaruh proses geologi terhadap alam dan kehidupan warga.",
        "detail": "Gunung Kelud beberapa kali mengalami perubahan bentuk akibat aktivitas vulkanik. Kawasan wisata di sekitarnya dapat memiliki aturan akses yang berubah mengikuti status gunung. Selalu periksa pengumuman resmi dan jangan mendekati kawah atau zona pembatasan."
    },
    "Gunung Merapi": {
        "provinsi": "Jawa Tengah / DI Yogyakarta", "wilayah": "Perbatasan Yogyakarta dan Jawa Tengah",
        "kategori": "Gunung api", "daya_tarik": "Lanskap vulkanik dan kawasan edukasi kebencanaan.",
        "deskripsi": "Merapi merupakan salah satu gunung api paling aktif di Indonesia. Kawasan sekitarnya penting untuk pendidikan kebencanaan, konservasi, dan kehidupan masyarakat.",
        "detail": "Aktivitas Merapi dipantau secara berkala oleh lembaga pemantauan gunung api. Status dan zona bahayanya dapat berubah sewaktu-waktu. Kunjungan harus mengikuti aturan resmi, tidak memasuki kawasan terlarang, dan mengutamakan keselamatan warga serta pengunjung."
    },
    "Gunung Merbabu": {
        "provinsi": "Jawa Tengah", "wilayah": "Magelang, Boyolali, dan Semarang",
        "kategori": "Pegunungan", "daya_tarik": "Padang sabana dan panorama gunung-gunung Jawa.",
        "deskripsi": "Merbabu terkenal dengan padang rumput, sabana, dan pemandangan pegunungan di sekitarnya. Kawasannya juga memiliki hutan pegunungan.",
        "detail": "Gunung Merbabu berada dalam kawasan taman nasional yang melindungi ekosistem pegunungan. Pemandangan sabana menjadi salah satu ciri khasnya. Pengunjung perlu menjaga tumbuhan, membawa kembali sampah, dan memeriksa pembukaan jalur serta kuota dari pengelola resmi."
    },
    "Gunung Sindoro": {
        "provinsi": "Jawa Tengah", "wilayah": "Temanggung dan Wonosobo",
        "kategori": "Gunung api", "daya_tarik": "Panorama pegunungan dan perkebunan di lereng.",
        "deskripsi": "Sindoro merupakan gunung api di Jawa Tengah yang berdekatan dengan Gunung Sumbing. Lanskapnya terlihat menonjol dari kawasan dataran tinggi Dieng dan sekitarnya.",
        "detail": "Lereng Sindoro dimanfaatkan masyarakat untuk pertanian dan perkebunan. Pemandangan gunung ini sering terlihat berdampingan dengan Sumbing. Sebelum melakukan perjalanan, periksa status gunung, kondisi cuaca, jalur resmi, dan ketentuan pengelola."
    },
    "Gunung Sumbing": {
        "provinsi": "Jawa Tengah", "wilayah": "Magelang, Temanggung, dan Wonosobo",
        "kategori": "Gunung api", "daya_tarik": "Lanskap pegunungan dan panorama alam Jawa Tengah.",
        "deskripsi": "Sumbing merupakan salah satu gunung besar di Jawa Tengah. Bentuknya sering terlihat berdampingan dengan Gunung Sindoro dari berbagai titik di wilayah sekitarnya.",
        "detail": "Kawasan Sumbing memiliki desa-desa dan lahan pertanian di kaki gunung. Bentang alamnya memperlihatkan hubungan antara lingkungan pegunungan dan aktivitas masyarakat. Pengunjung harus menggunakan akses resmi dan memastikan pendampingan serta persiapan yang sesuai."
    },
    "Gunung Slamet": {
        "provinsi": "Jawa Tengah", "wilayah": "Banyumas, Purbalingga, Tegal, Pemalang, dan Brebes",
        "kategori": "Gunung api", "daya_tarik": "Hutan pegunungan dan panorama wilayah Jawa Tengah.",
        "deskripsi": "Slamet merupakan gunung tertinggi di Jawa Tengah dan menjadi bagian penting dari bentang alam provinsi tersebut.",
        "detail": "Gunung Slamet memiliki kawasan hutan dan ekosistem pegunungan yang luas. Sebagai gunung api, kondisinya perlu dipantau melalui informasi resmi. Jangan menganggap jalur selalu terbuka; ikuti aturan pengelola dan arahan petugas."
    },
    "Gunung Prau": {
        "provinsi": "Jawa Tengah", "wilayah": "Dataran Tinggi Dieng, Wonosobo dan sekitarnya",
        "kategori": "Pegunungan", "daya_tarik": "Padang rumput dan panorama matahari terbit.",
        "deskripsi": "Prau dikenal dengan padang rumput dan pemandangan pegunungan di kawasan Dieng. Dari sejumlah titik, pengunjung dapat melihat jajaran gunung di Jawa Tengah.",
        "detail": "Gunung Prau berada di kawasan dataran tinggi yang memiliki suhu sejuk. Lingkungan padang rumputnya perlu dijaga agar tidak rusak akibat aktivitas pengunjung. Periksa cuaca, kuota, jadwal, dan ketentuan jalur resmi sebelum berkunjung."
    },
    "Gunung Ungaran": {
        "provinsi": "Jawa Tengah", "wilayah": "Kabupaten Semarang",
        "kategori": "Pegunungan", "daya_tarik": "Hutan, perkebunan, dan pemandangan alam.",
        "deskripsi": "Ungaran merupakan kawasan pegunungan di selatan Kota Semarang. Lerengnya memiliki hutan, perkebunan, serta sejumlah tujuan wisata alam.",
        "detail": "Gunung Ungaran dekat dengan kawasan permukiman dan wisata di Kabupaten Semarang. Lingkungannya memperlihatkan perpaduan hutan dan lahan budidaya. Pengunjung sebaiknya menghormati masyarakat lokal, menjaga kebersihan, dan mengikuti ketentuan pengelola."
    },
    "Gunung Ciremai": {
        "provinsi": "Jawa Barat", "wilayah": "Kabupaten Kuningan dan Majalengka",
        "kategori": "Gunung api", "daya_tarik": "Hutan konservasi dan panorama Jawa Barat.",
        "deskripsi": "Ciremai merupakan gunung tertinggi di Jawa Barat dan berada dalam kawasan Taman Nasional Gunung Ciremai.",
        "detail": "Taman nasional ini melindungi hutan dan keanekaragaman hayati di sekitar Ciremai. Pengelolaan kunjungan dilakukan melalui jalur dan aturan yang ditetapkan. Pastikan informasi resmi mengenai kuota, izin, cuaca, serta kondisi jalur sebelum membuat rencana."
    },
    "Gunung Gede": {
        "provinsi": "Jawa Barat", "wilayah": "Bogor, Cianjur, dan Sukabumi",
        "kategori": "Gunung api", "daya_tarik": "Hutan hujan pegunungan dan kawasan konservasi.",
        "deskripsi": "Gede merupakan bagian dari Taman Nasional Gunung Gede Pangrango. Kawasan ini memiliki hutan hujan pegunungan dan keanekaragaman hayati yang tinggi.",
        "detail": "Taman nasional memiliki fungsi konservasi, penelitian, dan pendidikan. Beberapa kawasan memiliki aturan kunjungan dan kuota khusus. Pengunjung wajib mematuhi sistem pendaftaran resmi, tidak memberi makan satwa, dan tidak meninggalkan sampah."
    },
    "Gunung Pangrango": {
        "provinsi": "Jawa Barat", "wilayah": "Bogor, Cianjur, dan Sukabumi",
        "kategori": "Pegunungan", "daya_tarik": "Hutan pegunungan dan padang edelweiss di kawasan tertentu.",
        "deskripsi": "Pangrango berada dalam kawasan Taman Nasional Gunung Gede Pangrango. Hutan pegunungannya menjadi habitat beragam jenis tumbuhan dan satwa.",
        "detail": "Gunung Pangrango merupakan bagian dari satu ekosistem konservasi bersama Gunung Gede. Kawasan taman nasional memiliki aturan ketat untuk menjaga lingkungan. Jangan memetik tumbuhan, termasuk edelweiss, dan selalu ikuti ketentuan kunjungan."
    },
    "Gunung Papandayan": {
        "provinsi": "Jawa Barat", "wilayah": "Kabupaten Garut",
        "kategori": "Gunung api", "daya_tarik": "Kawah, hutan mati, dan padang edelweiss.",
        "deskripsi": "Papandayan terkenal dengan kawasan kawah, hutan mati, dan padang edelweiss. Bentang alamnya memperlihatkan berbagai proses geologi.",
        "detail": "Gunung Papandayan merupakan kawasan gunung api yang memiliki area wisata alam. Kondisi gas, cuaca, dan aktivitas vulkanik perlu diperhatikan. Pengunjung harus tetap berada di area yang diizinkan, mengikuti papan informasi, dan tidak merusak tumbuhan."
    },
    "Gunung Tangkuban Perahu": {
        "provinsi": "Jawa Barat", "wilayah": "Bandung Barat dan Subang",
        "kategori": "Gunung api", "daya_tarik": "Kawah dan panorama alam dataran tinggi.",
        "deskripsi": "Tangkuban Perahu dikenal dengan bentuk kawahnya yang khas dan kawasan wisata alam di utara Bandung.",
        "detail": "Kawasan ini memiliki beberapa kawah dengan karakter geologi yang berbeda. Aktivitas vulkanik dan gas dapat memengaruhi area yang boleh dikunjungi. Ikuti arahan petugas, jangan melewati pagar pembatas, dan periksa informasi resmi sebelum datang."
    },
    "Gunung Rinjani": {
        "provinsi": "Nusa Tenggara Barat", "wilayah": "Pulau Lombok",
        "kategori": "Gunung api", "daya_tarik": "Kaldera dan Danau Segara Anak.",
        "deskripsi": "Rinjani merupakan gunung tertinggi kedua di Indonesia dan terkenal dengan kaldera luas serta Danau Segara Anak.",
        "detail": "Gunung Rinjani berada di dalam Taman Nasional Gunung Rinjani. Kawasan ini memiliki nilai ekologi dan budaya yang penting bagi masyarakat Lombok. Pengelola menerapkan aturan kunjungan, kuota, dan ketentuan keselamatan. Perjalanan harus direncanakan bersama orang dewasa yang bertanggung jawab dan sesuai aturan resmi."
    },
    "Gunung Tambora": {
        "provinsi": "Nusa Tenggara Barat", "wilayah": "Pulau Sumbawa",
        "kategori": "Gunung api", "daya_tarik": "Kaldera luas dan sejarah geologi dunia.",
        "deskripsi": "Tambora dikenal karena letusan besar pada tahun 1815 yang berdampak luas terhadap iklim dunia. Kini kawasan kalderanya menjadi bagian penting dari sejarah geologi.",
        "detail": "Gunung Tambora memiliki bentang alam yang terbentuk oleh sejarah letusan besar. Kawasan sekitarnya memiliki hutan, padang rumput, dan nilai konservasi. Pengunjung perlu memeriksa kondisi kawasan dan aturan resmi, serta menghormati alam dan masyarakat setempat."
    },
    "Gunung Agung": {
        "provinsi": "Bali", "wilayah": "Kabupaten Karangasem",
        "kategori": "Gunung api", "daya_tarik": "Panorama Bali dan nilai budaya masyarakat setempat.",
        "deskripsi": "Agung merupakan gunung tertinggi di Bali dan memiliki arti budaya serta spiritual yang penting bagi masyarakat Hindu Bali.",
        "detail": "Gunung Agung merupakan gunung api aktif dan tempat yang dihormati masyarakat setempat. Status vulkanik dapat berubah dan memengaruhi akses. Pengunjung harus menghormati kawasan suci, mematuhi aturan adat dan pengelola, serta tidak memasuki zona berbahaya."
    },
    "Gunung Batur": {
        "provinsi": "Bali", "wilayah": "Kintamani, Kabupaten Bangli",
        "kategori": "Gunung api", "daya_tarik": "Kaldera dan Danau Batur.",
        "deskripsi": "Batur dikenal dengan kaldera luas dan Danau Batur di kawasan Kintamani. Lanskapnya memperlihatkan sejarah aktivitas vulkanik Bali.",
        "detail": "Kawasan Batur memiliki perpaduan alam, pertanian, dan budaya lokal. Danau dan kalderanya menjadi bagian penting dari kehidupan masyarakat. Pengunjung perlu mengikuti arahan pemandu resmi dan menghormati tempat-tempat yang dianggap suci."
    },
    "Gunung Kerinci": {
        "provinsi": "Jambi / Sumatera Barat", "wilayah": "Taman Nasional Kerinci Seblat",
        "kategori": "Gunung api", "daya_tarik": "Hutan tropis dan panorama Pegunungan Bukit Barisan.",
        "deskripsi": "Kerinci merupakan gunung api tertinggi di Indonesia dan berada di kawasan Taman Nasional Kerinci Seblat.",
        "detail": "Kawasan Kerinci Seblat merupakan salah satu bentang alam konservasi penting di Sumatra. Hutan di sekitarnya menjadi habitat satwa liar dan tumbuhan khas. Kunjungan perlu mengikuti aturan taman nasional dan memperhatikan kondisi alam yang dapat berubah."
    },
    "Gunung Marapi": {
        "provinsi": "Sumatera Barat", "wilayah": "Kabupaten Agam dan Tanah Datar",
        "kategori": "Gunung api", "daya_tarik": "Lanskap vulkanik dan panorama dataran tinggi Minangkabau.",
        "deskripsi": "Marapi merupakan gunung api aktif di Sumatera Barat. Kawasannya menjadi bagian dari lanskap dataran tinggi Minangkabau.",
        "detail": "Karena merupakan gunung api aktif, status Marapi dapat berubah dan akses kawasan dapat dibatasi. Informasi wisata tidak berarti kawasan aman untuk dikunjungi. Ikuti peringatan lembaga resmi dan jangan memasuki zona larangan."
    },
    "Gunung Singgalang": {
        "provinsi": "Sumatera Barat", "wilayah": "Agam dan Padang Pariaman",
        "kategori": "Pegunungan", "daya_tarik": "Hutan pegunungan dan Telaga Dewi.",
        "deskripsi": "Singgalang dikenal dengan hutan pegunungan dan Telaga Dewi di kawasan puncaknya. Gunung ini berada tidak jauh dari Gunung Marapi.",
        "detail": "Lingkungan Gunung Singgalang memiliki vegetasi pegunungan dan sumber air alami. Keberadaan telaga menjadi daya tarik alam yang perlu dijaga. Pengunjung sebaiknya menggunakan jalur yang diizinkan dan menjaga kebersihan sumber air."
    },
    "Gunung Dempo": {
        "provinsi": "Sumatera Selatan", "wilayah": "Kota Pagar Alam",
        "kategori": "Gunung api", "daya_tarik": "Perkebunan teh dan panorama dataran tinggi.",
        "deskripsi": "Dempo merupakan gunung tertinggi di Sumatera Selatan dan berada dekat kawasan perkebunan teh di Pagar Alam.",
        "detail": "Kawasan Dempo memperlihatkan perpaduan lanskap gunung, kebun teh, dan kehidupan masyarakat dataran tinggi. Kondisi gunung api dan jalur dapat berubah. Periksa pengumuman resmi serta aturan setempat sebelum berkunjung."
    },
    "Gunung Sibayak": {
        "provinsi": "Sumatera Utara", "wilayah": "Kabupaten Karo, dekat Berastagi",
        "kategori": "Gunung api", "daya_tarik": "Kawah dan pemandangan dataran tinggi Karo.",
        "deskripsi": "Sibayak merupakan gunung api yang dikenal di kawasan wisata Berastagi. Pemandangan dataran tinggi Karo menjadi salah satu daya tariknya.",
        "detail": "Gunung Sibayak memiliki kawasan kawah dan lanskap vulkanik. Pengunjung perlu memperhatikan gas, cuaca, dan arahan petugas. Jangan mendekati area yang dibatasi dan selalu menjaga kebersihan kawasan."
    },
    "Gunung Leuser": {
        "provinsi": "Aceh / Sumatera Utara", "wilayah": "Kawasan Taman Nasional Gunung Leuser",
        "kategori": "Pegunungan", "daya_tarik": "Hutan hujan tropis dan keanekaragaman hayati.",
        "deskripsi": "Leuser merupakan kawasan pegunungan luas yang menjadi habitat berbagai satwa dan tumbuhan langka, termasuk spesies khas Sumatra.",
        "detail": "Ekosistem Leuser merupakan kawasan konservasi penting dengan hutan hujan tropis yang luas. Kegiatan wisata alam harus memperhatikan perlindungan satwa dan habitat. Kunjungan dilakukan melalui pengelola atau pemandu berizin sesuai ketentuan kawasan."
    },
    "Puncak Jaya": {
        "provinsi": "Papua Tengah", "wilayah": "Pegunungan Sudirman",
        "kategori": "Pegunungan tinggi", "daya_tarik": "Bentang alam pegunungan tinggi dan lingkungan alpin.",
        "deskripsi": "Puncak Jaya merupakan puncak tertinggi di Indonesia dan bagian dari Pegunungan Sudirman di Papua.",
        "detail": "Kawasan Puncak Jaya memiliki lingkungan pegunungan tinggi yang sangat khusus dan akses yang kompleks. Informasi ini merupakan pengenalan geografis, bukan ajakan untuk melakukan perjalanan. Kegiatan di kawasan tersebut memerlukan pengaturan profesional, izin, dan pertimbangan keselamatan yang ketat."
    },
    "Gunung Latimojong": {
        "provinsi": "Sulawesi Selatan", "wilayah": "Kabupaten Enrekang",
        "kategori": "Pegunungan", "daya_tarik": "Hutan pegunungan dan pemandangan Sulawesi Selatan.",
        "deskripsi": "Latimojong merupakan rangkaian pegunungan di Sulawesi Selatan. Puncak tertingginya dikenal sebagai Rante Mario.",
        "detail": "Pegunungan Latimojong memiliki ekosistem hutan dan bentang alam yang penting bagi wilayah Enrekang. Kawasan ini juga berhubungan erat dengan kehidupan masyarakat lokal. Pastikan akses dan ketentuan kunjungan melalui sumber resmi."
    },
    "Gunung Binaiya": {
        "provinsi": "Maluku", "wilayah": "Pulau Seram, kawasan Taman Nasional Manusela",
        "kategori": "Pegunungan", "daya_tarik": "Hutan tropis Pulau Seram dan keanekaragaman hayati.",
        "deskripsi": "Binaiya merupakan gunung tertinggi di Kepulauan Maluku dan berada di Pulau Seram, dalam kawasan Taman Nasional Manusela.",
        "detail": "Kawasan Binaiya memiliki hutan tropis dengan kekayaan flora dan fauna khas. Karena berada di kawasan taman nasional, kegiatan kunjungan perlu mengikuti aturan konservasi. Hormati masyarakat adat dan jangan mengambil tumbuhan atau satwa."
    },
    "Gunung Klabat": {
        "provinsi": "Sulawesi Utara", "wilayah": "Kabupaten Minahasa Utara",
        "kategori": "Gunung api", "daya_tarik": "Panorama alam Minahasa dan kawasan hutan.",
        "deskripsi": "Klabat merupakan gunung tertinggi di Sulawesi Utara dan menjadi penanda alam yang penting di wilayah Minahasa.",
        "detail": "Gunung Klabat memiliki kawasan hutan dan pemandangan wilayah sekitarnya. Kondisi jalur serta aturan akses dapat berubah, sehingga pengunjung perlu mencari informasi dari pengelola atau pemerintah setempat sebelum berkunjung."
    },
    "Gunung Lokon": {
        "provinsi": "Sulawesi Utara", "wilayah": "Kota Tomohon",
        "kategori": "Gunung api", "daya_tarik": "Lanskap vulkanik dan pemandangan kawasan Tomohon.",
        "deskripsi": "Lokon merupakan gunung api di dekat Kota Tomohon. Bentang alamnya menjadi bagian khas dari panorama dataran tinggi Minahasa.",
        "detail": "Gunung Lokon merupakan gunung api aktif. Kawasan tertentu dapat ditutup karena aktivitas vulkanik atau gas. Jangan mendekati kawah dan selalu ikuti informasi resmi dari otoritas pemantauan serta petugas setempat."
    },
    "Gunung Soputan": {
        "provinsi": "Sulawesi Utara", "wilayah": "Kabupaten Minahasa Tenggara",
        "kategori": "Gunung api", "daya_tarik": "Bentang alam vulkanik Sulawesi Utara.",
        "deskripsi": "Soputan merupakan gunung api di Sulawesi Utara yang dikenal melalui aktivitas vulkaniknya.",
        "detail": "Sebagai gunung api aktif, Soputan memiliki potensi perubahan kondisi yang cepat. Halaman ini hanya memberikan informasi umum. Jangan merencanakan kunjungan ke area berbahaya dan patuhi seluruh pengumuman resmi."
    },
    "Gunung Gamalama": {
        "provinsi": "Maluku Utara", "wilayah": "Pulau Ternate",
        "kategori": "Gunung api", "daya_tarik": "Lanskap pulau vulkanik dan pemandangan Kota Ternate.",
        "deskripsi": "Gamalama merupakan gunung api yang membentuk Pulau Ternate. Gunung ini memiliki hubungan erat dengan sejarah dan kehidupan masyarakat pulau.",
        "detail": "Kondisi Gamalama dipantau karena aktivitas vulkaniknya. Area yang dapat dikunjungi bergantung pada status dan arahan otoritas. Hormati lingkungan pulau dan ikuti informasi resmi sebelum melakukan kegiatan wisata."
    },
    "Gunung Kie Matubu": {
        "provinsi": "Maluku Utara", "wilayah": "Pulau Tidore",
        "kategori": "Gunung api", "daya_tarik": "Panorama Pulau Tidore dan lanskap kepulauan.",
        "deskripsi": "Kie Matubu merupakan gunung di Pulau Tidore yang menjadi titik tertinggi pulau tersebut. Lanskapnya berkaitan erat dengan sejarah dan kehidupan masyarakat Tidore.",
        "detail": "Gunung Kie Matubu merupakan bagian penting dari bentang alam Tidore. Pengunjung perlu menghormati masyarakat lokal, memperhatikan kondisi cuaca, dan mengikuti aturan akses yang berlaku."
    },
    "Gunung Ebulobo": {
        "provinsi": "Nusa Tenggara Timur", "wilayah": "Kabupaten Nagekeo, Pulau Flores",
        "kategori": "Gunung api", "daya_tarik": "Lanskap vulkanik Pulau Flores.",
        "deskripsi": "Ebulobo merupakan gunung api di Pulau Flores, Nusa Tenggara Timur. Bentuknya menjadi salah satu unsur penting panorama wilayah Nagekeo.",
        "detail": "Kawasan Ebulobo memiliki karakter vulkanik. Aktivitas gunung api dan cuaca harus menjadi pertimbangan utama. Gunakan informasi dari otoritas resmi dan jangan memasuki zona yang dibatasi."
    },
    "Gunung Inerie": {
        "provinsi": "Nusa Tenggara Timur", "wilayah": "Kabupaten Ngada, Pulau Flores",
        "kategori": "Gunung api", "daya_tarik": "Bentuk kerucut gunung dan panorama perkampungan adat.",
        "deskripsi": "Inerie memiliki bentuk kerucut yang khas dan menjadi latar alam bagi sejumlah kampung di Kabupaten Ngada, Flores.",
        "detail": "Gunung Inerie memiliki nilai lanskap dan budaya. Wilayah sekitarnya juga dikenal dengan kampung adat dan tradisi lokal. Pengunjung perlu menghormati adat, meminta izin jika diperlukan, dan mengikuti aturan masyarakat setempat."
    },
    "Gunung Mutis": {
        "provinsi": "Nusa Tenggara Timur", "wilayah": "Kabupaten Timor Tengah Selatan",
        "kategori": "Pegunungan", "daya_tarik": "Hutan pegunungan dan keanekaragaman hayati Timor.",
        "deskripsi": "Mutis merupakan kawasan pegunungan penting di Pulau Timor. Lingkungannya dikenal dengan hutan pegunungan dan kekayaan alam khas Nusa Tenggara Timur.",
        "detail": "Kawasan Mutis memiliki nilai konservasi dan menjadi bagian penting dari lingkungan Pulau Timor. Kegiatan wisata perlu menghormati masyarakat sekitar serta menjaga sumber air, hutan, dan satwa liar."
    }
}

# ---------------------------------------------------------
# Penyimpanan data pendaftaran
# ---------------------------------------------------------
def baca_data():
    if os.path.exists(FILE_DATA):
        try:
            with open(FILE_DATA, "r", encoding="utf-8") as f:
                isi = json.load(f)
                return isi if isinstance(isi, list) else []
        except (json.JSONDecodeError, OSError):
            return []
    return []

def simpan_data(data):
    with open(FILE_DATA, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

if "data" not in st.session_state:
    st.session_state.data = baca_data()
if "hasil" not in st.session_state:
    st.session_state.hasil = None
if "gunung_dipilih" not in st.session_state:
    st.session_state.gunung_dipilih = None
if "halaman" not in st.session_state:
    st.session_state.halaman = "Beranda"

# ---------------------------------------------------------
# Desain: kontras tinggi agar tulisan mudah dibaca
# ---------------------------------------------------------
st.markdown("""
<style>
.stApp {
    background: #F4F7F3;
    color: #18352A;
}
[data-testid="stAppViewContainer"] .main .block-container {
    padding-top: 2rem;
    padding-bottom: 3rem;
    max-width: 1250px;
}
h1, h2, h3, h4, p, label, li, .stMarkdown, [data-testid="stMetricLabel"],
[data-testid="stMetricValue"] {
    color: #18352A !important;
}
p, li, .stMarkdown {
    line-height: 1.65;
}
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #103D2C 0%, #1F6548 100%);
}
section[data-testid="stSidebar"] * {
    color: #FFFFFF !important;
}
section[data-testid="stSidebar"] [data-testid="stRadio"] label {
    color: #FFFFFF !important;
    font-weight: 600;
}
.hero {
    background: linear-gradient(120deg, #103D2C, #347A55);
    padding: 42px 38px;
    border-radius: 20px;
    color: #FFFFFF !important;
    margin-bottom: 25px;
}
.hero h1, .hero h2, .hero p {
    color: #FFFFFF !important;
}
.hero h1 {font-size: 42px; font-weight: 850;}
.hero p {font-size: 18px; color: #F0F7F1 !important;}
.kartu {
    background: #FFFFFF;
    border: 1px solid #C9DCCB;
    border-radius: 16px;
    padding: 20px;
    min-height: 210px;
    box-shadow: 0 3px 12px rgba(20, 60, 40, .06);
}
.kartu h3 {color: #124B34 !important; margin-top: 0;}
.kartu p {color: #29483A !important;}
.info-box {
    background: #E2F0E5;
    border-left: 5px solid #2C7950;
    border-radius: 10px;
    padding: 17px 20px;
    color: #173D2B !important;
}
.detail-box {
    background: #FFFFFF;
    border: 1px solid #D4E2D5;
    border-radius: 16px;
    padding: 24px;
    color: #203D2E !important;
}
div.stButton > button {
    border-radius: 10px;
    font-weight: 700;
    min-height: 42px;
}
div.stButton > button[kind="primary"] {
    background: #176342;
    border-color: #176342;
    color: #FFFFFF;
}
[data-testid="stMetric"] {
    background: #FFFFFF;
    border: 1px solid #D8E5D9;
    padding: 14px;
    border-radius: 12px;
}
[data-testid="stMetricLabel"], [data-testid="stMetricValue"] {
    color: #173D2B !important;
}
footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Navigasi
# ---------------------------------------------------------
st.sidebar.markdown("# ⛰️ MOUNTAIN")
st.sidebar.markdown("## ADVENTURE")
st.sidebar.caption("EXPLORE THE BEAUTY OF INDONESIA")
st.sidebar.divider()

pilihan_halaman = ["Beranda", "Jelajah Gunung", "Pendaftaran", "Hasil Registrasi", "Riwayat"]
halaman = st.sidebar.radio(
    "NAVIGASI",
    pilihan_halaman,
    index=pilihan_halaman.index(st.session_state.halaman)
)
st.session_state.halaman = halaman

st.sidebar.divider()
st.sidebar.markdown("🌿 **Jelajahi alam dengan bijak.**")
st.sidebar.caption("Mountain Adventure © 2026")

def buka_detail(nama):
    st.session_state.gunung_dipilih = nama
    st.session_state.halaman = "Detail Gunung"

def tampilkan_kartu(nama, info, key):
    with st.container(border=True):
        st.markdown(f"### ⛰️ {nama}")
        st.caption(f"📍 {info['provinsi']} · {info['kategori']}")
        st.write(info["deskripsi"])
        if st.button("Lihat detail gunung →", key=key, use_container_width=True):
            buka_detail(nama)
            st.rerun()

# ---------------------------------------------------------
# Beranda
# ---------------------------------------------------------
if halaman == "Beranda":
    st.markdown("""
    <div class="hero">
        <h1>⛰️ MOUNTAIN ADVENTURE</h1>
        <h2>Discover The Beauty of Indonesia</h2>
        <p>Temukan informasi pegunungan Indonesia, kenali keindahan alamnya,
        dan baca informasi sebelum merencanakan kunjungan.</p>
    </div>
    """, unsafe_allow_html=True)

    st.title("Selamat Datang, Petualang!")
    st.write("Mountain Adventure adalah platform informasi gunung dan pendaftaran pendakian. "
             "Jelajahi berbagai wilayah, baca profil gunung, dan periksa ketentuan resmi sebelum bepergian.")

    a, b, c = st.columns(3)
    a.metric("Daftar Gunung", len(GUNUNG))
    b.metric("Total Pendaftaran", len(st.session_state.data))
    c.metric("Wilayah", "Indonesia")

    st.divider()
    st.subheader("🌄 Gunung Pilihan")
    pilihan = ["Gunung Lawu", "Gunung Bromo", "Gunung Rinjani", "Gunung Ijen", "Gunung Prau", "Gunung Merbabu"]
    for awal in range(0, len(pilihan), 3):
        cols = st.columns(3)
        for col, nama in zip(cols, pilihan[awal:awal+3]):
            with col:
                tampilkan_kartu(nama, GUNUNG[nama], f"home_{nama}")

    st.markdown("""
    <div class="info-box">
    <b>⚠️ Utamakan keselamatan</b><br>
    Halaman ini berisi informasi umum, bukan izin pendakian atau kepastian bahwa jalur sedang dibuka.
    Periksa status gunung, cuaca, kuota, izin, dan aturan pengelola resmi. Pengunjung di bawah 18 tahun
    harus mengikuti aturan usia serta persetujuan dan pendampingan orang tua/wali.
    </div>
    """, unsafe_allow_html=True)

# ---------------------------------------------------------
# Jelajah semua gunung
# ---------------------------------------------------------
elif halaman == "Jelajah Gunung":
    st.title("🌄 Jelajah Gunung Indonesia")
    st.write(f"Temukan informasi dari {len(GUNUNG)} gunung di berbagai wilayah Indonesia.")

    wilayah = sorted(set(info["provinsi"] for info in GUNUNG.values()))
    f1, f2 = st.columns([1, 2])
    with f1:
        filter_wilayah = st.selectbox("Filter wilayah", ["Semua Wilayah"] + wilayah)
    with f2:
        cari = st.text_input("🔎 Cari nama gunung", placeholder="Contoh: Lawu, Rinjani, Bromo...")

    hasil = []
    for nama, info in GUNUNG.items():
        cocok_wilayah = filter_wilayah == "Semua Wilayah" or filter_wilayah == info["provinsi"]
        cocok_nama = cari.lower().strip() in nama.lower()
        if cocok_wilayah and cocok_nama:
            hasil.append((nama, info))

    st.caption(f"Menampilkan {len(hasil)} gunung")
    if hasil:
        for awal in range(0, len(hasil), 3):
            cols = st.columns(3)
            for col, (nama, info) in zip(cols, hasil[awal:awal+3]):
                with col:
                    tampilkan_kartu(nama, info, f"jelajah_{nama}")
    else:
        st.warning("Gunung tidak ditemukan. Coba kata kunci atau wilayah lain.")

# ---------------------------------------------------------
# Detail gunung (dibuka dari tombol kartu)
# ---------------------------------------------------------
elif halaman == "Detail Gunung":
    nama = st.session_state.gunung_dipilih
    if nama not in GUNUNG:
        st.warning("Pilih gunung dari halaman Jelajah Gunung.")
        if st.button("Kembali ke Jelajah Gunung"):
            st.session_state.halaman = "Jelajah Gunung"
            st.rerun()
    else:
        info = GUNUNG[nama]
        if st.button("← Kembali ke Jelajah Gunung"):
            st.session_state.halaman = "Jelajah Gunung"
            st.rerun()

        st.markdown(f"""
        <div class="hero">
            <h1>⛰️ {nama}</h1>
            <p>{info['provinsi']} · {info['kategori']}</p>
        </div>
        """, unsafe_allow_html=True)

        st.subheader("Tentang Gunung Ini")
        st.markdown(f"<div class='detail-box'>{info['detail']}</div>", unsafe_allow_html=True)
        st.subheader("Informasi Gunung")
        x, y = st.columns(2)
        with x:
            st.markdown(f"<div class='detail-box'><b>📍 Wilayah</b><br>{info['wilayah']}</div>", unsafe_allow_html=True)
        with y:
            st.markdown(f"<div class='detail-box'><b>🏷️ Kategori</b><br>{info['kategori']}</div>", unsafe_allow_html=True)
        st.subheader("Daya Tarik")
        st.write(info["daya_tarik"])
        st.info("Informasi ini merupakan pengenalan umum. Status gunung, cuaca, jalur, kuota, dan izin dapat berubah. Periksa sumber resmi pengelola sebelum membuat rencana. Jangan memasuki zona yang ditutup atau berbahaya.")

        if st.button("Lihat formulir pendaftaran", type="primary"):
            st.session_state.halaman = "Pendaftaran"
            st.rerun()

# ---------------------------------------------------------
# Pendaftaran
# ---------------------------------------------------------
elif halaman == "Pendaftaran":
    st.title("📝 Pendaftaran Pendakian")
    st.write("Isi formulir dengan data yang benar. Pendaftaran pada website ini adalah pencatatan awal, bukan izin resmi dari pengelola gunung.")

    with st.form("form_pendaftaran"):
        st.subheader("A. Identitas Pendaki")
        nama = st.text_input("Nama lengkap")
        umur = st.number_input("Umur", min_value=13, max_value=100, value=18)
        alamat = st.text_area("Alamat")
        hp = st.text_input("Nomor HP")

        st.divider()
        st.subheader("B. Informasi Pendakian")
        gunung = st.selectbox("Pilih gunung", list(GUNUNG.keys()))
        tanggal = st.date_input("Tanggal rencana kunjungan", min_value=date.today())
        jumlah = st.number_input("Jumlah pendaki", min_value=1, max_value=50, value=1)
        darurat = st.text_input("Nomor kontak darurat")

        persetujuan_wali = False
        if umur < 18:
            persetujuan_wali = st.checkbox(
                "Saya mendapat persetujuan orang tua/wali dan akan mengikuti aturan pendampingan usia dari pengelola."
            )
        setuju = st.checkbox("Saya memastikan data yang dimasukkan benar.")
        kirim = st.form_submit_button("KIRIM PENDAFTARAN", use_container_width=True)

    if kirim:
        if not all([nama.strip(), alamat.strip(), hp.strip(), darurat.strip()]):
            st.error("Lengkapi semua data terlebih dahulu.")
        elif umur < 18 and not persetujuan_wali:
            st.warning("Persetujuan orang tua/wali diperlukan.")
        elif not setuju:
            st.warning("Silakan centang pernyataan data.")
        else:
            data_baru = {
                "id": max([d.get("id", 0) for d in st.session_state.data], default=0) + 1,
                "nama": nama, "umur": int(umur), "alamat": alamat, "hp": hp,
                "gunung": gunung, "tanggal": str(tanggal), "jumlah": int(jumlah),
                "darurat": darurat
            }
            st.session_state.data.append(data_baru)
            simpan_data(st.session_state.data)
            st.session_state.hasil = data_baru
            st.success("Pendaftaran berhasil dicatat!")
            st.subheader(f"Nomor Registrasi: MA-{data_baru['id']:04d}")
            st.json(data_baru)
            st.info("Bukti ini bukan izin resmi pendakian. Pastikan pendaftaran resmi kepada pengelola kawasan.")

# ---------------------------------------------------------
# Hasil registrasi
# ---------------------------------------------------------
elif halaman == "Hasil Registrasi":
    st.title("✅ Hasil Registrasi")
    if st.session_state.hasil:
        data = st.session_state.hasil
        st.success("Data pendaftaran berhasil dicatat.")
        st.markdown(f"""
        <div class="hero">
            <h2>BUKTI REGISTRASI</h2>
            <h1>MA-{data['id']:04d}</h1>
            <p>Mountain Adventure</p>
        </div>
        """, unsafe_allow_html=True)
        for k, v in data.items():
            st.write(f"**{k.replace('_', ' ').title()}:** {v}")
    else:
        st.info("Belum ada hasil registrasi pada sesi ini. Silakan melakukan pendaftaran terlebih dahulu.")

# ---------------------------------------------------------
# Riwayat
# ---------------------------------------------------------
elif halaman == "Riwayat":
    st.title("📋 Riwayat Pendaftaran")
    if st.session_state.data:
        for data in reversed(st.session_state.data):
            with st.expander(f"MA-{data.get('id', 0):04d} | {data.get('nama', '-')} | {data.get('gunung', '-')}"):
                for k, v in data.items():
                    st.write(f"**{k.replace('_', ' ').title()}:** {v}")
    else:
        st.info("Belum ada data pendaftaran.")

st.divider()
st.markdown(
    "<div style='text-align:center;color:#52675B;padding:18px;'>"
    "<b>⛰️ MOUNTAIN ADVENTURE</b><br>Explore Indonesia, Respect Nature.<br>© 2026 Mountain Adventure</div>",
    unsafe_allow_html=True
)
'''
path = Path("/mnt/data/app_mountain_adventure_baru.py")
path.write_text(code, encoding="utf-8")
print(f"File berhasil dibuat: {path}")
print(f"Jumlah gunung: {code.count('\"provinsi\":')}")
