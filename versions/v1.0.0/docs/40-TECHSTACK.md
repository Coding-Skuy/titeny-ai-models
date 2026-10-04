> Versi: v1.0.0 | Status: disetujui | Menggantikan: -

# 40-TECHSTACK — titeny-ai-models

Mengacu: Titeny-TownHall v1.0.0 (https://github.com/Coding-Skuy/Titeny-TownHall/tree/main/versions/v1.0.0).

## Konteks TownHall

Stack divisi dikunci di TownHall v1.0.0: web Bun latest + Svelte 5 + SvelteKit Kit 2 + TypeScript latest; analis-desktop KMP Windows; backend Rust axum 0.8.4; model dan pipeline Python 3.12. Repo ini adalah model Python 3.12.

## Stack Repo Ini

| Lapisan | Pilihan | Versi target | STATUS |
|---|---|---|---|
| Bahasa | Python | 3.12 (repo `==3.12.7`) | defined |
| Tabel | pandas | 2.2.3 | defined |
| Angka | numpy | 2.1.3 | defined |
| Regresi | scikit-learn | 1.5.2, linier saja tanpa deep learning | defined |
| Ekspor | onnx + onnxruntime | 1.20.0 / 1.20.0 | defined |
| Uji | pytest (`tests/`) + backtest 90 hari | — | defined |

Metode mengikuti TownHall: baseline musiman-naif + koreksi tren/stok/logistik untuk harga 12 × 8 H+1–H+7; rumus luas × yield × cuaca × musim untuk panen; baseline × hari-besar × elastisitas untuk demand. Artefak: `koefisien.json`, `residual_p90.json`, `backtest.csv` per `harga_v1.0.0`/`panen_v1.0.0`/`demand_v1.0.0`.

## Perintah

```bash
pytest
```

## Batasan

Batasan dokumen ini: hanya stack model. Training tidak berjalan di desktop analis; terjadwal di server. Naik versi model hanya bila syarat backtest TownHall terpenuhi. Repo ini tidak menulis ke DB sumber.
