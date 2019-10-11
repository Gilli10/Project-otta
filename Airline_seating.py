def input_plane():
    rows = input("Enter number of rows: ")
    seats = input("Enter number of seats in each row: ")
    return rows , seats

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
    choose_seats(rows, seats)