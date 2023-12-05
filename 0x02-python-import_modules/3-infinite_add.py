#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argc = len(sys.argv)
    argv = sys.argv
    b = 0

    for a in range(1, argc):
        b = b + int(argv[a])

    print(b)
