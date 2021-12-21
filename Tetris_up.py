#print("\n".join(["▐▐ . .","▐▐▐▐▐▐"]))

import win32api as win,os,time,random as r

Tetr = [["----#X#---","------#---"],["----#X#---","----#-----"],["----#X#---","-----#----"],
        ["---##X#---","----------"],["----##----","----##----"],["----##----","-----X#---"],["-----##---","----#X----"]]


class Tetris_piece():
    def __init__(   self, cord = [], cent = []):
        self.cordinate = cord
        self.center = cent
    def Set_cord_cent(self,cord,cent):
        self.cordinate = cord
        self.center = cent
    def Pause(self):
        os.system('cls||clear')
        print("\n"*10, "PAUSE".center(120, " "), "\n"*10)
        while 1:
            inpu = win.GetKeyState(0x1B)
            if inpu > 0:
                os.system('cls||clear')
                break
    def Left(self):
        DO = True
        for y,x in self.cordinate:
            if new[y][x-1] == "@" or x-1 < 0:
                DO = False
                break
        if DO:
            for y,x in self.cordinate:
                new[y] = new[y][:x] + "-" + new[y][x+1:]
            for y,x in self.cordinate:
                new[y] = new[y][:x-1] + "#" + new[y][x:]    
            for i in range(len(self.cordinate)):
                self.cordinate[i][1] -= 1
            if len(self.center) != 0:
                self.center[1] -= 1
    def Right(self): 
        DO = True
        for y,x in self.cordinate:
            if x+1 >= len(new[0]) or new[y][x+1] == "@":
                DO = False
                break
        if DO:
            for y,x in self.cordinate:
                new[y] = new[y][:x] + "-" + new[y][x+1:]
            for y,x in self.cordinate:
                new[y] = new[y][:x+1] + "#" + new[y][x+2:]    
            for i in range(len(self.cordinate)):
                self.cordinate[i][1] += 1
            if len(self.center) != 0:
                self.center[1] += 1
    def Down(self):
        DO = True
        for y,x in self.cordinate:
            if y+1 >= len(new) or new[y+1][x] == "@":
                DO = False
                break
        if DO:
            for y,x in self.cordinate:
                new[y] = new[y][:x] + "-" + new[y][x+1:]
            for y,x in self.cordinate:
                new[y+1] = new[y+1][:x] + "#" + new[y+1][x+1:]    
            for i in range(len(self.cordinate)):
                self.cordinate[i][0] += 1
            if len(self.center) != 0:
                self.center[0] += 1
    def Rotate_clock(self):
        loc_cor = []
        for y,x in self.cordinate:
            if len(self.center) == 0:
                break
            new[y] = new[y][:x] + "-" + new[y][x+1:]
            loc_cor.append([x-self.center[1], self.center[0]-y])
        for y,x in loc_cor:
            if len(self.center) == 0:
                break
            elif len(new) <= self.center[0]+y:
                for i in range(len(new)):
                    new[i] = old[i]
                    new[i] = new[i].replace("#","-")
                for i,j in self.cordinate:
                    new[i] = new[i][:j] + "#" + new[i][j+1:]
                break
            new[self.center[0]-(y*-1)] = new[self.center[0]-(y*-1)][:(self.center[1]+x)] + "#" + new[self.center[0]-(y*-1)][(self.center[1]+x)+1:]
            if (old[self.center[0]+y].count("@") > new[self.center[0]+y].count("@")) or (len(new[self.center[0]+y]) > len(old[self.center[0]+y])) or (self.center[0]+y < 0):
                for i in range(len(new)):
                    new[i] = old[i]
                    new[i] = new[i].replace("#","-")
                for i,j in self.cordinate:
                    new[i] = new[i][:j] + "#" + new[i][j+1:]
                break
            elif loc_cor[-1] == [y,x]:
                for i,j in loc_cor:
                    self.cordinate[loc_cor.index([i,j])] = [self.center[0]+i, (self.center[1]+j)]
    def Rotate_counterclock(self):
        loc_cor = []
        for y,x in self.cordinate:
            if len(self.center) == 0:
                break
            new[y] = new[y][:x] + "-" + new[y][x+1:]
            loc_cor.append([x-self.center[1], self.center[0]-y])
        for x,y in loc_cor:
            if len(self.center) == 0 :
                break
            elif len(new) <= self.center[0]-x:
                for i in range(len(new)):
                    new[i] = old[i]
                    new[i] = new[i].replace("#","-")
                for i,j in self.cordinate:
                    new[i] = new[i][:j] + "#" + new[i][j+1:]
                break
            new[self.center[0]-x] = new[self.center[0]-x][:(self.center[1]-y)] + "#" + new[self.center[0]-x][(self.center[1]-y)+1:]
            if (old[self.center[0]-x].count("@") > new[self.center[0]-x].count("@")) or (len(new[self.center[0]-x]) > len(old[self.center[0]-x])) or (self.center[0]-x < 0):
                for i in range(len(new)):
                    new[i] = old[i]
                    new[i] = new[i].replace("#","-")
                for i,j in self.cordinate:
                    new[i] = new[i][:j] + "#" + new[i][j+1:]
                break
            elif loc_cor[-1] == [x,y]:
                for i,j in loc_cor:
                    self.cordinate[loc_cor.index([i,j])] = [self.center[0]-i, self.center[1]-j]
    def Check_end(self):
        for i,j in self.cordinate:
            if (i+2 > len(new)) or (new[i+1][j] == "@"):
                return True     
    def Clean_line(self):
        global new, score_line, level
        num = 0
        for i in range(len(old)):
            if "-" not in new[i]:
                num += 1
                del new[i]
                c = ["----------"]
                for i in range(len(new)):
                    c.append(new[i])
                new = c
        if num == 1:
            score_line[0] += 40*(level+1)
        if num == 2:
            score_line[0] += 100*(level+1)
        if num == 3:
            score_line[0] += 300*(level+1); 
        if num == 4:
            score_line[0] += 1200*(level+1); 
        score_line[1] += num
def Appear(a,b):
    cor,cen = [],[]
    rand = r.randint(0,len(Tetr)-1)
    for i in range(len(Tetr[rand])):
        for j in range(len(Tetr[rand][i])):
            if Tetr[rand][i][j] in "#X" :
                cor.append([i,j])
                if Tetr[rand][i][j] == "X":
                    cen = [i,j]
                a[i] = a[i][:j] + "#" + a[i][j+1:]
                b[i] = b[i][:j] + "#" + b[i][j+1:]
    Tetris.Set_cord_cent(cor,cen)
def update_lvl():
    global level
    if score_line[1] > 10*(level+1):
        level += 1
def Game_over():
    os.system('cls||clear')
    print("\n"*10, "GAME OVER!".center(120, " "), "\n"*10)
    input()
    os.system('cls||clear')
    out = []
    with open("score_table.txt", "+r") as st:
        sco_tab = st.readlines()
        out = []
        for i in range(len(sco_tab)):
            if int(sco_tab[i].split(" ")[3]) < score_line[0]:
                n = input("write your name: ")
                out.append(n[0:4] + " | score: " + str(score_line[0])+" \n")
                for i in range(i,len(sco_tab)-1):
                    out.append(sco_tab[i])
                break
            elif int(sco_tab[i].split(" ")[3]) > score_line[0]:
                out.append(sco_tab[i])
        st.seek(0)
        st.writelines(out)
        os.system('cls||clear')
        print("Score table")
        for i in out:
            print(i,end="")
    exit()

old = []
new = []
display = []
end_time, start_time = 2,0
frame, level, end = 0, 0, 0 
score_line = [0,0]
Tetris = Tetris_piece()
 

for i in range(20):
    old.append("----------")
    new.append("----------")
    display.append("----------")

while True:
    if new[0][5] == "@":
        Game_over() 
    Appear(old,new)

    end,frame = 0,0
    while True:
        frame += 1

        print(score_line[0], level)
        for i in range(len(display)):
            display[i] = new[i].center(120," ") 
        print("\n".join(display))
        for i in range(len(new)):
            old[i] = new[i]

        a = [win.GetKeyState(0x25),win.GetKeyState(0x28),win.GetKeyState(0x27),win.GetKeyState(0x58),win.GetKeyState(0x5A),win.GetKeyState(0x1B)]
        if (a[1] < 0) or (frame % 3 == 0):
            Tetris.Down() 
        if a[0] < 0:
            Tetris.Left()
        if a[2] < 0:
            Tetris.Right()
        if a[3] < 0:
            Tetris.Rotate_clock()
        if a[4] < 0:
            Tetris.Rotate_counterclock()
        if a[5] < 0:
            Tetris.Pause()
        time.sleep(0.02)
        os.system('cls||clear')

        if Tetris.Check_end() and end >= 3:
            for i,j in Tetris.cordinate:
                new[i] = new[i][:j] + "@" + new[i][j+1:]
                old[i] = old[i][:j] + "@" + old[i][j+1:]
            Tetris.Clean_line()
            update_lvl()
            break
        elif Tetris.Check_end(): end += 1 
