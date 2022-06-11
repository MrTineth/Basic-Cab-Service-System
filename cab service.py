#cab service system

details = [
    {
        'Type': 'Car',

        'Details': 'maximum number of passengers - 3 and 4 | AC/ Non AC'
    },
    {
        'Type': 'Van',

        'Details': 'Maximum number of passengers - 6 and 8 | AC/ Non AC'
    },
    {
        'Type': '3 Wheeler',

        'Details': 'Maximum number of passengers - 3'
    },
    {
        'Type': 'Lorry',

        'Details': 'Size – 7 ft and 12 ft'
    },
    {
        'Type': 'Truck',

        'Details': 'Max load and size - 2500kg and 3500kg'
    }
]

temDetails = []

username=input("Enter Your Name : ")
print('\n')
print("<-- Hello ",username," -->")
print("<-- WELCOME Cab Service System -->")
print("<-- Created by Tineth Vihanga -->")
print('\n')
print("<-- Main Menu -->")


while True:
    mainOption = input("\n1 for Add Vehicle\n2 for remove Vehicle \n3 for Assign Vehicle\n4 for Release Vehicle\n5 for View Available Vehicles \n6 for Book Cab \n7 for Exit\nChoose Number :")
    if mainOption == '7':
        break
#Add vehicle
    elif mainOption == '1':
        name = input("Enter the Vehicle Type: ")
        detail = input('Enter the Details: ')

        newDic = {
                'Type': name,
                'Details': detail
            }
        details.append(newDic)
#Remove Vehicle
    elif mainOption == '2':
        for detail in details:
            print("ID", details.index(detail), "Name: ", detail['Type'],"-->", "  Details: ", detail['Details'])
        remId = int(input("Select the ID for Remove Vehicle: "))
        details.pop(remId)
#Assign Vehicle
    elif mainOption == '3':
        for detail in details:
            print("ID", details.index(detail), "Name: ", detail['Type'],"-->", " Details: ", detail['Details'])
        userSelection = input("Assign 1 for Car\nAssign 2 for Van\nAssign 3 for 3 Wheeler\nAssign 4 for Lorry\nAssign 5 for Truck\n Choose Assign Nubmer : ")
        if userSelection == '1':
            for detail in details:
                if detail['Type'] == 'Car':
                    dic = detail
                    ID = details.index(detail)
                    break
        elif userSelection == '2':
            for detail in details:
                if detail['Type'] == 'Van':
                    dic = detail
                    ID = details.index(detail)
                    break
        elif userSelection == '3':
            for detail in details:
                if detail['Type'] == '3 Wheeler':
                    dic = detail
                    ID = details.index(detail)
                    break
        elif userSelection == '4':
            for detail in details:
                if detail['Type'] == 'Lorry':
                    dic = detail
                    ID = details.index(detail)
                    break
        elif userSelection == '5':
            for detail in details:
                if detail['Type'] == 'Truck':
                    dic = detail
                    ID = details.index(detail)
                    break
        temDetails.append(dic)

        details.pop(ID)
#Release Vehicle
    elif mainOption == '4':
        for detail in temDetails:
            print("ID", temDetails.index(detail), "Type: ", detail['Type'],"-->", " Details: ", detail['Details'])

        userSelection = int(input("Enter the id: "))
        relId = userSelection
        obj = temDetails[relId]
        details.append(obj)
        temDetails.pop(relId)

#View Available Vehicles
    elif mainOption == '5':

        print("Available Vehicles")
        for detail in details:
            print("ID", details.index(detail), "Type: ", detail['Type'],"-->", " Details: ", detail['Details'])
        print('\n')
        print("Assigned Vehicles")

        for detail in temDetails:

            print("ID", temDetails.index(detail), "Type: ", detail['Type'],"-->", " Details: ",
                  detail['Details'])
        print('\n')
#Booking Cab
    elif mainOption=='6':
        print('\n')
        print("<-- Book Your Cab -->")
        print('\n')
        name = str(input("Enter Your Name: "))
        address = input("Enter Your Address: ")
        tel = int(input("Enter Your Mobile Number: "))
        email = input("Enter Your e-mail Address : ")
        piclocation = str(input("Enter Your Pick Up Location: "))
        droplocation = str(input("Enter Your Drop Location: "))
        type=str(input("Enter Your Vehicle Type : "))



        print('\n')
        print("<-- Receipt -->")
        print('\n')

        print("Name : ", name)
        print("Address : ", address)
        print("Mobile : ", tel)
        print("E-mail :",email)
        print("PickUp : ", piclocation)
        print("Drop : ", droplocation)
        print("Vehicle Type :",type)


        print('\n')
        print("<-- Thank You  -->")
        print('\n')

#End