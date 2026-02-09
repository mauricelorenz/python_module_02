#!/usr/bin/env python3

def garden_operations(mode: int, test_str: str, test_dict: dict) -> None:
    """Execute the operations that will raise exceptions.

    Args:
        mode: The exception to be tested
        test_str: The string that leads to an exception
        test_dict: The dict that leads to an exception

    Raises:
        ValueError: If int() gets called on non-numeric value
        ZeroDivisionError: If passed value is zero
        FileNotFoundError: If file does not exist
        KeyError: If passed key does not exist in passed dict
    """
    if mode == 0:
        int(test_str)
    elif mode == 1:
        1 / int(test_str)
    elif mode == 2:
        f = open(test_str, "r")
        f.close()
    elif mode == 3:
        test_dict[test_str]


def test_error_types() -> None:
    """Test and output exceptions."""
    test_dict = {"a": "A", "b": "B", "c": "C"}
    print("\nTesting ValueError...")
    try:
        garden_operations(0, "abc", test_dict)
    except ValueError as e:
        print(f"Caught ValueError: {e}")
    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations(1, "0", test_dict)
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}")
    print("\nTesting FileNotFoundError...")
    try:
        garden_operations(2, "missing.txt", test_dict)
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}")
    print("\nTesting KeyError...")
    try:
        garden_operations(3, "missing_plant", test_dict)
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    print("\nTesting multiple errors together...")
    try:
        garden_operations(0, "abc", test_dict)
    except (ValueError, ZeroDivisionError, FileNotFoundError, KeyError):
        print("Caught an error, but program continues!")


def main() -> None:
    """Run the main program."""
    print("=== Garden Error Types Demo ===")
    test_error_types()
    print("\nAll error types tested successfully!")


if __name__ == "__main__":
    main()
