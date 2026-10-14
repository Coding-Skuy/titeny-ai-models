> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 40-TECHSTACK — titeny-ai-models

Mengacu: Titeny-TownHall v1.0.0 (`https://github.com/Coding-Skuy/Titeny-TownHall/tree/main/platform/versions/v1.0.0`). Stack pengikat divisi: [`FSD/30-kontrak.md`](https://github.com/Coding-Skuy/Titeny-TownHall/blob/main/platform/versions/v1.0.0/FSD/30-kontrak.md).

## Konteks TownHall

Stack divisi dikunci di TownHall v1.0.0: web Bun + Svelte 5 + SvelteKit 2 + TypeScript; analis-desktop KMP Windows (Kotlin, Compose Multiplatform, Navigation3); backend Rust Axum 0.8; model dan pipeline Python 3.12. Repo ini: Model prediksi Titeny (harga 12x8, panen 6x5, demand H+7/H+30) dengan evaluasi MAPE, backtest 90 hari, model card, dan artefak berversi.

## Stack Repo Ini

| Lapisan | Pilihan | Versi target | STATUS |
|---|---|---|---|
| Bahasa | Python | 3.12 (repo `==3.12.7`) | defined |
| Tabel | pandas | 2.2.3 | defined |
| Angka | numpy | 2.1.3 | defined |
| Regresi | scikit-learn (linier saja) | 1.5.2 | defined |
| Ekspor | onnx + onnxruntime | 1.20.0 / 1.20.0 | defined |
| Uji | pytest (`tests/`) + backtest 90 hari | - | defined |
| Artefak | `koefisien.json`, `residual_p90.json`, `backtest.csv` per versi | harga_v1.0.0, panen_v1.0.0, demand_v1.0.0 | defined |
| Dokumentasi model | Model card + metrik eval | wajib tiap versi | defined |

## Perintah

```bash
pytest
```

## Target Akurasi yang Dikunci

| Model | Metrik | Target v1.0.0 |
|---|---|---|
| Harga H+1 | MAPE per komoditas-pasar | <= 8% median 12 komoditas; tidak ada komoditas > 15% |
| Harga H+7 | MAPE | <= 12%; memburuk > 2 poin pada 1 komoditas = tolak rilis |
| Demand H+7 / H+30 | MAPE per zona | <= 15% / <= 22% (H+30 hanya pantau) |
| Panen per musim | MAPE total musim | <= 20% |
| Rentang P10-P90 | Cakupan aktual | 70-90%; < 60% = kalibrasi ulang |

Cakupan: harga 12 komoditas x 8 pasar H+1-H+7; panen 6 komoditas x 5 kabupaten (Karawang, Subang, Garut, Brebes, Malang) M+1-M+4; demand 12 komoditas x 8 zona + 8 pasar. Naik versi hanya bila backtest 90 hari menunjukkan MAPE H+7 turun >= 0,5 poin dan tidak ada komoditas memburuk > 2 poin.

## Batasan

Dokumen ini hanya mengatur stack repo `titeny-ai-models`. Perubahan versi pustaka atau stack dicatat sebagai ADR baru di `docs/decisions/` dan dilaporkan ke TownHall. Titeny read-only terhadap DB sumber; satu-satunya basis tulis adalah DB `titeny`.
