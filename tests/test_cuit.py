from fastapi.testclient import TestClient

from cuit import cuit_checksum_valido, normalizar_cuit

def test_invalid_input():
    assert normalizar_cuit(None) is None
    assert normalizar_cuit(True) is None

def test_invalid_float():
    assert normalizar_cuit("123456780.5") is None

def test_missing_digits():
    assert normalizar_cuit("1234567890") is None

def test_extra_digits():
    assert normalizar_cuit("123456789012") is None

def test_non_digit_characters():
    assert normalizar_cuit("1234567890a") is None

def test_unicode_digits():
    assert normalizar_cuit("2038927340７") is None  # ７ ancho completo  (U+FF17)
    assert normalizar_cuit("2038927340٧") is None  # ٧ arábigo          (U+0667)
    assert normalizar_cuit("2038927340⁷") is None  # ⁷ superíndice      (U+2077)

def test_valid_cuit():
    assert normalizar_cuit("20389273407") == "20389273407"
    assert normalizar_cuit(20389273407) == "20389273407"
    assert normalizar_cuit(20389273407.0) == "20389273407"
    assert normalizar_cuit(" 20389273407 ") == "20389273407"

def test_checksum_valid():
    assert cuit_checksum_valido("20389273407") is True

def test_checksum_invalid(): 
    assert cuit_checksum_valido("20389273408") is False


