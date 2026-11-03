
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# ==============================
# KONFIGURASI APLIKASI
# ==============================

root = tk.Tk()
root.title("Mountain Adventure | Pendaftaran Pendakian")
root.geometry("1100x720")
root.minsize(900, 620)
root.configure(bg="#F3F6F1")

HIJAU = "#174B35"
HIJAU2 = "#26734D"
HIJAU_MUDA = "#E5F0E7"
KREM = "#F3F6F1"
PUTIH = "#FFFFFF"
ABU = "#64746A"
GELAP = "#20372A"

data_pendaftaran = []
nomor_id = 1

# ==============================
# STYLE
# ==============================

style = ttk.Style()
style.theme_use("clam")

style.configure(
    "Treeview",
    background="white",
    foreground=GELAP,
    rowheight=35,
    fieldbackground="white",
    font=("Arial", 10)
)

style.configure(
    "Treeview.Heading",
    background=HIJAU,
    foreground="white",
    font=("Arial", 10, "bold"),
    padding=10
)

style.map(
    "Treeview",
    background=[("selected", "#BBD9C3")],
    foreground=[("selected", GELAP)]
)

# ==============================
# FUNGSI BANTUAN
# ==============================

def bersihkan():
    for widget in area_isi.winfo_children():
        widget.destroy()


def buat_label(parent, teks, ukuran=11, warna=GELAP,
               tebal=False, bg=PUTIH):
    return tk.Label(
        parent,
        text=teks,
        font=("Arial", ukuran, "bold" if tebal else "normal"),
        fg=warna,
        bg=bg
    )


def tombol(parent, teks, fungsi, warna=HIJAU2):
    return tk.Button(
        parent,
        text=teks,
        command=fungsi,
        bg=warna,
        fg="white",
        activebackground=HIJAU,
        activeforeground="white",
        font=("Arial", 10, "bold"),
        relief="flat",
        cursor="hand2",
        padx=18,
        pady=11
    )


def buat_kartu(parent, padding=20):
    return tk.Frame(
        parent,
        bg=PUTIH,
        padx=padding,
        pady=padding,
        highlightbackground="#E1E9E1",
        highlightthickness=1
    )


def pindah(halaman):
    if halaman == "beranda":
        tampil_beranda()
    elif halaman == "pendaftaran":
        tampil_pendaftaran()
    elif halaman == "riwayat":
        tampil_riwayat()


# ==============================
# SIDEBAR
# ==============================

sidebar = tk.Frame(root, bg=HIJAU, width=235)
sidebar.pack(side="left", fill="y")
sidebar.pack_propagate(False)

tk.Label(
    sidebar,
    text="⛰",
    font=("Arial", 45),
    bg=HIJAU,
    fg="white"
).pack(pady=(30, 0))

tk.Label(
    sidebar,
    text="MOUNTAIN\nADVENTURE",
    font=("Arial", 17, "bold"),
    bg=HIJAU,
    fg="white",
    justify="center"
).pack(pady=10)

tk.Label(
    sidebar,
    text="SISTEM PENDAFTARAN\nPENDAKIAN GUNUNG",
    font=("Arial", 8),
    bg=HIJAU,
    fg="#C6DDCE",
    justify="center"
).pack(pady=(0, 35))


def menu_sidebar(teks, halaman):
    tk.Button(
        sidebar,
        text=teks,
        command=lambda: pindah(halaman),
        bg=HIJAU,
        fg="white",
        activebackground=HIJAU2,
        activeforeground="white",
        font=("Arial", 11, "bold"),
        anchor="w",
        padx=25,
        pady=15,
        relief="flat",
        cursor="hand2"
    ).pack(fill="x", padx=12, pady=4)


menu_sidebar("⌂   BERANDA", "beranda")
menu_sidebar("✎   PENDAFTARAN", "pendaftaran")
menu_sidebar("▤   RIWAYAT PENDAFTARAN", "riwayat")

tk.Frame(sidebar, bg="#47765A", height=1).pack(
    fill="x", padx=20, pady=25
)

tk.Label(
    sidebar,
    text="Jelajahi Alam Indonesia\nDengan Aman dan Nyaman",
    bg=HIJAU,
    fg="#D3E5D7",
    font=("Arial", 10),
    justify="center"
).pack(side="bottom", pady=30)

# ==============================
# AREA UTAMA
# ==============================

area_utama = tk.Frame(root, bg=KREM)
area_utama.pack(side="right", fill="both", expand=True)

header = tk.Frame(area_utama, bg=PUTIH, height=65)
header.pack(fill="x")
header.pack_propagate(False)

tk.Label(
    header,
    text="  MOUNTAIN ADVENTURE",
    bg=PUTIH,
    fg=HIJAU,
    font=("Arial", 13, "bold")
).pack(side="left", padx=20)

tk.Label(
    header,
    text="Sistem Informasi Pendakian",
    bg=PUTIH,
    fg=ABU,
    font=("Arial", 10)
).pack(side="right", padx=25)

area_isi = tk.Frame(area_utama, bg=KREM)
area_isi.pack(fill="both", expand=True, padx=25, pady=20)

# ==============================
# HALAMAN BERANDA
# ==============================

def tampil_beranda():
    bersihkan()

    tk.Label(
        area_isi,
        text="SELAMAT DATANG DI",
        bg=KREM,
        fg=ABU,
        font=("Arial", 11, "bold")
    ).pack(anchor="w", pady=(5, 3))

    # Banner
    banner = tk.Frame(area_isi, bg=HIJAU, height=190)
    banner.pack(fill="x", pady=10)
    banner.pack_propagate(False)

    tk.Label(
        banner,
        text="⛰  MOUNTAIN ADVENTURE",
        bg=HIJAU,
        fg="#D4E8D8",
        font=("Arial", 12, "bold")
    ).pack(anchor="w", padx=25, pady=(25, 5))

    tk.Label(
        banner,
        text="Wujudkan Petualanganmu!",
        bg=HIJAU,
        fg="white",
        font=("Arial", 25, "bold")
    ).pack(anchor="w", padx=25)

    tk.Label(
        banner,
        text="Daftarkan perjalanan pendakianmu dengan mudah.",
        bg=HIJAU,
        fg="#D4E8D8",
        font=("Arial", 11)
    ).pack(anchor="w", padx=25, pady=8)

    tombol(
        banner,
        "MULAI PENDAFTARAN  →",
        tampil_pendaftaran
    ).pack(anchor="w", padx=25, pady=5)

    # Penjelasan
    kartu = buat_kartu(area_isi)
    kartu.pack(fill="x", pady=10)

    buat_label(
        kartu,
        "TENTANG WEBSITE INI",
        15,
        HIJAU,
        True
    ).pack(anchor="w")

    tk.Label(
        kartu,
        text=(
            "Mountain Adventure merupakan aplikasi sistem informasi "
            "dan pendaftaran pendakian gunung yang dibuat untuk "
            "mempermudah calon pendaki melakukan registrasi.\n\n"
            "Melalui aplikasi ini, pengguna dapat mengisi formulir "
            "pendaftaran, memilih gunung tujuan, menentukan tanggal "
            "pendakian, serta memasukkan informasi kontak darurat.\n\n"
            "Setelah pendaftaran dikirim, pengguna dapat melihat "
            "hasil registrasi dan memeriksa riwayat pendaftaran "
            "yang telah dilakukan."
        ),
        bg=PUTIH,
        fg=ABU,
        font=("Arial", 10),
        justify="left",
        wraplength=750
    ).pack(anchor="w", pady=12)

    # Statistik
    statistik = tk.Frame(area_isi, bg=KREM)
    statistik.pack(fill="x", pady=8)

    for judul, nilai in [
        ("TOTAL PENDAFTARAN", str(len(data_pendaftaran))),
        ("STATUS SISTEM", "AKTIF"),
        ("JENIS APLIKASI", "PYTHON")
    ]:
        kotak = buat_kartu(statistik, 15)
        kotak.pack(side="left", fill="both", expand=True, padx=5)

        buat_label(
            kotak, nilai, 18, HIJAU, True
        ).pack(anchor="w")

        buat_label(
            kotak, judul, 8, ABU
        ).pack(anchor="w", pady=5)

    tk.Label(
        area_isi,
        text="© 2026 Mountain Adventure | Pendakian Aman, Alam Lestari",
        bg=KREM,
        fg=ABU,
        font=("Arial", 9)
    ).pack(anchor="center", pady=10)


# ==============================
# HALAMAN PENDAFTARAN
# ==============================

def tampil_pendaftaran():
    bersihkan()

    buat_label(
        area_isi,
        "FORMULIR PENDAFTARAN",
        20,
        HIJAU,
        True,
        KREM
    ).pack(anchor="w", pady=(0, 5))

    buat_label(
        area_isi,
        "Silakan lengkapi informasi calon pendaki.",
        10,
        ABU,
        bg=KREM
    ).pack(anchor="w", pady=(0, 15))

    kartu = buat_kartu(area_isi, 20)
    kartu.pack(fill="both", expand=True)

    form = {}

    def input_data(label, baris, kolom):
        tk.Label(
            kartu,
            text=label,
            bg=PUTIH,
            fg=GELAP,
            font=("Arial", 10, "bold")
        ).grid(
            row=baris,
            column=kolom,
            sticky="w",
            pady=(12, 5),
            padx=10
        )

        entri = tk.Entry(
            kartu,
            font=("Arial", 11),
            relief="solid",
            bd=1
        )

        entri.grid(
            row=baris + 1,
            column=kolom,
            sticky="ew",
            padx=10,
            ipady=8
        )

        form[label] = entri
        return entri

    kartu.grid_columnconfigure(0, weight=1)
    kartu.grid_columnconfigure(1, weight=1)

    input_data("Nama Lengkap", 0, 0)
    input_data("Umur", 0, 1)
    input_data("Alamat", 2, 0)
    input_data("Nomor HP", 2, 1)

    tk.Label(
        kartu,
        text="Gunung Tujuan",
        bg=PUTIH,
        fg=GELAP,
        font=("Arial", 10, "bold")
    ).grid(row=4, column=0, sticky="w", padx=10, pady=(12, 5))

    pilihan_gunung = ttk.Combobox(
        kartu,
        values=[
            "Gunung Lawu",
            "Gunung Bromo",
            "Gunung Semeru",
            "Gunung Merbabu",
            "Gunung Arjuno",
            "Gunung Ijen"
        ],
        state="readonly",
        font=("Arial", 10)
    )

    pilihan_gunung.grid(
        row=5, column=0, sticky="ew",
        padx=10, ipady=7
    )

    tk.Label(
        kartu,
        text="Tanggal Pendakian (YYYY-MM-DD)",
        bg=PUTIH,
        fg=GELAP,
        font=("Arial", 10, "bold")
    ).grid(row=4, column=1, sticky="w", padx=10, pady=(12, 5))

    tanggal = tk.Entry(
        kartu,
        font=("Arial", 11),
        relief="solid",
        bd=1
    )

    tanggal.grid(
        row=5, column=1, sticky="ew",
        padx=10, ipady=8
    )

    input_data("Jumlah Pendaki", 6, 0)
    input_data("Kontak Darurat", 6, 1)

    tk.Label(
        kartu,
        text="Pastikan semua data yang dimasukkan sudah benar.",
        bg=PUTIH,
        fg=ABU,
        font=("Arial", 9)
    ).grid(
        row=8, column=0, columnspan=2,
        sticky="w", padx=10, pady=15
    )

    def kirim():
        global nomor_id

        nama = form["Nama Lengkap"].get().strip()
        umur = form["Umur"].get().strip()
        alamat = form["Alamat"].get().strip()
        hp = form["Nomor HP"].get().strip()
        gunung = pilihan_gunung.get()
        tgl = tanggal.get().strip()
        jumlah = form["Jumlah Pendaki"].get().strip()
        darurat = form["Kontak Darurat"].get().strip()

        if not all([nama, umur, alamat, hp, gunung,
                    tgl, jumlah, darurat]):
            messagebox.showwarning(
                "Data Belum Lengkap",
                "Mohon lengkapi semua formulir!"
            )
            return

        try:
            umur = int(umur)
            jumlah = int(jumlah)

            if umur < 13 or umur > 100 or jumlah < 1:
                raise ValueError

            datetime.strptime(tgl, "%Y-%m-%d")

        except ValueError:
            messagebox.showerror(
                "Data Tidak Valid",
                "Periksa umur, jumlah pendaki, dan format tanggal.\n"
                "Gunakan format tanggal YYYY-MM-DD."
            )
            return

        data = {
            "id": nomor_id,
            "nama": nama,
            "umur": umur,
            "alamat": alamat,
            "hp": hp,
            "gunung": gunung,
            "tanggal": tgl,
            "jumlah": jumlah,
            "darurat": darurat
        }

        data_pendaftaran.append(data)
        nomor_id += 1

        messagebox.showinfo(
            "Berhasil",
            "Pendaftaran berhasil disimpan!"
        )

        tampil_hasil(data)

    tombol(
        kartu,
        "KIRIM PENDAFTARAN",
        kirim
    ).grid(
        row=9, column=0, columnspan=2,
        pady=20
    )


# ==============================
# HALAMAN HASIL REGISTRASI
# ==============================

def tampil_hasil(data):
    bersihkan()

    tk.Label(
        area_isi,
        text="REGISTRASI BERHASIL!",
        bg=KREM,
        fg=HIJAU2,
        font=("Arial", 22, "bold")
    ).pack(pady=15)

    tk.Label(
        area_isi,
        text="Berikut adalah informasi pendaftaran pendakian Anda.",
        bg=KREM,
        fg=ABU,
        font=("Arial", 10)
    ).pack(pady=5)

    kartu = buat_kartu(area_isi, 25)
    kartu.pack(fill="x", pady=15)

    buat_label(
        kartu,
        "BUKTI PENDAFTARAN",
        15,
        HIJAU,
        True
    ).pack(anchor="center", pady=10)

    tk.Label(
        kartu,
        text=f"ID REGISTRASI: MA-{data['id']:04d}",
        bg=HIJAU_MUDA,
        fg=HIJAU,
        font=("Arial", 12, "bold"),
        pady=10
    ).pack(fill="x", pady=10)

    informasi = [
        ("Nama Lengkap", data["nama"]),
        ("Umur", str(data["umur"]) + " tahun"),
        ("Alamat", data["alamat"]),
        ("Nomor HP", data["hp"]),
        ("Gunung Tujuan", data["gunung"]),
        ("Tanggal Pendakian", data["tanggal"]),
        ("Jumlah Pendaki", str(data["jumlah"])),
        ("Kontak Darurat", data["darurat"])
    ]

    for label, nilai in informasi:
        baris = tk.Frame(kartu, bg=PUTIH)
        baris.pack(fill="x", pady=6)

        tk.Label(
            baris,
            text=label,
            bg=PUTIH,
            fg=ABU,
            font=("Arial", 10),
            width=22,
            anchor="w"
        ).pack(side="left")

        tk.Label(
            baris,
            text=nilai,
            bg=PUTIH,
            fg=GELAP,
            font=("Arial", 10, "bold"),
            anchor="w",
            wraplength=430
        ).pack(side="left")

    tk.Label(
        area_isi,
        text="Simpan informasi ini sebagai catatan pendaftaran.",
        bg=KREM,
        fg=ABU,
        font=("Arial", 9)
    ).pack(pady=5)

    tombol(
        area_isi,
        "+ DAFTAR LAGI",
        tampil_pendaftaran
    ).pack(pady=5)

    tombol(
        area_isi,
        "LIHAT RIWAYAT",
        tampil_riwayat
    ).pack(pady=5)


# ==============================
# HALAMAN RIWAYAT
# ==============================

def tampil_riwayat():
    bersihkan()

    buat_label(
        area_isi,
        "RIWAYAT PENDAFTARAN",
        20,
        HIJAU,
        True,
        KREM
    ).pack(anchor="w", pady=10)

    buat_label(
        area_isi,
        "Daftar seluruh registrasi selama aplikasi berjalan.",
        10,
        ABU,
        bg=KREM
    ).pack(anchor="w", pady=(0, 15))

    kartu = buat_kartu(area_isi, 15)
    kartu.pack(fill="both", expand=True)

    tabel = ttk.Treeview(
        kartu,
        columns=("ID", "Nama", "Gunung", "Tanggal", "Jumlah"),
        show="headings"
    )

    kolom = {
        "ID": 60,
        "Nama": 150,
        "Gunung": 140,
        "Tanggal": 120,
        "Jumlah": 80
    }

    for nama, lebar in kolom.items():
        tabel.heading(nama, text=nama)
        tabel.column(nama, width=lebar, anchor="center")

    tabel.pack(fill="both", expand=True)

    for data in data_pendaftaran:
        tabel.insert(
            "",
            "end",
            values=(
                data["id"],
                data["nama"],
                data["gunung"],
                data["tanggal"],
                data["jumlah"]
            )
        )

    def detail():
        pilihan = tabel.selection()

        if not pilihan:
            messagebox.showwarning(
                "Pilih Data",
                "Silakan pilih salah satu pendaftaran."
            )
            return

        nilai = tabel.item(pilihan[0], "values")
        id_data = int(nilai[0])

        data = next(
            (d for d in data_pendaftaran if d["id"] == id_data),
            None
        )

        if data:
            tampil_hasil(data)

    tombol(
        kartu,
        "LIHAT DETAIL PENDAFTARAN",
        detail
    ).pack(pady=15)

    tombol(
        area_isi,
        "+ BUAT PENDAFTARAN BARU",
        tampil_pendaftaran
    ).pack(pady=12)

tampil_beranda()
root.mainloop()