import pygame
pygame.init()
DISPLAY = pygame.display.set_mode((1024,600),0,32)
WHITE = (255,255,255)
blue = (0,0,255)
pygame.time.set_timer(pygame.USEREVENT, 100)
blabla="bebe"
############KEYBOARD INITIALIZE#########################
my_font = pygame.font.Font("calibri.ttf", 72)
lower = False
keys = []
special_keys = []
digit_keys = []
digit_special_keys = []
last_key = -1
tf=""
keyboard_shown = False
keyboard_entry="error"
keyboard_digital=False
keyboard_target=""
keyboard_switchable=True
blinker=" "
letters = "QWERTYUIOPASDFGHJKLZXCVBNM"
for i in range(10):
    keys.append([10+i*100,200,100,100,i,False])
for i in range(9):
    keys.append([60+i*100,300,100,100,i+10,False])
for i in range(7):
    keys.append([160+i*100,400,100,100,i+19,False])
for i in range(3):
    for j in range(3):
        digit_keys.append([350+(j*100),200+(i*100),100,100,j+1+(i*3),False])
digit_keys.append([450,500,100,100,0,False])

special_keys.append([0,400,150,100,"shift",False])
special_keys.append([870,400,150,100,"bksp",False])
special_keys.append([300,500,500,100,"",False])
special_keys.append([810,500,150,100,"OK",False])
special_keys.append([40,500,150,100,"X",False])
special_keys.append([200,500,100,100,"֍",False])

digit_special_keys.append([725,300,150,100,"OK",False])
digit_special_keys.append([125,300,150,100,"X",False])
digit_special_keys.append([550,500,100,100,"C",False])
digit_special_keys.append([350,500,100,100,"ce",False])
digit_special_keys.append([200,500,100,100,"֍",False])
###################################################
def hide_keyboard():
    global keyboard_shown
    global keyboard_entry
    global keyboard_target
    keyboard_entry = "error"
    tf = ""
    keyboard_target = ""
    for key in keys:
        key[5] = False
    for key in digit_keys:
        key[5] = False
    for key in special_keys:
        key[5] = False
    for key in digit_special_keys:
        key[5] = False
    keyboard_shown = False

def display_keyboard(title,to_set,digital=False,switchable=True,begin_with_upper=False):
    global keyboard_shown
    global keyboard_entry
    global lower
    global keyboard_digital
    global keyboard_target
    global letters
    global keyboard_switchable
    keyboard_switchable = switchable
    keyboard_target = to_set
    keyboard_entry = title
    keyboard_digital = digital
    lower = not begin_with_upper
    keyboard_shown = True
    if begin_with_upper:
        letters = letters.upper()
    else:
        letters = letters.lower()
    if begin_with_upper and not digital:
        special_keys[0][5] = True


def keyboard_press():
    global tf
    global lower
    global letters
    global last_key
    global keyboard_digital
    global keyboard_switchable
    if not keyboard_digital:
        if last_key != -1:
            if last_key<100:
                key = keys[last_key]
                key[5] = False
                tf += letters[key[4]]
                if not lower:
                    lower = True
                    special_keys[0][5] = False
                    letters = letters.lower()
                last_key = -1
            else:
                key = special_keys[last_key-100]
                key[5] = False
                if key[4] == "bksp":
                    tf = tf[:-1]
                elif key[4] == "shift":
                    if lower:
                        letters = letters.upper()
                        lower = False
                        key[5] = True
                    else:
                        letters = letters.lower()
                        lower = True
                elif key[4] == "":
                    tf += " "
                elif key[4] == "OK":
                    globals()[keyboard_target] = tf
                    hide_keyboard()
                elif key[4] == "X":
                    hide_keyboard()
                elif key[4] == "֍" and keyboard_switchable:
                    keyboard_digital = True
                last_key = -1
    else:
        if last_key != -1:
            if last_key<100:
                key = digit_keys[last_key]
                key[5] = False
                tf += str(key[4])
                last_key = -1
            else:
                key = digit_special_keys[last_key-100]
                key[5] = False
                if key[4] == "C":
                    tf = tf[:-1]
                elif key[4] == "ce":
                    tf = ""
                elif key[4] == "OK":
                    if keyboard_switchable:
                        globals()[keyboard_target] = tf
                    else:
                        globals()[keyboard_target] = int(tf)
                    hide_keyboard()
                elif key[4] == "X":
                    hide_keyboard()
                elif key[4] == "֍" and keyboard_switchable:
                    keyboard_digital = False
                last_key = -1


def keyboard_highlight():
    global last_key
    if not keyboard_digital:
        for index,key in enumerate(keys):
            if pygame.Rect(key[0], key[1], key[2], key[3]).collidepoint(pygame.mouse.get_pos()):
                key[5] = True
                last_key = index
                break
        for index,key in enumerate(special_keys):
            if pygame.Rect(key[0], key[1], key[2], key[3]).collidepoint(pygame.mouse.get_pos()):
                key[5] = True
                last_key = 100+index
                break
    else:
        for index,key in enumerate(digit_keys):
            if pygame.Rect(key[0], key[1], key[2], key[3]).collidepoint(pygame.mouse.get_pos()):
                key[5] = True
                last_key = index
                break
        for index,key in enumerate(digit_special_keys):
            if pygame.Rect(key[0], key[1], key[2], key[3]).collidepoint(pygame.mouse.get_pos()):
                key[5] = True
                last_key = 100+index
                break


def draw_keyboard():
    if not keyboard_digital:
        for key in keys:
            if key[5]:
                pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
            pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)
            DISPLAY.blit(my_font.render(letters[key[4]], False, (0,0,0)),(key[0]+20,key[1]+20))
        for key in special_keys:
            if key[4] == "֍" and not keyboard_switchable:
                continue
            if key[5]:
                pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
            pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)
            DISPLAY.blit(my_font.render(key[4], False, (0,0,0)),(key[0]+20,key[1]+20))
    else:
        for key in digit_keys:
            if key[5]:
                pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
            pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)
            DISPLAY.blit(my_font.render(str(key[4]), False, (0,0,0)),(key[0]+20,key[1]+20))
        for key in digit_special_keys:
            if key[4] == "֍" and not keyboard_switchable:
                continue
            if key[5]:
                pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
            pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)
            DISPLAY.blit(my_font.render(key[4], False, (0,0,0)),(key[0]+20,key[1]+20))
    pygame.draw.rect(DISPLAY, (0, 0, 0), (50,80,900,100), 5)
    textfield_surface = my_font.render(tf, False, (0, 0, 0))
    DISPLAY.blit(textfield_surface,  (500-(textfield_surface.get_size()[0] / 2),100))
    DISPLAY.blit(my_font.render(blinker, False, (0, 0, 0)),  (485+(textfield_surface.get_size()[0] / 2),100))
    name_surface = my_font.render(keyboard_entry, False, (0, 0, 0))
    DISPLAY.blit(name_surface,  (500-(name_surface.get_size()[0] / 2),10))


counter = 0
#pygame.mouse.set_pos(480, 200)
display_keyboard("Name","blabla",False,True)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if keyboard_shown:
                keyboard_press()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if keyboard_shown:
                keyboard_highlight()
        if event.type == pygame.USEREVENT:
            counter+=1
            if counter % 4 == 0:
                if blinker==" ":
                    blinker="|"
                else:
                    blinker=" "
    DISPLAY.fill(WHITE)
    if keyboard_shown:
        draw_keyboard()
    #pygame.draw.rect(DISPLAY, blue, (pos[0]-25,pos[1], 50, 250))
    pygame.display.update()