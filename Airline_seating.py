big_list = ["A","B","C","D","E","F","G","H","I"]


def input_plane():
    rows = int(input("Enter number of rows: "))
    seats = int(input("Enter number of seats in each row: "))
    return rows , seats


def print_seats(big_list,rows,seats):
    seat_list = []
    counter = 0
    while counter < rows:
        seat_list.append(big_list[0:seats])
        counter +=1
    print(seat_list)


def choose_seats(rows,seats):
    loop = True
    while loop == True:
        seat = input("Input seat number (row seat): ")
        #búa til fall til að taka frá sæti
        more = input("More seats (y/n)? ")
        if more == "n":
            loop = False
        







def main():
    rows, seats = input_plane()
    print_seats(big_list,rows,seats)
    choose_seats(rows, seats)

main()