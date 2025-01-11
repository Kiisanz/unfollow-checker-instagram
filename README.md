# Unfollow Tracker

Unfollow Tracker adalah aplikasi sederhana yang membantu pengguna Instagram melacak akun yang telah di-unfollow oleh mereka. Aplikasi ini memanfaatkan data JSON untuk menganalisis hubungan antara pengikut dan akun yang diikuti.

## Fitur

- Membaca data pengikut dari file JSON.
- Membaca data yang diikuti dari file JSON.
- Mengidentifikasi akun yang telah unfollow dan menampilkan URL profil mereka.

## Prasyarat

Sebelum menjalankan aplikasi ini, pastikan Anda telah menginstal Python dan memiliki akses ke data JSON yang diperlukan. Anda perlu memiliki dua file JSON berikut:

1\. `followers_1.json`: berisi data pengikut Anda.
2\. `following.json`: berisi data akun yang Anda ikuti.

### Struktur File JSON

**followers_1.json**

```json\
[
    {
        "string_list_data": [
            {"value": "username1"},
            {"value": "username2"}
        ]
    }
]
```

**following.json**

```json\
{
    "relationships_following": [
        {
            "string_list_data": [
                {"value": "username3"},
                {"value": "username4"}
            ]
        }
    ]
}
```

## Instalasi

1\. Clone repository ini ke mesin lokal Anda.
   `   git clone https://github.com/Kiisanz/november-nonstop-ngding/tree/development/unfollow_checker
  `

2\. Navigasi ke direktori proyek.
   `   cd unfollow_checker
  `

3\. Pastikan Anda memiliki file `followers_1.json` dan `following.json` dalam folder `./data/`.

## Cara Menggunakan

1\. Jalankan skrip Python:
   `   python main.py
  `

2\. Aplikasi akan menampilkan daftar akun yang telah di-unfollow dengan format URL Instagram.

## Contoh Keluaran

```plaintext\
https://www.instagram.com/username3
https://www.instagram.com/username4
```

## Penjelasan Kode

- **Membaca Data**: Skrip memuat data pengikut dan yang diikuti dari file JSON yang ditentukan.
- **Menganalisis Hubungan**: Aplikasi kemudian membandingkan dua daftar untuk menemukan akun yang tidak lagi mengikuti pengguna.
- **Menampilkan Hasil**: Akun yang telah di-unfollow akan dicetak dalam format URL.

## Kontribusi

Jika Anda ingin berkontribusi pada proyek ini, silakan ajukan pull request atau buka issue untuk berdiskusi.
