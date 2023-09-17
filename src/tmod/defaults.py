from tempfile \
    import TemporaryDirectory

from os.path    \
    import      \
    isdir,      \
    join,       \
    expanduser

from os \
    import mkdir

temporary_file: TemporaryDirectory | None = None
installation_for_os: str | None = None


def default_temporary() -> str:
    global temporary_file
    temporary_file = TemporaryDirectory()
    return temporary_file.name


def validation_of_path() -> None:
    global installation_for_os

    if not isdir(
        installation_for_os
    ):
        mkdir(
            installation_for_os
        )


def setup_default_for_os() -> None:
    global installation_for_os

    installation_for_os = expanduser('~')
    installation_for_os = join(
        installation_for_os, 
        '.dataset'
    )

    if not isdir(installation_for_os):
        mkdir(installation_for_os)

    installation_for_os = join(
        installation_for_os, 
        'TMOD'
    )
    
    if not isdir(installation_for_os):
        mkdir(installation_for_os)


def default_installation() -> str:
    global installation_for_os
    setup_default_for_os()
    return installation_for_os
