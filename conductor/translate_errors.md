# Plan: Melokalkan Pesan Error ke Bahasa Indonesia (MyPyro)

Tujuan dari rencana ini adalah untuk menerjemahkan pesan error RPC yang masih berbahasa Inggris ke dalam bahasa Indonesia di seluruh file `.tsv` dalam folder `compiler/errors/source/`. Ini akan memastikan bahwa pengguna Synchro Userbot menerima pesan kesalahan yang konsisten dan mudah dipahami dalam bahasa lokal.

## Komponen Utama
- **Files**: `.tsv` files di `compiler/errors/source/`.
- **Format**: File dipisahkan oleh Tab (`id\tmessage`).
- **Target**: Menerjemahkan pesan Inggris yang tersisa dan memperbaiki beberapa terjemahan yang kurang pas.

## Langkah-langkah Implementasi

### 1. Update 401_UNAUTHORIZED.tsv
Menerjemahkan pesan status unauthorized.
- `ACTIVE_USER_REQUIRED`: "Metode ini hanya tersedia untuk pengguna yang sudah aktif"
- `AUTH_KEY_INVALID`: "Key tidak valid"
- `AUTH_KEY_PERM_EMPTY`: "Metode tidak tersedia untuk kunci otorisasi sementara"

### 2. Update 403_FORBIDDEN.tsv
Menerjemahkan pesan akses ditolak.
- `EDIT_BOT_INVITE_FORBIDDEN`: "Tautan undangan chat bot tidak dapat diedit"
- `INLINE_BOT_REQUIRED`: "Aksi ini harus dilakukan melalui callback bot inline"
- `POLL_VOTE_REQUIRED`: "Berikan suara pada jajak pendapat sebelum memanggil metode ini"
- `SENSITIVE_CHANGE_FORBIDDEN`: "Pengaturan konten sensitif tidak dapat diubah saat ini"
- `TAKEOUT_REQUIRED`: "Metode harus dipanggil di dalam sesi takeout"
- `USER_BOT_INVALID`: "Metode ini hanya dapat dipanggil oleh bot"
- `USER_PRIVACY_RESTRICTED`: "Pengaturan privasi pengguna mencegah Anda melakukan tindakan ini"
- `LIVE_DISABLED`: "Fitur Live dinonaktifkan dari sisi server"

### 3. Update 420_FLOOD.tsv
Menerjemahkan pesan flood/limit.
- `2FA_CONFIRM_WAIT_X`: "Tunggu selama {value} detik karena akun ini aktif dan dilindungi password 2FA"
- `TAKEOUT_INIT_DELAY_X`: "Konfirmasi permintaan ekspor data di perangkat seluler atau tunggu {value} detik"

### 4. Batch Update 400_BAD_REQUEST.tsv (Sebagian)
Karena file ini sangat besar, saya akan fokus pada pesan-pesan umum yang sering muncul:
- `ACCESS_TOKEN_EXPIRED`: "Token bot telah kedaluwarsa"
- `ACCESS_TOKEN_INVALID`: "Token akses bot tidak valid"
- `ALBUM_PHOTOS_TOO_MANY`: "Terlalu banyak foto dalam album"
- `API_ID_INVALID`: "Kombinasi api_id/api_hash tidak valid"
- `BOT_METHOD_INVALID`: "Metode ini tidak dapat digunakan oleh bot"
- `MSG_WAIT_FAILED`: "Pesan gagal dikirim atau sedang menunggu"
- Dan pesan lainnya yang masih berbahasa Inggris.

### 5. Kompilasi Ulang
Setelah semua file `.tsv` diperbarui, jalankan perintah kompilasi:
```bash
make api
```

## Verifikasi
1. Periksa file yang dihasilkan di `pyrogram/errors/exceptions/`.
2. Pastikan file `all.py` mencakup semua perubahan.
3. Jalankan `pytest` untuk memastikan tidak ada error sintaksis pada file yang baru dihasilkan.
