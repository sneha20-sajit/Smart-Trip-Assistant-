from tabulate import tabulate
import textwrap
import mysql.connector
import matplotlib.pyplot as plt
import numpy as np

def filter_by_region():
    print("Which region of India would you like to explore?")
    print("1. North India")
    print("2. South India")
    print("3. East India")
    print("4. West India")
    print("5. North-East India")
    print("6. Central India")
    choice = input("Enter your choice: ")
    state = {
        "1": {"places": ["Delhi", "Uttar Pradesh", "Jammu & Kashmir", "Ladakh", "Punjab", "Uttarakhand", "Haryana", "Himachal Pradesh"]},
        "2": {"places": ["Kerala", "Karnataka", "Tamil Nadu", "Andhra Pradesh", "Telangana", "Puducherry", "Lakshadweep"]},
        "3": {"places": ["Odisha", "West Bengal", "Andaman & Nicobar Islands", "Bihar", "Jharkhand"]},
        "4": {"places": ["Goa", "Maharashtra", "Rajasthan", "Gujarat", "Dadra & Nagar Haveli and Daman & Diu"]},
        "5": {"places": ["Manipur", "Sikkim", "Arunachal Pradesh", "Assam", "Meghalaya", "Nagaland", "Mizoram", "Tripura"]},
        "6": {"places": ["Madhya Pradesh", "Chhattisgarh"]}
    }
    if choice in state:
        return state[choice]["places"]
    else:
        print("Invalid choice")
        return None

def filtered_vacations(connection, state_input):
    cursor = connection.cursor()
    query = ("SELECT ID, TYPES_OF_TOURISM, STATE_UT, POPULAR_THINGS_TO_DO, KNOWN_FOR, LOCATION, BEST_TIME_TO_VISIT, BUDGET "
             "FROM TRAVEL_GUIDE WHERE STATE_UT LIKE %s")
    cursor.execute(query, (f"%{state_input}%",))
    result = cursor.fetchall()
    cursor.close()
    return result

def wrap_text(text, width):
    return textwrap.fill(text, width=width)

def packing_tips(month_input, connection):
    season_map = {
        "mar": "Spring", "march": "Spring", "apr": "Spring", "april": "Spring",
        "may": "Summer", "jun": "Summer", "june": "Summer",
        "jul": "Monsoon", "july": "Monsoon", "aug": "Monsoon", "august": "Monsoon",
        "sep": "Monsoon", "september": "Monsoon",
        "oct": "Autumn", "october": "Autumn", "nov": "Autumn", "november": "Autumn",
        "dec": "Winter", "december": "Winter", "jan": "Winter", "january": "Winter",
        "feb": "Winter", "february": "Winter"
    }
    month = month_input.strip().lower()
    season = season_map.get(month)
    if not season:
        print("Invalid month entered")
        return
    cursor = connection.cursor()
    query2 = "SELECT PACKING_TIPS FROM TIPS WHERE season = %s"
    cursor.execute(query2, (season,))
    result = cursor.fetchone()
    cursor.close()
    if result:
        print(f"\nYou’re traveling in {season} season")
        print("Packing Tips:")
        print(result[0])
    else:
        print("No tips found for this season")

def compare_state(connection, state_name):
    cursor = connection.cursor()
    Q2 = """SELECT Location, AVG((CAST(REPLACE(SUBSTRING_INDEX(Budget, ' to ', 1), ',', '') AS UNSIGNED) + CAST(REPLACE(SUBSTRING_INDEX(Budget, ' to ', -1), ',', '') AS UNSIGNED)) / 2) AS avg_cost FROM TRAVEL_GUIDE WHERE STATE_UT = %s GROUP BY Location"""
    cursor.execute(Q2, (state_name,))
    rows = cursor.fetchall()
    cursor.close()
    if not rows:
        print(f"No cost data found for {state_name}.")
        return
    # Sort by cost 
    rows.sort(key=lambda x: x[1])
    Places = [row[0] for row in rows]
    Costs = [row[1] for row in rows]
    colors = plt.cm.Pastel1(np.linspace(0, 1, len(Places)))
    plt.figure(figsize=(12, 6))
    plt.bar(Places, Costs, color=colors, edgecolor='black')  
    plt.xlabel("Places")
    plt.ylabel("Average Travel Cost")
    plt.title(f"Travel Cost Comparison for {state_name}")
    plt.xticks(rotation=45, ha='right')
    # Add cost labels on top of each bar
    for i, cost in enumerate(Costs):
        plt.text(i, cost, f"{int(cost)}", ha='center', va='bottom')
    plt.tight_layout()
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.show()

def main():
    import os
    connection = mysql.connector.connect(host="localhost", user="root", password=os.getenv("MYSQL_PASSWORD"), database="tourism")
    if connection.is_connected():
        # Welcome message
        print("\n Welcome to the Smart Trip Assistant! \n")

        # Choose region and state
        states = filter_by_region()
        if not states:
            connection.close()
            return

        while True:
            print("Available States/UTs in this region:")
            for idx, state in enumerate(states, start=1):
                print(f"{idx}. {state}")
            try:
                state_choice = int(input("Enter the number for the state you want to explore: "))
                if state_choice < 1 or state_choice > len(states):
                    print("Invalid state number. Exiting.")
                    connection.close()
                    return
                state_input = states[state_choice - 1]
            except ValueError:
                print("Invalid input. Please enter a number.")
                connection.close()
                return

            # Get vacations for that state
            vacations = filtered_vacations(connection, state_input)
            if not vacations:
                print(f"No vacation options found for {state_input}. Please choose another state.")
                continue

            headers = ["ID", "Type of Tourism", "State/UT", "Popular Things To Do", "Known For", "Location", "Best Time To Visit", "Budget"]
            wrapped_table = []
            for vacation in vacations:
                wrapped_row = [
                    vacation[0],
                    wrap_text(vacation[1], width=20),
                    wrap_text(vacation[2], width=20),
                    wrap_text(vacation[3], width=20),
                    wrap_text(vacation[4], width=20),
                    wrap_text(vacation[5], width=20),
                    vacation[6],
                    vacation[7]
                ]
                wrapped_table.append(wrapped_row)
            print("\nAvailable vacation options:")
            print(tabulate(wrapped_table, headers=headers, tablefmt="grid"))

            # Compare all places in the selected state
            do_compare = input(f"\nWould you like to compare travel costs of all places in {state_input}? (yes/no): ").strip().lower()
            if do_compare in ["yes", "y"]:
                compare_state(connection, state_input)

            # Packing tips
            user_month = input("\nEnter the month you plan to travel in: ")
            packing_tips(user_month, connection)
            break

        # Thank you message
        print("\n Thank you for using the Smart Trip Assistant! \n")

    connection.close()

# Run the program
main()
