#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    """Check if the passed values are valid.

    Args:
        plant_name: The name of the plant
        water_level: The current water level
        sunlight_hours: The time of sunlight exposure in hours
    """
    try:
        if plant_name == "":
            raise ValueError("Plant name cannot be empty!")
        elif water_level < 1 or water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        elif sunlight_hours < 2 or sunlight_hours > 12:
            raise ValueError(f"Sunlight hours {sunlight_hours} "
                             "is too low (min 2)")
    except ValueError as e:
        print(f"Error: {e}\n")
        return
    print(f"Plant '{plant_name}' is healthy!\n")


def test_plant_checks() -> None:
    """Call check_plant_health() with valid and invalid values."""
    print("Testing good values...")
    check_plant_health("tomato", 5, 7)
    print("Testing empty plant name...")
    check_plant_health("", 5, 7)
    print("Testing bad water level...")
    check_plant_health("tomato", 15, 7)
    print("Testing bad sunlight hours...")
    check_plant_health("tomato", 5, 0)


def main() -> None:
    """Run the main program."""
    print("=== Garden Plant Health Checker ===\n")
    test_plant_checks()
    print("All error raising tests completed!")


if __name__ == "__main__":
    main()
