import shutil


def binary_dependencies(dependencies: list[str]) -> list[str]:
    return [
        dependency for dependency in dependencies if shutil.which(dependency) is None
    ]


# def python_dependencies():
