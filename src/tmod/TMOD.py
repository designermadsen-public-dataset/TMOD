from requests \
    import get

from shutil \
    import unpack_archive

from defaults           \
    import              \
    default_temperary,  \
    default_installation


class TMOD:
    def __init__(
        self, 
        installation: str | None = None,
        tmp: str | None = None
    ) -> None:
        self.installation: None | str = installation
        self.tmp_dir: None | str = tmp

    def get_installation(
        self
    ) -> str:
        if self.installation is None:
            self.set_installation(
                default_installation()
            )

        return self.installation
    
    def set_installation(
        self, 
        value: str
    ) -> None:
        self.installation = value
    
    def get_temperary_directory(
        self
    ) -> str:
        if self.tmp_dir is None:
            self.set_temperary_directory(
                default_temperary()
            )

        return self.tmp_dir
    
    def set_temperary_directory(
        self, 
        value: str
    ) -> None:
        self.tmp_dir = value
