class GardenError(Exception):
    def __init__(self, message: str = "Uknown plant error"):
        super().__init__(message)


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def garden_error_demo_one(value: str) -> None:
    try:
        error_helper(value)
    except PlantError as e:
        print(f"Caught PlantError: {e}")
    except WaterError as e:
        print(f"Caught WaterError: {e}")


def garden_error_demo_two(value: str) -> None:
    try:
        error_helper(value)
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        """ if this except block is placed first,
            only GardenError will be caught """


def error_helper(value: str) -> None:
    if value == 'wilted':
        raise PlantError("Plant is wilted!")
    elif value == 'zero':
        raise WaterError("Not enough water!")


def main() -> None:
    print("Testing WaterError...")
    garden_error_demo_one('zero')
    print("\nTesting PlantError...")
    garden_error_demo_one('wilted')
    print("\nTesting catching all GardenError...")
    garden_error_demo_two('zero')
    garden_error_demo_two('wilted')


main()
