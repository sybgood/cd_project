#!/usr/bin/env python3


import os


def main():
    while True:
        var = input("> ")
        if var == "pwd":  # For command pwd
            print(os.getcwd())
        elif var == "ls":  # Ls
            dirs = os.listdir(os.getcwd())
            for file in dirs:
                if file[0] != ".":
                    print(file)
        elif (len(var) > 3) and var[:2] == "cd" and var[2] == " ":  # Cd
            try:
                os.chdir(var[3::])
            except FileNotFoundError:
                print("cd : %s: No such file or directory" % var[3::])
        elif var == "end":
            break
        else:
            print("%s: command not find" % var)


if __name__ == "__main__":
    main()
