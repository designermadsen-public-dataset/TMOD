from os \
    import listdir

from os.path    \
    import      \
        isfile, \
        join


def is_downloaded(
    sample_size: str, 
    temperary_dir: str
) -> bool:
    found_files_and_dirs = listdir(
        temperary_dir
    )
    
    for file_or_dir in found_files_and_dirs:
        full_path = join(
            temperary_dir, 
            file_or_dir
        )
        
        if isfile(
            full_path
        ):
            file = file_or_dir.split('.')
            if sample_size == file[0]:
                return True

    return False