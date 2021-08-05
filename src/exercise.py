def main():
    #write your code below this line
    while True:
        number = input()
        
        if number == "end":
            break

        number = int(number)
        print(number*number*number)

if __name__ == '__main__':
    main()
