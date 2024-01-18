from Cell import Cell
from Window import Window


win=Window(800,600,"Window")
cell=Cell(x1=1,y1=1,x2=100,y2= 100,win=win.canvas,has_right_wall=False)
cell.draw_cell()
c2=Cell(x1=100,y1=1,x2=100+100,y2= 100,win=win.canvas,has_left_wall=False,has_bottom_wall=False)
c2.draw_cell()
cell.draw_move(c2)
c3=Cell(x1=100,y1=100,x2=100+100,y2= 100+100,win=win.canvas,has_top_wall=False)
c3.draw_cell()
c2.draw_move(c3)
win.redraw()
win.wait_for_close()
