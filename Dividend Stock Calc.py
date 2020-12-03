# Personal project that I made to calculate a high yielding dividend stock
# to determine what the end value would be over a given number of months.

def main():

    print("This program calculates the compounded value of a")
    print("given stock or investment over the entered time. \n")
    name = input("Please enter stock name: ")
    start = int(input("Please enter a starting deposit: "))
    x = float(input("Please enter the monthly deposit: "))
    a = int(input("Enter the number of months: "))
    
    y = float(input("Enter the interest rate (as a decimal): "))
    z = x * y
    total = start + x + z
    sub_month = x * a + start
    print("**", name, "Dividend Compound Interest Calculator**")
    print("@********************************************@")
    print("* First month:", '\t \t \t', '$', ('%.2f' % total), "     *", sep='')

    for com in range(1, a):
        INT = (total * y)
        total = total + INT + x
        print("* Monthly total:", '\t \t', '$', ('%.2f' % total), "     *", sep='')
    print("* Total investment: $", ('%.2F' % sub_month), '\t \t', "     *", sep='')
    print("* Total number of months: ", a, '\t \t', "    *")
    INT = (total * y)
    INTEREST = (total - start) - (sub_month - start) + INT
    print("* Final months interest earning: $", ('%.2F' % INT), "      *", sep ='')
    print("* Total interest realized: $", ('%.2F' % INTEREST), '\t', "     *", sep='')
    print("@********************************************@")
    print("End program")
    
main()
