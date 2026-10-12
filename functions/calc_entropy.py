def from_file(filepath: str) -> float:
    """Calculate the Shannon-Entropy of a given file.

    Args:
    filepath (str): The path to the file.

    Returns:
    float: The calculated entropy with the value of 0.00 to 8.00 (based on log2(256)).
    """
    from collections import Counter
    import math

    with open(filepath, "rb") as f:
        data = f.read()

    value_counts = Counter(data)
    total_count = len(data)

    entropy = 0.0
    for count in value_counts.values():
        probability = count / total_count
        entropy += probability * math.log2(probability)

    return round(entropy * -1, 2)
