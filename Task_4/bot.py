from commands import process_command

def main():
    print("Welcome to the assistant bot!")
    while True:
        command = input("Enter a command: ").strip().lower()

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        cmd, *args = command.split(maxsplit=1)
        args = args[0] if args else ""

        if cmd in ["add", "change", "phone"] and not args:
            print("Enter the argument for the command")
            continue

        print(process_command(f"{cmd} {args}"))

if __name__ == "__main__":
    main()
