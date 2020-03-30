from tkinter import *
from functools import partial     # To prevent unwanted windows
import random


class Start:
    def __init__(self, parent):

        # GUI to get starting balance and stakes
        self.start_frame = Frame(padx=10, pady=10)
        self.start_frame.grid()

        # Mystery Heading (Row 0)
        self.mystery_box_label = Label(self.start_frame, text="Mystery Box Game",
                                       font="Arial 19 bold")
        self.mystery_box_label.grid(row=0)

        # Initial Instructions (Row 1)
        self.mystery_instructions = Label(self.start_frame, font="Arial 10 italic",
                                          text="Please enter a dollar amount "
                                               "(between $5 and $50) in the box "
                                               "below. Then choose the stakes. "
                                               "The higher the stakes, the more "
                                               "you can win!",
                                          wrap=275, justify=LEFT, padx=10, pady=10)
        self.mystery_instructions.grid(row=1)

        # Entry Box (Row 2)
        self.start_amount_entry = Entry(self.start_frame, font="Arial 16 bold")
        self.start_amount_entry.grid(row=2)

        # Play Button Frame (Note: Not Youtube) (Row 3)
        self.stakes_frame = Frame(self.start_frame)
        self.stakes_frame.grid(row=3)

        # Buttons go here...
        button_font = "Arial 12 bold"
        # Orange Low Stakes Button
        self.low_stakes_button = Button(self.stakes_frame, text="Low ($5)",
                                        command=lambda: self.to_game(1),
                                        font=button_font, bg="#FC9003")
        self.low_stakes_button.grid(row=0, column=0, pady=10)

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

        # error label (added by GK)
        self.amount_error_label = Label(self.start_frame, text="")
        self.amount_error_label.grid(row=4)

        # Help Button
        self.help_button = Button(self.start_frame, text="Help / Rules",
                                  bg="#808080", fg="white", font=button_font)
        self.help_button.grid(row=5, pady=10)

        #

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
                error_feedback = "Sorry, the least you" \
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
            error_feedback = "Pleas enter a dollar amount (No text / Decimals)"

        if has_errors == "yes":
            self.start_amount_entry.config(bg=error_back)
            self.amount_error_label.config(text=error_feedback)

        else:
            Game(self, stakes, starting_balance)

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
