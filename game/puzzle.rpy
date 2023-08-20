default mark=-1
default possitions =  [[0.05,0.1],[0.05,0.4],[0.05,0.7]]
default xrand = [0.05,0.35,0.65]
default yrand = [0.1,0.4,0.7]
image key = "key2.png" #"./images/key.png"
image skull = "skull2.png" 
define newx = 0
define newy = 0
define virtualwidth = config.screen_width * 10000
define virtualheight = config.screen_height * 10000

    
init python:
    def getMousePosition ():
        import pygame
        u, i = renpy.get_physical_size()
        store.physicalwidth = u
        store.physicalheight = i
        store.p = virtualwidth / physicalwidth
        store.p2 = virtualheight / physicalheight
        c, d = pygame.mouse.get_pos()
        store.mousex = c
        store.mousey = d
        store.newx = (mousex * p) / 10000
        store.newy = (mousey * p2) / 10000

label puzzle:
    play music "../audio/piano.mp3" fadein 1.0 volume 0.4
    scene bg cabin1 

    $renpy.random.shuffle(yrand)
    $renpy.random.shuffle(xrand)
    show key2:
            xalign 0.5
            yalign 0.5
    "CLICK around the room to find this key"
    hide key2 
    show skull:
        xalign 0.5
        yalign 0.5
    "AVOID CLicking on these skulls"
    hide skull2
    "getting 6 skulls resets the game so make sure to avoid them"
    scene bg cabin1 
    show bar1:
            xalign 0.80
            yalign 0.01
    
    show screen hiddenobjects

    jump healthbar

label endgame:
    
    hide screen hiddenobjects
    scene bg end2 with dissolve
    "You made to much noise"
    jump puzzle

label foundkey:
    play audio "../audio/victory.mp3" volume 0.5
    hide screen hiddenobjects
    scene bg cabin1 
    show key2:
        xalign 0.5
        yalign 0.5
    "You found the key...escape" 
    jump scene16


label healthbar():
    $mark = mark+1
    if mark==1:
        show bara:
            xalign 0.80
            yalign 0.01
    elif mark==2:
        show barb:
            xalign 0.80
            yalign 0.01
    elif mark==3:
        show barc:
            xalign 0.80
            yalign 0.01
    elif mark==4:
        show bard:
            xalign 0.80
            yalign 0.01
    elif mark==5:
        show bare:
            xalign 0.80
            yalign 0.01
    elif mark==6:
        show bar2:
            xalign 0.80
            yalign 0.01
        jump endgame
        
    if mark>0:
        play audio "<from 0 to 1>../audio/failure3.mp3" fadeout 1.0 volume 0.1

    #stop sound fadeout 1.0
    $ui.interact()




screen hiddenobjects():
    imagebutton:
        xalign xrand[0]
        yalign yrand[0]
        idle "hiddenobject2.png"
        hover "key2.png"
        action [getMousePosition(),Jump("foundkey")]
    imagebutton:
        xalign xrand[0]
        yalign yrand[1]
        idle "hiddenobject2.png"
        action Jump("sellect1")
    imagebutton:
        xalign xrand[0]
        yalign yrand[2]
        idle "hiddenobject2.png"
        action Jump("sellect2")
    imagebutton:
        xalign xrand[1]
        yalign yrand[0]
        idle "hiddenobject2.png"
        action Jump("sellect3")
    imagebutton:
        xalign xrand[1]
        yalign yrand[1]
        idle "hiddenobject2.png"
        action Jump("sellect4")
    imagebutton:
        xalign xrand[1]
        yalign yrand[2]
        idle "hiddenobject2.png"
        action Jump("sellect5")
    imagebutton:
        xalign xrand[2]
        yalign yrand[0]
        idle "hiddenobject2.png"
        action Jump("sellect6")
    imagebutton:
        xalign xrand[2]
        yalign yrand[1]
        idle "hiddenobject2.png"
        action Jump("sellect7")
    imagebutton:
        xalign xrand[2]
        yalign yrand[2]
        idle "hiddenobject2.png"
        action Jump("sellect8")




label sellect1:
    show skull:
        xpos xrand[0]
        ypos yrand[1]
    jump healthbar
label sellect2:
    show skull:
        xpos xrand[0]
        ypos yrand[2]
    jump healthbar
label sellect3:
    show skull:
        xpos xrand[1]
        ypos yrand[0]
    jump healthbar
label sellect4:
    show skull:
        xpos xrand[1]
        ypos yrand[1]
    jump healthbar
label sellect5:
    show skull:
        xpos xrand[1]
        ypos yrand[2]
    jump healthbar
label sellect6:
    show skull:
        xpos xrand[2]
        ypos yrand[0]
    jump healthbar
label sellect7:
    show skull:
        xpos xrand[2]
        ypos yrand[1]
    jump healthbar
label sellect8:
    
    show skull:
        xpos xrand[2]
        ypos yrand[2]
    jump healthbar