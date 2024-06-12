import random
import time

# Function to display a message character by character with a slight delay
def prompt_msg(chars):
    for cha in chars:
        print(cha, end='', flush=True)  # Print each character without a newline
        time.sleep(0.1)  # Pause for a short duration between characters
    print()  # Move to the next line after printing the message

# Function to create a blinking effect for warning messages
def warning_msg(chars):
    for _ in range(3):  # Repeat the blinking effect three times
        # Print the characters and move the cursor to the start of the line
        print('\r' + chars, end='', flush=True)
        time.sleep(0.2)  # Pause to display the characters
        # Clear the line by printing spaces equal to the length of the message
        print('\r' + ' ' * len(chars), end='', flush=True)
        time.sleep(0.2)  # Pause before the next iteration

    print('\r' + chars)  # Print the characters at the end of the blinking effect

# Function to spin a row of the slot machine
def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']
    return [random.choice(symbols) for _ in range(3)]  # Randomly select 3 symbols

# Function to print the row in a formatted manner
def print_row(row):
    print('*************')
    print(' | '.join(row))
    print('*************')

# Function to calculate the payout based on the row and bet
def get_payout(row, bet):
    if row[0] == row[1] == row[2]:  # Check if all symbols in the row are the same
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0  # No payout if symbols do not match

# Main function to orchestrate the game
def main():
    balance = 100  # Starting balance for the player

    # Welcome message
    print('*************************')
    print('Welcome to Python Slots')
    print('*************************')
    print("Symbols: 🍒 🍉 🍋 🔔 ⭐")
    print('*************************')

    # Main game loop
    while balance > 0:
        print(f'Current Balance: ${balance}')
        bet = input('Please place your bet: ')

        # Validate the bet input
        if not bet.isdigit():
            warning_msg('Please enter a valid number')
            continue

        bet = int(bet)

        # Check if the bet is within the player's balance
        if bet > balance:
            warning_msg('Insufficient balance')
            continue

        # Check if the bet is greater than zero
        if bet <= 0:
            warning_msg('Please enter a number greater than zero')
            continue

        balance -= bet  # Deduct the bet from the balance

        prompt_msg('Spinning...\n')
        row = spin_row()  # Spin the row to get random symbols
        print_row(row)  # Print the row

        payout = get_payout(row, bet)  # Calculate the payout

        # Display the result of the spin
        if payout > 0:
            warning_msg(f'You won ${payout}')
        else:
            warning_msg('Sorry, you lost this round')

        balance += payout  # Update the balance with the payout

        # Ask the player if they want to play again
        while True:
            play_again = input('Do you want to play again? (Y/N): ').strip().upper()
            if play_again == 'N':
                break  # Exit the loop if the player does not want to play again
            elif play_again == 'Y':
                break  # Continue the loop if the player wants to play again
            else:
                warning_msg('Invalid input, please enter Y or N')  # Handle invalid input

        if play_again == 'N':
            break  # Exit the main loop if the player does not want to play again

    # Game over message
    warning_msg(f'Game Over! Your final balance: ${balance}')

if __name__ == '__main__':
    main()
