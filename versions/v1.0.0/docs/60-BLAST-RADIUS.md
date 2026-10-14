> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 60-BLAST-RADIUS — titeny-ai-models

Mengacu: Titeny-TownHall v1.0.0 (`https://github.com/Coding-Skuy/Titeny-TownHall/tree/main/platform/versions/v1.0.0`), [`townhall-roadmap.md` bagian 2](https://github.com/Coding-Skuy/ChefGenie-TownHall/blob/main/townhall-roadmap.md) (baris Titeny: point of concern "11 event; MAPE H+1 <= 8%"; batas context "12 komoditas x 8 pasar; read-only ke DB sumber") dan [`KONTEKS-LINTAS-DIVISI.md` bagian 8-9](https://github.com/Coding-Skuy/ChefGenie-TownHall/blob/main/KONTEKS-LINTAS-DIVISI.md).

## Pernyataan read-only

Repo ini tidak menulis ke DB sumber. Titeny hanya membaca dari Lumbung, TitipO, dan Pasaree (lewat event/konektor SELECT); satu-satunya basis tulis adalah DB `titeny`.

## Yang BOLEH disentuh repo ini

Kode training/evaluasi, fitur, artefak berversi, model card, backtest; membaca agregat dari DB `titeny` (read) dan menulis baris prediksi ke DB `titeny` lewat jalur yang disepakati dengan backend.

## Yang DILARANG

- Koneksi ke DB Lumbung, TitipO, atau Pasaree.
- Menaikkan versi model bila ada komoditas memburuk > 2 poin atau MAPE H+7 tidak turun >= 0,5 poin.
- Menayangkan kandidat tanpa `model_version`; memakai fitur teks bebas/sentimen media sosial.
- Mengubah kontrak output tanpa ADR baru dan bump versi.

## Kontrak

- **Dikonsumsi**: Agregat dari event 11 terkunci yang sudah tersimpan di DB `titeny` (S1-S10 via pipeline); kontrak output `FSD/20-model-data.md`.
- **Diproduksi**: Baris prediksi `prediksi_harga`, `prediksi_panen`, `prediksi_demand` dengan `model_version`; artefak versi; skor MAPE mingguan (Minggu 23.00 WIB).
- Modul bersama `:shared:pantry-resep` adalah milik Pawonee dan tidak dipakai atau diubah oleh Titeny. `pedaree.stok.v1` adalah kontrak bilateral Pedaree-TitipO dan bukan bagian registry Titeny (11 event terkunci).

## Radius Dampak per Perubahan

| Perubahan | Dampak | Batas penahan |
|---|---|---|
| Ambang/kolom fitur | Prediksi 12 × 8 ikut berubah | Backtest 90 hari wajib sebelum naik minor |
| Ganti algoritma | Seluruh papan ikut berubah | Naik mayor + dual-read 30 hari |
| Artefak ONNX | Inferensi server ikut berubah | Uji MAPE per komoditas sebelum rilis |
| Kalibrasi P10–P90 | Rentang dan lencana ikut berubah | Cakupan 70–90 persen dipantau mingguan |

## Rollback

Setiap rilis menyimpan artefak versi sebelumnya. Rollback berarti mengembalikan `model_version` lama dan memverifikasi satu pasangan komoditas-pasar tampil dengan versi lama.

## Batasan

Dokumen ini hanya mengatur radius repo `titeny-ai-models`. Dampak repo lain ada di dokumen blast-radius repo tersebut. Insiden DB sumber diteruskan ke pemilik sumber.
