from pathlib import Path


def src(folders_src: list[str]) -> list[str]:
    """Returns all missing source folders from given list of source folders

    Args:
        folders_src (list[str]): List of folders absolute path to check for existence

    Returns:
        list[str]: List of all missing source folders from given list of source folders
    """
    return [folder for folder in folders_src if not Path(folder).exists()]


def dest(folder_dst: str) -> bool:
    """Checks for existance of a specified destination path

    Args:
        folder_dst (str): Absolute path to destination folder to check for existence

    Returns:
        bool: True if exists, False otherwise.
    """
    return Path(folder_dst).exists()
