"""Manipulating the single cell """
from types import CellType
from Line import Line


class Cell:
    """
    Manipulating the single cell
    """

    def __init__(
        self,
        x1,
        x2,
        y1,
        y2,
        win,
        has_left_wall=True,
        has_right_wall=True,
        has_top_wall=True,
        has_bottom_wall=True,
    ):
        self.has_left_wall = has_left_wall
        self.has_right_wall = has_right_wall
        self.has_top_wall = has_top_wall
        self.has_bottom_wall = has_bottom_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._win = win

    def __draw_line(self, win, x1, y1, x2, y2, color="black", width=3):
        return Line(canvas=win, x1=x1, y1=y1, x2=x2, y2=y2, color=color, width=width)

    def draw_cell(self):
        """Draw a cell"""
        height = self._y2 - self._y1
        width = self._x2 - self._x1
        if self.has_top_wall:
            self.__draw_line(
                win=self._win,
                x1=self._x1,
                y1=self._y1,
                x2=(self._x1 + width),
                y2=self._y1,
            ).draw()
        if self.has_bottom_wall:
            self.__draw_line(
                win=self._win,
                x1=self._x1,
                y1=self._y1 + height,
                x2=self._x1 + width,
                y2=self._y1 + height,
            ).draw()
        if self.has_left_wall:
            self.__draw_line(
                win=self._win,
                x1=self._x1,
                y1=self._y1,
                x2=self._x1,
                y2=(self._y1 + height),
            ).draw()
        if self.has_right_wall:
            self.__draw_line(
                win=self._win,
                x1=self._x1 + width,
                y1=self._y1,
                x2=self._x1 + width,
                y2=self._y1 + height,
            ).draw()   

    def get_middle(self):
        """
        returns the middle point of the cell.
        """
        return ((self._x1 + self._x2)//2 , (self._y1 + self._y2)//2)
    def draw_move(self,to_cell,undo=False):
        """
        draw a line base cell to target cell.
        """
        self.__draw_line(
            win=self._win,
            x1=self.get_middle()[0],y1=self.get_middle()[1],
            x2=to_cell.get_middle()[0],y2=to_cell.get_middle()[1],
            color=["grey" if undo else "red"]
        ).draw()