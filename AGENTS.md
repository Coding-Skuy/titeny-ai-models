# AGENTS.md — titeny-ai-models

Model prediksi Titeny (harga 12x8, panen 6x5, demand H+7/H+30) dengan evaluasi MAPE, backtest 90 hari, model card, dan artefak berversi.

## Sumber kebenaran

Semua requirement bersumber dari [Titeny-TownHall](https://github.com/Coding-Skuy/Titeny-TownHall) versi beku `v1.0.0`. Dilarang menduplikasi requirement di repo kode; requirement berubah = PR di TownHall dulu.

| Dokumen (Titeny-TownHall) | Isi |
|---|---|
| [`platform/versions/v1.0.0/BRD/20-prediksi.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/platform/versions/v1.0.0/BRD/20-prediksi.md) | BR-201..BR-206: harga 12x8, panen 6x5, demand, versi model |
| [`platform/versions/v1.0.0/BRD/30-akurasi-dampak.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/platform/versions/v1.0.0/BRD/30-akurasi-dampak.md) | BR-301..BR-305: target MAPE, adopsi, instrumentasi |
| [`model/10-prediksi-harga.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/model/10-prediksi-harga.md) | Metode 5 langkah harga_v1.0.0 |
| [`model/20-prediksi-panen-demand.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/model/20-prediksi-panen-demand.md) | Metode panen/demand, sinyal, rekomendasi |
| [`metrik/10-akurasi-dan-adopsi.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/metrik/10-akurasi-dan-adopsi.md) | Target MAPE, adopsi, instrumentasi |
| [`platform/versions/v1.0.0/FSD/20-model-data.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/platform/versions/v1.0.0/FSD/20-model-data.md) | Entitas, enum, aturan angka, retensi |
| [`data/10-sumber-data.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/data/10-sumber-data.md) | S1-S10 dan matriks keterlacakan |
| [`platform/versions/v1.0.0/SRS/40-acceptance-criteria.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/platform/versions/v1.0.0/SRS/40-acceptance-criteria.md) | QA-001..QA-004 (QA gate) |
| [`KONTEKS-LINTAS-DIVISI.md`](https://github.com/Coding-Skuy/ChefGenie-TownHall/blob/main/KONTEKS-LINTAS-DIVISI.md) (ChefGenie-TownHall) | Event registry (bagian 3), satuan/ID/uang (bagian 6), metrik lintas-divisi (bagian 7) |
| [`townhall-roadmap.md`](https://github.com/Coding-Skuy/ChefGenie-TownHall/blob/main/townhall-roadmap.md) (ChefGenie-TownHall) | Epic E4 #5, batas blast radius (bagian 2), definisi selesai (bagian 6) |

Rujukan versi: `https://github.com/Coding-Skuy/Titeny-TownHall/tree/main/platform/versions/v1.0.0`.

## Tech stack terkunci

- **Python 3.12.7** untuk training dan evaluasi; pandas 2.2.3, numpy 2.1.3, scikit-learn 1.5.2 (regresi linier saja, tanpa deep learning di v1.0.0), onnx/onnxruntime 1.20.0.
- Wajib: model card, metrik eval, dan versi model (`harga_v1.0.0`, `panen_v1.0.0`, `demand_v1.0.0`) pada setiap output; artefak `koefisien.json`, `residual_p90.json`, `backtest.csv`.
- Serving via API Rust (`titeny-backend-service`); training berjalan terjadwal di server, bukan di desktop analis.
- **Dilarang**: deep learning/sentimen di v1.0.0; menayangkan kandidat tanpa `model_version` eksplisit; koneksi ke DB sumber.

Detail matriks: `versions/v1.0.0/docs/40-TECHSTACK.md`. Batas context: `versions/v1.0.0/docs/60-BLAST-RADIUS.md`.

## Aturan kerja AI

1. Baca `AGENTS.md` ini dan semua ADR di `docs/decisions/` sebelum coding.
2. TDD merah-hijau: tulis test yang gagal dulu; rilis diblokir bila QA gate gagal (QA-001..QA-004, tidak boleh skip test).
3. Kontrak API/event hanya diubah lewat bump versi + catatan di ADR baru; tidak ada `event_type` di luar 11 terkunci tanpa bump versi + dual-read 30 hari.
4. Commit memakai awalan `docs:` / `feat:` / `fix:` dan wajib memperbarui `CHANGELOG.md` repo.
5. Keputusan arsitektur baru = tambah ADR bernomor di `docs/decisions/`; jangan edit ADR lama (immutable, sama seperti aturan versi TownHall).
6. Dilarang menyentuh DB divisi lain: DB per service; Titeny read-only terhadap DB Lumbung, TitipO, dan Pasaree dan hanya menulis ke DB `titeny`.
7. Bahasa artefak: Indonesia; uang integer IDR; waktu ISO-8601 Asia/Jakarta; tanpa data pribadi di Titeny.

## Definisi selesai

Dari [`townhall-roadmap.md` bagian 6](https://github.com/Coding-Skuy/ChefGenie-TownHall/blob/main/townhall-roadmap.md):

- Dokumen versi lengkap (BRD/FRD/FSD/PRD/SRS) + `SNAPSHOT-ROADMAP.md` di TownHall; dokumen beku tidak diedit.
- QA gate berbasis SRS lulus (TDD merah-hijau, QA-001..QA-004); rilis diblokir bila gagal.
- Kontrak API terbit; audit keamanan bersih (JWT audiens `titeny` + DB per service).
- Bukti metrik lintas-divisi (KONTEKS-LINTAS-DIVISI.md bagian 7) tercatat: MAPE harga H+1 <= 8% median / H+7 <= 12%, demand H+7 <= 15%, panen <= 20%, cakupan P10-P90 70-90%.
- CHANGELOG repo dan CHANGELOG versi diperbarui.
