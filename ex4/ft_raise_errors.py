#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> str:
    """Check if the passed values are valid.

    Args:
        plant_name: The name of the plant
        water_level: The current water level
        sunlight_hours: The hours of sunlight exposure

    Returns:
        A message that the plant is healthy, if so

    Raises:
        ValueError: If water level or sunlight hours are out of bounds
    """
    if plant_name == "":
        raise ValueError("Plant name cannot be empty!")
    elif water_level < 1:
        raise ValueError(f"Water level {water_level} is too low (min 1)")
    elif water_level > 10:
        raise ValueError(f"Water level {water_level} is too high (max 10)")
    elif sunlight_hours < 2:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         "is too low (min 2)")
    elif sunlight_hours > 12:
        raise ValueError(f"Sunlight hours {sunlight_hours} "
                         "is too high (max 12)")
    return f"Plant '{plant_name}' is healthy!\n"


def test_plant_checks() -> None:
    """Call check_plant_health() with valid and invalid values."""
    test_cases = [("Testing good values...", "tomato", 5, 7),
                  ("Testing empty plant name...", "", 5, 7),
                  ("Testing bad water level...", "tomato", 15, 7),
                  ("Testing bad sunlight hours...", "tomato", 5, 0)]
    for test_case in test_cases:
        try:
            print(test_case[0])
            check_plant_health(*test_case[1:])
            print(f"Plant '{test_case[1]}' is healthy!\n")
        except ValueError as e:
            print(f"Error: {e}\n")


def main() -> None:
    """Run the main program."""
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")


if __name__ == "__main__":
    main()
