#!/usr/bin/env python3

def water_plants(plant_list: list) -> None:
    """Water the plants passed as list.

    Args:
        plant_list: the plants to water
    """
    error_occured = 0
    print("Opening watering system")
    try:
        for plant in plant_list:
            if plant is None:
                raise Exception
            print(f"Watering {plant}")
    except Exception:
        print(f"Error: Cannot water {plant} - invalid plant!")
        error_occured = 1
    finally:
        print("Closing watering system (cleanup)")
    if not error_occured:
        print("Watering completed successfully!")


def test_watering_system() -> None:
    """Call water_plants() with a valid and an invalid list."""
    print("Testing normal watering...")
    water_plants(["tomato", "lettuce", "carrots"])
    print("\nTesting with error...")
    water_plants(["tomato", None, "carrots"])


def main() -> None:
    """Run the main program."""
    print("=== Garden Watering System ===\n")
    test_watering_system()
    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    main()
