def display_menu():
    print("=============================")
    print("      SIMPLE CALCULATOR")
    print("=============================")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Exit")
    print("=============================")

def main():
    while True:
        # Tampilkan menu
        display_menu()

        # Dapatkan pilihan dari pengguna
        choice = int(input("Enter your choice (1-5): "))

        if choice == 5:
            print("Thank you for using this calculator. Goodbye!")
            break

        # Dapatkan nilai dari pengguna
        value1 = float(input("Enter value 1: "))
        value2 = float(input("Enter value 2: "))

        # Lakukan operasi yang dipilih
        if choice == 1:
            result = value1 + value2
            operation = "+"
        elif choice == 2:
            result = value1 - value2
            operation = "-"
        elif choice == 3:
            result = value1 * value2
            operation = "*"
        elif choice == 4:
            if value2 != 0:
                result = value1 / value2
                operation = "/"
            else:
                print("Error: Division by zero is not allowed.")
                continue
        else:
            print("Invalid choice. Please try again.")
            continue

        # Tampilkan hasil
        print(f"RESULT: {value1} {operation} {value2} = {result}\n")

if __name__ == "__main__":
    main()
