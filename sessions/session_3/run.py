from app import get_aliquot_sum


if __name__ == "__main__":
    print("-----------------  START OF THE APPLICATION -----------------")

    number_str = input("Enter the number to check: ")
    number = int(number_str)
    print(f"Checking number {number}...")

    aliquot_sum = get_aliquot_sum(number)

    if aliquot_sum == number:
        print(f"{number} is a perfect number")
    elif aliquot_sum < number:
        print(f"{number} is a deficient number")
    else:
        print(f"{number} is an abundant number")
