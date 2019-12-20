def get_path(arr, last):
    import random
    random.shuffle(arr)
    print(arr, last)
    if not arr:
        return True
    for i in range(len(arr)):
        if arr[i][0] == last or not last:
            if get_path(arr[:i] + arr[i+1:], arr[i][-1]):
                return True
    return False


def main():
    array = ["hello", "or", "rever", "redis", "stock"]
    print(get_path(array, ""))


if __name__ == '__main__':
    main()
