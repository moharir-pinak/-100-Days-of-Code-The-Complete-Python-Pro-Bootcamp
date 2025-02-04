# def full_name(first_name, last_name):
#     a = first_name.title()
#     b = last_name.title()
#     return f"{a} {b}"

# def main():
#     first_name = input("Enter the first name: ")
#     last_name = input("Enter the last name: ")
#     formatted_name = full_name(first_name, last_name)
#     print(formatted_name)

# if __name__ == "__main__":
#     main()
def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    
    if year % 4 == 0 and year % 100 != 0 :
        return True 
    else :
        return False
    
year = int(input("Enter Year :\n"))
answer = is_leap_year(year)
print(answer) 
    