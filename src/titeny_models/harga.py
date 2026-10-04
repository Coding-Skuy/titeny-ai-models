"""Prediksi harga 7 harian (regresi sederhana, contoh awal)."""
import argparse

def ramal_harga(komoditas: str, hari: int = 7) -> list[int]:
    dasar = {"cabai": 10000, "padi": 8000, "bawang": 12000}.get(komoditas, 9000)
    return [dasar + i * 50 for i in range(hari)]

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--komoditas", default="cabai")
    p.add_argument("--hari", type=int, default=7)
    a = p.parse_args()
    print(ramal_harga(a.komoditas, a.hari))
