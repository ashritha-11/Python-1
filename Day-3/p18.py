#Scenario based question
def tech_workshop_report(day1, day2, day3):
    day1 = set(email.lower() for email in day1)
    day2 = set(email.lower() for email in day2)
    day3 = set(email.lower() for email in day3)
    all_unique = day1 | day2 | day3
    all_three = day1 & day2 & day3
    exactly_one = ((day1 - day2 - day3) |
                   (day2 - day1 - day3) |
                   (day3 - day1 - day2))
    day1_day2 = day1 & day2
    day2_day3 = day2 & day3
    day1_day3 = day1 & day3
    print("\n Tech Workshop Report \n")
    print(f"Total unique attendees: {len(all_unique)}")
    print("List of unique attendees:", sorted(all_unique), "\n")
    print(f"Attendees who attended all three days: {len(all_three)}")
    print("List:", sorted(all_three), "\n")
    print(f"Attendees who attended exactly one day: {len(exactly_one)}")
    print("List:", sorted(exactly_one), "\n")
    print(f"Pairwise overlap counts:")
    print(f"Day1 & Day2: {len(day1_day2)} -> {sorted(day1_day2)}")
    print(f"Day2 & Day3: {len(day2_day3)} -> {sorted(day2_day3)}")
    print(f"Day1 & Day3: {len(day1_day3)} -> {sorted(day1_day3)}")
day1 = ["ashritha@gmail.com", "Ash123@gmail.com", "akhila@gmail.com", "Akhila28@gmail.com"]
day2 = ["mohangoud@gmail.com", "ashritha824@gmail.com", "mohangoud824@gmail.com", "saritha@gmail.com"]
day3 = ["ashrithareddypally@gmail.com", "akhila1090@gmail.com", "Saritha13@gmail.com"]

tech_workshop_report(day1, day2, day3)
