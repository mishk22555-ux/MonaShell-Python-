from enum import Enum
import subprocess

# Greeting
print("Welcome to MonaShell\n")
name = input("Enter username: ")
comp_name = input("Enter computer name: ")

# Available commands
class Command(Enum):
    HELP = "help"
    ECHO = "echo"
    CLEAR = "clear"
    PWD = "pwd"
    LS = "ls"
    LSLA = "ls -la"
    LSLAH = "ls -lah"
    MAN = "man"
    HEAD = "head"
    CAT = "cat"
    EXIT = "exit"

print("\nEnter help to show available commands\n")

# Infinite loop
while True:
    # Try to execute code
    try:
        user_input = input(f"{name}@{comp_name} ~ $ ")
        parts = user_input.split(" ", 1)

        if parts[0] == "ls" and len(parts) > 1:
            command = Command(f"ls {parts[1]}")
        else:
            command = Command(parts[0])

    # Value error
    except ValueError as ve:
        print("Error: ValueError. Unknown command")
        print(ve)
        continue

    # Program interruption error
    except KeyboardInterrupt as ke:
        print("\nError: KeyboardInterrupt. Exit using the exit command")
        print(ke)
        continue

    # Input terminated
    except EOFError:
        print("Input terminated")
        break

    # Just in case
    except Exception as e:
        print("Error")
        print(e)
        continue

    # `help` command
    if command == Command.HELP:
        print("Available commands:")
        print("\n1. help - show available commands")
        print("2. echo - print the given text to the terminal")
        print("3. clear - clear the terminal")
        print("4. pwd - current directory")
        print("5. ls - list files/directories")
        print("6. ls -la - list files/directories with detailed information")
        print("7. ls -lah - list all files/directories with detailed human-readable information")
        print("8. man - show the manual for a command")
        print("9. head - show the first lines of a file")
        print("10. cat - show the contents of a file")
        print("11. exit - exit the program\n")

    # `echo` command
    elif command == Command.ECHO:
        if len(parts) > 1:
            subprocess.run(["bash", "commands/echo.sh", parts[1]])
        else:
            print("Error: no text specified for echo")

    # `clear` command
    elif command == Command.CLEAR:
        subprocess.run(["bash", "commands/clear.sh"])

    # `pwd` command
    elif command == Command.PWD:
        subprocess.run(["bash", "commands/pwd.sh"])

    # `ls` command
    elif command == Command.LS:
        subprocess.run(["bash", "commands/ls.sh"])

    # `ls -la` command
    elif command == Command.LSLA:
        subprocess.run(["bash", "commands/ls-la.sh"])

    # `ls -lah` command
    elif command == Command.LSLAH:
        subprocess.run(["bash", "commands/ls-lah.sh"])

    # `man` command
    elif command == Command.MAN:
        if len(parts) > 1:
            subprocess.run(["bash", "commands/man.sh", parts[1]])
        else:
            print("Error: no command specified for man")

    # `head` command
    elif command == Command.HEAD:
        if len(parts) > 1:
            subprocess.run(["bash", "commands/head.sh", parts[1]])
        else:
            print("Error: no file specified for head")

    # `cat` command
    elif command == Command.CAT:
        if len(parts) > 1:
            subprocess.run(["bash", "commands/cat.sh", parts[1]])
        else:
            print("Error: no file specified for cat")

    # `exit` command
    elif command == Command.EXIT:
        break
