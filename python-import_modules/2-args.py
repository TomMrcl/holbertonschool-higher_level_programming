#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    argv = sys.argv[1:]
    count = len(argv)

    if count == 0:
        print("0 arguments.")
    else:
        # argument / arguments
        word = "argument" if count == 1 else "arguments"
        print(f"{count} {word}:")

        # Print each argument with its index starting at 1
        for i, arg in enumerate(argv, start=1):
            print(f"{i}: {arg}")
