#!/usr/bin/env python3

# Created by: Khang Le
# Created on: Sep 2019
# This program does some calculation


def main():
    gia_tri_vong_lap = 1
    congdon = 1
    user_input = input("Enter a positive number: ")
    print("")

    # process & output
    try:
        user_number = int(user_input)

        while gia_tri_vong_lap <= user_number:
            print("The number is: {}".format(gia_tri_vong_lap))
            congdon = congdon * gia_tri_vong_lap
            gia_tri_vong_lap = gia_tri_vong_lap + 1
        print("The factarial is: {} ".format(congdon))
    except Exception:
        print("This is not an integer")
    finally:
        print("UwU")


if __name__ == "__main__":
    main()
