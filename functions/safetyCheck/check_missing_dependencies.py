import shutil


def binary_dependencies(dependencies: list[str]) -> list[str]:
    """Returns all missing system dependencies from $PATH in Linux

    Args:
        dependencies (list[str]): Dependencies to check for in the system $PATH

    Returns:
        list[str]: All missing system dependencies
    """
    return [
        dependency for dependency in dependencies if shutil.which(dependency) is None
    ]
