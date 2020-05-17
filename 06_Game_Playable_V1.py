from tkinter import *
from functools import partial     # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # Formatting Variables
        background_color = "#7EA6E0"

        # GUI to get starting balance and stakes
        self.start_frame = Frame(width=300, height=100, bg=background_color,
                                 pady=10)
        self.start_frame.grid()

        # Set Initial balance to zero..
        self.starting_funds = IntVar()
        self.starting_funds.set(0)

        # Mystery Heading (Row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", bg=background_color,
                                       font=("Arial", "16", "bold"),
                                       padx=20, pady=20)
        self.mystery_box_label.grid(row=0)

        # Initial Instructions (Row 1)
        self.mystery_instructions = Label(self.start_frame,
                                          text="Please enter a dollar amount "
                                               "(between $5 and $50) in the box "
                                               "below. Then choose the stakes. "
                                               "The higher the stakes, the more "
                                               "you can win!",
                                          font="Arial 10 italic", wrap=250,
                                          justify=LEFT, bg=background_color,
                                          padx=5, pady=5)
        self.mystery_instructions.grid(row=1)

        # Entry Box, Button and Error Label (Row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200, bg=background_color)
        self.entry_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.entry_error_frame,
                                        font="Arial 16 bold", width=20)
        self.start_amount_entry.grid(row=0, column=0, padx=5)

        self.add_funds_button = Button(self.entry_error_frame,
                                       font="Arial 14 bold",
                                       text="Add Funds",
                                       command=self.check_funds)
        self.add_funds_button.grid(row=0, column=1, padx=5)

        # Error Label
        self.amount_error_label = Label(self.entry_error_frame,
                                        bg=background_color, fg="maroon", text="",
                                        font="Arial 10 bold", wrap=175,
                                        justify=LEFT)
        self.amount_error_label.grid(row=1, columnspan=2, pady=5)

        # Play Button Frame (Note: Not Youtube) (Row 3)
        self.stakes_frame = Frame(self.start_frame, bg=background_color)
        self.stakes_frame.grid(row=4)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Orange Low Stakes Button
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)",
                                        command=lambda: self.to_game(1),
                                        font=button_font, bg="#FC9003")
        self.low_stakes_button.grid(row=0, column=0, pady=10, padx=5)

        # Yellow Medium Stakes Button
        self.medium_stakes_button = Button(self.stakes_frame, text="Medium ($10)",
                                           command=lambda: self.to_game(2),
                                           font=button_font, bg="#FFFF00")
        self.medium_stakes_button.grid(row=0, column=1, padx=5, pady=10)

        # Green High Stakes Button
        self.high_stakes_button = Button(self.stakes_frame, text="High ($15)",
                                         command=lambda: self.to_game(3),
                                         font=button_font, bg="#00994D")
        self.high_stakes_button.grid(row=0, column=2, padx=5, pady=10)

        # Help and Game Stats Frame
        self.help_and_stats_frame = Frame(self.start_frame, bg=background_color)
        self.help_and_stats_frame.grid(row=6)

        # Help Button
        self.help_button = Button(self.help_and_stats_frame, text="Help / Rules",
                                  bg="#808080", fg="white", font=button_font,
                                  padx=10)
        self.help_button.grid(row=0, column=0, padx=10, pady=5)

        # Game Stats Button
        self.game_stats_button = Button(self.help_and_stats_frame, text="Game Stats...",
                                        bg="#003366", fg="white", font=button_font,
                                        padx=10)
        self.game_stats_button.grid(row=0, column=1, padx=10, pady=5)

    def check_funds(self):
        starting_balance = self.start_amount_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # Change background to white (For testing purposes)...
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        # Disable all stakes buttons in case user changes mind and
        # decreases amount entered.
        self.low_stakes_button.config(state=DISABLED)
        self.medium_stakes_button.config(state=DISABLED)
        self.high_stakes_button.config(state=DISABLED)

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you " \
                                 "can play with is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! The most you can risk in this game is $50"
            elif starting_balance >= 15:
                # Enable all buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
                self.high_stakes_button.config(state=NORMAL)
            elif starting_balance >= 10:
                # Enable Low and Medium Stakes Buttons
                self.low_stakes_button.config(state=NORMAL)
                self.medium_stakes_button.config(state=NORMAL)
            else:
                self.low_stakes_button.config(state=NORMAL)

        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (No text / Decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback, fg="#ff1100")

        else:
            # Set starting balance to amount entered by user
            self.starting_funds.set(starting_balance)

    def to_game(self, stakes):

        # Retrieve starting balance
        starting_balance = self.starting_funds.get()

        Game(self, stakes, starting_balance)

        # Hide startup window
        self.start_frame.destroy()

class Game:
    def __init__(self, partner, stakes, starting_balance):
        box_back = "#9cff45"
        box_text = "Arial"
        box_width = 5

        # Initialise variables
        self.balance = IntVar()

        self.multiplier = IntVar()
        self.multiplier.set(stakes)

        # Set starting balance to amount entered by user at start of game
        self.balance.set(starting_balance)

        # GUI Setup
        self.game_box = Toplevel()
        self.game_box.protocol('WM_DELETE_WINDOW', self.to_quit())
        self.game_frame = Frame(self.game_box)
        self.game_frame.grid()

        self.box_frame = Frame(self.game_frame)
        self.box_frame.grid(row=2, pady=10)

        # Prize Labels
        self.prize1_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize1_label.grid(row=0, column=0)

        self.prize2_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize2_label.grid(row=0, column=1, padx=10)

        self.prize3_label = Label(self.box_frame, text="?\n", font=box_text,
                                  bg=box_back, width=box_width, padx=10, pady=10)
        self.prize3_label.grid(row=0, column=2)
        # Heading Row
        self.heading_label = Label(self.game_frame, text="Heading",
                                   font="Arial 24 bold", padx=10,
                                   pady=10)
        self.heading_label.grid(row=0)

        # Balance Label
        self.balance_frame = Frame(self.game_frame)
        self.balance_frame.grid(row=1)

        self.balance_label = Label(self.game_frame, text="Balance...")
        self.balance_label.grid(row=4)

        self.play_button = Button(self.game_frame, text="Open Boxes", bg="#FFFF33",
                                  padx=10, pady=10, command=self.reveal_boxes)

        # Bind button to <enter> (Users can push enter to reveal the boxes)

        self.play_button.focus()
        self.play_button.bind('<Return>', lambda e: self.reveal_boxes())
        self.play_button.grid(row=3)

        # Help and Game Stats Frame
        self.help_and_stats_frame = Frame(self.game_frame)
        self.help_and_stats_frame.grid(row=6)

        # Help Button
        self.help_button = Button(self.help_and_stats_frame, text="Help / Rules",
                                  bg="#808080", fg="white", font="Arial",
                                  padx=10)
        self.help_button.grid(row=0, column=0, padx=10, pady=5)

        # Game Stats Button
        self.game_stats_button = Button(self.help_and_stats_frame, text="Game Stats...",
                                        bg="#003366", fg="white", font="Arial",
                                        padx=10)
        self.game_stats_button.grid(row=0, column=1, padx=10, pady=5)

    def reveal_boxes(self):
        # Retrieval the balance from the initial function...
        current_balance = self.balance.get()
        stakes_multiplier = self.multiplier.get()

        round_winnings = 0
        prizes = []
        backgrounds =[]
        for item in range(0, 3):
            prize_num = random.randint(1, 100)

            if 0 < prize_num <= 5:
                prize = "gold\n(${})".format(5 * stakes_multiplier)
                back_color = "#CEA935"  # Gold Color
                round_winnings += 5 * stakes_multiplier
            elif 5 < prize_num <= 25:
                prize = "silver\n(${})".format(2 * stakes_multiplier)
                back_color = "#B7B7B5"  # Silver Color
                round_winnings += 2 * stakes_multiplier
            elif 25 < prize_num <= 65:
                prize = "copper\n(${})".format(1 * stakes_multiplier)
                back_color = "#CD7F32"  # Bronze Color
                round_winnings += stakes_multiplier
            else:
                prize = "lead\n($0)"
                back_color = "#CC6600"  # Lead Color

            prizes.append(prize)
            backgrounds.append(back_color)

        # Display Prizes
        self.prize1_label.config(text=prizes[0], backgrounds=[0])
        self.prize2_label.config(text=prizes[1], backgrounds=[1])
        self.prize3_label.config(text=prizes[2], backgrounds=[2])

        # Deduct cost of game
        current_balance -= 5 * stakes_multiplier

        # Add winnings
        current_balance += round_winnings

        # Set balance to adjusted balance
        self.balance.set(current_balance)

        # Balance statement
        balance_statement = "Game Cost: ${}\n Payback: ${} \n" \
                            "Current Balance: ${}".format(5 * stakes_multiplier,
                                                          round_winnings,
                                                          current_balance)

        # Edit label so user can see their balance
        self.balance_label.configure(text=balance_statement)

        if current_balance < 5 * stakes_multiplier:
            self.play_button.config(state=DISABLED)
            self.game_box.focus()
            self.play_button.config(text="GAME OVER")

            balance_statement = "Current Balance: ${}\n"
            "Your balance is too low. You can only quit "
            "or view your stats. Sorry about that.".format(current_balance)
            self.balance_label.config(fg="#660000", font="Arial 10 bold",
                                      text=balance_statement)

    def to_quit(self):
        root.destroy()


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    start_program = Start(root)
    root.mainloop()