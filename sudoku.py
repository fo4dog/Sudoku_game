import pgzrun       # импорт Pygame Zero
import random

WIDTH= 700          # создаем окно 700x900
HEIGHT= 900


sudokupole = Actor("sudokupole", center = (WIDTH/2,600/2+50))
youwin2 = Actor("youwin2", center = (-10000,-10000))
chisla = [0]*9
kletki = [0]*9
notsee = open('sudokunotsee.txt')
sudokupole = Actor("sudokupole", center = (WIDTH/2,600/2+50))      # загружаем Картино4ку поля как класс Actor и обозначаем его координаты
youwin2 = Actor("youwin2", center = (-10000,-10000))               # загружаем Картино4ку youwin2, которая будет высвечиваться при победе
chisla = [0]*9                                                     # создаем массивы 'числа' с 9 нулями 
kletki = [0]*9                                                     # создаем 'клетки' с 9 нулями                                                                                                      
notsee = open('sudokunotsee.txt')                                  # открываем файл sudokunotsee.txt (это файл с уже решенным судоку)
notsee = notsee.read()                                             # читаем файл sudokunotsee.txt 
                                                                  
see = open('sudokusee.txt')                                        # открываем и читаем файл sudokusee.txt (не заполненное судоку)
see = see.read()
i1 = 0
j1 = 0
a = 0

for i in range(0,9):
    chisla[i] =[0,0]
    chisla[i][1] = Actor("mychislo" + str(i+1), center = (50 + 32 + i*3 + i*64, 775))
    chisla[i][0] = Actor("white", center = (50 + 32 + i*64 + i*3, 775))
    kletki[i] = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
for i in range(0,9):                                                                       # в этом цикле присваеваем массивам актеров, с помощью которых будем делать начальное поле и числа для выбора в панели под полем
    chisla[i] = [0,0]                                                                      # делаем массив 'числа' двумерным
    chisla[i][1] = Actor("mychislo" + str(i+1), center = (50 + 32 + i*3 + i*64, 775))      # присваеваем второму элементу из пары в массиве 'числа' актера с картинкой числа и его координаты
    chisla[i][0] = Actor("white", center = (50 + 32 + i*64 + i*3, 775))                    # присваеваем первому элементу из пары в массиве 'числа' белый квадрат (фон) и его координаты
    kletki[i] = [[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0],[0,0,0]]  # делаем массив 'клетки' многомерным
    for j in range(0,9):
        kletki[i][j][0] = Actor("white", center = (50 + 3 + j + 32 + j*64 + j//3*3, 50 + 3 + i + 32 + i*64 + i//3*3))
        if see[i*9+j]=="0":
            kletki[i][j][1] = Actor("false0", center = (50 + 3 + j + 32 + j*64 + j//3*3, 50 + 3 + i + 32 + i*64 + i//3*3))
        else:
        kletki[i][j][0] = Actor("white", center = (50 + 3 + j + 32 + j*64 + j//3*3, 50 + 3 + i + 32 + i*64 + i//3*3)) # присваеваем первому элементу из тройки в массиве 'клетки' белый квадрат (фон) и его координаты
        if see[i*9+j]=="0":                                                                                           # если в ряде чисел, которые прорисовываем в начале встречается 0, то присваеваем второму элементу вместо нуля актера 
            kletki[i][j][1] = Actor("false0", center = (50 + 3 + j + 32 + j*64 + j//3*3, 50 + 3 + i + 32 + i*64 + i//3*3)) # белым квадратом, но с другим названием и его координаты
        else:                                                                                                              # иначе присваеваем актера с картинкой нужного числа и его координаты
            kletki[i][j][1] = Actor("mychislo" + see[i*9+j], center = (50 + 3 + j + 32 + j*64 + j//3*3, 50 + 3 + i + 32 + i*64 + i//3*3))
            kletki[i][j][2] = 1
kletki[0][0][0].image = "blue"
def stechkin(i1,j1,n):
            kletki[i][j][2] = 1                                                            # в третий элемент записываем единицу для отличия от простого белого квадрата
kletki[0][0][0].image = "blue"                                                             # 'cтавим курсор' на первую клеточку в таблице 
def stechkin(i1,j1,n):                                                                     # функция 'подсветки'
    global kletki
    for x in range(0,9):
        for y in range(0,9):
            if (x!=i1 or y!=j1) and kletki[x][y][0].image != "red":
                if kletki[x][y][1].image[-1] == kletki[i1][j1][1].image[-1] != "0":
            if (x!=i1 or y!=j1) and kletki[x][y][0].image != "red":                        # выбираем не красные клетки, которые находятся в тех же строке и столбце, что и выбранная клетка
                if kletki[x][y][1].image[-1] == kletki[i1][j1][1].image[-1] != "0":        # если находим по последним номерам названий изображений совпадающие числа, то подсвечиваем их фон нужным цветом 
                    kletki[x][y][0].image = n
                if x == i1:
                if x == i1:                                                                # подсвечиваем, если находятся в одной строке
                    kletki[x][y][0].image = n
                if y == j1:
                if y == j1:                                                                # подсвечиваем, если в одном столбце
                    kletki[x][y][0].image = n
                if i1//3*3 <= x < (i1//3 + 1)*3 and j1//3*3 <= y < (j1//3 + 1)*3 :
                if i1//3*3 <= x < (i1//3 + 1)*3 and j1//3*3 <= y < (j1//3 + 1)*3 :         # подсвечиваем, если в одном квадрате 3х3
                    kletki[x][y][0].image = n
def on_mouse_down(pos):
def on_mouse_down(pos):                                                                    # функция для нажатий 
    global i1, j1, b
    b = 0
    if kletki[i1][j1][2] == 0:
        for i in range(0,9):
            if chisla[i][1].collidepoint(pos):
                stechkin(i1,j1,"white")
                if chisla[i][1].image != "mychislo" + notsee[i1*9+j1]:
    if kletki[i1][j1][2] == 0:                                                             # если клетка изначально была пустая, то выполняем цикл
        for i in range(0,9):                                                               # цикл для выбора числа в панели под полем
            if chisla[i][1].collidepoint(pos):                                             # если на одно из чисел под полем кликнули, то:
                stechkin(i1,j1,"white")                                                    # красим клетку предыдущего выбранного числа в белый
                if chisla[i][1].image != "mychislo" + notsee[i1*9+j1]:                     # если выбранное число не совпадает с решением, то красим в красный
                    kletki[i1][j1][0].image = "red"
                else:
                else:                                                                      # если совпадает, то подсвечиваем синим
                    kletki[i1][j1][0].image = "blue"
                kletki[i1][j1][1].image = "chislo" + str(i+1)                              # ставим выбранное число на выбранное место и делаем его синего цвета
                stechkin(i1,j1,"grey")                                                     # подсвечиваем фон серым
                break
    for i in range(0,9):
    for i in range(0,9):                                                                   # циклы для выбора места в поле
        for j in range(0,9):
            if kletki[i][j][1].image[-1] == notsee[i*9 + j] != 0:                          # если клетка соответсвует той, которая должна стоять в ответе и не нулевая, то увечиличаем счетчик
                b += 1
            if kletki[i][j][0].collidepoint(pos):
                stechkin(i1,j1,"white")
                if kletki[i][j][0].image != "red":
            if kletki[i][j][0].collidepoint(pos):                                          # если на одну клетку на поле кликнули, то:
                stechkin(i1,j1,"white")                                                    # перекрашиваем предыдущую в белый
                if kletki[i][j][0].image != "red":                                         # если клетка не красная, то меняем на синий
                    kletki[i][j][0].image = "blue"
                if kletki[i1][j1][0].image == "blue" and (i1 != i or j1 != j):             # если клетка синяя, и координаты клетки не совпадают с текущей, делаем клетку белой
                    kletki[i1][j1][0].image = "white"
                i1 = i                                                                     # переделываем в глобальные переменные
                j1 = j
                stechkin(i1,j1,"grey")
    if b == 81 :
                stechkin(i1,j1,"grey")                                                     # делаем клетку серой
    if b == 81 :                                                                           # если по счетчику видно, что судоку решено, выводим надпись для победы
        youwin2.x = WIDTH/2
        youwin2.y = 700/2

def draw():
    screen.clear()
    screen.fill((0,0,0))
                                                                                         
    if youwin2.x < 0:
    if youwin2.x < 0:                                                                      # если не победа, то прорисовываем поле, числа и фоны
        for i in range(0,9):
            chisla[i][0].draw()
            chisla[i][1].draw()
            for j in range(0,9):
                kletki[i][j][0].draw()
                kletki[i][j][1].draw()
    youwin2.draw()                                                                        # конец игры
pgzrun.go()
