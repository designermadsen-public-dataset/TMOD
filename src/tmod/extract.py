from shutil     \
    import unpack_archive

from os         \
    import listdir

from os.path    \
    import      \
    isfile,     \
    join


def is_sample(
    sample_name: str,
    filename: str
):
    file = filename.split('.')
    return file[0] == sample_name


def extract(
    sample_name: str,
    temporary_location: str,
    to_directory: str
) -> None:
    for file_or_dir in listdir(
        temporary_location
    ):
        full_path = join(
            temporary_location,
            file_or_dir
        )

        if isfile(
            full_path
        ):
            if is_sample(
                sample_name,
                file_or_dir
            ):
                unpack_archive(
                    full_path,
                    to_directory
                )

            return None
