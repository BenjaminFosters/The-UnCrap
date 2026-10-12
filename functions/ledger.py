from pathlib import Path
from datetime import datetime, timezone
import csv
from entropy import calc_entropy_from_file


def build(directory: str, ledger_path: str) -> None:
    """Builds a CSV-based Ledger with the format "RelativePath;Date;FileSize;Entropy" for all files in given directory.

    Args:
        directory (str): The path to the directory.
        ledger_path (str): The path to the ledger file. (Ended with CSV)

    Raises:
        ValueError: If the ledgerPath does not end with ".csv".
    """
    if ledger_path.split(".")[-1] != "csv":
        raise ValueError("Ledger file must be a CSV file.")

    with Path(ledger_path).open("w") as file:
        writer = csv.writer(file)
        writer.writerow(["RelativePath", "Date", "FileSize", "Entropy"])

        for file_path in sorted(Path(directory).rglob("*")):
            if file_path.is_file() and file_path != Path(ledger_path):
                modified = datetime.fromtimestamp(file_path.stat().st_mtime).astimezone(
                    timezone.utc
                )

                writer.writerow(
                    [
                        file_path.relative_to(directory),
                        modified,
                        file_path.stat().st_size,
                        calc_entropy_from_file(str(file_path)),
                    ]
                )


def compare(old: str, new: str) -> bool:
    """Compares two ledger files to check if they are identical.

    Args:
        old (str): The path to the old ledger file.
        new (str): The path to the new ledger file.

    Raises:
        e: Exception: If there is an error reading the files.

    Returns:
        bool: True if the files are identical, False otherwise.
    """
    try:
        with open(old, "r") as file1, open(new, "r") as file2:
            return file1.read() == file2.read()
    except FileNotFoundError:
        return False


def promote(old: str, new: str) -> None:
    """Promotes the new ledger to replace the old ledger.

    Args:
        old (str): The path to the old ledger file.
        new (str): The path to the new ledger file.

    Returns:
    None
    """
    Path(new).replace(old)
