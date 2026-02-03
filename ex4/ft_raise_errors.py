#!/usr/bin/env python3

def check_plant_health(plant_name: str, water_level: int,
                       sunlight_hours: int) -> None:
    pass


def test_plant_checks() -> None:
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
