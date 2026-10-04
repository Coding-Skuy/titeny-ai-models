> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 60-BLAST-RADIUS — titeny-ai-models

Mengacu: Titeny-TownHall v1.0.0 (https://github.com/Coding-Skuy/Titeny-TownHall/tree/main/versions/v1.0.0).

## Pernyataan read-only

Repo ini tidak menulis ke DB sumber. Model hanya membaca agregat dari DB `titeny` dan menulis artefak versi (`koefisien.json`, `residual_p90.json`, `backtest.csv`) plus baris prediksi ke DB `titeny`. Tidak ada koneksi ke DB Lumbung, TitipO, atau Pasaree.

## Radius Dampak per Perubahan

| Perubahan | Dampak | Batas penahan |
|---|---|---|
| Ambang/kolom fitur | Prediksi 12 × 8 ikut berubah | Backtest 90 hari wajib sebelum naik minor |
| Ganti algoritma | Seluruh papan ikut berubah | Naik mayor + dual-read 30 hari |
| Artefak ONNX | Inferensi server ikut berubah | Uji MAPE per komoditas sebelum rilis |
| Kalibrasi P10–P90 | Rentang dan lencana ikut berubah | Cakupan 70–90 persen dipantau mingguan |

## Larangan Eksplisit

- Dilarang menambah koneksi ke DB sumber.
- Dilarang menaikkan versi model bila ada komoditas memburuk lebih dari 2 poin.
- Dilarang menayangkan kandidat tanpa `model_version` eksplisit.

## Rollback

Setiap rilis menyimpan artefak versi sebelumnya. Rollback berarti mengembalikan `model_version` lama dan memverifikasi satu pasangan komoditas-pasar tampil dengan versi lama.

## Batasan

Batasan dokumen ini: hanya radius repo model. Dampak ingest ada di `titeny-data-pipeline`, dampak tayang ada di `titeny-web`. Insiden DB sumber diteruskan ke pemilik sumber.
