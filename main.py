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
        "months": ["January","February","March","April","May","June","July","August","September","October","November","December"],
        "weekdays": ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"],
        "show": "Show",
        "hide": "Hide",
        "reminders": "Reminders:",
        "refresh": "refresh",
        "no": "no",
        "yes": "yes",
        "editing": "editing",
        "otherlang": "БГ"
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
        "months": ["Януари","Февруари","Март","Април","Май","Юни","Юли","Август","Септември","Октомври","Ноември","Декември"],
        "weekdays": ["понеделник","вторник","сряда","четвъртък","петък","събота","неделя"],
        "show": "Покажи",
        "hide": "Скрий",
        "reminders": "Бележки:",
        "refresh": "опресни",
        "no": "не",
        "yes": "да",
        "editing": "редакт.",
        "otherlang": "EN"
    }
}
lan = "en"
############IMPORT AND MAIN SETTINGS####################
#region
print("Importing libraries...")
import pygame
import json
import datetime
import os
from sys import exit as terminate_program
pygame.init()
DISPLAY = pygame.display.set_mode((1024,600),0,32)
WHITE = (255,255,255)
pygame.time.set_timer(pygame.USEREVENT, 100)
db={}
current_wkday = datetime.datetime.today().weekday()
current_month = datetime.datetime.today().month
current_date = datetime.datetime.today().day
current_year = datetime.datetime.today().year
#endregion
###########MESSAGE ENGINE INITIALIZE####################
#region
print("Initializing message engine...")
message_show = False
message_to_show = "You can't leave@any field empty!"
message_ok_hl = False
msg_okfunc=""

def display_message(title,okfunc=""):
    global message_show
    global message_ok_hl
    global message_to_show
    global msg_okfunc
    if okfunc!="":
        msg_okfunc=okfunc
    message_to_show = title
    message_ok_hl = False
    message_show = True
def draw_message():
    global message_to_show
    global terminal_message
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
    if not run:
        name_surface=my_font_xs.render(os.getcwd(),True,(0,0,0))
        DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 520))


def message_highlight():
    global message_ok_hl
    if pygame.Rect(406,400,212,75).collidepoint(pygame.mouse.get_pos()):
        message_ok_hl = True
def message_press():
    global message_ok_hl
    global message_to_show
    global message_show
    global msg_okfunc
    if message_ok_hl:
        message_ok_hl = False
        message_to_show = "Error"
        message_show = False
    if msg_okfunc!="":
        exec(msg_okfunc,globals())
        msg_okfunc=""
#endregion
run=True
def download_font():
    global run
    global my_font
    global my_font_m
    global my_font_s
    global my_font_xs
    try:
        import requests
    except ModuleNotFoundError:
        run=False
        display_message("\"requests\" module not found!@Please download \"calibri.ttf\"@manually and place it@in the directory below!")
    else:
        try:
            URL = "https://github.com/hellgames1/life-manager/raw/main/calibri.ttf"
            response = requests.get(URL,timeout=3)
            response.raise_for_status()
        except requests.exceptions.HTTPError:
            run=False
            display_message("HTTP Error!@Please download \"calibri.ttf\"@manually and place it@in the directory below!")
        except requests.exceptions.ConnectionError:
            run=False
            display_message("Connection error!@Please download \"calibri.ttf\"@manually and place@it in the directory below!")
        except requests.exceptions.Timeout:
            run=False
            display_message("Error - timeout!@Please download \"calibri.ttf\"@manually and place@it in the directory below!")
        except requests.exceptions.RequestException:
            run=False
            display_message("Weird error!@Please download \"calibri.ttf\"@manually and place@it in the directory below!")
        else:
            try:
                open("calibri.ttf", "wb").write(response.content)
            except:
                run=False
                display_message("Error saving file!@Please download \"calibri.ttf\"@manually and place it@in the directory below!")
            else:
                my_font = pygame.font.Font("calibri.ttf", 72)
                my_font_m = pygame.font.Font("calibri.ttf", 48)
                my_font_s = pygame.font.Font("calibri.ttf", 36)
                my_font_xs = pygame.font.Font("calibri.ttf", 24)
                display_message("Success!")

############KEYBOARD INITIALIZE#########################
#region
print("Initializing keyboard...")
try:
    my_font = pygame.font.Font("calibri.ttf", 72)
    my_font_m = pygame.font.Font("calibri.ttf", 48)
    my_font_s = pygame.font.Font("calibri.ttf", 36)
    my_font_xs = pygame.font.Font("calibri.ttf", 24)
except FileNotFoundError:
    my_font = pygame.font.SysFont("Calibri", 72)
    my_font_m = pygame.font.SysFont("Calibri", 48)
    my_font_s = pygame.font.SysFont("Calibri", 36)
    my_font_xs = pygame.font.SysFont("Calibri", 24)
    display_message("\"calibri.ttf\" font file not found!@Attempting to download from@hellgames1 github...","download_font()")
    #display_message("\"calibri.ttf\" font file not found!@Please place the file in the@program's directory below!")

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

def okfuncs(which,misc=-1):
    global db_editingcol
    global widget_editingpart
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
    if which==5:
        newdb = db.copy()
        tsatsa=round((db["days"][currentday]["ints"][misc]-widget_editingpart)*100)/100
        if tsatsa == int(tsatsa):
            tsatsa=int(tsatsa)
        newdb["days"][currentday]["ints"][misc] = tsatsa
        updatedb(newdb)
    if which==6:
        newdb = db.copy()
        tsatsa=round((db["days"][currentday]["ints"][misc]+widget_editingpart)*100)/100
        if tsatsa == int(tsatsa):
            tsatsa=int(tsatsa)
        newdb["days"][currentday]["ints"][misc] = tsatsa
        updatedb(newdb)
    if which==7:
        newdb = db.copy()
        widget_editingpart = round(widget_editingpart*100)/100
        if widget_editingpart == int(widget_editingpart):
            widget_editingpart = int(widget_editingpart)
        newdb["days"][currentday]["ints"][misc] = widget_editingpart
        updatedb(newdb)
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
###################################################
#endregion

############COLOR PICKER INITIALIZE#####################
#region
print("Initializing color picker...")
colorpicker_show = False
colorpicker_displaytext = "error"
colorpicker_currentcol = (0,0,0)
colorpicker_ok_hl = False
colorpicker_tovar=""
colorpicker_okfunc=""

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
#########################################################
#endregion

currentday=0
###########DB EDITOR INITALIZE##########################
#region
print("Initializing database editor...")
db_dbname=""
db_name=""
db_nums = []
db_bools = []
db_editingname = ""
db_editingdefault = 0
db_editingcol = (0,0,0)
db_length=365
def loaddb(filename,set_current_day):
    global db
    global menu_current
    global calendar_shown
    global calendar
    global currentday
    global calendar_scrolled
    global db_dbname
    db_dbname = filename
    f = open(filename, "r")
    db = json.loads(f.read())
    calendar=[]
    for i in range(len(db["days"])):
        calendar.append([db["days"][i]["wkd"]*80, db["days"][i]["wksince"]*80,80,80,db["days"][i]["dt"],db["days"][i]["mn"],db["days"][i]["yr"]])
        if set_current_day:
            if db["days"][i]["dt"] == datetime.datetime.today().day:
                if db["days"][i]["mn"] == datetime.datetime.today().month:
                    if db["days"][i]["yr"] == datetime.datetime.today().year:
                        currentday = len(calendar)-1
                        calendar_scrolled= - db["days"][i]["wksince"]*80+260

    #calendar_shown = True
    load_widgets()
    menu_current=6
def createdb():
    global menu_current
    global db
    print("creating")
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
    db["datealignment"]=widget_alignments
    db["positionstyles"]=[]
    for item in widgets:
        db["positionstyles"].append([item[2],item[3],item[1]])
    db["days"]=[]
    day = {"wkd": -1, "dt": -1, "mn": -1, "yr": -1, "wksince": -1, "reminders": [], "ints": [], "bools": []}
    day["ints"]=db["intdefs"]
    day["bools"]=db["booldefs"]
    wkday = datetime.datetime.today().weekday()
    month = datetime.datetime.today().month
    date = datetime.datetime.today().day
    year = datetime.datetime.today().year
    wksince=0
    for i in range(db_length):
        cday = day.copy()
        cday["wkd"]=wkday
        cday["dt"]=date
        cday["mn"]=month
        cday["yr"]=year
        cday["wksince"]=wksince
        db["days"].append(cday)
        wkday+=1
        if wkday>=7:
            wkday=0
            wksince+=1
        date+=1
        if month==1 or month==3 or month==5 or month==7 or month==8 or month==10 or month==12:
            if date==32:
                date=1
                month+=1
        elif month == 4 or month == 6 or month == 9 or month == 11:
            if date == 31:
                date = 1
                month += 1
        elif month == 2:
            if year % 4 == 0 and date == 30:
                date = 1
                month += 1
            elif year % 4 != 0 and date == 29:
                date = 1
                month += 1
        if month == 13:
            month = 1
            year+=1

    with open(db_dbname, 'w') as outfile:
        json.dump(db, outfile)
        menu_current = 0
        display_message(tx[lan]["database"]+"@"+db_dbname+"@"+tx[lan]["created"])
def dblist_show():
    global menus
    global menu_current
    menus[4]=[]
    menus[4].append(["label", -1, 0, -1, -1, True, tx[lan]["loaddb"], "large", False])
    menus[4].append(["button",750,500,250,75,False,tx[lan]["refresh"],"medium",False])
    menus[4].append(["button",25,500,250,75,False,tx[lan]["cancel"],"medium",False])
    index=0
    for obj in os.listdir():
        if obj[-5:] == ".json":
            menus[4].append(["button", -1, 100+index*60, 500, 50, True, obj, "small", False])
            index+=1
            if index==6:
                break
    menu_current=4
#endregion


#############MENU ENGINE INITIALIZE#################
#region
print("Initializing menus...")
menu_current = 0
last_button = -1
menus = [[],[],[],[],[],[],[]]
# if label, no w or h applicable, if centered, only y applicable
# if centered button, no x applicable
# type||xpos||ypos||w||h||center||text||font||highlighted
# 0type 1xpos 2ypos 3w 4h 5center 6text 7font 8hl
def buildmenus():
    global menus
    menus = [[],[],[],[],[],[],[]]
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

    menus[5].append(["button", 0, 200, 80, 200, False, "OK", "medium", False])
    menus[5].append(["button_context", 0, 400, 80, 100, False, tx[lan]["hide"], "tiny", False,"widgets_visualize",True])
    menus[5].append(["button_context", 0, 400, 80, 100, False, tx[lan]["show"], "tiny", False,"widgets_visualize",False])

    menus[6].append(["button_context",200,0,200,80,False,"↑↑↑","medium",False,"calendar_shown",True])
    menus[6].append(["button_context",200,520,200,80,False,"↓↓↓","medium",False,"calendar_shown",True])
    menus[6].append(["button_context",560,200,80,200,False,"<","medium",False,"calendar_shown",True])
    menus[6].append(["button_context",0,200,80,200,False,">","medium",False,"calendar_shown",False])
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
            elif item[7] == "tiny":
                name_surface = my_font_xs.render(item[6], False, color )
            if item[5] == True: # if centered
                DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), item[2]))
            else: # if not centered
                DISPLAY.blit(name_surface, (item[1], item[2]))
        elif item[0] == "button" or item[0] == "button_context" or item[0] == "textfield":
            if item[0] == "button" or item[0] == "button_context":
                label=item[6]
            else:
                label=str(globals()[item[6]])
            if item[7] == "large":
                name_surface = my_font.render(label, False, (0, 0, 0))
            elif item[7] == "medium":
                name_surface = my_font_m.render(label, False, (0, 0, 0))
            elif item[7] == "small":
                name_surface = my_font_s.render(label, False, (0, 0, 0))
            elif item[7] == "tiny":
                name_surface = my_font_xs.render(label, False, (0, 0, 0))
            draw=True
            if item[0] == "button_context" and globals()[item[9]] == (not item[10]):
                draw=False
            if draw:
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
    global calendar_shown
    global calendar_scroll
    for index,button in enumerate(menus[menu_current]):
        if button[0] == "button_context" and globals()[button[9]] == (not button[10]):
            continue
        if button[5] == True:
            iscolliding = pygame.Rect(512-(button[3]/2), button[2], button[3], button[4]).collidepoint(pygame.mouse.get_pos())
        else:
            iscolliding = pygame.Rect(button[1], button[2], button[3], button[4]).collidepoint(pygame.mouse.get_pos())
        if iscolliding:
            button[8] = True
            last_button = index
            if menu_current==6 and calendar_shown:
                if index==0:
                    calendar_scroll=20
                elif index==1:
                    calendar_scroll=-20
            break
def menu_press():
    global last_button
    global menu_current
    global lan
    global calendar_scroll
    global calendar_shown
    global widgets_visualize
    if last_button != -1:
        button = menus[menu_current][last_button]
        button[8] = False
        last_button = -1
        if button[0] == "button_context" and globals()[button[9]] == (not button[10]):
            return
        if button is menus[0][3]:
            terminate_program()
        elif button is menus[0][1]:
            menu_current = 1
        elif button is menus[0][2]:
            dblist_show()
        elif button is menus[0][4]:
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
            generate_widgets()
            menu_current = 5
        elif button is menus[5][0]:
            createdb()
        elif button is menus[5][1]:
            widgets_visualize=False
        elif button is menus[5][2]:
            widgets_visualize=True
        elif button is menus[6][0] or button is menus[6][1]:
            calendar_scroll=0
        elif button is menus[6][2] or button is menus[6][3]:
            calendar_shown = not calendar_shown
        else:
            try:
                if button is menus[4][1]:
                    dblist_show()
                elif button is menus[4][2]:
                    menu_current = 0
                elif button is menus[4][3]:
                    loaddb(menus[4][3][6],True)
                elif button is menus[4][4]:
                    loaddb(menus[4][4][6],True)
                elif button is menus[4][5]:
                    loaddb(menus[4][5][6],True)
                elif button is menus[4][6]:
                    loaddb(menus[4][6][6],True)
                elif button is menus[4][7]:
                    loaddb(menus[4][7][6],True)
                elif button is menus[4][8]:
                    loaddb(menus[4][8][6],True)
            except IndexError:
                print("index error baby")
        for i in range(13,22):
            if button is menus[2][i]:
                db_nums.pop(i-13)
            elif button is menus[3][i]:
                db_bools.pop(i-13)
#endregion
#############EDITOR############################
widgets=[]
widget_selected = -1
widget_selected_actual = -1
widget_selected_type="bool"
widget_selection_offset=[]
widget_alignments="left"
widget_datesize=0
widgets_visualize=True
widget_tempsizes=[[0,0],[0,0],[0,0]]
boolstart=-1
widget_editingpart=""
istoday=True
def load_widgets():
    global db
    global widgets
    global widget_alignments
    global currentday
    global widget_tempsizes
    global boolstart
    widget_alignments = db["datealignment"]
    widgets=[["__clock",0,db["positionstyles"][0][0],db["positionstyles"][0][1],(0,0,0),-1]]
    widgets.append(["__date",0,db["positionstyles"][1][0],db["positionstyles"][1][1],(0,0,0),-1])
    widgets.append(["__rem",0,db["positionstyles"][2][0],db["positionstyles"][2][1],(0,0,0),-1])
    widget_tempsizes = [[0,0],[0,0],[0,0]]
    for index,item in enumerate(db["days"][currentday]["ints"]):
        widgets.append([db["intnames"][index],
                        db["positionstyles"][index+3][2],db["positionstyles"][index+3][0],
                        db["positionstyles"][index+3][1],db["intcols"][index],str(item)])
        widget_tempsizes.append([0,0])
    boolstart=len(widgets)
    for index,item in enumerate(db["days"][currentday]["bools"]):
        widgets.append([db["boolnames"][index],
                        db["positionstyles"][index+boolstart][2],db["positionstyles"][index+boolstart][0],
                        db["positionstyles"][index+boolstart][1],db["boolcols"][index],item])
        widget_tempsizes.append([0,0])

def draw_awidget(placing_x,placing_y,text,index,style,color,value=-1):
    global widget_selected
    global widget_selected_actual
    global widget_datesize
    global widget_tempsizes
    global istoday
    value=str(value)
    if text=="__clock":
        if istoday:
            name_surface = my_font_m.render(datetime.datetime.now().strftime("%H:%M:%S"), False, (0, 0, 0))
        else:
            name_surface = my_font_m.render(tx[lan]["editing"], False, (128, 128, 128))
    elif text=="__date":
        if db["days"][currentday]["dt"] == datetime.datetime.today().day and db["days"][currentday]["mn"] == datetime.datetime.today().month and db["days"][currentday]["yr"] == datetime.datetime.today().year:
            name_surface = my_font_m.render(str(current_date) + " " + tx[lan]["months"][current_month-1] + " " + str(current_year), False, (0, 0, 0))
            istoday=True
        else:
            name_surface = my_font_m.render(str(db["days"][currentday]["dt"]) + " " + tx[lan]["months"][db["days"][currentday]["mn"]-1] + " " + str(db["days"][currentday]["yr"]), False, (128, 128, 128))
            istoday=False
        widget_datesize = name_surface.get_size()[0]
    elif text == "__rem":
        name_surface = my_font_xs.render(tx[lan]["reminders"], False, (0, 0, 0))


    if text=="__clock":
        DISPLAY.blit(name_surface, (placing_x, placing_y))
    elif text=="__date":
        if widget_alignments=="left":
            DISPLAY.blit(name_surface, (placing_x, placing_y))
        elif widget_alignments=="center":
            DISPLAY.blit(name_surface, (placing_x-widget_datesize/2, placing_y))
        elif widget_alignments=="right":
            DISPLAY.blit(name_surface, (placing_x-widget_datesize, placing_y))
    elif text=="__rem":
        DISPLAY.blit(name_surface, (placing_x-name_surface.get_size()[0]/2, placing_y+5))
        pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - 178, placing_y+2, 360, 116), 5)
    else:
        name_surfacea = my_font_s.render(text, False, color)
        widget_tempsizes[index][0]=name_surfacea.get_size()[0]
        DISPLAY.blit(name_surfacea, (placing_x - widget_tempsizes[index][0] / 2, placing_y))
        name_surface = my_font_s.render(value, False, (0, 0, 0))
        widget_tempsizes[index][1] = name_surface.get_size()[0]

        if style==0:
            if widget_selected_actual==index:
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x - widget_tempsizes[index][1]/2 - 20, placing_y+40, widget_tempsizes[index][1]+40, 40))
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x - widget_tempsizes[index][1]/2 - 20, placing_y+40, widget_tempsizes[index][1]+40, 40),5)
        elif style==1:
            if widget_selected_actual==index:
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x + widget_tempsizes[index][0] / 2 + 8 , placing_y-5, widget_tempsizes[index][1]+40, 40))
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x + widget_tempsizes[index][0] / 2 + 8 , placing_y-5, widget_tempsizes[index][1]+40, 40),5)
        elif style==2:
            if widget_selected_actual==index and widget_selected_type=="int-":
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x - widget_tempsizes[index][1] / 2 - 60, placing_y + 40, 40, 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - widget_tempsizes[index][1] / 2 - 60, placing_y + 40, 40, 40), 5)
            DISPLAY.blit(my_font_m.render("-", False, (0, 0, 0)), (placing_x - widget_tempsizes[index][1] / 2 - 50, placing_y + 40))
            if widget_selected_actual==index and widget_selected_type=="int+":
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 40, 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 40, 40), 5)
            DISPLAY.blit(my_font_m.render("+", False, (0, 0, 0)), (placing_x + widget_tempsizes[index][1] / 2 + 30, placing_y + 40))
        elif style==3:
            if widget_selected_actual==index and widget_selected_type=="int--":
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x - widget_tempsizes[index][1] / 2 - 70, placing_y + 40, 50, 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - widget_tempsizes[index][1] / 2 - 70, placing_y + 40, 50, 40), 5)
            DISPLAY.blit(my_font_s.render("--", False, (0, 0, 0)), (placing_x - widget_tempsizes[index][1] / 2 - 60, placing_y + 44))
            if widget_selected_actual==index and widget_selected_type=="int++":
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 50, 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 50, 40), 5)
            DISPLAY.blit(my_font_s.render("++", False, (0, 0, 0)), (placing_x + widget_tempsizes[index][1] / 2 + 28, placing_y + 44))
        elif style==4:
            if widget_selected_actual==index:
                pygame.draw.rect(DISPLAY,(127,127,127), (placing_x - 20, placing_y+40, 40, 40))
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x - 20, placing_y+40, 40, 40),5)
        elif style==5:
            if widget_selected_actual==index:
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x + widget_tempsizes[index][0] / 2 + 8 , placing_y-5, 40, 40))
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x + widget_tempsizes[index][0] / 2 + 8 , placing_y-5, 40, 40),5)
        elif style==6:
            if widget_selected_actual==index:
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x - widget_tempsizes[index][0] / 2 - 48 , placing_y-5, 40, 40))
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x - widget_tempsizes[index][0] / 2 - 48 , placing_y-5, 40, 40),5)


        if style == 4:
            if value=="True":
                name_surface = my_font_m.render("√", False, (0, 0, 0))
                DISPLAY.blit(name_surface, (placing_x - 12, placing_y + 40))
        elif style == 5:
            if value=="True":
                name_surface = my_font_m.render("√", False, (0, 0, 0))
                DISPLAY.blit(name_surface, (placing_x + name_surfacea.get_size()[0] / 2 + 16, placing_y - 5))
        elif style == 6:
            if value=="True":
                name_surface = my_font_m.render("√", False, (0, 0, 0))
                DISPLAY.blit(name_surface, (placing_x - name_surfacea.get_size()[0] / 2 -40, placing_y - 5))
        elif style!=1:
            DISPLAY.blit(name_surface, (placing_x - widget_tempsizes[index][1] / 2, placing_y + 45))
        else:
            DISPLAY.blit(name_surface, (placing_x + widget_tempsizes[index][0] / 2 + 8 + widget_tempsizes[index][1]/2+20 - widget_tempsizes[index][1]/2, placing_y))

def updatedb(newdb):
    global db_dbname
    with open(db_dbname, 'w') as outfile:
        json.dump(newdb, outfile)
    loaddb(db_dbname,False)
def highlight_awidget(placing_x,placing_y,index,style):
    global widget_selected
    global widget_selected_actual
    global widget_selected_type
    global widget_datesize
    global widget_alignments
    global widget_tempsizes
    if widget_selected==-1:
        if style==0:
            if pygame.Rect(placing_x - widget_tempsizes[index][1]/2 - 20, placing_y+40, widget_tempsizes[index][1]+40, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int"
                print("change int number "+str(index-3))
        elif style==1:
            if pygame.Rect(placing_x + widget_tempsizes[index][0] / 2 + 8 , placing_y-5, widget_tempsizes[index][1]+40, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int"
                print("change int number "+str(index-3))
        elif style==2:
            if pygame.Rect(placing_x - widget_tempsizes[index][1] / 2 - 60, placing_y + 40, 40, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int-"
                print("minus int number "+str(index-3))
            if pygame.Rect(placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 40, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int+"
                print("plus int number "+str(index-3))
        elif style==3:
            if pygame.Rect(placing_x - widget_tempsizes[index][1] / 2 - 70, placing_y + 40, 50, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int--"
                print("minus minus int number "+str(index-3))
            if pygame.Rect(placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 50, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int++"
                print("plus plus int number "+str(index-3))
        elif style==4:
            if pygame.Rect(placing_x - 20, placing_y+40, 40, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-boolstart
                widget_selected_actual=index
                widget_selected_type="bool"
                print("bool int number "+str(index-boolstart))
        elif style==5:
            if pygame.Rect(placing_x + widget_tempsizes[index][0] / 2 + 8 , placing_y-5, 40, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-boolstart
                widget_selected_actual=index
                widget_selected_type="bool"
                print("bool int number "+str(index-boolstart))
        elif style==6:
            if pygame.Rect(placing_x - widget_tempsizes[index][0] / 2 - 48 , placing_y-5, 40, 40).collidepoint(pygame.mouse.get_pos()):
                widget_selected=index-boolstart
                widget_selected_actual=index
                widget_selected_type="bool"
                print("bool int number "+str(index-boolstart))

def press_awidget():
    global widget_selected
    global widget_selected_actual
    global widget_selected_type
    global currentday
    if widget_selected!=-1:
        if widget_selected_type=="bool":
            newdb = db.copy()
            newdb["days"][currentday]["bools"][widget_selected] = not db["days"][currentday]["bools"][widget_selected]
            updatedb(newdb)
        elif widget_selected_type=="int-":
            newdb = db.copy()
            newdb["days"][currentday]["ints"][widget_selected] = db["days"][currentday]["ints"][widget_selected]-1
            updatedb(newdb)
        elif widget_selected_type=="int+":
            newdb = db.copy()
            newdb["days"][currentday]["ints"][widget_selected] = db["days"][currentday]["ints"][widget_selected]+1
            updatedb(newdb)
        elif widget_selected_type=="int--":
            display_keyboard(db["intnames"][widget_selected]+" = "+str(db["days"][currentday]["ints"][widget_selected])+" - ?","widget_editingpart",True,False,False,True,"okfuncs(5,"+str(widget_selected)+")","",False)
        elif widget_selected_type=="int++":
            display_keyboard(db["intnames"][widget_selected]+" = "+str(db["days"][currentday]["ints"][widget_selected])+" + ?","widget_editingpart",True,False,False,True,"okfuncs(6,"+str(widget_selected)+")","",False)
        elif widget_selected_type=="int":
            display_keyboard(db["intnames"][widget_selected]+" = ?","widget_editingpart",True,False,False,True,"okfuncs(7,"+str(widget_selected)+")","",False)
        widget_selected=-1
        widget_selected_actual=-1
def generate_widgets():
    global widgets
    x=300
    y=80
    widgets = [["__clock", 0, 60, 20, (0,0,0),-1], ["__date", 0, 800, 20, (0,0,0),-1], ["__rem", 0, 300, 20, (0,0,0),-1]]
    for index,item in enumerate(db_nums):
        widgets.append([item[0],0,x,y,item[2],item[1]])
        if y<480:
            y+=80
        else:
            x+=250
            y=80
    for index,item in enumerate(db_bools):
        widgets.append([item[0],4,x,y,item[2],item[1]])
        if y<480:
            y+=80
        else:
            x+=250
            y=80

def highlight_ewidget():
    global widget_selected
    global widget_selection_offset
    global widget_datesize
    global widget_alignments
    if widget_selected==-1:
        for index, widget in enumerate(widgets):
            if index==1 and pygame.Rect(widget[2]-20,widget[3]+40,40,40).collidepoint(pygame.mouse.get_pos()):
                if widget_alignments=="left":
                    widget_alignments="center"
                elif widget_alignments=="center":
                    widget_alignments="right"
                elif widget_alignments=="right":
                    widget_alignments="left"

            if pygame.Rect(widget[2]-20,widget[3],40,40).collidepoint(pygame.mouse.get_pos()):
                widget_selection_offset = [pygame.mouse.get_pos()[0]-widget[2],pygame.mouse.get_pos()[1]-widget[3]]
                widget_selected=index

            if index!=0 and index!=1 and pygame.Rect(widget[2] -20, widget[3]-40, 40, 40).collidepoint(pygame.mouse.get_pos()):
                if type(widget[5])==bool:
                    if widget[1]<6:
                        widget[1]+=1
                    else:
                        widget[1]=4
                else:
                    if widget[1]<3:
                        widget[1]+=1
                    else:
                        widget[1]=0
def press_ewidget():
    global widget_selected
    widget_selected=-1
def draw_ewidget(placing_x,placing_y,text,index,style,color,defvalue=0):
    global widget_selected
    global widget_datesize
    global widgets_visualize
    defvalue=str(defvalue)
    if text=="__clock":
        name_surface = my_font_m.render(datetime.datetime.now().strftime("%H:%M:%S"), False, (0, 0, 0))
    elif text=="__date":
        name_surface = my_font_m.render(str(current_date) + " " + tx[lan]["months"][counter-1] + " " + str(current_year), False, (0, 0, 0))
        widget_datesize = name_surface.get_size()[0]
        if widgets_visualize:
            DISPLAY.blit(my_font_s.render("↔", False, (230, 230, 230)), (placing_x -20, placing_y +42))
            pygame.draw.rect(DISPLAY, (230, 230, 230), (placing_x -20, placing_y+40, 40, 40), 5)
    elif text == "__rem":
        name_surface = my_font_xs.render(tx[lan]["reminders"], False, (0, 0, 0))
    else:
        if widgets_visualize:
            DISPLAY.blit(my_font_s.render("S", False, (230, 230, 230)), (placing_x -8, placing_y -36))
            pygame.draw.rect(DISPLAY, (230, 230, 230), (placing_x -20, placing_y-40, 40, 40), 5)


    if widgets_visualize:
        if widget_selected==index:
            pygame.draw.rect(DISPLAY, (230, 230, 230), (placing_x - 20, placing_y, 40, 40))
            DISPLAY.blit(my_font_s.render("≡", False, (255, 255, 255)), (placing_x - 8, placing_y+2))
        else:
            DISPLAY.blit(my_font_s.render("≡", False, (230, 230, 230)), (placing_x - 8, placing_y + 2))
            pygame.draw.rect(DISPLAY, (230, 230, 230), (placing_x - 20, placing_y, 40, 40), 5)
    if text=="__clock":
        DISPLAY.blit(name_surface, (placing_x, placing_y))
    elif text=="__date":
        if widget_alignments=="left":
            DISPLAY.blit(name_surface, (placing_x, placing_y))
        elif widget_alignments=="center":
            DISPLAY.blit(name_surface, (placing_x-widget_datesize/2, placing_y))
        elif widget_alignments=="right":
            DISPLAY.blit(name_surface, (placing_x-widget_datesize, placing_y))
    elif text=="__rem":
        DISPLAY.blit(name_surface, (placing_x-name_surface.get_size()[0]/2, placing_y+5))
        pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - 178, placing_y+2, 360, 116), 5)
    else:
        name_surfacea = my_font_s.render(text, False, color)
        DISPLAY.blit(name_surfacea, (placing_x - name_surfacea.get_size()[0] / 2, placing_y))
        name_surface = my_font_s.render(defvalue, False, (0, 0, 0))
        #if name_surface.get_size()[0] < 34:
        #    tempsize = 34
        #else:
        tempsize = name_surface.get_size()[0]
        if style == 4:
            name_surface = my_font_m.render("√", False, (0, 0, 0))
            DISPLAY.blit(name_surface, (placing_x - 12, placing_y + 40))
        elif style == 5:
            name_surface = my_font_m.render("√", False, (0, 0, 0))
            DISPLAY.blit(name_surface, (placing_x + name_surfacea.get_size()[0] / 2 + 16, placing_y - 5))
        elif style == 6:
            name_surface = my_font_m.render("√", False, (0, 0, 0))
            DISPLAY.blit(name_surface, (placing_x - name_surfacea.get_size()[0] / 2 -40, placing_y - 5))
        elif style!=1:
            DISPLAY.blit(name_surface, (placing_x - name_surface.get_size()[0] / 2, placing_y + 45))
        else:
            DISPLAY.blit(name_surface, (placing_x + name_surfacea.get_size()[0] / 2 + 8 + tempsize/2+20 - name_surface.get_size()[0]/2, placing_y))

        if style==0:
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x - tempsize/2 - 20, placing_y+40, tempsize+40, 40),5)
        elif style==1:
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x + name_surfacea.get_size()[0] / 2 + 8 , placing_y-5, tempsize+40, 40),5)
        elif style==2:
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - tempsize / 2 - 60, placing_y + 40, 40, 40), 5)
            DISPLAY.blit(my_font_m.render("-", False, (0, 0, 0)), (placing_x - tempsize / 2 - 50, placing_y + 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x + tempsize / 2 + 20, placing_y + 40, 40, 40), 5)
            DISPLAY.blit(my_font_m.render("+", False, (0, 0, 0)), (placing_x + tempsize / 2 + 30, placing_y + 40))
        elif style==3:
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - tempsize / 2 - 70, placing_y + 40, 50, 40), 5)
            DISPLAY.blit(my_font_s.render("--", False, (0, 0, 0)), (placing_x - tempsize / 2 - 60, placing_y + 44))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x + tempsize / 2 + 20, placing_y + 40, 50, 40), 5)
            DISPLAY.blit(my_font_s.render("++", False, (0, 0, 0)), (placing_x + tempsize / 2 + 28, placing_y + 44))
        elif style==4:
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x - 20, placing_y+40, 40, 40),5)
        elif style==5:
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x + name_surfacea.get_size()[0] / 2 + 8 , placing_y-5, 40, 40),5)
        elif style==6:
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x - name_surfacea.get_size()[0] / 2 - 48 , placing_y-5, 40, 40),5)
###############CALENDAR
#region
calendar_shown = False
calendar_scroll = 0
calendar_scrolled = 0
calendar_scrolledmonth = 0
calendar_redbit=(0,0)
calendar=[]
def calendar_highlight():
    global currentday
    global calendar_scrolled
    for index,key in enumerate(calendar):
        ypos = calendar_scrolled + key[1]
        if 520 >= ypos >=0 and 80 < pygame.mouse.get_pos()[1] < 520:
            if pygame.Rect(key[0], ypos , key[2], key[3]).collidepoint(pygame.mouse.get_pos()) and currentday!=index:
                currentday=index
                load_widgets()
def draw_calendar():
    global calendar_scrolledmonth
    global calendar_redbit
    global current_date
    global current_month
    global current_year
    for index,key in enumerate(calendar):
        ypos = calendar_scrolled + key[1]
        if datetime.datetime.today().day==key[4] and datetime.datetime.today().month==key[5]:
            calendar_redbit=(key[0], ypos)
            current_date = key[4]
            current_month = key[5]
            current_year = key[6]
        if 260 >= ypos >= 180:
            calendar_scrolledmonth = key[5]
        if 520 >= ypos >=0:
            if index==currentday:
                pygame.draw.rect(DISPLAY, (199, 199, 199), (key[0], ypos , key[2], key[3]))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (key[0], ypos , key[2], key[3]), 5)
            DISPLAY.blit(my_font_s.render(str(key[4]), False, (0, 0, 0)), (key[0] + 10, ypos + 10))
    pygame.draw.rect(DISPLAY, (200, 0, 0), (calendar_redbit[0],calendar_redbit[1], 80,80), 5)
    pygame.draw.rect(DISPLAY, (255, 255, 255), (0,0,563,80))
    pygame.draw.rect(DISPLAY, (255, 255, 255), (0,520,563,80))
    DISPLAY.blit(my_font_s.render(tx[lan]["months"][calendar_scrolledmonth-1], False, (0, 0, 0)), (420, 20))
    dayshowing = my_font_m.render(str(db["days"][currentday]["dt"]) + " " + tx[lan]["months"][db["days"][currentday]["mn"]-1] + " " + str(db["days"][currentday]["yr"]), False, (0, 0, 0))
    DISPLAY.blit(dayshowing,(792-dayshowing.get_size()[0]/2,0))
    y=60
    for index,item in enumerate(db["intnames"]):
        displaying=my_font_s.render(item + " = " + str(db["days"][currentday]["ints"][index]), False, (db["intcols"][index][0],db["intcols"][index][1],db["intcols"][index][2]))
        DISPLAY.blit(displaying,(670,y))
        y+=30
    for index,item in enumerate(db["boolnames"]):
        if db["days"][currentday]["bools"][index] == True:
            displaying=my_font_s.render(item + " = "+tx[lan]["yes"], False, (db["boolcols"][index][0],db["boolcols"][index][1],db["boolcols"][index][2]))
        else:
            displaying=my_font_s.render(item + " = "+tx[lan]["no"], False, (db["boolcols"][index][0],db["boolcols"][index][1],db["boolcols"][index][2]))
        DISPLAY.blit(displaying,(670,y))
        y+=30
#endregion
counter = 1
print("Beginning main loop...")
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
        elif menu_current == 5 and widget_selected !=- 1:
            widgets[widget_selected][2]=round((pygame.mouse.get_pos()[0]-widget_selection_offset[0])/10)*10
            widgets[widget_selected][3]=round((pygame.mouse.get_pos()[1]-widget_selection_offset[1])/10)*10
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
                    if menu_current==5:
                        press_ewidget()
                    elif menu_current==6:
                        if not calendar_shown:
                            press_awidget()
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
                    if menu_current==5:
                        highlight_ewidget()
                    elif menu_current==6:
                        if not calendar_shown:
                            for index, widget in enumerate(widgets):
                                highlight_awidget(widgets[index][2], widgets[index][3], index, widgets[index][1])
                        else:
                            calendar_highlight()
                    menu_highlight()
        if event.type == pygame.USEREVENT:
            calendar_scrolled += calendar_scroll
            counter+=1
            if counter==13:
                counter=1
            if counter % 4 == 0:
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
        if not run:
            break
        if keyboard_shown:
            draw_keyboard()
        elif colorpicker_show:
            draw_colorpicker()
        else:
            if menu_current==5:
                for index, widget in enumerate(widgets):
                    draw_ewidget(widgets[index][2], widgets[index][3], widgets[index][0], index, widgets[index][1],widgets[index][4],widgets[index][5])
            elif menu_current==6:
                if calendar_shown:
                    draw_calendar()
                else:
                    for index, widget in enumerate(widgets):
                        draw_awidget(widgets[index][2], widgets[index][3], widgets[index][0], index, widgets[index][1],
                                     widgets[index][4], widgets[index][5])
            draw_menu(menu_current)
    pygame.draw.rect(DISPLAY, (255, 0, 0), (1024, 0,1500,2500))
    pygame.draw.rect(DISPLAY, (255, 0, 0), (0,600,2500,1900))
            #print(db_nums)
    pygame.display.update()
    #endregion