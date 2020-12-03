#!/usr/bin/env python3
# encoding: UTF-8

def read_label(filename):
    with open(filename, mode='rb') as file_:
        magic = file_.read(4)
        print("Magic:", magic, int.from_bytes(magic, "big"))
        numItems = file_.read(4)
        print("NumItems:", numItems, int.from_bytes(numItems, "big"))
        nums = file_.read()
        print(len(nums))
        for i in range(10):
            print("Label:", i, nums[i])#, int.from_bytes(nums[i], "big"))


def main():
    read_label("train-labels-idx1-ubyte")


if __name__ == "__main__":
    main()
