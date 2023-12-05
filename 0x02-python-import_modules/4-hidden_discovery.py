#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4
    b = dir(hidden_4)
    for a in range(len(b)):
        if (b[a][:2] != "__"):
            print(b[a])
