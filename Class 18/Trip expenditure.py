# Trip Expenditure

def hotel_cost(nights):
    return 140*nights
def plane_cost(city):
    if city == "los angles":
        return 800
    elif city == "new york":
        return 550
    elif city == "New jersey":
        return 1200
    elif city == "Atlanta":
        return 600
def rental_car_cost(days):   
    daily_rate = 40
    total_cost = daily_rate * days

    if days >= 7:
        total_cost -= 50
    elif days >= 3:
        total_cost -= 20

    return total_cost
def trip_cost(city, days, spending_money):
    return rental_car_cost(days) + hotel_cost(days) + plane_cost(city) + spending_money

print("The total trip cost to New jersey is", trip_cost("New jersey",7,1200))         