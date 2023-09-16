from requests \
    import get

from shutil \
    import unpack_archive


class TMOD:
    def __init__(
        self, 
        installation: str | None = None
    ) -> None:
        self.installation: None | str = installation
        

    def get_installation(
        self
    ) -> str:
        return self.installation
    
    def set_installation(
        self, 
        value: str
    ) -> None:
        self.installation = value
    