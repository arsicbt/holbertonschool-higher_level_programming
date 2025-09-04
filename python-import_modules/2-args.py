#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv
    argc = len(argv) - 1

    if argc <= 1:
        print(
                "0 arguments."
                if argc == 0
                else "{} argument:\n{}: {}".format(argc, 1, argv[1])
            )
    else:
        print("{} arguments:\n{}: {}".format(argc, 1, argv[1]))

    for i in range(2, len(argv)):
        print("{}: {}".format(i, argv[i]))
        i += 1
