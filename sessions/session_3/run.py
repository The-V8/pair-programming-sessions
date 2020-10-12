from app import get_aliquot_sum


if __name__ == "__main__":
    print("-----------------  START OF THE APPLICATION -----------------")

    number = input("Enter the number to check: ")
    print(f"Checking number {number}...")

    # TODO: Check, if the current number is perfect, abundant or deficient
    print(get_aliquot_sum(number))
