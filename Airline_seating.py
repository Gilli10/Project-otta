big_list = ["A","B","C","D","E","F","G","H","I"]


def input_plane(): #Fáum fjölda af röðum og sætafjöldan í hverri röð
    rows = int(input("Enter number of rows: "))
    seats = int(input("Enter number of seats in each row: "))
    return rows , seats


def to_seats_list(big_list,rows,seats): # Notum raða- og sætafjöldan til að búa til lista með öllum sætum
    seat_list = []
    counter = 0
    while counter < rows:
        seat_list.append(big_list[0:seats])
        counter +=1
    return seat_list

def print_seats(seat_list):
    meat_list = list(seat_list)
    counter = 0
    seat_row_1 =''.join(meat_list)
    for i in meat_list:
        counter += 1
        print("{0:2},{1:4},{2:4}".format(counter,"ABC","DEF"))


def choose_seats(seat_list):
    loop = True
    while loop == True:
        #búa til fall til að prenta út listann
        print_seats(seat_list)
        seat = input("Input seat number (row seat): ")
        chosen = seat.split(" ")
        if int(chosen[0]) < 1 or int(chosen[0]) > len(seat_list) or chosen[1] not in seat_list[int(chosen[0])-1]:
            print("Invalid seat!")
        #búa til fall til að taka frá sæti
        more = input("More seats (y/n)? ")
        if more == "n":
            loop = False
        



def main():
    rows, seats = input_plane()
    seat_list = to_seats_list(big_list,rows,seats)
    choose_seats(seat_list)

main()