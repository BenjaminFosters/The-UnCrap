import csv
from datetime import UTC, datetime
from pathlib import Path

from functions import calc_entropy

TempLedgerName = ".TheUnCrap_Ledger.tmp"
FinLedgerName = ".TheUnCrap_Ledger.csv"


def build(scan_directory: str) -> None:
    """Makes a temporary ledger of all files in the given directory and saves it as a CSV file.

    Args:
        scan_directory (str): The directory to scan for files and build the ledger.
    """
    with Path(f"{scan_directory}/{tempLedgerName}").open("w") as file:
        writer = csv.writer(file)
        writer.writerow(["RelativePath", "Date", "FileSize", "Entropy"])

        for file_path in sorted(Path(scan_directory).rglob("*")):
            if (
                file_path.is_file()
                and file_path.name != tempLedgerName
                and file_path.name != finLedgerName
            ):
                modified = datetime.fromtimestamp(file_path.stat().st_mtime).astimezone(
                    UTC
                )

                writer.writerow(
                    [
                        file_path.relative_to(scan_directory),
                        modified,
                        file_path.stat().st_size,
                        calc_entropy.from_file(str(file_path)),
                    ]
                )


def compare(scan_directory: str) -> bool:
    """Compare new and old ledger

    Args:
        scan_directory (str): The directory to scan for files and compare the ledgers.

    Returns:
        bool: True if the ledgers are identical, False otherwise.
    """
    try:
        with (
            Path(f"{scan_directory}/{tempLedgerName}").open("r") as pending,
            Path(f"{scan_directory}/{finLedgerName}").open("r") as old,
        ):
            return pending.read() == old.read()
    except FileNotFoundError:
        return False


def promote(scan_directory: str) -> None:
    """Promote (replace) old ledger with a new one

    Args:
        scan_directory (str): The directory to scan for files and promote the ledgers.
    """
    Path(f"{scan_directory}/{tempLedgerName}").replace(
        f"{scan_directory}/{finLedgerName}"
    )


def delete_temp(scan_directory: str) -> None:
    """Delete temporary ledger file

    Args:
        scan_directory (str): The directory to scan for files and delete the temporary ledger.
    """
    temp_ledger_path = Path(f"{scan_directory}/{tempLedgerName}")
    if temp_ledger_path.exists():
        temp_ledger_path.unlink()
