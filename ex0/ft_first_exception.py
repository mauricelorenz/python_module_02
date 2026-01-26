#!/usr/bin/env python3

def check_temperature(temp_str: str) -> int | None:
    """Check if temperature is a valid integer and suitable for plants.

    Args:
        temp_str: The temperature string

    Returns:
        The temperature on success, else None
    """
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number\n")
        return None
    if temp < 0:
        print(f"Error: {temp}°C is too cold for plants (min 0°C)\n")
        return None
    if temp > 40:
        print(f"Error: {temp}°C is too hot for plants (max 40°C)\n")
        return None
    print(f"Temperature {temp}°C is perfect for plants!\n")
    return temp


def test_temperature_input() -> None:
    """Call check_temperature() with test values."""
    check_temperature("25")
    check_temperature("abc")
    check_temperature("100")
    check_temperature("-50")


def main() -> None:
    """Run the main program."""
    print("=== Garden Temperature Checker ===\n")
    test_temperature_input()
    print("All tests completed - program didn't crash!")


if __name__ == "__main__":
    main()
