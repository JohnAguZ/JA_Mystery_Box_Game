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

        # Mystery Heading (Row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game", bg=background_color,
                                       font=("Arial", "16", "bold"),
                                       padx=25, pady=25)
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
                                          padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry Box, Button and Error Label (Row 2)
        self.entry_error_frame = Frame(self.start_frame, width=200, bg=background_color)
        self.entry_error_frame.grid(row=2)

        self.start_amount_entry = Entry(self.start_frame,
                                        font="Arial 16 bold", width=20)
        self.start_amount_entry.grid(row=3)

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

        # Error Label
        self.amount_error_label = Label(self.start_frame, bg=background_color, text="")
        self.amount_error_label.grid(row=5)

        # Help and Game Stats Frame
        self.help_and_stats_frame = Frame(self.start_frame, bg=background_color)
        self.help_and_stats_frame.grid(row=6)

        # Help Button
        self.help_button = Button(self.help_and_stats_frame, text="Help / Rules",
                                  bg="#808080", fg="white", font=button_font,
                                  padx=10)
        self.help_button.grid(row=0, column=0, padx=10)

        # Game Stats Button
        self.game_stats_button = Button(self.help_and_stats_frame, text="Game Stats...",
                                        bg="#003366", fg="white", font=button_font,
                                        padx=10)
        self.game_stats_button.grid(row=0, column=1, padx=5)

    def to_game(self, stakes):
        starting_balance = self.start_amount_entry.get()

        # Set error background colours (and assume that there are no
        # errors at the start...
        error_back = "#ffafaf"
        has_errors = "no"

        # Change background to white (For testing purposes)...
        self.start_amount_entry.config(bg="white")
        self.amount_error_label.config(text="")

        try:
            starting_balance = int(starting_balance)

            if starting_balance < 5:
                has_errors = "yes"
                error_feedback = "Sorry, the least you " \
                                 "can play with is $5"
            elif starting_balance > 50:
                has_errors = "yes"
                error_feedback = "Too high! The most you can risk in " \
                                 "this game is $50"
            elif starting_balance < 10 and (stakes == 2 or stakes == 3):
                has_errors = "yes"
                error_feedback = "Sorry, you can oly afford to " \
                                 "play a low stakes game."
            elif starting_balance < 15 and stakes == 3:
                has_errors = "yes"
                error_feedback = "Sorry, you can oly afford to " \
                                 "play a medium stakes game."
        except ValueError:
            has_errors = "yes"
            error_feedback = "Please enter a dollar amount (No text / Decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback, fg="#ff1100")

        else:
            Game(self, stakes, starting_balance)

            # Hide start up window
            # root.withdraw()


class Game:
    def __init__(self, partner, stakes, starting_balance):
        print(stakes)
        print(starting_balance)


# main routine
if __name__ == "__main__":
    root = Tk()
    root.title("Mystery Box Game")
    start_program = Start(root)
    root.mainloop()
