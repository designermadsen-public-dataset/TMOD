from shutil \
    import unpack_archive

from src.tmod.defaults      \
    import                  \
    default_temperary,      \
    default_installation

from urllib.request \
    import urlretrieve

from src.tmod.providers         \
    import retrieve_providers

from src.tmod.state \
    import is_downloaded

from os.path \
    import join

def get_label_versions() -> str:
    return 'versions'

def get_label_current_version() -> str:
    return '1.0.0'

def get_label_samples() -> str:
    return 'samples'


class TMOD:
    def __init__(
        self, 
        installation: str | None = None,
        tmp: str | None = None
    ) -> None:
        self.providers = retrieve_providers()
        self.installation: None | str = installation
        self.tmp_dir: None | str = tmp

    def download(
        self,
        sample: str
    ) -> None:
        if is_downloaded(
            sample, 
            self.tmp_dir
        ):
            raise IOError('is already present')
        
        self.__download_to_tmp(
            sample
        )

    def get_provider(
        self, 
        sample: str
    ):
        return self.providers[
            get_label_versions()
        ][
            get_label_current_version()
        ][
            get_label_samples()
        ][sample][0]

    def __download_to_tmp(
        self, 
        sample: str
    ) -> None:
        file_name = sample + '.zip'
        
        full_path = join(
            self.get_temperary_directory(), 
            file_name
        )

        response = urlretrieve(
            self.get_provider(sample), 
            full_path
        )
    
    def install(
        self,
        sample: str
    ) -> None:
        pass

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
