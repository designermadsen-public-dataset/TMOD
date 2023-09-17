from src.tmod \
    import TMOD


def test_tmod() -> None:
    tmod = TMOD()
    
    tmod.download('1000')

    assert True

