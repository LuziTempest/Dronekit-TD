# Penugasan Magang Dronekit-TD

| Nama           | NRP        | Prodi     |
| ---            | ---        | ----------|
|...|...|...|

### Link Video Demo (Youtube)
`...`

## Tugas 1
Implementasikan skrip Python menggunakan DroneKit dan Mavlink untuk menyusun misi yang komprehensif (**Takeoff, Waypoint, dan Landing**). 

Skrip harus mampu menghasilkan **empat waypoint** yang membentuk pola cardinal terhadap Homepoint (Utara, Barat, Selatan, dan Timur) dengan radius sejauh **x meter**, di mana nilai x ditentukan melalui input pengguna. 

Misi diakhiri dengan Landing pada titik yang berjarak **100 meter** dari waypoint terakhir.

**Contoh:**
![map2](/img/image.png)

#### Kirim hasil generate Waypoint pada folder `/img`


## Tugas 2

Buat sebuah **website** yang memiliki fungsi-fungsi berikut:

### 1. Form Pengaturan Parameter
- Menyediakan **form untuk mengubah 3 parameter**.
- Setiap parameter pada form **sudah memiliki nilai awal (default value)**.

### 2. Kontrol Vehicle
- Menyediakan tombol untuk:
  - **Arm** vehicle
  - **Disarm** vehicle
- Menyediakan fitur untuk **mengganti mode terbang** antara:
  - **MANUAL**
  - **AUTO**

### 3. Monitoring Parameter
- Website dapat **menampilkan seluruh parameter vehicle** (Tampilkan dalam format json). 

### 4. Pembuatan Waypoint Berdasarkan Jarak
- Menyediakan **form input jarak (dalam meter)** untuk pembuatan waypoint.
- Contoh:
  - Jika user memasukkan nilai **100**, maka sistem akan **membuat misi dengan jarak 100 meter** (sesuai dengan Tugas 1).

### 5. Informasi Penerbangan Saat Misi Berjalan
- Jika vehicle dalam kondisi:
  - Sudah **Arm**
  - Berada pada mode **AUTO**
- Maka website harus menampilkan informasi berikut selama misi berjalan:
  - **Altitude**
  - **Groundspeed**
  - **Airspeed**
  - **Current Mission**

#### Kirim hasil Tampilan Website pada folder `/img` dan demokan tiap-tiap fungsi.

## Modul
https://github.com/LuziTempest/magang-dronekit.git
