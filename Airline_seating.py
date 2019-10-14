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


def print_seats(seat_list): # Here we split the newest seed list into 2 aisles and print them out
    meat_list = list(seat_list)
    counter = 0
    half_len = len(meat_list[0]) // 2
    for i in range(len(meat_list)):
        seat_row_1 =' '.join(meat_list[i][0:half_len])
        seat_row_2 =' '.join(meat_list[i][half_len:])
        counter += 1
        print(("{0:2}" +"   "+ "{1:1}" +"   "+ "{2:1}"+" ").format(counter,seat_row_1,seat_row_2))


def reserve_seat(seat_list, chosen): # Here we use the enumerate function to cahnge the seat list when a seat is reserved
    seat_list = list(seat_list)
    chosen = list(chosen)
    for x in range(len(seat_list)):
        if x + 1 == int(chosen[0]):
            for n, i in enumerate(seat_list[x]):  
                if i == chosen[1]:
                    seat_list[x][n] = "X"


def check_seat(big_list,seat_list):
    big_list = list(big_list)
    seat_list = list(seat_list)
    index = 0
    loop = True
    print_seats(seat_list)
    while loop == True:
        full_plane = 0
        for i in seat_list:
            for x in i:
                if x != "X":
                    full_plane +=1
        if full_plane != 0:
            seat = input("Input seat number (row seat): ")
            chosen = seat.split(" ")
            
            try:
                for i in range(len(big_list)):
                    if big_list[i] == chosen[1]:
                        index = i
                if seat_list[int(chosen[0])-1][index] == "X":
                    print("That seat is taken!")
                else:
                    if int(chosen[0]) < 1 or int(chosen[0]) > len(seat_list) or chosen[1] not in seat_list[int(chosen[0])-1]:
                        print("Seat number is invalid!")
                    else:
                        reserve_seat(seat_list,chosen)
                        print_seats(seat_list)
                        full_plane = 0
                        for i in seat_list:
                            for x in i:
                                if x != "X":
                                    full_plane +=1
                        if full_plane != 0:
                            more = input("More seats (y/n)? ")
                            if more != "y":
                                loop = False
                        else:
                            loop = False
                           
                                      
            except ValueError:
                    print("Seat number is invalid!")
            except IndexError:
                    print("Seat number is invalid!")
        else:
            print_seats(seat_list)
        
    
    
    
        

def main():
    rows, seats = input_plane()
    seat_list = to_seats_list(big_list,rows,seats)
    check_seat(big_list,seat_list)

main()