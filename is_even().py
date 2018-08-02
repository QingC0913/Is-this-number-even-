def is_even(num):
    tf = True
    if num % 2 == 0:
        print (tf)
    if num % 2 == 1:
        tf = False
        print (tf)
    return (tf)

def main():
    num = 10
    is_even(num)

if __name__ == "__main__":
    main()
