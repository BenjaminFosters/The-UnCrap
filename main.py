from functions import ledger
from functions.safety_check.check_missing import dependencies, path

# Temporary Variables
folder_src = [
    "/mnt/bprd/Shared OS/Misc Codes/Real Project/TheUnCrap/testflight_folder/src/Obsidian Vault",
    "/mnt/bprd/Shared OS/Misc Codes/Real Project/TheUnCrap/testflight_folder/src/KeePass Vault",
]

folder_dst = (
    "/mnt/bprd/Shared OS/Misc Codes/Real Project/TheUnCrap/testflight_folder/dst"
)

# password = "TheUnCrap"
# executable = "7z"


# Safety Check
def safety_check():
    missing_dependencies = dependencies.binary_dependencies(["7z"])
    if missing_dependencies:
        print("Missing dependencies detected:")
        for dependency in missing_dependencies:
            print(f"- {dependency}")
        print("Install your missing system dependencies on your package manager.")
        exit(1)

    missing_folders_src = path.src(folder_src)
    if missing_folders_src:
        print("Missing source folders detected:")
        for folder in missing_folders_src:
            print(f"- {folder}")
        print("Please ensure all source folders exist before proceeding.")
        exit(1)

    if not path.dest(folder_dst):
        print(f"Destination folder does not exist: {folder_dst}")
        print("Please ensure the destination folder exists before proceeding.")
        exit(1)


def ledgering(src_folder: str) -> None:
    ledger.build(src_folder)
    if ledger.compare(src_folder):
        print(f"Ledger files are identical for {src_folder}.")
        ledger.delete_temp(src_folder)
    else:
        print(f"Ledger files differ for {src_folder}.")
        ledger.promote(src_folder)


if __name__ == "__main__":
    safety_check()
    for i_src_folder in folder_src:
        ledgering(i_src_folder)
