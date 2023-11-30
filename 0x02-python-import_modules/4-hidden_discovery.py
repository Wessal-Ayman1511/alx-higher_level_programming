#!/usr/bin/python3
if __name__ == "__main__":
    import hidden_4

    for dirr in dir(hidden_4):
        if dirr[:2] != "__":
            print(dirr)
