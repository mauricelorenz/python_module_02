#!/usr/bin/env python3

def garden_operations(test_str: str) -> None:
    try:
        pass
    except ValueError as e:
        print(f"Caught ValueError: {e}")


def test_error_types() -> None:
    garden_operations("abc")


def main() -> None:
    """Run the main program."""
    test_error_types()


if __name__ == "__main__":
    main()
