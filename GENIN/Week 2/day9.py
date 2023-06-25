#writing my day nine code below here
    #Grading Program    
student_scores = {
    "Harry": 81,
    "Ron": 78,
    "Hermoine": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grade = {}

for i in student_scores:
    value = student_scores[i]
    if value <= 70:
        student_grade[value] = "Fail"
    elif value >= 71 and value <= 80:
        student_grade[value] = "Acceptable"
    elif value >= 81 and value <= 90:
        student_grade[value] = "Exceeds expectation"
    elif value >= 91 and value <= 100:
        student_grade[value] = "Outstanding"
print(student_grade)

    #Dictionary List
travel_log = [
    {"country": "France",
        "visits": 12,
        "cities":["Paris", "Lyo", "Dijon"], },
    {"country": "Germany",
        "visits": 5,
        "cities":["Munich", "Hamburg", "Stuttgart"],}
]
def add_new_country(country_visited, times_visited, cities_visited):
    country = {}
    country["country"] = country_visited
    country["visits"] = times_visited
    country["cities"] = cities_visited
    travel_log.append(country)
add_new_country("Russia", 2, ["Moscow", "Saint Petersburg"])
print(travel_log)

    #Secret Auction
bids = {}
playing = True
def auction(bidding):
    highest = 0
    win_name = ""
    for bidder in bidding:
        bid_amount = bidding[bidder]
        if bid_amount > highest:
            highest = bid_amount
            win_name = bidder
            print(f"{win_name} wins with a bid of {highest}")
while playing:
    name = input("Please enter your name: ").lower()
    bid = int(input("Enter your bid: $"))
    bids[name] = bid  
    cont = input("Any other bidder?: ")
    if cont == "n":
        playing = False
        auction(bids)
