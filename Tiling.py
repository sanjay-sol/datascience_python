import math
import seaborn as sns
tile=1
def TileBoard(toprow,topcol,defrow,defcol,size):
    global tile
    tile_to_use=tile
    if size==1:
        return
    tile+=1
    quad=size//2
    #first quadrant
    if (defrow<(toprow+quad))and (defcol<(topcol+quad)):
        TileBoard(toprow,topcol,defrow,defcol,quad)
    else:
        board[toprow+quad-1][topcol+quad-1]=tile_to_use
        TileBoard(toprow,topcol,toprow+quad-1,topcol+quad-1,quad)
    #second quadrant
    if (defrow<toprow+quad)and(defcol>=topcol+quad):
        TileBoard(toprow,topcol+quad,defrow,defcol,quad)
    else:
        board[toprow+quad-1][topcol+quad]=tile_to_use
        TileBoard(toprow,topcol+quad,toprow+quad-1,topcol+quad,quad)
    #third quadrant
    if (defrow>=toprow+quad)and(defcol<topcol+quad):
        TileBoard(toprow+quad,topcol,defrow,defcol,quad)
    else:
        board[toprow+quad][topcol+quad-1]=tile_to_use
        TileBoard(toprow+quad,topcol,toprow+quad,topcol+quad-1,quad)
    #fourth quadrant
    if (defrow>=toprow+quad)and(defcol>=topcol+quad):
        TileBoard(toprow+quad,topcol+quad,defrow,defcol,quad)
    else:
        board[toprow+quad][topcol+quad]=tile_to_use
        TileBoard(toprow+quad,topcol+quad,toprow+quad,topcol+quad,quad)
def isPower2(x):
    if math.ceil(math.log10(x)/math.log10(2))==math.floor(math.log10(x)/math.log10(2)):
        return True
    return False
n=int(input('enter size of chessboard'))
if(isPower2(n)==False):
    print('re enter a size which is a power of 2!!!!')
    n=int(input())
board= [[0 for i in range(n)] for j in range(n)]
print('enter index of defective tile')
def_row=int(input())
def_col=int(input())
board[def_row][def_col]=-1
TileBoard(0,0,def_row,def_col,n)     
sns.heatmap(board,annot=True,xticklabels=False,yticklabels=False)