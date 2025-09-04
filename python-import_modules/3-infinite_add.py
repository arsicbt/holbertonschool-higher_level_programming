#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv, result = sys.argv, 0

    for i in range(1, len(argv)):
        result += int(argv[i])
    print(result)
