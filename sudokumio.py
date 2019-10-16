import pygame, sys
from pygame.locals import *


FPS  =  10 
multventana  = 5   
Tamaño_de_ventana  =  81
Ancho  =  Tamaño_de_ventana  *   multventana
Alto  =  Tamaño_de_ventana  *  multventana
CuadriculaP =  ( Tamaño_de_ventana  *  multventana )  //  3
CeldaS = CuadriculaP // 3
DetEspacio = CeldaS /3

Ancho = 460
Alto = 405
Blanco = (255,255,255)
Negro = (0,  0,  0)
Gris = (200, 200, 200)
Verde = (0  ,255, 0 )

def  DibujarCuadriculas(): 
    for x in range(0, Ancho, CeldaS): #Dibuja las lineas verticales
        pygame.draw.line(Pantalla,Gris, (x,0),(x,Alto))
    for y in range (0, Alto, CeldaS): #Dibuja las lineas horizontales
        pygame.draw.line(Pantalla, Gris, (0,y), (Ancho, y))
    #Dibuja las lineas mayores
    for x in range(0, Ancho, CuadriculaP): #Dibuja las lineas verticales
        pygame.draw.line(Pantalla, Negro, (x,0),(x,Alto))
    for y in range (0, Alto, CuadriculaP): #Dibuja las lineas horizontales
        pygame.draw.line(Pantalla, Negro, (0,y), (Ancho, y))    
    return None
 
def IniciarCeldas():
    CuadriculaActual = {}
    Celdallena = [1,2,3,4,5,6,7,8,9]
    for CoordenadasX in range(0,9):
        for CoordenadasY in range(0,9):
            CuadriculaActual[CoordenadasX,CoordenadasY] = list(Celdallena) #Copia lista
    return CuadriculaActual
#Toma los números restantes y los muestra en las celdas. 
def MostrarCeldas(CuadriculaActual):
    #Crea factores para mostrar los numeros en la celda correcta
    FactorX = 0
    FactorY = 0
    for item in CuadriculaActual: 
        DatosdeCelda = CuadriculaActual[item] 
        for Numero in DatosdeCelda: 
            if Numero != ' ': 
                Factorx = ((Numero-1)%3) 
                if Numero <= 3:
                    FactorY = 0
                elif Numero <=6:
                    FactorY = 1
                else:
                    FactorY = 2
                if DatosdeCelda.count(' ') < 8:    
                    LLenarCeldas(Numero,(item[0]*CeldaS)+(Factorx*DetEspacio),(item[1]*CeldaS)+(FactorY*DetEspacio),'Chico')
                else:
                    LLenarCeldas(Numero,(item[0]*CeldaS),(item[1]*CeldaS),'Grande')
    return None
def  LLenarCeldas ( DatosdeCelda ,  x ,  y , Tamaño ): 
    if  Tamaño  ==  'Chico' : 
        RecorrerCeldas  =  BASICFONT . render ( ' % s '  % ( DatosdeCelda ),  True ,  Gris ) 
    elif  Tamaño  ==  'Grande' : 
        RecorrerCeldas  =  LARGEFONT . render ( ' % s '  % (DatosdeCelda ),  True ,  Verde ) 
        
    cellRect  =  RecorrerCeldas . get_rect () 
    cellRect . topleft  =  ( x ,  y ) 
    Pantalla . blit ( RecorrerCeldas ,  cellRect )


def NumeroSeleccionado(mousex, mousey, CuadriculaActual):


    xNumero = (mousex*31) // Ancho 
    yNumero = (mousey*31) // Ancho 
    
    modXNumero = xNumero % 3
    modYNumero = yNumero % 3       
    if modXNumero == 0:
    
        xChoices = [1,4,7]
        Numero = xChoices[modYNumero]        
    elif modXNumero == 1:

        xChoices = [2,5,8]
        Numero = xChoices[modYNumero]
    else:
        xChoices = [3,6,9]
        Numero = xChoices[modYNumero]
    #Determina la celda en la que estamos
    xNumeroCelda = xNumero // 3
    yNumeroCelda = yNumero // 3
   
    
    EstadoActual = CuadriculaActual[xNumeroCelda,yNumeroCelda]
    incNum = 0
    
    while incNum < 9:
        
        if incNum+1 != Numero:
            EstadoActual[incNum] = ' ' 
        else:
            EstadoActual[incNum] = Numero 
        
        CuadriculaActual[xNumeroCelda,yNumeroCelda] = EstadoActual
        incNum += 1
    CuadriculaActual = RefrescarCuadricula(CuadriculaActual)
    return CuadriculaActual    
def RefrescarCuadricula(CuadriculaActual):
    Celdallena = [1,2,3,4,5,6,7,8,9]
    for CoordenadasX in range(0,9):
        for CoordenadasY in range(0,9):
            DatosdeCelda = CuadriculaActual[CoordenadasX, CoordenadasY]
            if DatosdeCelda.count(' ') < 8:
                CuadriculaActual[CoordenadasX,CoordenadasY] = list(Celdallena) #Copia lista
    return CuadriculaActual    
def Disponibilidad(CuadriculaActual):
    for item in CuadriculaActual: 
        DatosdeCelda = CuadriculaActual[item] 
        if DatosdeCelda.count(' ') == 8: 
            for Numero in DatosdeCelda: 
                if Numero != ' ':
                    updateNumero = Numero
            CuadriculaActual = BorrarX(CuadriculaActual, item, updateNumero)
            CuadriculaActual = BorrarY(CuadriculaActual, item, updateNumero)
            CuadriculaActual = EliminarCuadricula(CuadriculaActual, item, updateNumero)

    return CuadriculaActual
def BorrarX(CuadriculaActual, item, Numero):
    for x in range(0,9):
        if x != item[0]:
            EstadoActual = CuadriculaActual[(x,item[1])]
            EstadoActual[Numero-1] = ' '
            CuadriculaActual[(x,item[1])] = EstadoActual
    return CuadriculaActual    
def BorrarY(CuadriculaActual, item, Numero):
    for y in range(0,9):
        if y != item[1]:
            EstadoActual = CuadriculaActual[(item[0],y)]
            EstadoActual[Numero-1] = ' '
            CuadriculaActual[(item[0],y)] = EstadoActual
    return CuadriculaActual        
def EliminarCuadricula(CuadriculaActual, item, Numero):
    
    if item[0] < 3:
        CuadriculaX = [0,1,2]
    elif item[0] > 5:
        CuadriculaX = [6,7,8]
    else: CuadriculaX = [3,4,5]

    if item[1] < 3:
        X = [0,1,2]
    elif item[1] > 5:
        X = [6,7,8]
    else: X = [3,4,5]
    
    
    for x in CuadriculaX:
        for y in X:
            if (x,y) != item: 
                EstadoActual = CuadriculaActual[(x,y)] 
                EstadoActual[Numero-1] = ' ' 
                CuadriculaActual[(x,y)] = EstadoActual
                
    return CuadriculaActual      
def main():
    global FPSCLOCK, Pantalla

    pygame.init()

    FPSCLOCK = pygame.time.Clock()

    Pantalla = pygame.display.set_mode((405,405)) 
    mouseClicked  =  False 
    
    

    pygame.display.set_caption('Sudoku.py')
    global BASICFONT, BASICFONTTamaño, LARGEFONT, LARGEFONTTamaño
    BASICFONTTamaño = 15
    LARGEFONTTamaño = 55
    BASICFONT = pygame.font.Font('freesansbold.ttf', BASICFONTTamaño)
    LARGEFONT = pygame.font.Font('freesansbold.ttf', LARGEFONTTamaño)
    
    CuadriculaActual = IniciarCeldas()
    

    while True: 
        mouseClicked = False
        
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEMOTION:
                mousex, mousey = event.pos

            
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
                mouseClicked = True

            if mouseClicked == True:
                
            
                CuadriculaActual = NumeroSeleccionado(mousex, mousey, CuadriculaActual)
                Disponibilidad(CuadriculaActual)
        Pantalla.fill(Blanco)
        MostrarCeldas(CuadriculaActual)
        DibujarCuadriculas()
        
        pygame.display.update()
        FPSCLOCK.tick(FPS)
if __name__=='__main__':
    main()         
    