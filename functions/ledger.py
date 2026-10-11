from pathlib import Path
from datetime import datetime, timezone
import csv
from entropy import calc_entropy_from_file


def buildLedger(directory: str, ledgerPath: str) -> None:
    """Builds a CSV-based Ledger with the format "RelativePath;Date;FileSize;Entropy" for all files in given directory.

    Args:
        directory (str): The path to the directory.
        ledgerPath (str): The path to the ledger file. (Ended with CSV)

    Raises:
        ValueError: If the ledgerPath does not end with ".csv".
    """
    if ledgerPath.split(".")[-1] != "csv":
        raise ValueError("Ledger file must be a CSV file.")

    with Path(ledgerPath).open("w") as file:
        writer = csv.writer(file)
        writer.writerow(["RelativePath", "Date", "FileSize", "Entropy"])

        for file_path in sorted(Path(directory).rglob("*")):
            if file_path.is_file() and file_path != Path(ledgerPath):
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


def compareLedger(oldLedger: str, newLedger: str) -> bool:
    """Compares two ledger files to check if they are identical.

    Args:
        oldLedger (str): The path to the old ledger file.
        newLedger (str): The path to the new ledger file.

    Raises:
        e: Exception: If there is an error reading the files.

    Returns:
        bool: True if the files are identical, False otherwise.
    """

    try:
        with open(oldLedger, "r") as file1, open(newLedger, "r") as file2:
            return file1.read() == file2.read()
    except FileNotFoundError:
        return False


def promoteLedger(oldLedger: str, newLedger: str) -> None:
    """Promotes the new ledger to replace the old ledger.

    Args:
    oldLedger (str): The path to the old ledger file.
    newLedger (str): The path to the new ledger file.

    Returns:
    None
    """

    Path(newLedger).replace(oldLedger)
