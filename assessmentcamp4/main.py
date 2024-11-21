import re

import mysql.connector
from tabulate import tabulate
from datetime import datetime, timedelta


databaseobj = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1234',
    database='hotelRoomBookingSystem'
)



print(databaseobj)

HMS = databaseobj.cursor()

HMS.execute("create database if not exists hotelRoomBookingSystem")

HMS.execute("CREATE TABLE if not exists role("
            "roleId INT PRIMARY KEY,"
            "roleName VARCHAR(20))")
role_insert = "INSERT IGNORE INTO role(roleId,roleName) values(%s,%s)"
role_values =[(1001,'Admin'),
              (1002,'Manager')]
HMS.executemany(role_insert,role_values)

HMS.execute("CREATE TABLE if not exists users("
            "userId INT auto_increment PRIMARY KEY,"
            "userName VARCHAR(50) UNIQUE,"
            "password VARCHAR(50) NOT NULL,"
            "registeredON DATETIME DEFAULT CURRENT_TIMESTAMP,"
            "roleId INT NOT NULL,"
            "FOREIGN KEY(roleId) REFERENCES role(roleId))")


admin_insert="INSERT IGNORE INTO users(userName,password,roleId)values(%s,%s,%s)"
admin_insert_values= [('admin01','@1',1001),
                      ('admin02','123',1001)]
HMS.executemany(admin_insert,admin_insert_values)
databaseobj.commit()



# Room Categories Table and insertin values
HMS.execute("""
    CREATE TABLE IF NOT EXISTS RoomCategory (
        CategoryID INT AUTO_INCREMENT PRIMARY KEY,
        CategoryName VARCHAR(50) NOT NULL,
        HourlyRate DECIMAL(10, 2),
        DailyRate DECIMAL(10, 2)
    )
""")


# roomCat_query = "INSERT INTO RoomCategory (CategoryName, HourlyRate, DailyRate) VALUES (%s, %s, %s)"
# roomCat_values = [("Single", None, 1500),
#                   ("Double", None, 2000),
#                   ("Suite", None, 3000),
#                   ("Convention Hall", 500, None),
#                   ("Ball Room", 700, None)]

# HMS.executemany(roomCat_query,roomCat_values)

# Rooms Table
HMS.execute("""
    CREATE TABLE IF NOT EXISTS Rooms (
        RoomID INT AUTO_INCREMENT PRIMARY KEY,
        RoomNumber VARCHAR(10) UNIQUE NOT NULL,
        CategoryID INT NOT NULL,
        BaseRate DECIMAL(10, 2),
        IsOccupied BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (CategoryID) REFERENCES RoomCategory(CategoryID)
    )
""")

# Customers Table
HMS.execute("""
    CREATE TABLE IF NOT EXISTS Customers (
        CustomerID INT AUTO_INCREMENT PRIMARY KEY,
        FirstName VARCHAR(50),
        LastName VARCHAR(50),
        Phone VARCHAR(15),
        Email VARCHAR(100)
    )
""")

# Bookings Table
HMS.execute("""
    CREATE TABLE IF NOT EXISTS Bookings (
        BookingID VARCHAR(10) PRIMARY KEY,
        CustomerID INT NOT NULL,
        RoomID INT NOT NULL,
        BookingDate DATETIME DEFAULT CURRENT_TIMESTAMP,
        OccupancyDate DATE NOT NULL,
        OccupancyDuration INT,
        AdvanceReceived DECIMAL(10, 2),
        FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
        FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
    )
""")



# Rates Table
HMS.execute("""
    CREATE TABLE IF NOT EXISTS Rates (
        RateID INT AUTO_INCREMENT PRIMARY KEY,
        RoomID INT NOT NULL,
        Tax DECIMAL(5, 2),
        HousekeepingCharge DECIMAL(10, 2),
        MiscCharge DECIMAL(10, 2),
        FOREIGN KEY (RoomID) REFERENCES Rooms(RoomID)
    )
""")

# Additional Charges Table
HMS.execute("""
    CREATE TABLE IF NOT EXISTS AdditionalCharges (
        ChargeID INT AUTO_INCREMENT PRIMARY KEY,
        BookingID VARCHAR(10) NOT NULL,
        Description VARCHAR(255),
        Amount DECIMAL(10, 2),
        FOREIGN KEY (BookingID) REFERENCES Bookings(BookingID)
    )
""")

import mysql.connector





# Function to add room by admin
def add_room():
    try:

        # inputs
        print("Enter Room Details:")
        room_number = input("Enter Room Number (e.g., 101, Suite-01, etc.): ")
        category_id = int(
            input("Enter The Category ID - 1: Single, 2: Double, 3: Suite, 4: Convention Hall, 5: Ball Room: "))
        base_rate = float(input("Enter Base Rate: "))

        room_query = "INSERT INTO Rooms (RoomNumber, CategoryID, BaseRate) VALUES (%s, %s, %s)"
        room_values = (room_number, category_id, base_rate,)
        HMS.execute(room_query,room_values)

        databaseobj.commit()

        print(f"Room {room_number} added successfully🤩!")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def searchRoomByBookingID():
    booking_id = input("Enter the BookingID: ")
    query = """
        SELECT b.BookingID, r.RoomNumber, rc.CategoryName, r.BaseRate,
               c.FirstName, c.LastName, c.Phone, c.Email
        FROM Bookings b
        JOIN Rooms r ON b.RoomID = r.RoomID
        JOIN RoomCategory rc ON r.CategoryID = rc.CategoryID
        JOIN Customers c ON b.CustomerID = c.CustomerID
        WHERE b.BookingID = %s;
    """

    try:
        # Execute the query to fetch room and customer details by booking ID
        HMS.execute(query, (booking_id,))
        result = HMS.fetchall()

        if result:
            print(tabulate(result,
                           headers=["BookingID", "RoomNumber", "Category", "BaseRate", "FirstName", "LastName", "Phone",
                                    "Email"], tablefmt="pretty"))
        else:
            print(f"No booking found for BookingID: {booking_id}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def displayRoomsInIncreasingOrderOfRate():
    # SQL Query to fetch all rooms ordered by increasing rate per day (DailyRate)
    query = """
        SELECT r.RoomID, r.RoomNumber, rc.CategoryName, r.BaseRate
        FROM Rooms r
        JOIN RoomCategory rc ON r.CategoryID = rc.CategoryID
        ORDER BY r.BaseRate ASC;
    """

    try:
        # Execute the query to fetch room details ordered by rate
        HMS.execute(query)
        rooms = HMS.fetchall()

        # Check if rooms were fetched and display them
        if rooms:
            print(tabulate(rooms, headers=["RoomID", "RoomNumber", "Category", "BaseRate"], tablefmt="pretty"))
        else:
            print("No rooms found.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")



# Function to display category-wise list of rooms and their rate per day
def displayCategoryRooms():
    try:
        query = """
        SELECT rc.CategoryName, r.RoomNumber, r.BaseRate
        FROM Rooms r
        JOIN RoomCategory rc ON r.CategoryID = rc.CategoryID
        ORDER BY rc.CategoryName, r.RoomNumber;
        """

        HMS.execute(query)
        rooms = HMS.fetchall()

        if rooms:
            table_data = []
            for room in rooms:
                category_name, room_number, base_rate = room
                table_data.append([category_name, room_number, f"{base_rate:.2f}"])

            # Display the table using tabulate
            headers = ["Category Name", "Room Number", "Rate Per Day"]
            print(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            print("No rooms available.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")


def displayUnbookedRooms():

    # SQL Query to fetch rooms that are not booked
    query = """
          SELECT r.RoomID, r.RoomNumber, rc.CategoryName, r.BaseRate
        FROM Rooms r
        JOIN RoomCategory rc ON r.CategoryID = rc.CategoryID
        WHERE r.IsOccupied = FALSE;
    """
    try:
        HMS.execute(query)
        rooms_not_booked = HMS.fetchall()
        if rooms_not_booked:
            print(tabulate(rooms_not_booked, headers=["RoomID", "RoomNumber", "CategoryID", "BaseRate"], tablefmt="pretty"))
        else:
            print("No unbooked rooms found.")
    except mysql.connector.Error as err:
        print(f"Error: {err}")





def displayOccupiedRoomsNextTwoDays():
    currentDate = datetime.now()
    twoDays = currentDate + timedelta(days=2)

    current_date_str = currentDate.strftime('%Y-%m-%d')
    two_days_later_str = twoDays.strftime('%Y-%m-%d')

    query = """
        SELECT r.RoomID, r.RoomNumber, rc.CategoryName, r.BaseRate, b.BookingID, b.OccupancyDate, b.OccupancyDuration
        FROM Rooms r
        JOIN Bookings b ON r.RoomID = b.RoomID
        JOIN RoomCategory rc ON r.CategoryID = rc.CategoryID
        WHERE b.OccupancyDate BETWEEN %s AND %s
        AND (b.OccupancyDate <= %s AND DATE_ADD(b.OccupancyDate, INTERVAL b.OccupancyDuration DAY) > %s);
    """

    try:
        HMS.execute(query, (current_date_str, two_days_later_str, two_days_later_str, current_date_str))
        rooms_occupied = HMS.fetchall()

        if rooms_occupied:
            print(tabulate(rooms_occupied,
                           headers=["RoomID", "RoomNumber", "Category", "BaseRate", "BookingID", "OccupancyDate",
                                    "OccupancyDuration"], tablefmt="pretty"))
        else:
            print("No rooms occupied for the next two days.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")




def updateUnoccupied():
    # Ask the user to enter the room number
    room_number = input("Please enter the room number you want to mark as unoccupied: ")


    check_query = """
        SELECT RoomID, RoomNumber, IsOccupied
        FROM Rooms
        WHERE RoomNumber = %s;
    """

    update_query = """
        UPDATE Rooms
        SET IsOccupied = FALSE
        WHERE RoomNumber = %s;
    """

    try:
        HMS.execute(check_query, (room_number,))
        room = HMS.fetchone()

        if room:
            room_id, room_number, is_occupied = room
            if is_occupied:
                # Room is occupied, so we can update it to unoccupied
                HMS.execute(update_query, (room_number,))
                databaseobj.commit()
                print(f"Room {room_number} is now marked as unoccupied.")
            else:
                print(f"Room {room_number} is already unoccupied.")
        else:
            print(f"Room {room_number} does not exist.")

    except mysql.connector.Error as err:
        print(f"Error: {err}")




# Function to add a new booking
def newBooking():
    try:
        while True:
            first_name = input("Enter the first name : ")
            if re.fullmatch("[A-Za-z]{2,25}", first_name):
                break
            else:
                print("Oops😑! Enter only alphabets of length 2 to 25.")
        # last name
        while True:
            last_name = input("Enter the last name : ")
            if re.fullmatch("[A-Za-z]{2,25}", last_name):
                break
            else:
                print("Oops😑! Enter only alphabets of length 2 to 25.")

        while True:
            phone = input("Enter customer's phone number (10 digits, starting from 7, 8, or 9): ")
            if re.fullmatch("[789][0-9]{9}", phone):
                break
            else:
                print("Oops😑! Enter a valid phone number starting with 7, 8, or 9 and having 10 digits.")

        while True:
            email = input("Enter customer's email: ")
            if re.fullmatch("[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+", email):
                break
            else:
                print("Oops😑! Enter a valid email address (e.g., user@example.com).")

        HMS.execute("""
            INSERT INTO Customers (FirstName, LastName, Phone, Email) 
            VALUES (%s, %s, %s, %s)
        """, (first_name, last_name, phone, email))
        databaseobj.commit()

    # vcustomer id needed in booking table
        customer_id = HMS.lastrowid

        print("Available Room Categories: 1. Single 2. Double 3. Suite 4. Convention Hall 5. Ball Room")
        category_choice = int(input("Select Room Category: "))

        category_map = {1: "Single", 2: "Double", 3: "Suite", 4: "Convention Hall", 5: "Ball Room"}
        selected_category = category_map.get(category_choice)

        if selected_category is None:
            print("Invalid choice, please try again.")
            return

        # Checking for available rooms in the selected category
        querybooking = "SELECT RoomID, RoomNumber, IsOccupied FROM Rooms WHERE CategoryID = (SELECT CategoryID FROM RoomCategory WHERE CategoryName = %s) AND IsOccupied = FALSE"
        querybookinginput = (selected_category,)
        HMS.execute(querybooking,querybookinginput)
        available_rooms = HMS.fetchall()

        if not available_rooms:
            print("No available rooms in the selected category.")
            return

        print(f"Available rooms in {selected_category}:")
        for room in available_rooms:
            print(f"Room ID: {room[0]}, Room Number: {room[1]}")

        room_choice = int(input("Select Room ID from available rooms: "))

        # Check if the selected room is available
        room_available = False
        for room in available_rooms:
            if room[0] == room_choice:
                room_available = True
                room_number = room[1]
                break

        if not room_available:
            print("Invalid room selection.")
            return

      # test
        HMS.execute("SELECT MAX(CAST(SUBSTRING(BookingID, 3) AS UNSIGNED)) FROM Bookings")
        last_booking_number = HMS.fetchone()[0]

        if last_booking_number is None:
            last_booking_number = 0  # If no bookings exist yet

        new_booking_number = last_booking_number + 1
        booking_id = f"BK{new_booking_number:05d}"
      #   test


        occupancy_date = input("Enter occupancy date (YYYY-MM-DD): ")
        occupancy_duration = int(input("Enter number of days of occupancy: "))
        advance_received = float(input("Enter advance received: "))

        #convention  and ballrooms
        if selected_category in ["Convention Hall", "Ball Room"]:
            hourly_rate = float(input("Enter hourly rate for the room: "))
            total_charge = hourly_rate * occupancy_duration * 24  # Assuming full day occupancy
        else:
            daily_rate = float(input(f"Enter daily rate for the {selected_category}: "))
            total_charge = daily_rate * occupancy_duration

        # Insert booking details
        HMS.execute("""
            INSERT INTO Bookings (BookingID, CustomerID, RoomID, OccupancyDate, OccupancyDuration, AdvanceReceived)
            VALUES (%s, %s, %s, %s, %s, %s)
        """, (booking_id, customer_id, room_choice, occupancy_date, occupancy_duration, advance_received))
        databaseobj.commit()

        HMS.execute("""
            UPDATE Rooms SET IsOccupied = TRUE WHERE RoomID = %s
        """, (room_choice,))
        databaseobj.commit()

        tax = float(input("Enter tax rate: "))
        housekeeping_charge = float(input("Enter housekeeping charge: "))
        misc_charge = float(input("Enter misc charge: "))

        HMS.execute("""
            INSERT INTO Rates (RoomID, Tax, HousekeepingCharge, MiscCharge)
            VALUES (%s, %s, %s, %s)
        """, (room_choice, tax, housekeeping_charge, misc_charge))
        databaseobj.commit()

        print(f"Booking confirmed for room({selected_category}). Total charge: {total_charge}")

    except mysql.connector.Error as err:
        print(f"Error: {err}")
        databaseobj.rollback()



def loginFunction():
    global userDetails
    while True:
        userName = input("Enter the user id : ")
        if userName == "":
            print("🙄This field cannot be empty.")
        else:
            break
    while True:
        password = input("Enter the password : ")
        if password == "":
            print("🙄This field cannot be empty.")
        else:
            break
    login_query= 'SELECT * FROM users WHERE userName=%s COLLATE utf8mb4_bin and password=%s COLLATE utf8mb4_bin'
    login_query_values = (userName,password)
    HMS.execute(login_query,login_query_values)
    userDetails =HMS.fetchone()
    # print(userDetails)
    if userDetails!= None:
        if userDetails[-1] == 1001:
            loggedinAdmin()
        else:
            print("Oops")
    else:
        print("🙄 Incorrect userid or password!")

def loggedinAdmin():
    while True:
        print(f"""                            
                                    WELCOME, {userDetails[1]}! 🥰
                                  
              Choose an option :
              1.Add a Room
              2.List of Rooms
              3.Booking
              4.Unbooked Rooms
              5.Update Unoccupied Room
              6.List all rooms which are occupied for next two days
              7.Display the list of all rooms in Their increasing order of rate per day
              8.Search Rooms&Customer details based on BookingID
              9.LogOut
              """)
        number = input("Enter a number from above list : ")
        if number == "1":
            add_room()
        elif number == "2":
            displayCategoryRooms()
        elif number == "3":
            newBooking()
        elif number == "4":
            displayUnbookedRooms()
        elif number == "5":
            updateUnoccupied()
        elif number == "6":
            displayOccupiedRoomsNextTwoDays()
        elif number == "7":
            displayRoomsInIncreasingOrderOfRate()
        elif number == "8":
            searchRoomByBookingID()
        elif number == "9":
            print("Logging Out")
            break
        else:
            print("invalid input😮!!!")




#// Global Landing page
while True:
    print("""                              --------------------------------------
                                WELCOME TO ALONN HOTELS PVT LTD 👶
                              --------------------------------------
          Choose an option :
          1.Login
          2.Exit""")

    number=input("Enter a number from above list : ")
    if number=="1":
        loginFunction()
    elif number=="2":
        print("""        -------------------------------
        Thanks for visiting our hotel 😍
        -------------------------------""")
        break
    else:
        print("invalid input😮!!!")


