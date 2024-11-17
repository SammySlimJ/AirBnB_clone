# AirBnB_clone
This is a team project for the AirBnB-clone that I am doing solo, hence the Author is just me and I go by the name Samantha Salimu.

# Command Line Interpreter Project

This project implements a simple command-line interpreter that emulates a shell environment. It allows users to execute commands, manage files, and interact with the operating system in a structured and controlled way.

The interpreter supports built-in commands and can execute external programs, making it a foundational tool for understanding systems programming and shell behavior.

## Command Interpreter Overview

The command interpreter functions as a minimalist shell that reads commands from the user, parses them, and executes them. It supports:

- Running built-in commands (e.g., `cd`, `exit`, `env`).
- Executing external programs by searching the `$PATH`.
- Redirection and basic piping.
- Interactive and non-interactive modes.

### Features
1. **Interactive Mode**: Accepts commands in real-time from the user.
2. **Non-Interactive Mode**: Processes commands from a script or file.
3. **Error Handling**: Provides meaningful feedback for invalid commands or errors.

## How to Start the Command Interpreter
1. Clone the repository:
```bash
   git clone https://github.com/SammySlimJ//command-interpreter.git
2. Navigate to the project directory:
cd command-interpreter
3. Compile the program
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 *.c -o hsh
4. Run the interpreter:
./hsh


