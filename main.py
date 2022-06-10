tx = {
    "en": {
        "error": "Error",
        "database": "Database",
        "created": "created!",
        "welcometo": "Welcome to Life Manager",
        "createdb": "Create database",
        "loaddb": "Load database",
        "exitpr": "Exit program",
        "dbcreation": "Database creation",
        "dbname": "Database name",
        "urname": "Your name",
        "next": "next",
        "cancel": "cancel",
        "howmanydays": "How many days?",
        "setvaluestrack": "Set values to track",
        "empty": "<empty>",
        "addvalue": "add value",
        "previous": "previous",
        "remove": "remove",
        "setcheckstrack": "Set checks to track",
        "addcheck": "add check",
        "itemcantbeempty": "Item cannot be empty!",
        "defvalue?": "Default value?",
        "checkedunchecked": "1 = checked | 0 = unchecked",
        "nameurdb": "Name your database",
        "wasurname": "What's your name?",
        "dbcantbeempty": "Database name@cannot be empty!",
        "mustfillname": "You must fill out@your name!",
        "dblengthmust": "Database length@needs to be at@least 1 day!",
        "howmanydays": "How many days?",
        "whattotrack": "What to track?",
        "default": "default",
        "choosecolor": "Choose a color",
        "otherlang": "БГ",
    },
    "bg": {
        "error": "Грешка",
        "database": "База данни",
        "created": "създанена!",
        "welcometo": "Добре дошли в Life Manager",
        "createdb": "Създай база данни",
        "loaddb": "Зареди база данни",
        "exitpr": "Излез от програмата",
        "dbcreation": "Създаване на база данни",
        "dbname": "Име на базата",
        "urname": "Вашето име",
        "next": "напред",
        "cancel": "отказ",
        "howmanydays": "Колко дни да е?",
        "setvaluestrack": "Стойности за следене",
        "empty": "<празно>",
        "addvalue": "добави стойност",
        "previous": "назад",
        "remove": "изтрий",
        "setcheckstrack": "Отметки за следене",
        "addcheck": "добави отметка",
        "itemcantbeempty": "Не може да е празно!",
        "defvalue?": "Стойност по подразбиране?",
        "checkedunchecked": "1 = отметнато | 0 = неотметнато",
        "nameurdb": "Име на базата данни",
        "wasurname": "Как се казвате?",
        "dbcantbeempty": "Името на базата данни@не може да е празно!",
        "mustfillname": "Трябва да си@попълните името!",
        "dblengthmust": "Дължината на базата@данни трябва да е@поне 1 ден!",
        "whattotrack": "Какво да следя?",
        "default": "по подразбиране",
        "choosecolor": "Избери цвят",
        "otherlang": "EN"
    }
}
lan = "en"

import pygame
import json
from sys import exit as terminate_program
pygame.init()
DISPLAY = pygame.display.set_mode((1024,600),0,32)
WHITE = (255,255,255)
pygame.time.set_timer(pygame.USEREVENT, 100)
############KEYBOARD INITIALIZE#########################
#region
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
keyboard_multilingual=False
keyboard_finalfunc=""
blinker=" "
letters_lat = "QWERTYUIOPASDFGHJKLZXCVBNM?"
letters_cyr = "ЯВЕРТЪУИОПАСДФГХЙКЛЗЧЦЖБНМЩ"
letters = letters_lat
for i in range(10):
    keys.append([10+i*100,200,100,100,i,False])
for i in range(9):
    keys.append([60+i*100,300,100,100,i+10,False])
for i in range(7):
    keys.append([160+i*100,400,100,100,i+19,False])
keys.append([960,300,60,100,26,False,True])
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
special_keys.append([920,20,80,50,"БГ",False,True])


digit_special_keys.append([725,300,150,100,"OK",False])
digit_special_keys.append([125,300,150,100,"X",False])
digit_special_keys.append([350,500,100,100,"C",False])
digit_special_keys.append([200,500,100,100,"֍",False])
digit_special_keys.append([550,500,100,100,".",False])
###################################################
#endregion

############COLOR PICKER INITIALIZE#####################
#region
colors_pick=[]
colors_pick.append([(200, 0, 200), (200, 250, 90, 90)])
colors_pick.append([(200, 0, 0), (300, 250, 90, 90)])
colors_pick.append([(200, 200, 0), (400, 250, 90, 90)])
colors_pick.append([(0, 200, 0), (500, 250, 90, 90)])
colors_pick.append([(0, 200, 200), (600, 250, 90, 90)])
colors_pick.append([(0, 0, 0), (700, 250, 90, 90)])
colors_pick.append([(127, 127, 127), (200, 350, 90, 90)])
colors_pick.append([(0, 0, 200), (300, 350, 90, 90)])
colors_pick.append([(230, 170, 0), (400, 350, 90, 90)])
colors_pick.append([(150, 120, 0), (500, 350, 90, 90)])
colors_pick.append([(0, 120, 0), (600, 350, 90, 90)])
colors_pick.append([(250, 50, 150), (700, 350, 90, 90)])
#########################################################
#endregion

db_dbname=""
db_name=""
db_nums = []
db_bools = []
db_editingname = ""
db_editingdefault = 0
db_editingcol = (0,0,0)
db_length=365


message_show = False
message_to_show = "You can't leave@any field empty!"
message_ok_hl = False

colorpicker_show = False
colorpicker_displaytext = "error"
colorpicker_currentcol = (0,0,0)
colorpicker_ok_hl = False
colorpicker_tovar=""
colorpicker_okfunc=""

def display_colorpicker(tovar,displaytext,okfunc):
    global colorpicker_show
    global colorpicker_ok_hl
    global colorpicker_currentcol
    global colorpicker_tovar
    global colorpicker_okfunc
    global colorpicker_displaytext
    colorpicker_displaytext = displaytext
    colorpicker_okfunc = okfunc
    colorpicker_tovar = tovar
    colorpicker_currentcol = globals()[tovar]
    colorpicker_ok_hl = False
    colorpicker_show = True

def draw_colorpicker():
    global colors_pick
    global colorpicker_currentcol
    global colorpicker_displaytext
    for color in colors_pick:
        pygame.draw.rect(DISPLAY, color[0],color[1])
    if colorpicker_ok_hl:
        pygame.draw.rect(DISPLAY,(127,127,127),(406,500,212,75))


    name_surface = my_font.render(tx[lan]["choosecolor"], False, (0, 0, 0))
    DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 20))

    name_surface = my_font_m.render(colorpicker_displaytext, False, colorpicker_currentcol)
    DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 170))

    pygame.draw.rect(DISPLAY, (0, 0, 0), (406,500,212,75), 5)
    name_surface = my_font_m.render("OK", False, (0, 0, 0))
    DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 537-name_surface.get_size()[1]/2))
def colorpicker_highlight():
    global colorpicker_ok_hl
    global colorpicker_currentcol
    if pygame.Rect(406,500,212,75).collidepoint(pygame.mouse.get_pos()):
        colorpicker_ok_hl = True
    else:
        for color in colors_pick:
            if pygame.Rect(color[1]).collidepoint(pygame.mouse.get_pos()):
                colorpicker_currentcol=color[0]
def colorpicker_press():
    global colorpicker_ok_hl
    global colorpicker_tovar
    global colorpicker_currentcol
    global colorpicker_show
    if colorpicker_ok_hl:
        colorpicker_ok_hl = False
        globals()[colorpicker_tovar] = colorpicker_currentcol
        exec(colorpicker_okfunc)
        colorpicker_currentcol=(0,0,0)
        colorpicker_show = False


def display_message(title):
    global message_show
    global message_ok_hl
    global message_to_show
    message_to_show = title
    message_ok_hl = False
    message_show = True
def draw_message():
    global message_to_show
    messages = message_to_show.split("@")
    name_surfaces=[]
    heights=[]
    total_height=0
    index=0
    for message in messages:
        name_surfaces.append(my_font_m.render(message, False, (0, 0, 0)))
        total_height += name_surfaces[index].get_size()[1]+10
        heights.append(total_height)
        index+=1
    for index, surface in enumerate(name_surfaces):
        DISPLAY.blit(surface,(512 - (name_surfaces[index].get_size()[0] / 2), 200 - total_height/2 + heights[index]))
    pygame.draw.rect(DISPLAY, (0, 0, 0), (200,100,612,400), 5)

    if message_ok_hl:
        pygame.draw.rect(DISPLAY,(127,127,127),(406,400,212,75))

    pygame.draw.rect(DISPLAY, (0, 0, 0), (406,400,212,75), 5)
    name_surface = my_font_m.render("OK", False, (0, 0, 0))
    DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 437-name_surface.get_size()[1]/2))
def message_highlight():
    global message_ok_hl
    if pygame.Rect(406,400,212,75).collidepoint(pygame.mouse.get_pos()):
        message_ok_hl = True
def message_press():
    global message_ok_hl
    global message_to_show
    global message_show
    if message_ok_hl:
        message_ok_hl = False
        message_to_show = "Error"
        message_show = False
def createdb():
    global menu_current
    print("creating")
    db={}
    db["dbname"] = db_dbname
    db["name"] = db_name
    db["intnames"] = []
    db["intdefs"] = []
    db["intcols"] = []
    for index,nam in enumerate(db_nums):
        db["intnames"].append(nam[0])
        db["intdefs"].append(nam[1])
        db["intcols"].append(nam[2])
    db["boolnames"] = []
    db["booldefs"] = []
    db["boolcols"] = []
    for index,nam in enumerate(db_bools):
        db["boolnames"].append(nam[0])
        db["booldefs"].append(nam[1])
        db["boolcols"].append(nam[2])
    db["days"]=[]
    day = {"reminder": "", "ints": [], "bools": []}
    day["ints"]=db["intdefs"]
    day["bools"]=db["booldefs"]
    for i in range(db_length):
        db["days"].append(day)
    with open(db_dbname, 'w') as outfile:
        json.dump(db, outfile)
        menu_current = 0
        display_message(tx[lan]["database"]+"@"+db_dbname+"@"+tx[lan]["created"])

##################################################
menu_current = 0
last_button = -1
menus = [[],[],[],[],[]]
# if label, no w or h applicable, if centered, only y applicable
# if centered button, no x applicable
# type||xpos||ypos||w||h||center||text||font||highlighted
# 0type 1xpos 2ypos 3w 4h 5center 6text 7font 8hl
def buildmenus():
    global menus
    menus = [[],[],[],[],[]]
    menus[0].append(["label",-1,100,-1,-1,True,tx[lan]["welcometo"],"large",False])
    menus[0].append(["button",-1,350,450,80,True,tx[lan]["createdb"],"medium",False])
    menus[0].append(["button",-1,250,450,80,True,tx[lan]["loaddb"],"medium",False])
    menus[0].append(["button",-1,450,450,80,True,tx[lan]["exitpr"],"medium",False])
    menus[0].append(["button",920,20,80,50,False,tx[lan]["otherlang"],"medium",False])

    menus[1].append(["label",-1,0,-1,-1,True,tx[lan]["dbcreation"],"large",False])
    menus[1].append(["label",50,200,-1,-1,False,tx[lan]["dbname"],"medium",False])
    menus[1].append(["textfield",360,200,600,50,False,"db_dbname","medium",False])
    menus[1].append(["label",50,300,-1,-1,False,tx[lan]["urname"],"medium",False])
    menus[1].append(["textfield",360,300,600,50,False,"db_name","medium",False])
    menus[1].append(["button",750,500,250,75,False,tx[lan]["next"],"medium",False])
    menus[1].append(["button",25,500,250,75,False,tx[lan]["cancel"],"medium",False])
    menus[1].append(["label",50,400,-1,-1,False,tx[lan]["howmanydays"],"medium",False])
    menus[1].append(["textfield",400,400,300,50,False,"db_length","medium",False])

    menus[2].append(["label",-1,0,-1,-1,True,tx[lan]["setvaluestrack"],"medium",False])
    menus[2].append(["clabel",-1,75,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["clabel",-1,125,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["clabel",-1,175,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["clabel",-1,225,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["clabel",-1,275,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["clabel",-1,325,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["clabel",-1,375,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["clabel",-1,425,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["clabel",-1,475,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[2].append(["button",-1,525,270,50,True,tx[lan]["addvalue"],"small",False])
    menus[2].append(["button",25,500,250,75,False,tx[lan]["previous"],"medium",False])
    menus[2].append(["button",750,500,250,75,False,tx[lan]["next"],"medium",False])
    menus[2].append(["button",900,75,120,30,False,tx[lan]["remove"],"small",False])
    menus[2].append(["button",900,125,120,30,False,tx[lan]["remove"],"small",False])
    menus[2].append(["button",900,175,120,30,False,tx[lan]["remove"],"small",False])
    menus[2].append(["button",900,225,120,30,False,tx[lan]["remove"],"small",False])
    menus[2].append(["button",900,275,120,30,False,tx[lan]["remove"],"small",False])
    menus[2].append(["button",900,325,120,30,False,tx[lan]["remove"],"small",False])
    menus[2].append(["button",900,375,120,30,False,tx[lan]["remove"],"small",False])
    menus[2].append(["button",900,425,120,30,False,tx[lan]["remove"],"small",False])
    menus[2].append(["button",900,475,120,30,False,tx[lan]["remove"],"small",False])

    menus[3].append(["label",-1,0,-1,-1,True,tx[lan]["setcheckstrack"],"medium",False])
    menus[3].append(["clabel",-1,75,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["clabel",-1,125,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["clabel",-1,175,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["clabel",-1,225,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["clabel",-1,275,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["clabel",-1,325,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["clabel",-1,375,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["clabel",-1,425,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["clabel",-1,475,-1,-1,True,tx[lan]["empty"],"small",False,(0,0,0)])
    menus[3].append(["button",-1,525,270,50,True,tx[lan]["addcheck"],"small",False])
    menus[3].append(["button",25,500,250,75,False,tx[lan]["previous"],"medium",False])
    menus[3].append(["button",750,500,250,75,False,tx[lan]["next"],"medium",False])
    menus[3].append(["button",900,75,120,30,False,tx[lan]["remove"],"small",False])
    menus[3].append(["button",900,125,120,30,False,tx[lan]["remove"],"small",False])
    menus[3].append(["button",900,175,120,30,False,tx[lan]["remove"],"small",False])
    menus[3].append(["button",900,225,120,30,False,tx[lan]["remove"],"small",False])
    menus[3].append(["button",900,275,120,30,False,tx[lan]["remove"],"small",False])
    menus[3].append(["button",900,325,120,30,False,tx[lan]["remove"],"small",False])
    menus[3].append(["button",900,375,120,30,False,tx[lan]["remove"],"small",False])
    menus[3].append(["button",900,425,120,30,False,tx[lan]["remove"],"small",False])
    menus[3].append(["button",900,475,120,30,False,tx[lan]["remove"],"small",False])

buildmenus()

def draw_menu(phase=0):
    for index,item in enumerate(menus[phase]):
        if item[0] == "label" or item[0] == "clabel":
            color = (0, 0, 0)
            if item[0] == "clabel":
                color=item[9]
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
    menu_current=1
def okfuncs(which,misc=""):
    global db_editingcol
    if which==0:
        global db_dbname
        db_dbname = db_dbname.replace(" ", "_")
        if db_dbname[-5:] != ".json":
            db_dbname+=".json"
    if which==1:
        if db_editingname == "":
            display_message(tx[lan]["itemcantbeempty"])
        else:
            display_keyboard(tx[lan]["defvalue?"], "db_editingdefault", digital=True, switchable=False, begin_with_upper=False,
                         fraction=True, okfunc="okfuncs(2)")
    if which==2:
        db_editingcol=(0,0,0)
        display_colorpicker("db_editingcol",db_editingname,"okfuncs(2.5)")
    if which==2.5:
        db_nums.append([db_editingname,db_editingdefault,db_editingcol])

    if which==3:
        if db_editingname == "":
            display_message(tx[lan]["itemcantbeempty"])
        else:
            display_keyboard(tx[lan]["checkedunchecked"], "db_editingdefault", digital=True, switchable=False, begin_with_upper=False,
                         fraction=False, okfunc="okfuncs(4)")
    if which==4:
        db_editingcol=(0,0,0)
        display_colorpicker("db_editingcol",db_editingname,"okfuncs(4.5)")
    if which==4.5:
        if db_editingdefault == 1:
            db_bools.append([db_editingname,True,db_editingcol])
        else:
            db_bools.append([db_editingname,False,db_editingcol])
def menu_press():
    global last_button
    global menu_current
    global lan
    if last_button != -1:
        button = menus[menu_current][last_button]
        button[8] = False
        last_button = -1
        if button is menus[0][3]:
            terminate_program()
        elif button is menus[0][1]:
            menu_current = 1
        elif button is menus[0][4]:
            print("haha")
            if lan=="en":
                lan="bg"
            else:
                lan="en"
            buildmenus()
        elif button is menus[1][2]:
            display_keyboard(tx[lan]["nameurdb"], "db_dbname", digital=False, switchable=True, begin_with_upper=False,fraction=True, default_text=db_dbname,okfunc='okfuncs(0)')
        elif button is menus[1][4]:
            display_keyboard(tx[lan]["wasurname"],"db_name",digital=False,switchable=False,begin_with_upper=True,fraction=True,default_text=db_name,multilingual=True)
        elif button is menus[1][5]:
            if db_dbname == "":
                display_message(tx[lan]["dbcantbeempty"])
            elif db_name == "":
                display_message(tx[lan]["mustfillname"])
            elif db_length <= 0:
                display_message(tx[lan]["dblengthmust"])
            else:
                menu_current = 2
        elif button is menus[1][6]:
            menu_current = 0
        elif button is menus[1][8]:
            display_keyboard(tx[lan]["howmanydays"],"db_length",digital=True,switchable=False,begin_with_upper=True,fraction=False,default_text=db_length)
        elif button is menus[2][10]:
            display_keyboard(tx[lan]["whattotrack"], "db_editingname", digital=False, switchable=True, begin_with_upper=False,fraction=False,okfunc="okfuncs(1)",multilingual=True)
        elif button is menus[2][11]:
            menu_current = 1
        elif button is menus[2][12]:
            menu_current = 3
        elif button is menus[3][10]:
            display_keyboard(tx[lan]["whattotrack"], "db_editingname", digital=False, switchable=True, begin_with_upper=False,fraction=False,okfunc="okfuncs(3)",multilingual=True)
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
def display_keyboard(title,to_set,digital=False,switchable=True,begin_with_upper=False,fraction=False,okfunc="",default_text="",multilingual=False):
    global keyboard_shown
    global keyboard_entry
    global lower
    global keyboard_digital
    global keyboard_target
    global letters
    global letters_lat
    global letters_cyr
    global keyboard_switchable
    global keyboard_fraction
    global keyboard_finalfunc
    global keyboard_multilingual
    global tf
    if default_text != "":
        tf=str(default_text)
    special_keys[6][4] = "БГ"
    letters = letters_lat
    keyboard_finalfunc = okfunc
    keyboard_switchable = switchable
    keyboard_target = to_set
    keyboard_entry = title
    keyboard_digital = digital
    keyboard_fraction = fraction
    if lan=="bg":
        keyboard_multilingual = multilingual
    else:
        keyboard_multilingual = False
    if switchable:
        keyboard_fraction = True
    lower = not begin_with_upper
    keyboard_shown = True
    if begin_with_upper:
        letters = letters.upper()
        letters_lat = letters_lat.upper()
        letters_cyr = letters_cyr.upper()
    else:
        letters = letters.lower()
        letters_lat = letters_lat.lower()
        letters_cyr = letters_cyr.lower()
    if begin_with_upper and not digital:
        special_keys[0][5] = True
def keyboard_press():
    global tf
    global lower
    global letters
    global letters_lat
    global letters_cyr
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
                if key[4] != 26 or letters == letters_cyr:
                    tf += letters[key[4]]
                    if not lower:
                        lower = True
                        special_keys[0][5] = False
                        letters = letters.lower()
                        letters_lat = letters_lat.lower()
                        letters_cyr = letters_cyr.lower()
                last_key = -1
            else:
                key = special_keys[last_key-100]
                key[5] = False
                if key[4] == "bksp":
                    tf = tf[:-1]
                elif key[4] == "shift":
                    if lower:
                        letters = letters.upper()
                        letters_lat = letters_lat.upper()
                        letters_cyr = letters_cyr.upper()
                        lower = False
                        key[5] = True
                    else:
                        letters = letters.lower()
                        letters_lat = letters_lat.lower()
                        letters_cyr = letters_cyr.lower()
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
                elif key[4] == "EN" and keyboard_multilingual:
                    letters = letters_lat
                    special_keys[6][4]="БГ"
                elif key[4] == "БГ" and keyboard_multilingual:
                    letters = letters_cyr
                    special_keys[6][4]="EN"
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
            if key[4]==26 and letters == letters_lat:
                continue
            if key[5]:
                pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
            pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)
            if len(key)==7:
                tempsurface = my_font_s.render(letters[key[4]], False, (0,0,0))
                DISPLAY.blit(tempsurface,(key[0]+10,key[1]+50-tempsurface.get_size()[1]/2))
            else:
                DISPLAY.blit(my_font.render(letters[key[4]], False, (0,0,0)),(key[0]+20,key[1]+20))
        for key in special_keys:
            if key[4] == "֍" and not keyboard_switchable:
                continue
            if not (not keyboard_multilingual and len(key)==7):
                if key[5]:
                    pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
                pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)
            if len(key)==7:
                if keyboard_multilingual:
                    tempsurface = my_font_s.render(key[4], False, (0,0,0))
                    DISPLAY.blit(tempsurface,(key[0]+10,key[1]+(key[3]/2)-tempsurface.get_size()[1]/2))
            else:
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
testcol = (0,0,0)

while True:
    # step
    #region
    if not keyboard_shown and not message_show:
        if menu_current == 2:
            for i in range(9):
                if i <= len(db_nums) - 1:
                    menus[2][i + 1][6] = db_nums[i][0] + " | "+tx[lan]["default"]+": " + str(db_nums[i][1])
                    menus[2][i + 1][9] = db_nums[i][2]
                    menus[2][i + 13][1] = 900
                else:
                    menus[2][i + 1][6] = tx[lan]["empty"]
                    menus[2][i + 1][9] = (127,127,127)
                    menus[2][i + 13][1] = 1100
        elif menu_current == 3:
            for i in range(9):
                if i <= len(db_bools) - 1:
                    if db_bools[i][1] == True:
                        menus[3][i + 1][6] = db_bools[i][0] + " | "+tx[lan]["default"]+": √"
                    else:
                        menus[3][i + 1][6] = db_bools[i][0] + " | "+tx[lan]["default"]+": X"
                    menus[3][i + 1][9] = db_bools[i][2]
                    menus[3][i + 13][1] = 900
                else:
                    menus[3][i + 1][6] = tx[lan]["empty"]
                    menus[3][i + 1][9] = (127,127,127)
                    menus[3][i + 13][1] = 1100
    #endregion
    # events
    #region
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONUP:
            if message_show:
                message_press()
            else:
                if keyboard_shown:
                    keyboard_press()
                elif colorpicker_show:
                    colorpicker_press()
                else:
                    menu_press()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if message_show:
                message_highlight()
            else:
                if keyboard_shown:
                    keyboard_highlight()
                elif colorpicker_show:
                    colorpicker_highlight()
                else:
                    menu_highlight()
        if event.type == pygame.USEREVENT:
            counter+=1
            if counter % 4 == 0:
                print(testcol)
                if blinker==" ":
                    blinker="|"
                else:
                    blinker=" "
    #endregion
    # draw
    #region
    DISPLAY.fill(WHITE)
    if message_show:
        draw_message()
    else:
        if keyboard_shown:
            draw_keyboard()
        elif colorpicker_show:
            draw_colorpicker()
        else:
            draw_menu(menu_current)
    pygame.display.update()
    #endregion