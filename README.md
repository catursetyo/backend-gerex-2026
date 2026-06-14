# Backend GEREX 2026 - Gugus Checker

Backend sederhana untuk fitur **Gugus Checker** pada penugasan Web Development GERIGI X UKM EXPO ITS 2026. Fitur ini digunakan untuk mengecek data gugus mahasiswa baru berdasarkan input **NRP**.

## Deskripsi Project

Project ini dibuat menggunakan **Node.js**, **Express.js**, dan **SQLite**. User dapat memasukkan NRP, lalu backend akan mencari data mahasiswa baru di database dan mengembalikan informasi berupa:

- NRP
- Nama mahasiswa
- Gugus
- Region

## Tech Stack

- Node.js
- Express.js
- SQLite
- CORS

## Struktur Project

```txt
backend-gerex-2026/
├── gugus-checker/
│   ├── database.db
│   ├── db.js
│   ├── init-db.js
│   ├── package.json
│   └── server.js
├── node_modules/
├── README.md
└── package-lock.json
```

## Instalasi

Clone repository:

```bash
git clone https://github.com/catursetyo/backend-gerex-2026.git
cd backend-gerex-2026
```

Install dependency:

```bash
npm install
```

Inisialisasi database:

```bash
npm run init-db
```

Jalankan server:

```bash
npm run dev
```

Server akan berjalan di:

```txt
http://localhost:3000
```

## Database Schema

Project ini menggunakan 3 tabel utama:

<img src="/assets/image1.png">

Relasinya adalah satu **region** dapat memiliki banyak **gugus**, dan satu **gugus** dapat memiliki banyak **mahasiswa baru**.

## Endpoint API

### Cek Status API

```http
GET /
```

Contoh response:

```json
{
  "message": "Gugus Checker API is running"
}
```

### Gugus Checker

```http
GET /api/gugus-checker?nrp=5027251066
```

Endpoint ini digunakan untuk mencari data gugus mahasiswa baru berdasarkan NRP.

## Contoh Response Berhasil

```json
{
  "success": true,
  "message": "Data gugus berhasil ditemukan",
  "data": {
    "nrp": "5027251066",
    "nama": "Catur Setyo Ragil",
    "gugus": "Gugus Arjuna",
    "region": "Region Surabaya"
  }
}
```

## Contoh Response Jika NRP Kosong

```json
{
  "success": false,
  "message": "NRP wajib diisi"
}
```

## Contoh Response Jika Data Tidak Ditemukan

```json
{
  "success": false,
  "message": "Data mahasiswa dengan NRP tersebut tidak ditemukan"
}
```

## Alur Endpoint API

1. User memasukkan NRP.
2. Frontend mengirim request ke endpoint `/api/gugus-checker?nrp=...`.
3. Backend mengambil NRP dari query parameter.
4. Backend memvalidasi apakah NRP sudah diisi.
5. Jika NRP kosong, backend mengembalikan error.
6. Jika NRP ada, backend mencari data mahasiswa di database.
7. Backend melakukan join antara tabel `mahasiswa_baru`, `gugus`, dan `regions`.
8. Jika data ditemukan, backend mengembalikan NRP, nama, gugus, dan region.
9. Jika data tidak ditemukan, backend mengembalikan pesan error.

## Validasi dan Keamanan

Backend menggunakan parameterized query dengan placeholder `?` saat menjalankan query database. Hal ini bertujuan untuk memisahkan query SQL dan input user agar lebih aman dari SQL Injection.

Contoh:

```js
WHERE m.nrp = ?
```

Nilai NRP dimasukkan secara terpisah melalui array parameter, bukan langsung digabungkan ke string SQL.

---
