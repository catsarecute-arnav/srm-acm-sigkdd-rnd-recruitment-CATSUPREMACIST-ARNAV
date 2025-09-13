def armstrong():
    try:
        num=int(input("Enter a number: "))
        if num<0:
            print(f"{num} is not an Armstrong number.")
            return
        str_num=str(num)
        len_str_num=len(str_num)
        armstrong_sum=0
        for i in str_num:
            digit=int(i)
            armstrong_sum+=digit**len_str_num
        if armstrong_sum==num:
            print(f"{num} is an Armstrong number.")
        else:
            print("Your arms are not strong :(")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")
if __name__=="__main__":armstrong()
