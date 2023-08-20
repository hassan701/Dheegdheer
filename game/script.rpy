default Dhegdheer = Character('Dhegdheer', color="#dd0404")       
default Child = Character('Child', color="#2fdd04") 
default Daughter = Character('Daughter', color="#2a2974")
default Ali = Character('Daughter', color="#2a2974")
# The game starts here.
define moveinhome = MoveTransition(delay=6, layers= ['master'])
define moveinkid = MoveTransition(delay=3, layers= ['master'])
default rsprite = (0.5, 0)
default lsprite = (0.1, 1.0)
transform SpriteLoc2(x, y):
    pos (x, y)
define moveindaugh = MoveTransition(delay=4, enter= SpriteLoc2(0.37, 0.5), leave= left, layers= ['master'])
label start:
    scene desert:
        xzoom 0.2 yzoom 0.2
    with fade
    play music "audio/bgm_intro.mp3" noloop
    "Once upon a time, a fierce cannibal named Dhegdheer roamed the Hargega Valley in Somalia. Her Horrific ways cursed a land once green and lush. Turning it into a crumbling dust.
    Dhegdheer was as strong and swift as the wind. She had an unusually long pointy ear with the strange power to hear even the gait of camels a half day’s journey away."
label scene2:
    stop music
    show dheegdheer head at left with moveinright:
        xzoom 0.75 yzoom 0.75
    play music "audio/scene2.mp3"  noloop
    Dhegdheer "I shall come upon a young woman weaving mats under a thorn tree"


label scene3:
    scene outhouse
    show dhegdheer full at left:
        xzoom 0.7 yzoom 0.6
    show dhegdheer full at SpriteLoc2(0.7, 0.7) with moveinhome:
        xzoom 0.7 yzoom 0.6
    play music "audio/scene3.mp3" noloop
    Dhegdheer "Today I havent found a victim but i vow to never come back  emptyhanded"
label scene4:
    scene inhouse:
        xzoom 1 yzoom 0.85
    show dhegdheer full at right:
        xzoom 0.7 yzoom 0.6
    play music "audio/scene4.mp3" noloop
    Dhegdheer "I will use my powers to trap lonely travelers, Don’t tired souls need some water and moment’s rest? I shall be lucky. Gather up some wood, grass, and lots of sticks daughter!"
label scene5:
    scene inhouse:
        xzoom 1 yzoom 0.85
    show dhegdheer full at right:
        xzoom 0.7 yzoom 0.6
    show come at SpriteLoc2(0.65,0.28)
    play music "audio/come.mp3" noloop
    show daughter1 at SpriteLoc2(0.37, 0.5) with moveindaugh:
        xzoom 0.7 yzoom 0.5
    show hello at SpriteLoc2(0.45, 0.3)
    play sound "audio/daughter2.mp3" noloop

    Dhegdheer "Dhegdheer with her daughter"
label scene6:
    scene inhouse:
        xzoom 1 yzoom 0.85
    with fade
    show dhegdheer full at right:
        xzoom 0.7 yzoom 0.6
    show gather at SpriteLoc2(0.65,0.28)
    play audio "audio/gather.mp3" noloop fadeout 3.0
    show daughter1 at SpriteLoc2(0.37, 0.5):
        xzoom 0.7 yzoom 0.5
    show start at SpriteLoc2(0.45, 0.3)
    play audio [ "<silence 3>", "audio/daughter1.mp3"] noloop
    

    Dhegdheer "Dhegdheer with her daughter"
label scene7:
    scene inhouse:
        xzoom 1 yzoom 0.85
    show dhegdheer full at right:
        xzoom 0.7 yzoom 0.6
    show daughter1 at left with moveinright:
        xzoom 0.7 yzoom 0.5
label scene8:
    stop music
    stop audio
    scene desert3:
        xzoom 1 yzoom 0.85
    show kid5 at left with moveinright:
        xzoom 0.4 yzoom 0.4
    play music "audio/kid1.mp3"  noloop
    Child "I have been walking for so long i dont think i will be able to walk for longer if i don’t find a place to stay. I will not last longer!"
label scene9:
    scene deserthut:
        xzoom 1 yzoom 0.85
    play music "audio/kid2.mp3"  noloop
    Child "What is that a hut I can rest in! I shall hurry and rest there"
label scene10:
    scene deserthut2:
        xzoom 1 yzoom 0.85
    play music "audio/kid3.mp3"  noloop
    Child "Hello, can i get somewhere to rest and food"
    play audio "audio/yay.mp3" noloop
    Daughter " I see you desperately need help, but if you need to stay here you shall hide from my mom. She is very dangerous, hide in that room and don’t make any noise otherwise my mom will eat you for dinner. I will bring food and water to you."
    play music "audio/kid4.mp3" noloop
    Child "Ok, i will go inside and hide"

label scene11:
    scene food1:
        xzoom 1 yzoom 0.85
    Daughter""

label scene12:
    scene hut2:
        xzoom 1.2 yzoom 1
    play music "audio/daughterend.mp3"  noloop
    Daughter "Here’s the food, if my mother tries to come through the front door, the key to the backdoor is in this room and run away through the backdoor." 
    play music "audio/kidend.mp3"  noloop
    Child " Okay, thank you very much"
label scene13:
    scene inhouse:
        xzoom 1 yzoom 0.85
    show dhegdheer full at right:
        xzoom 0.7 yzoom 0.6
    show daughter1 at SpriteLoc2(0.37, 0.5) with moveinleft:
        xzoom 0.7 yzoom 0.5
    play music "audio/dhegdheerend.mp3" noloop
    Dhegdheer "Daughter come here at once! What is that I smell? Do I smell  human?"
    play sound "audio/daughterend 1.mp3" noloop
    Daughter "No mother you must be so hungry you are imagining it."
    play sound "audio/dhegdheerend 3.mp3" noloop
    Dhegdheer "No, move out of my way I will find this measly human and have them for dinner!"
label scene14:
    scene inhouse:
        xzoom 1 yzoom 0.85
    show dhegdheer full at right with moveinleft:
        xzoom 0.7 yzoom 0.6
    show daughter1 at left :
        xzoom 0.7 yzoom 0.5
label scene15:
    scene hutchild:
        xzoom 1 yzoom 1
    play music "audio/doorbang.mp3"  noloop
    Dhegdheer "*Dhegdheer banging on door*"
    play audio "audio/kidend 1.mp3" noloop
    Child "Oh no, Dhegdheer has found me. I need to find a way out of here."
    jump puzzle

label scene16:
    scene nig:
        xzoom 1.3 yzoom 1
    play audio "audio/yay.mp3" noloop
    Child "Yay I have made it out of the hut, but Dhegdheer is still close to me I will try to run away"
label scene17:
    scene e3:
        xzoom 1 yzoom 1
    play audio "audio/kidend 2.mp3" noloop
    Child "Oh no, Dhegdheer is far too fast for me to outrun her, Wait I see the forest maze if I can outsmart her by making it through the maze I will be able to outrun her."

label scene18:
    scene e2:
        xzoom 1 yzoom 1
    play audio "audio/kidend 3.mp3" noloop
    "Navigate through this maze and get to the exit."
    "avoid the BLUE enimes as they will bring you back to the start"
    jump maze
    
label scene19:
    scene run:
        xzoom 1 yzoom 1
    play audio "audio/kidend 4.mp3" noloop
    Child " Hooray, I was able to make it out of the maze with your help, now I can go back home in peace. Thank you."
label scene20:
    scene conclusion:
        xzoom 1 yzoom 1
    play audio "audio/conclusion.mp3" noloop
    "Dhegdheer followed the little kid into the forest maze, she was not able to find the exit out of the maze; she got stuck and could not get out. The village went back to its old glory and everyone lived happily ever after."