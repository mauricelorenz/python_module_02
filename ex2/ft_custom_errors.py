#!/usr/bin/env python3

class GardenError(Exception):
    """General exception type for garden errors."""

    pass


class PlantError(GardenError):
    """Exception type for plant errors that inherits from GardenError."""

    pass


class WaterError(GardenError):
    """Exception type for water errors that inherits from GardenError."""

    pass


def handle_errors() -> None:
    """Raise and catch the custom errors."""
    print("\nTesting PlantError...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    print("\nTesting WaterError...")
    try:
        raise WaterError("Not enough water in the tank!")
    except WaterError as e:
        print(f"Caught WaterError: {e}")
    print("\nTesting catching all garden errors...")
    try:
        raise PlantError("The tomato plant is wilting!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")
    try:
        raise WaterError("Not enough water in the tank!")
    except GardenError as e:
        print(f"Caught a garden error: {e}")


def main() -> None:
    """Run the main program."""
    print("=== Custom Garden Errors Demo ===")
    handle_errors()
    print("\nAll custom error types work correctly!")


if __name__ == "__main__":
    main()
