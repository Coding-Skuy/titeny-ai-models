from titeny_models.harga import ramal_harga
from titeny_models.panen import ramal_panen

def test_harga():
    assert ramal_harga("cabai", 7) == [10000, 10050, 10100, 10150, 10200, 10250, 10300]

def test_panen():
    assert ramal_panen("padi")["siap_dalam_hari"] == 12
