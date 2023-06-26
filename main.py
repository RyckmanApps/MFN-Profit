from calculations import calculate_profit
from handlers import handle_input

def main():
    # Get user input
    user_input = handle_input()

    # Perform calculations
    results = calculate_profit(user_input)

    # Display results
    print("Net Gain: ", results['net_gain'])
    print("Per RO Net Profit: ", results['per_ro_net_profit'])

if __name__ == "__main__":
    main()

