import pygame
import json
pygame.init()
DISPLAY = pygame.display.set_mode((1024,600),0,32)
WHITE = (255,255,255)
blue = (0,0,255)
pygame.time.set_timer(pygame.USEREVENT, 100)
blabla="bebe"
############KEYBOARD INITIALIZE#########################
my_font = pygame.font.Font("calibri.ttf", 72)
my_font_m = pygame.font.Font("calibri.ttf", 48)
my_font_s = pygame.font.Font("calibri.ttf", 36)
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
keyboard_fraction=False
keyboard_finalfunc=""
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
digit_special_keys.append([350,500,100,100,"C",False])
digit_special_keys.append([200,500,100,100,"֍",False])
digit_special_keys.append([550,500,100,100,".",False])
###################################################

db_dbname=""
db_name=""
db_nums = []
db_bools = []
db_editingname = ""
db_editingdefault = 0
db_length=365

def createdb():
    global menu_current
    print("creating")
    db={}
    db["dbname"] = db_dbname
    db["name"] = db_name
    db["intnames"] = ["","","","","","","","",""]
    db["intdefs"] = [0,0,0,0,0,0,0,0,0]
    for index,nam in enumerate(db_nums):
        db["intnames"][index]=nam[0]
        db["intdefs"][index]=nam[1]
    db["boolnames"] = ["","","","","","","","",""]
    db["booldefs"] = [False,False,False,False,False,False,False,False,False,]
    for index,nam in enumerate(db_bools):
        db["boolnames"][index]=nam[0]
        db["booldefs"][index]=nam[1]
    db["days"]=[]
    day = {"reminder": "", "ints": [db["intdefs"][0],db["intdefs"][1],db["intdefs"][2],db["intdefs"][3],db["intdefs"][4],db["intdefs"][5],db["intdefs"][6],db["intdefs"][7],db["intdefs"][8]], "bools": [db["booldefs"][0],db["booldefs"][1],db["booldefs"][2],db["booldefs"][3],db["booldefs"][4],db["booldefs"][5],db["booldefs"][6],db["booldefs"][7],db["booldefs"][8]]}
    for i in range(db_length):
        db["days"].append(day)
    with open(db_dbname, 'w') as outfile:
        json.dump(db, outfile)
        menus[0][3][2] = 550
        menu_current = 0

"""db_num1=-999
db_num2=-999
db_num3=-999
db_num4=-999
db_num5=-999
db_num6=-999
db_num7=-999
db_num8=-999
db_num9=-999"""

##################################################
menu_current = 0
last_button = -1
menus = [[],[],[],[],[]]
# if label, no w or h applicable, if centered, only y applicable
# if centered button, no x applicable
# type||xpos||ypos||w||h||center||text||font||highlighted
# 0type 1xpos 2ypos 3w 4h 5center 6text 7font 8hl
menus[0].append(["label",-1,100,-1,-1,True,"Welcome to Life Manager","large",False])
menus[0].append(["button",-1,275,350,100,True,"Create database","medium",False])
menus[0].append(["button",-1,400,350,100,True,"Load database","medium",False])
menus[0].append(["label",-1,650,-1,-1,True,"Database created!","small",False])

menus[1].append(["label",-1,0,-1,-1,True,"Database creation","large",False])
menus[1].append(["label",50,200,-1,-1,False,"Database name","medium",False])
menus[1].append(["textfield",360,200,600,50,False,"db_dbname","medium",False])
menus[1].append(["label",50,300,-1,-1,False,"Your name","medium",False])
menus[1].append(["textfield",360,300,600,50,False,"db_name","medium",False])
menus[1].append(["button",750,500,250,75,False,"next","medium",False])
menus[1].append(["button",25,500,250,75,False,"cancel","medium",False])
menus[1].append(["label",50,400,-1,-1,False,"How many days?","medium",False])
menus[1].append(["textfield",400,400,300,50,False,"db_length","medium",False])

menus[2].append(["label",-1,0,-1,-1,True,"Set values to track","medium",False])
menus[2].append(["label",-1,75,-1,-1,True,"<empty>","small",False])
menus[2].append(["label",-1,125,-1,-1,True,"<empty>","small",False])
menus[2].append(["label",-1,175,-1,-1,True,"<empty>","small",False])
menus[2].append(["label",-1,225,-1,-1,True,"<empty>","small",False])
menus[2].append(["label",-1,275,-1,-1,True,"<empty>","small",False])
menus[2].append(["label",-1,325,-1,-1,True,"<empty>","small",False])
menus[2].append(["label",-1,375,-1,-1,True,"<empty>","small",False])
menus[2].append(["label",-1,425,-1,-1,True,"<empty>","small",False])
menus[2].append(["label",-1,475,-1,-1,True,"<empty>","small",False])
menus[2].append(["button",-1,525,200,50,True,"add value","small",False])
menus[2].append(["button",25,500,250,75,False,"previous","medium",False])
menus[2].append(["button",750,500,250,75,False,"next","medium",False])
menus[2].append(["button",900,75,120,30,False,"remove","small",False])
menus[2].append(["button",900,125,120,30,False,"remove","small",False])
menus[2].append(["button",900,175,120,30,False,"remove","small",False])
menus[2].append(["button",900,225,120,30,False,"remove","small",False])
menus[2].append(["button",900,275,120,30,False,"remove","small",False])
menus[2].append(["button",900,325,120,30,False,"remove","small",False])
menus[2].append(["button",900,375,120,30,False,"remove","small",False])
menus[2].append(["button",900,425,120,30,False,"remove","small",False])
menus[2].append(["button",900,475,120,30,False,"remove","small",False])

menus[3].append(["label",-1,0,-1,-1,True,"Set checks to track","medium",False])
menus[3].append(["label",-1,75,-1,-1,True,"<empty>","small",False])
menus[3].append(["label",-1,125,-1,-1,True,"<empty>","small",False])
menus[3].append(["label",-1,175,-1,-1,True,"<empty>","small",False])
menus[3].append(["label",-1,225,-1,-1,True,"<empty>","small",False])
menus[3].append(["label",-1,275,-1,-1,True,"<empty>","small",False])
menus[3].append(["label",-1,325,-1,-1,True,"<empty>","small",False])
menus[3].append(["label",-1,375,-1,-1,True,"<empty>","small",False])
menus[3].append(["label",-1,425,-1,-1,True,"<empty>","small",False])
menus[3].append(["label",-1,475,-1,-1,True,"<empty>","small",False])
menus[3].append(["button",-1,525,200,50,True,"add check","small",False])
menus[3].append(["button",25,500,250,75,False,"previous","medium",False])
menus[3].append(["button",750,500,250,75,False,"next","medium",False])
menus[3].append(["button",900,75,120,30,False,"remove","small",False])
menus[3].append(["button",900,125,120,30,False,"remove","small",False])
menus[3].append(["button",900,175,120,30,False,"remove","small",False])
menus[3].append(["button",900,225,120,30,False,"remove","small",False])
menus[3].append(["button",900,275,120,30,False,"remove","small",False])
menus[3].append(["button",900,325,120,30,False,"remove","small",False])
menus[3].append(["button",900,375,120,30,False,"remove","small",False])
menus[3].append(["button",900,425,120,30,False,"remove","small",False])
menus[3].append(["button",900,475,120,30,False,"remove","small",False])

def draw_menu(phase=0):
    for item in menus[phase]:
        if item[0] == "label":
            if "<" in item[6] and ">" in item[6]:
                color = (127,127,127)
            else:
                color = (0,0,0)
            if item[7] == "large":
                name_surface = my_font.render(item[6], False, color )
            elif item[7] == "medium":
                name_surface = my_font_m.render(item[6], False, color )
            elif item[7] == "small":
                name_surface = my_font_s.render(item[6], False, color )
            if item[5] == True: # if centered
                DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), item[2]))
            else: # if not centered
                DISPLAY.blit(name_surface, (item[1], item[2]))
        elif item[0] == "button" or item[0] == "textfield":
            if item[0] == "button":
                label=item[6]
            else:
                label=str(globals()[item[6]])
            if item[7] == "large":
                name_surface = my_font.render(label, False, (0, 0, 0))
            elif item[7] == "medium":
                name_surface = my_font_m.render(label, False, (0, 0, 0))
            elif item[7] == "small":
                name_surface = my_font_s.render(label, False, (0, 0, 0))
            if item[5] == True: # if centered
                if item[8]:
                    pygame.draw.rect(DISPLAY,(127,127,127),(512-(item[3]/2),item[2],item[3],item[4]))
                DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), item[2]+item[4]/2-name_surface.get_size()[1]/2))
                pygame.draw.rect(DISPLAY,(0,0,0),(512-(item[3]/2),item[2],item[3],item[4]),5)
            else: # if not centered
                if item[8]:
                    pygame.draw.rect(DISPLAY,(127,127,127),(item[1],item[2],item[3],item[4]))
                DISPLAY.blit(name_surface, (item[1]+item[3]/2-(name_surface.get_size()[0] / 2), item[2]+item[4]/2-name_surface.get_size()[1]/2))
                pygame.draw.rect(DISPLAY,(0,0,0),(item[1],item[2],item[3],item[4]),5)


def menu_highlight():
    global last_button
    global menu_current
    for index,button in enumerate(menus[menu_current]):
        if button[5] == True:
            iscolliding = pygame.Rect(512-(button[3]/2), button[2], button[3], button[4]).collidepoint(pygame.mouse.get_pos())
        else:
            iscolliding = pygame.Rect(button[1], button[2], button[3], button[4]).collidepoint(pygame.mouse.get_pos())
        if iscolliding:
            button[8] = True
            last_button = index
            break

def start_creating_db():
    global menu_current
    global blabla
    menu_current=1

def okfuncs(which):
    if which==0:
        global db_dbname
        db_dbname = db_dbname.replace(" ", "_")
        if db_dbname[-5:] != ".json":
            db_dbname+=".json"
    if which==1:
        display_keyboard("Default value?", "db_editingdefault", digital=True, switchable=False, begin_with_upper=False,
                         fraction=True, okfunc="okfuncs(2)")
    if which==2:
        db_nums.append([db_editingname,db_editingdefault])

    if which==3:
        display_keyboard("1 = checked | 0 = unchecked", "db_editingdefault", digital=True, switchable=False, begin_with_upper=False,
                         fraction=False, okfunc="okfuncs(4)")
    if which==4:
        if db_editingdefault == 1:
            db_bools.append([db_editingname,True])
        else:
            db_bools.append([db_editingname,False])

def menu_press():
    global last_button
    global menu_current
    if last_button != -1:
        button = menus[menu_current][last_button]
        button[8] = False
        last_button = -1
        if button is menus[0][1]:
            menu_current = 1
        elif button is menus[1][2]:
            display_keyboard("Name your database", "db_dbname", digital=False, switchable=True, begin_with_upper=False,fraction=True, default_text=db_dbname,okfunc='okfuncs(0)')
        elif button is menus[1][4]:
            display_keyboard("What's your name?","db_name",digital=False,switchable=False,begin_with_upper=True,fraction=True,default_text=db_name)
        elif button is menus[1][5]:
            menu_current = 2
        elif button is menus[1][6]:
            menu_current = 0
        elif button is menus[1][8]:
            display_keyboard("How many days?","db_length",digital=True,switchable=False,begin_with_upper=True,fraction=False,default_text=db_length)
        elif button is menus[2][10]:
            display_keyboard("What to track?", "db_editingname", digital=False, switchable=False, begin_with_upper=False,fraction=False,okfunc="okfuncs(1)")
        elif button is menus[2][11]:
            menu_current = 1
        elif button is menus[2][12]:
            menu_current = 3
        elif button is menus[3][10]:
            display_keyboard("What to track?", "db_editingname", digital=False, switchable=False, begin_with_upper=False,fraction=False,okfunc="okfuncs(3)")
        elif button is menus[3][11]:
            menu_current = 2
        elif button is menus[3][12]:
            createdb()
        for i in range(13,22):
            if button is menus[2][i]:
                db_nums.pop(i-13)
            elif button is menus[3][i]:
                db_bools.pop(i-13)


def hide_keyboard():
    global keyboard_shown
    global keyboard_entry
    global keyboard_target
    global tf
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

def display_keyboard(title,to_set,digital=False,switchable=True,begin_with_upper=False,fraction=False,okfunc="",default_text=""):
    global keyboard_shown
    global keyboard_entry
    global lower
    global keyboard_digital
    global keyboard_target
    global letters
    global keyboard_switchable
    global keyboard_fraction
    global keyboard_finalfunc
    global tf
    if default_text != "":
        tf=str(default_text)
    keyboard_finalfunc = okfunc
    keyboard_switchable = switchable
    keyboard_target = to_set
    keyboard_entry = title
    keyboard_digital = digital
    keyboard_fraction = fraction
    if switchable:
        keyboard_fraction = True
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
    global keyboard_fraction
    global keyboard_finalfunc
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
                    exec(keyboard_finalfunc)
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
                elif key[4] == "OK":
                    if keyboard_switchable:
                        globals()[keyboard_target] = tf
                    else:
                        if '.' in tf:
                            globals()[keyboard_target] = float(tf)
                        else:
                            try:
                                globals()[keyboard_target] = int(tf)
                            except ValueError:
                                globals()[keyboard_target] = 0
                    hide_keyboard()
                    exec(keyboard_finalfunc)
                elif key[4] == "X":
                    hide_keyboard()
                elif key[4] == "֍" and keyboard_switchable:
                    keyboard_digital = False
                elif key[4] == "." and keyboard_fraction and (not "." in tf or keyboard_switchable):
                    tf += "."
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
            if key[4] == "." and (not keyboard_fraction or "." in tf) and not keyboard_switchable:
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


    """name_surface = my_font.render("Welcome to Life Manager", False, (0, 0, 0))
    DISPLAY.blit(name_surface,  (512-(name_surface.get_size()[0] / 2),100))
    name_surface = my_font_m.render("Please enter your name", False, (0, 0, 0))
    DISPLAY.blit(name_surface,  (512-(name_surface.get_size()[0] / 2),200))"""


counter = 0
#pygame.mouse.set_pos(480, 200)
#display_keyboard("Name","blabla",digital=True,switchable=True,begin_with_upper=False,fraction=True)
while True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if keyboard_shown:
                keyboard_press()
            else:
                menu_press()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if keyboard_shown:
                keyboard_highlight()
            else:
                menu_highlight()
        if event.type == pygame.USEREVENT:
            counter+=1
            if counter % 4 == 0:
                #print(blabla)
                #print(type(blabla))
                if blinker==" ":
                    blinker="|"
                else:
                    blinker=" "
    DISPLAY.fill(WHITE)
    if keyboard_shown:
        draw_keyboard()
    else:
        draw_menu(menu_current)
        if menu_current == 2:
            for i in range(9):
                if i<=len(db_nums)-1:
                    menus[2][i+1][6] = db_nums[i][0] + " | default: "+str(db_nums[i][1])
                    menus[2][i+13][1] = 900
                else:
                    menus[2][i + 1][6] = "<empty>"
                    menus[2][i+13][1] = 1100
        elif menu_current == 3:
            for i in range(9):
                if i<=len(db_bools)-1:
                    if db_bools[i][1]==True:
                        menus[3][i+1][6] = db_bools[i][0] + " | default: √"
                    else:
                        menus[3][i+1][6] = db_bools[i][0] + " | default: X"
                    menus[3][i+13][1] = 900
                else:
                    menus[3][i + 1][6] = "<empty>"
                    menus[3][i+13][1] = 1100
    #pygame.draw.rect(DISPLAY, blue, (pos[0]-25,pos[1], 50, 250))
    pygame.display.update()