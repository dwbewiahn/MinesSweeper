from tkinter import Button
import random
import settings


class Cell:
    all = []
    def __init__(self, x, y, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None
        self.x = x
        self.y = y

        Cell.all.append(self) # Append the object to the all list


    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,

        )

        btn.bind('<Button-1>', self.left_click_actions)
        btn.bind('<Button-3>', self.right_click_actions)

        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if self.is_mine:
            self.show_mine()

    def show_mine(self):
        # a logic to game over
        self.cell_btn_object.configure(bg='red')

    def right_click_actions(self, event):
        print(event)


    @staticmethod
    def randomize_mines():
        picked_cells = random.sample(
            Cell.all, settings.MINES_COUNT
        )
        for picked_cell in picked_cells:
           picked_cell.is_mine = True

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"