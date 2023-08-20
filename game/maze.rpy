# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Maze cleared")

transform pan_view:
    yalign 0.0
    ease 6.0 yalign 1.0
    ease 6.0 yalign 0.0
    repeat 2

default sX = 160
default sY = 32
default dist = 5
default gX = 160 
default gY = 32 
default standWalk = 0
default mX = -800
default mY = -800

default vright = True
default goup = True
default move = False

default eX =400
default eY = 270
default eX2= 950
default eY2 = -8


image slime2 = "enemy slime2"
image slime3 = "enemy slime3"
image mask = "mask2"

init python:
    
    def declarevar():
        global eX , vright,sX,eX2,eY2,goup
        eX2= 950
        eY2 = -8
        vright =True
        goup =True
        eX = 400
        sX = 160
        sY = 32
        return eX

    def getex():
        global eX
        return eX

    def getey():
        global eY2
        return eY2

    def getxy(x,y):
        sX = x
        sY = y
        print("called down: "+str(sX)+" "+str(sY))
        return True

    def canmoveLeft(x,y):
        sX = x
        sY = y
        if (sX==125 and sY<167):
            return False
        elif (sX==640 and sY<112 and sY>37):
            return False
        elif (sX==335 and sY<32 and sY>-28):
            return False
        elif (sX==935 and sY<162 and sY>92):
            return False
        elif (sX==935 and sY<27 and sY>-28):
            return False
        elif (sX==850 and sY<112 and sY>22):
            return False
        elif (sX==1010 and sY<12 and sY>-23):
            return False
        elif (sX==1190 and sY<112 and sY>-23):
            return False
        elif (sX==1110 and sY<292 and sY>162):
            return False
        elif (sX==1015 and sY<162 and sY>92):
            return False
        elif (sX==685 and sY<367 and sY>237):
            return False
        elif (sX==980 and sY<547 and sY>417):
            return False
        elif (sX==895 and sY<417 and sY>287):
            return False
        elif (sX==215 and sY<502 and sY>372):
            return False
        elif (sX==40 and sY<2000 and sY>282):
            return False
        elif (sX==470 and sY<452 and sY>287):
            return False
        elif (sX==385 and sY<287 and sY>242):
            return False
        elif (sX==470 and sY<242 and sY>162):
            return False
        else:
            return True
    
    def canmoveRight(x,y):
        sX = x
        sY = y
        if (sX==185 and sY<112):
            return False
        elif (sX==700 and sY<112 and sY>-18):
            return False
        elif (sX==995 and sY<12 and sY>-18):
            return False
        elif (sX==1080 and sY<112 and sY>-23):
            return False
        elif (sX==1255 and sY<162 and sY>-23):
            return False
        elif (sX==1165 and sY<292 and sY>162):
            return False
        elif (sX==995 and sY<162 and sY>92):
            return False
        elif (sX==920 and sY<162 and sY>92):
            return False
        elif (sX==525 and sY<247 and sY>162):
            return False
        elif (sX==610 and sY<292 and sY>247):
            return False
        elif (sX==525 and sY<372 and sY>292):
            return False
        elif (sX==955 and sY<367 and sY>237):
            return False
        elif (sX==1035 and sY<497 and sY>362):
            return False
        elif (sX==740 and sY<412 and sY>292):
            return False
        elif (sX==525 and sY<502 and sY>412):
            return False
        elif (sX==95 and sY<2000 and sY>377):
            return False
        elif (sX==270 and sY<452 and sY>282):
            return False
        else:
            return True

    def canmoveUp(x,y):
        sX = x
        sY = y
        if (sX<190 and sX>120 and sY==-18):
            return False
        elif (sX<640 and sX>185 and sY==117):
            return False
        elif (sX<710 and sX>335 and sY==-18):
            return False
        elif (sX<855 and sX>112 and sY==112):
            return False
        elif (sX<935 and sX>845 and sY==27):
            return False
        elif (sX<1010 and sX>930 and sY==-13):
            return False
        elif (sX<1010 and sX>995 and sY==12):
            return False
        elif (sX<1080 and sX>1005 and sY==-18):
            return False
        elif (sX<1190 and sX>1080 and sY==112):
            return False
        elif (sX<615 and sX>525 and sY==242):
            return False
        elif (sX<685 and sX>525 and sY==367):
            return False
        elif (sX<955 and sX>685 and sY==237):
            return False
        elif (sX<1040 and sX>955 and sY==367):
            return False
        elif (sX<2000 and sX>1035 and sY==497):
            return False
        elif (sX<270 and sX>60 and sY==282):
            return False
        elif (sX<470 and sX>270 and sY==452):
            return False
        elif (sX<470 and sX>385 and sY==242):
            return False
        else:
            return True
    
    def canmoveDown(x,y):
        sX = x
        sY = y
        if (sY==157 and sX<460):
            return False
        elif (sY==172 and sX==460):
            return False
        elif (sY==172 and sX>529 and sX<536):
            return False
        elif (sY==162 and sX>525 and sX<1110):
            return False    
        elif (sY==92 and sX>920 and sX<935):
            return False  
        elif (sY==92 and sX>995 and sX<1010):
            return False    
        elif (sY==172 and sX>1105 and sX<1105):
            return False
        elif (sY==172 and sX>1169 and sX<1180):
            return False
        elif (sY==157 and sX>1175):
            return False
        elif (sY==287 and sX>1100 and sX<1170 ):
            return False
        elif (sY==287 and sX>360 and sX<470 ):
            return False
        elif (sY==287 and sX>360 and sX<470 ):
            return False
        elif (sY==287 and sX>525 and sX<625 ):
            return False
        elif (sY==412 and sX>525 and sX<750  ):
            return False
        elif (sY==497 and sX>200 and sX<520  ):
            return False
        elif (sY==372 and sX>90 and sX<215  ):
            return False
        elif (sY==597 and sX>20 and sX<120  ):
            return False
        elif (sY==287 and sX>740 and sX<900  ):
            return False
        elif (sY==417 and sX>875 and sX<980  ):
            return False
        elif (sY==32 and sX>330 and sX<640  ):
            return False
        elif (sY==547 and sX>965  ):
            return False
        else:
            return True
           




    def cam():
        sX = x
        sY = y
        print("called down: "+str(sX)+" "+str(sY))
        if sY<162 and sX<1100:
            print("top")
            if sX<180:
                return True
            elif sY>112:
                return True
            elif sX<700 and sX>640:
                return True
            elif sY<=32:
                return True
            elif sX<1250 and sX>850 and sX!=930 and sX!=1000:
                return True
        elif sY<530 and sX>460 and sY>=162:
            print("middle")
            if sX>1100 and sX<1170 and sY<273:
                return True
            elif sX>460 and sX<530 and sY<502:
                return True
            elif sX>232 and sX<450 and sY<282:
                return True
            elif sX>550 and sX<610 and sY<282:
                return True
            else:
                return False
        elif sY<502 and sY>452:
            print("lower left")
            if sX>210:
                return True
            elif sY<372:
                return True
            elif sX<110:
                return True
        elif sY<672 and sX>40 and sX<110:
            return True      
        elif sX>530 and sY<412:
            return True
        else:
            return False
        


        return False


    def mright():
        global eX, vright
        if eX < 550 and vright:
            eX = eX+10
            print(eX)
            if eX >= 550:
                vright = False
        elif vright == False:
            eX = eX-10
            if eX <= 400:
                vright = True
        else:
            vright = True
        return eX
    def mup():
        global eY2, goup
        if eY2 < 98 and goup:
            eY2 = eY2+10
            print(eY2)
            if eY2 >= 98:
                vright = False
        elif goup == False:
            eY2 = eY2-10
            if eY2 <= -8:
                goup = True
        else:
            goup = True
        return eY2

image charstandidle = im.MatrixColor("char standidle.jpg",im.matrix.brightness(1))


label maze:

    # show mask:
    #     xpos mX
    #     ypos mY
    show mapmaze4
    
    play music "<from 0 to 17>../audio/ForestAmbience.mp3" fadein 1.0 fadeout 1.0 volume 0.7
    
    $ declarevar()

    show slime3 #behind mask:
        xpos 32
        ypos 32

    show slime2 #behind mask:
        xpos eX
        ypos eY

    show slime3 #behind mask:
        xpos eX2
        ypos eY2

    show slime2:
        linear 1.0 xpos mright()
        linear 1.0 xpos mright()
        linear 1.0 xpos mright()
        linear 1.0 xpos mright()
        linear 1.0 xpos mright()
        repeat
    show slime3:
        linear 1.0 ypos mup()
        linear 1.0 ypos mup()
        linear 1.0 ypos mup()
        linear 1.0 ypos mup()
        linear 1.0 ypos mup()
        repeat

    show char walkright:
        xpos sX
        ypos sY
    
    show screen keynav

    
    

    
    $ ui.interact()






label moveenemy:
    while move:
        if eX<240 and vright:
            while eX<240:
                $eX = eX+1
                show slime2:
                    linear 1.0 xpos eX
            $vright = False
        elif eX ==240 and vright == False:
            while eX>200:
                $eX = eX-1
                show slime2:
                    linear 1.0 xpos eX
            $vright = True

    



label enemy:
    if gX>getey() and gX<(getex()+104) :
        if gY>eY and gY<eY+52:
            jump reset
        else:
            jump standstill
    elif gX>eX2 and gX<(eX2+104) :
        if gY>getey() and gY<getey()+22:
            jump reset
        else:
            jump standstill
    elif gX>1190 and gY<2:
        jump won
    else:
        jump standstill


label won:
    play audio "../audio/victory.mp3" volume 0.5
    e "You did it, Maze Cleared!"
    jump scene16


label reset:
    play audio "<from 0 to 1>../audio/failure3.mp3" fadeout 1.0
    $gX =sX
    $gY =sY
    $mX =-800
    $mY =-800
    #fadein .1 fadeout 0.2 volume 0.5
    show char walkright:
        xpos gX
        ypos sY
    show masktest:
        xpos mX
        ypos mY
    jump standstill

label standstill:
    stop sound fadeout 1.0
    $ ui.interact()

label stopmusic:
    pause 1
    play music "../audio/victory.mp3" volume 0.5



label Walkright:
    if canmoveRight(gX,gY):
        $gX = gX+dist
        $mX = mX+dist
        play sound "./audio/running grass.mp3"
        show char walkright:
            linear dist/100.0 xpos gX
        show masktest:
            linear dist/100.0 xpos mX
        $ renpy.pause(delay=dist/100.0,hard=True)
        jump enemy
    else:
        jump standstill


label Walkleft:
    if canmoveLeft(gX,gY):
        $gX = gX-dist
        $mX = mX-dist
        play sound "./audio/running grass.mp3"
        show char walkright:
            linear dist/100.0 xpos gX 
        show masktest:
            linear dist/100.0 xpos mX 
        $ renpy.pause(delay=dist/100.0,hard=True)
        jump enemy
    else:
        jump standstill


label Walkdown:
    if canmoveDown(gX,gY):
        $gY = gY+dist
        $mY = mY+dist
        play sound "./audio/running grass.mp3"
        show char walkright:
            linear dist/100.0 ypos gY 
        show masktest:
            linear dist/100.0 ypos mY 
        $ renpy.pause(delay=dist/100.0,hard=True)
        jump enemy
    else:
        jump standstill

label Walkup:
    if canmoveUp(gX,gY):
        $gY = gY-dist
        $mY = mY-dist
        play sound "./audio/running grass.mp3"
        show char walkright:
            linear dist/100.0 ypos gY 
        show masktest:
            linear dist/100.0 ypos mY 
        $ renpy.pause(delay=dist/100.0,hard=True)
        jump enemy
    else:
        jump standstill
    
label getcord:
    if getxy(gX,gY):
        jump standstill




    

screen keynav:
    key "K_UP" action Jump("Walkup")
    key "K_DOWN" action Jump("Walkdown")
    key "K_RIGHT" action Jump("Walkright")
    key "K_LEFT" action Jump("Walkleft")
    key "1" action Jump("getcord")
    # ... etc.