import time
from Cell import Cell


class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for x_axis in range(self.x1, self.num_rows*50, 50):
            column = []
            for y_axis in range(self.y1, self.num_cols*50, 50):
                column.append((x_axis, y_axis))
            self._cells.append(column)
        self._draw_maze(self._cells)

    def _draw_maze(self, matrix):
        for i in matrix:
            for j in i:
                
                Cell(
                    x1=j[0],
                    y1=j[1],
                    x2=j[0] + 50,
                    y2=j[1] + 50,
                    win=self.win.canvas,
                ).draw_cell()
                self._animate()
    def _animate(self):
        self.win.redraw()
        time.sleep(1)