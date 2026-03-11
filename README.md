# Learn FastAPI API

## Prasyarat
- Python 3.x
- PostgreSQL

## Cara Instalasi dan Menjalankan Proyek

### 1. Clone repositori
```bash
git clone https://github.com/herupurnomoid/learn-fastapi.git
cd learn-fastapi
```

### 2. Buat virtual environment

```bash
python -m venv .venv
```

### 3. Aktifkan virtual environment

```bash
source .venv/bin/activate
```

### 4. Instal dependensi

```bash
pip install -r requirements.txt
```

### 5. Konfigurasi Database

Pastikan PostgreSQL sudah berjalan. Jika konfigurasi berbeda dari default, setel variabel lingkungan `DATABASE_URL` sebelum menjalankan aplikasi:

```bash
export DATABASE_URL="postgresql://username:password@localhost/nama_database"
```

### 6. Jalankan server lokal

```bash
fastapi dev
```

## Akses Dokumentasi API (Swagger UI)

Buka peramban dan akses URL berikut:

```
http://localhost:8000/docs
```
