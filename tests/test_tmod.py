from src.tmod \
    import TMOD


def test_tmod() -> None:
    tmod = TMOD()

    version_to_download = '1000'

    tmod.download(
        version_to_download
    )

    tmod.install(
        version_to_download
    )

    assert True

