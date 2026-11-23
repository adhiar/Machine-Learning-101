# Tutorial Agno + Groq + RAG (LanceDB)

Contoh sederhana menggunakan **Agno** sebagai framework agent, **Groq** sebagai penyedia LLM, dan **LanceDB + SentenceTransformer** sebagai knowledge base lokal berbasis *vector search*.

## Isi proyek

| File | Fungsi |
| --- | --- |
| `Tutorial Simple LLM w Agno.py` | Menjalankan agent Groq sederhana tanpa RAG. |
| `Tutorial RAG.py` | Membaca `Dummy.csv`, membuat embedding lokal, dan memasukkannya ke tabel LanceDB `layanan`. |
| `Tutorial Panggil Knowledge.py` | Menjalankan agent Groq dengan pencarian knowledge dari tabel LanceDB `layanan`. |
| `requirements.txt` | Daftar dependensi Python. |
| `.gitignore` | Mengabaikan `.env`, virtual environment, cache, dan database lokal dari Git. |

> **Catatan:** `Dummy.csv` merupakan input yang akan dijadikan percontohan

## Persyaratan

- Python **3.11** direkomendasikan (terutama untuk kemudahan kompatibilitas paket embedding di Windows).
- Koneksi internet untuk instalasi paket, penggunaan Groq, dan pengunduhan model embedding pada eksekusi pertama.
- API key Groq dari [Groq Console](https://console.groq.com/keys).

## Instalasi

Jalankan perintah berikut di terminal pada folder proyek.

**Windows (PowerShell):**

```powershell
py -3.11 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

**Linux / macOS:**

```bash
python3.11 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Jika PowerShell menolak aktivasi virtual environment karena execution policy, gunakan Python dari virtual environment secara langsung, misalnya ` .\.venv\Scripts\python.exe -m pip install -r requirements.txt `.

## Konfigurasi `.env`

Buat file bernama **`.env`** di folder yang sama dengan script Python. Isi:

```dotenv
GROQ_API_KEY= Isi disini
```

`load_dotenv()` pada script agent membaca variabel tersebut.

## Cara menjalankan

### 1. Uji agent LLM tanpa knowledge

```bash
python "Tutorial Simple LLM w Agno.py"
```

Script akan mengirim pertanyaan contoh tentang resistansi internal baterai ke model Groq `qwen/qwen3.8-27b`.

### 2. Buat / perbarui knowledge base dari CSV

Pastikan file **`Dummy.csv`** ada di direktori proyek, kemudian jalankan:

```bash
python "Tutorial RAG.py"
```

Script menggunakan `CSVReader` dan `SentenceTransformerEmbedder` untuk mengindeks data CSV ke:

- **Lokasi LanceDB:** `token/lancedb`
- **Nama tabel:** `layanan`
- **Nama koleksi/dokumen saat insert:** `Layanan-1`
- **`upsert=True`:** mengupayakan pembaruan data saat proses dijalankan ulang.

Model embedding akan diunduh otomatis pada penggunaan pertama (jika belum ada di cache Hugging Face).

### 3. Panggil agent dengan knowledge base

Setelah proses indexing berhasil, jalankan:

```bash
python "Tutorial Panggil Knowledge.py"
```

Script mencari referensi di LanceDB dengan `SearchType.vector` dan memberikan konteks kepada agent Groq untuk menjawab pertanyaan.

**Penting:** Path `token/lancedb`, nama tabel `layanan`, serta konfigurasi/model embedding harus konsisten di kedua script RAG. Jika database belum dibuat atau nama tabel berbeda, pencarian knowledge dapat gagal atau tidak menemukan hasil.

## Struktur folder yang diharapkan

```text
agno-rag-tutorial/
├── Tutorial Simple LLM w Agno.py
├── Tutorial RAG.py
├── Tutorial Panggil Knowledge.py
├── Dummy.csv                # disediakan oleh pengguna
├── requirements.txt
├── README.md
├── .gitignore
├── .env                     # privat, tidak masuk Git
├── .venv/                   # dibuat saat setup, tidak masuk Git
└── token/
    └── lancedb/             # dibuat saat indexing, tidak masuk Git
```