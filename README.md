# titeny-ai-models

Model AI **inti** divisi **Titeny (AI Insight)**, org **Coding-Skuy**. Berisi model **prediksi harga** dan **prediksi panen**.

Ekosistem: [Titeny-TownHall](https://github.com/Coding-Skuy/Titeny-TownHall).

## Prasyarat (versi dipin)

- Python 3.12.7
- scikit-learn 1.5.2
- pandas 2.2.3
- numpy 2.1.3
- onnx 1.20.0, onnxruntime 1.20.0

## Cara pakai

```sh
python -m venv .venv
source .venv/bin/activate
pip install -e .
python -m titeny_models.harga --komoditas cabai --hari 7
python -m titeny_models.panen --komoditas padi --hari 30
```

## Struktur

```text
src/titeny_models/harga.py  # regresi harga 7 harian
src/titeny_models/panen.py  # klasifikasi waktu panen
tests/                      # uji cepat
```

Keluaran model dikonsumsi oleh `titeny-backend-service` pada titik `/insight/harga` dan oleh dasbor `titeny-web`.
