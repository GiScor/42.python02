def garden_operations(operation_number: int) -> int:
    if operation_number == 0:
        i = int('abc')
    elif operation_number == 1:
        i = 1 / 0
    elif operation_number == 2:
        open("nonexistent.mkv")
    elif operation_number == 3:
        i = 1 + 'abc'
    else:
        i = 1
    return i


def test_error_types() -> None:
    for i in range(0, 5):
        print(f"Testing operation {i}")
        try:
            garden_operations(i)
            print("Operation successfull")
        except Exception as e:
            print(f"Caught {e.__class__.__name__}: {e}\n")

    print("\nAll error types tested with no crashes!")


def main() -> None:
    test_error_types()


main()
