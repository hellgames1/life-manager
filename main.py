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
        "reminderfor": "Reminder for",
        "refresh": "refresh",
        "no": "no",
        "yes": "yes",
        "editing": "editing",
        "stoppedauto": "Stopped auto-load feature!",
        "couldntstopauto": "Couldn't stop auto-load!",
        "startedauto": "Turned auto-load feature on!@Database: ",
        "couldntstartauto": "Couldn't turn on auto-load!",
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
        "reminderfor": "Бележка за",
        "refresh": "опресни",
        "no": "не",
        "yes": "да",
        "editing": "редакт.",
        "stoppedauto": "Спрях автоматичното зареждане!",
        "couldntstopauto": "Не успях да спра@автоматичното зареждане!",
        "startedauto": "Включих автоматичното зареждане!@База данни: ",
        "couldntstartauto": "Не успях да включа@автоматичното зареждане!",
        "otherlang": "EN"
    }
}
lan = "en"
############IMPORT AND MAIN SETTINGS####################
#region
print("Importing libraries...")
from sys import exit as terminate_program
try:
    import pygame
except:
    print("!!!!!!!!!!!!!!!\nYou need pygame module! This application is tested under pygame 2.0.1 (SDL 2.0.14, Python 3.9.2)\n!!!!!!!!!!!!!!!")
    terminate_program()
import json
import datetime
import os
import hashlib
pygame.init()
pygame.display.set_caption('Life Manager by hellgames1')
DISPLAY = pygame.Surface((1024,600))
DISPLAYFINAL = pygame.display.set_mode((1024,600),pygame.RESIZABLE,32)
WHITE = (255,255,255)
pygame.time.set_timer(pygame.USEREVENT, 100)
db={}
current_wkday = datetime.datetime.today().weekday()
current_month = datetime.datetime.today().month
current_date = datetime.datetime.today().day
current_year = datetime.datetime.today().year
antialiasing = False
hasset = False
fs_scaletype = 3
temp_rem = ""
line_one = []
line_two = []
#endregion

def check_md5(file_name):
    original_md5 = '3dea6da513097358f7fbb4408aacb736'
    with open(file_name, 'rb') as file_to_check:
        data = file_to_check.read()
        md5_returned = hashlib.md5(data).hexdigest()
    return original_md5 == md5_returned

def smart_display_update(checkSize=False):
    global fs_scaletype
    DISPLAYFINAL.fill((0,0,0))
    if pygame.display.get_surface().get_size() == (1024,600) or fs_scaletype == 0:
        DISPLAYFINAL.blit(DISPLAY,(0,0))
    elif fs_scaletype == 1:
        DISPLAYFINAL.blit(pygame.transform.scale(DISPLAY,pygame.display.get_surface().get_size()),(0,0))
    elif fs_scaletype == 2:
        DISPLAYFINAL.blit(pygame.transform.smoothscale(DISPLAY,pygame.display.get_surface().get_size()),(0,0))
    elif fs_scaletype == 3:
        if checkSize:
            settings(True)
        else:
            DISPLAYFINAL.blit(pygame.transform.scale(DISPLAY,pygame.display.get_surface().get_size()),(0,0))
    pygame.display.update()

def smart_get_pos():
    global fs_scaletype
    xscale, yscale = pygame.display.get_surface().get_size()
    x, y = pygame.mouse.get_pos()
    if (xscale == 1024 and yscale == 600) or fs_scaletype == 0:
        return(x,y)
    else:
        xscale/=1024
        yscale/=600
        x /= xscale
        y /= yscale
        return (int(x),int(y))

###########IMAGE ENGINE INITIALIZE#####################
#region
print("Initializing image engine...")
img_a_gear = [(64,64),27,10,53,12,51,13,51,14,50,4,6,4,50,3,7,4,38,2,10,3,7,4,9,3,24,6,7,4,8,3,8,6,21,8,4,6,8,6,3,9,19,19,8,19,17,5,2,12,10,12,2,5,15,5,4,9,14,8,5,5,13,5,7,4,20,4,7,4,13,4,44,4,12,4,44,4,12,5,42,4,14,4,42,4,15,4,40,4,16,5,16,6,16,5,17,4,13,12,13,4,18,4,11,16,11,4,18,4,10,18,10,4,17,4,10,6,8,6,10,3,17,4,9,5,12,5,9,4,16,4,8,5,14,5,8,4,11,8,9,4,16,4,9,9,3,10,8,4,18,4,8,10,1,10,9,4,18,4,9,16,13,3,20,3,13,10,14,4,20,4,14,8,14,4,20,4,14,8,14,4,20,4,14,8,14,4,20,4,14,8,14,4,20,4,14,8,14,4,20,4,14,9,14,3,19,4,13,16,9,4,18,4,9,10,1,10,8,4,17,5,8,10,3,9,9,4,16,4,9,8,10,5,8,5,14,4,9,4,16,4,9,5,11,6,9,4,16,4,10,6,7,7,9,4,18,4,10,18,10,4,18,4,11,15,11,4,19,4,13,12,13,4,17,5,16,5,17,5,16,4,40,4,15,4,42,4,14,4,42,4,13,4,44,4,12,4,33,1,10,4,13,4,7,4,19,5,7,4,14,5,5,8,14,8,5,5,15,5,2,12,10,12,2,5,17,19,8,7,1,11,19,9,4,5,8,5,4,9,21,6,8,3,8,3,8,6,24,3,9,3,8,3,9,3,38,4,6,4,50,4,6,4,50,14,50,13,52,12,53,10,27]
img_a_businessman = [(232,224),157,14,215,21,208,26,204,30,200,34,197,36,194,40,191,42,189,44,187,46,185,48,183,50,182,51,180,52,179,54,178,55,176,56,176,57,174,58,174,59,172,60,172,60,172,61,170,62,170,62,170,62,170,62,170,63,168,64,144,2,22,64,144,4,20,64,145,5,18,64,145,7,16,64,145,9,14,64,146,9,13,64,117,4,25,10,13,63,113,11,23,10,12,63,108,18,21,11,11,62,107,23,19,11,10,62,108,24,18,11,9,62,108,26,17,11,9,61,109,28,16,10,8,60,111,29,15,11,6,60,111,32,14,10,6,59,112,33,13,10,5,58,114,35,12,9,4,58,114,37,11,9,4,56,116,39,10,8,4,55,117,40,9,8,3,54,122,38,9,7,3,52,127,37,7,7,3,51,131,35,7,6,2,50,136,34,5,7,1,48,141,32,4,7,1,46,146,31,3,6,1,44,151,29,3,5,1,42,156,27,2,5,1,40,162,30,2,37,167,27,2,34,173,24,3,31,173,26,4,27,169,34,4,22,167,42,4,16,167,46,9,4,170,51,178,55,175,58,171,63,167,66,164,69,161,72,158,74,157,76,154,79,151,81,150,83,147,86,145,87,144,89,141,91,140,92,139,94,137,95,136,97,134,98,133,100,131,102,129,104,127,106,43,7,75,108,40,12,71,41,1,68,37,15,69,39,4,70,34,17,68,37,6,72,30,20,66,37,6,75,27,22,64,36,8,78,21,26,62,35,10,83,12,30,62,34,10,126,61,34,11,127,60,32,13,127,59,32,13,128,59,31,14,128,58,31,15,128,57,31,15,129,33,2,22,30,16,129,32,4,21,29,17,128,32,6,19,29,17,129,31,8,18,28,18,128,31,10,16,28,19,128,30,12,15,28,19,127,29,15,14,27,19,127,29,16,13,27,20,126,29,18,12,27,20,125,29,20,9,28,20,61,3,60,30,22,6,30,20,61,4,57,31,24,4,30,21,61,7,53,31,26,2,31,20,62,9,49,32,33,2,24,21,61,12,44,34,32,4,24,21,61,15,39,35,32,5,24,20,62,18,33,37,34,5,22,21,61,24,24,40,36,4,22,21,61,31,10,46,38,4,20,21,62,86,40,3,20,21,61,86,42,3,18,22,61,85,44,3,16,22,62,83,46,5,12,24,61,83,48,6,8,26,61,82,50,7,4,27,62,81,52,7,4,26,61,81,54,6,4,26,61,80,56,5,4,26,61,79,58,3,4,26,61,79,60,1,4,27,61,78,65,28,61,77,65,28,62,77,65,28,61,79,65,27,61,80,65,25,62,81,65,24,61,83,64,24,61,84,64,22,62,85,64,21,61,87,64,20,61,88,64,18,62,89,64,17,61,91,64,16,61,92,64,15,61,93,64,14,60,95,64,12,61,95,64,12,61,96,62,13,60,98,60,15,59,99,58,16,59,100,56,16,59,102,54,17,59,103,52,18,59,104,49,19,60,105,47,20,59,107,45,21,59,108,43,21,60,109,41,22,59,111,39,22,60,112,37,23,59,114,35,24,59,114,34,24,60,115,32,25,59,117,30,26,59,118,28,26,61,118,26,27,62,118,24,27,63,119,22,28,64,119,20,29,65,119,17,30,66,120,15,31,67,120,13,32,68,120,11,32,69,121,9,33,31,2,37,121,7,33,32,4,36,121,5,34,31,6,36,121,3,35,31,7,35,121,2,35,31,8,36,157,31,9,36,156,31,10,35,155,31,11,36,154,31,12,36,140,44,13,35,119,64,15,35,110,72,15,36,107,73,17,35,106,74,18,35,103,76,18,36,101,76,20,36,99,77,21,35,99,77,21,36,97,77,23,35,97,77,24,35,95,77,25,35,95,77,26,35,94,77,27,34,94,76,29,33,94,76,29,33,93,77,30,32,94,75,32,31,94,75,32,31,94,74,34,30,94,74,34,30,94,73,35,30,95,72,34,31,95,71,35,30,97,69,36,30,98,67,37,30,99,64,38,30,101,61,40,30,102,57,43,30,104,35,1,1,60,31,106,14,81,30,202,30,202,30,201,31,201,30,202,30,202,30,201,30,202,30,72]
img_a_exerciseman = [(247,235),53,4,240,9,237,11,235,13,233,14,233,15,231,16,231,17,230,17,231,16,231,17,231,16,231,17,215,3,12,17,211,11,9,17,208,15,7,17,206,18,7,16,205,20,6,17,204,21,5,17,203,23,1,21,185,5,12,45,183,9,9,47,180,12,8,47,179,14,7,30,1,16,179,14,7,27,4,17,177,15,7,27,5,16,177,16,7,27,4,16,177,16,7,27,4,16,47,8,122,17,6,28,4,15,42,18,117,17,6,28,4,15,39,23,116,17,4,29,5,14,37,28,113,17,2,32,4,13,36,31,113,50,5,11,36,34,111,51,5,8,36,37,111,50,7,3,38,40,109,21,1,29,46,42,108,19,4,28,45,44,108,17,5,29,43,46,107,17,6,28,42,48,107,16,6,29,40,49,107,17,6,28,40,50,107,16,6,29,38,52,106,17,6,28,37,53,106,17,6,29,36,54,106,17,6,28,35,55,106,17,6,29,34,56,106,16,7,28,33,57,106,16,7,29,32,58,106,15,8,28,32,58,106,15,8,29,30,59,106,14,10,28,30,60,106,12,11,29,29,60,107,10,13,28,29,60,108,7,15,29,27,61,110,2,19,28,27,61,131,29,26,61,132,28,26,62,131,29,25,62,132,28,25,62,133,28,24,62,133,28,24,61,135,28,23,61,135,28,23,61,136,28,23,60,136,28,23,60,137,28,22,60,137,28,22,59,139,28,22,58,140,27,22,58,140,28,21,57,142,27,22,56,36,8,42,8,48,28,21,55,35,11,40,11,47,27,22,54,35,12,38,13,46,28,21,53,35,14,36,14,47,27,22,52,34,15,36,15,47,27,22,50,35,16,35,15,47,27,22,49,36,16,10,10,15,15,48,27,22,48,36,16,7,16,12,15,48,28,22,46,37,16,7,18,10,15,49,27,23,44,38,16,6,21,8,15,49,28,23,42,39,16,6,22,7,15,50,27,24,40,40,16,5,23,7,15,51,27,24,37,42,16,5,24,6,15,51,27,26,34,43,16,5,24,6,15,52,27,26,31,45,16,5,24,6,15,52,28,27,28,46,66,53,27,29,23,49,66,53,28,31,18,51,66,54,27,36,8,56,66,55,27,99,66,55,28,98,66,56,28,97,16,5,25,5,15,56,28,97,16,5,25,5,15,57,28,96,16,5,25,5,15,58,28,95,16,5,25,5,15,58,30,93,16,5,25,5,15,59,31,91,16,5,25,5,15,59,43,47,13,19,16,5,25,5,15,60,45,40,22,14,16,4,26,5,15,61,46,35,28,11,16,4,26,5,15,61,49,30,33,8,15,5,26,5,15,62,50,25,37,8,14,5,26,5,14,64,51,21,41,6,14,5,26,6,13,64,54,15,45,6,12,6,26,6,12,66,57,8,49,6,9,8,25,9,9,67,115,22,25,86,115,21,25,87,115,20,25,87,116,19,25,88,116,18,25,89,116,17,25,89,117,16,25,90,117,15,25,91,117,14,25,91,118,13,25,92,118,12,25,93,118,11,25,93,119,10,25,94,119,9,25,95,119,8,25,96,119,7,25,96,120,6,25,97,120,5,25,98,120,3,26,99,120,3,25,100,120,2,25,101,146,102,145,103,144,105,142,105,141,106,141,106,79,1,61,106,79,2,60,106,79,3,59,106,79,4,58,106,79,5,57,106,79,6,56,106,79,7,55,106,79,7,55,106,79,8,54,106,79,9,52,107,79,10,51,107,79,11,50,107,79,13,48,107,79,14,47,107,79,15,46,107,79,16,44,108,79,17,43,108,79,18,42,108,79,19,40,109,79,20,39,109,79,21,38,109,79,23,35,110,79,24,34,110,79,25,32,111,79,27,30,111,79,28,28,112,79,30,25,113,79,32,22,114,79,35,18,115,79,38,13,117,79,43,6,119,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,168,79,84]
img_a_numswap = [(65,67),22,1,63,3,62,3,61,4,61,3,62,3,3,10,49,21,27,3,13,24,22,6,13,7,10,9,20,2,1,3,13,5,16,7,21,3,14,8,15,6,19,3,15,9,15,5,18,3,17,8,15,5,17,3,5,5,11,4,17,4,16,3,4,7,32,4,15,3,4,1,4,3,32,4,14,3,9,3,33,4,13,3,9,3,34,3,10,9,6,3,4,6,24,4,9,9,5,3,4,8,24,3,22,3,5,1,4,3,24,4,20,3,11,3,25,3,19,3,11,4,25,3,18,3,9,5,27,4,17,9,3,7,26,3,17,9,7,4,25,3,34,3,25,3,34,3,25,3,28,1,4,4,25,3,28,8,26,3,15,1,13,6,27,3,14,3,45,3,14,3,44,3,14,3,27,3,15,3,14,3,26,5,14,3,14,3,26,2,1,2,15,2,14,3,26,2,1,3,29,3,26,3,1,3,29,3,26,2,3,2,30,3,25,2,3,3,29,3,24,3,3,3,29,3,24,9,3,7,19,3,24,10,2,9,17,4,22,3,5,3,2,3,3,3,18,3,22,2,6,3,2,3,3,3,18,4,20,3,7,3,1,3,3,3,19,3,34,7,21,4,33,9,20,4,32,3,3,4,20,3,32,3,4,3,20,4,31,3,4,3,21,4,30,3,3,4,4,5,13,4,29,9,3,8,13,4,28,8,3,4,4,1,14,5,12,4,21,3,21,5,10,10,15,3,23,6,8,11,14,3,25,6,11,6,14,3,26,7,9,6,14,3,28,8,4,8,14,3,30,18,14,4,31,11,2,3,15,4,4,1,30,3,5,2,17,8,37,3,18,6,38,3,62,3,62,3,25]

def generate_image_from_array(img) -> pygame.Surface:
    temp = pygame.Surface((img[0][0], img[0][1]), pygame.SRCALPHA)
    x, y = 0, 0
    colors = [(0, 0, 0, 255), (0, 0, 0, 0)]
    color = 0
    for swap in range(1, len(img)):
        color = 1 - color
        for i in range(img[swap]):
            temp.set_at((x, y), colors[color])
            x += 1
            if x == img[0][0]:
                x = 0
                y += 1
    return temp

img_gear = generate_image_from_array(img_a_gear)
img_businessman = generate_image_from_array(img_a_businessman)
img_exerciseman = generate_image_from_array(img_a_exerciseman)
img_numswap = generate_image_from_array(img_a_numswap)
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
    max_width=612
    index=0
    for message in messages:
        name_surfaces.append(my_font_m.render(message, antialiasing, (0, 0, 0)))
        total_height += name_surfaces[index].get_size()[1]+10
        if (name_surfaces[index].get_size()[0]+20)>max_width:
            max_width=name_surfaces[index].get_size()[0]+20
        heights.append(total_height)
        index+=1
    for index, surface in enumerate(name_surfaces):
        DISPLAY.blit(surface,(512 - (name_surfaces[index].get_size()[0] / 2), 200 - total_height/2 + heights[index]))
    pygame.draw.rect(DISPLAY, (0, 0, 0), (512-max_width/2,100,max_width,400), 5)

    if message_ok_hl:
        pygame.draw.rect(DISPLAY,(127,127,127),(406,400,212,75))

    pygame.draw.rect(DISPLAY, (0, 0, 0), (406,400,212,75), 5)
    name_surface = my_font_m.render("OK", antialiasing, (0, 0, 0))
    DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 437-name_surface.get_size()[1]/2))
    if not run:
        name_surface=my_font_xs.render(os.getcwd(),True,(0,0,0))
        DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 520))


def message_highlight():
    global message_ok_hl
    if pygame.Rect(406,400,212,75).collidepoint(smart_get_pos()):
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

############SETTINGS LOAD#################################
#region
run=True
def draw_flag(x,y,country):
    if country=="gb":
        red = (200,16,46)
        blue = (1,33,105)
        pygame.draw.polygon(DISPLAY,red,[(x,y), (x+79,y+53), (x+60,y+53),(x,y+12)])
        pygame.draw.polygon(DISPLAY,blue,[(x+30,y), (x+93,y+43), (x+93,y)])
        pygame.draw.polygon(DISPLAY,blue,[(x,y+19), (x,y+53), (x+50,y+53)])

        pygame.draw.rect(DISPLAY,red,(x+104,y,31,159))
        pygame.draw.rect(DISPLAY,red,(x,y+64,239,31))

        pygame.draw.polygon(DISPLAY,red,[(x+220,y), (x+146,y+50),(x+146,y+53),(x+159,y+53),(x+239,y)])
        pygame.draw.polygon(DISPLAY,blue,[(x+146,y), (x+146,y+43), (x+210,y)])
        pygame.draw.polygon(DISPLAY,blue,[(x+239,y+19), (x+189,y+53), (x+239,y+53)])

        pygame.draw.polygon(DISPLAY,red,[(x+80,y+106), (x+93,y+106), (x+93,y+109),(x+19,y+159),(x,y+159)])
        pygame.draw.polygon(DISPLAY,blue,[(x,y+106), (x+50,y+106), (x,y+140)])
        pygame.draw.polygon(DISPLAY,blue,[(x+30,y+159), (x+93,y+159), (x+93,y+116)])

        pygame.draw.polygon(DISPLAY,red,[(x+160,y+106), (x+179,y+106), (x+239,y+147),(x+239,y+159)])
        pygame.draw.polygon(DISPLAY,blue,[(x+189,y+106), (x+239,y+106), (x+239,y+140)])
        pygame.draw.polygon(DISPLAY,blue,[(x+146,y+116), (x+146,y+159), (x+210,y+159)])
    elif country=="bg":
        white = (255,255,255)
        green = (0,150,110)
        red = (214,38,18)
        pygame.draw.rect(DISPLAY,white,(x,y,239,53))
        pygame.draw.rect(DISPLAY,green,(x,y+53,239,53))
        pygame.draw.rect(DISPLAY,red,(x,y+106,239,53))
    pygame.draw.rect(DISPLAY,(0,0,0),(x,y,240,160),5)

antialiasfont = pygame.font.SysFont("Calibri", 32)
genericfont = pygame.font.SysFont("Calibri", 48)
def draw_bigtext(x,y,text,aa):
    drawsurf = antialiasfont.render(text, aa, (0, 0, 0))
    drawsurf = pygame.transform.scale(drawsurf,(80,160))
    DISPLAY.blit(drawsurf,(x+80,y))
    pygame.draw.rect(DISPLAY,(0,0,0),(x,y,240,160),5)
def settings(onlyscaling=False):
    global hasset
    global lan
    global antialiasing
    global fs_scaletype
    if not onlyscaling:
        hasset = False
        while not hasset:
            for eventh in pygame.event.get():
                if eventh.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(200, 220, 240, 160).collidepoint(smart_get_pos()):
                        lan = "en"
                        hasset = True
                    elif pygame.Rect(600, 220, 240, 160).collidepoint(smart_get_pos()):
                        lan = "bg"
                        hasset = True
            DISPLAY.fill(WHITE)
            draw_flag(200, 220, "gb")
            draw_flag(600, 220, "bg")
            DISPLAY.blit(genericfont.render("Language / език", False, (0, 0, 0)), (360, 90))
            smart_display_update()
        hasset = False
        while not hasset:
            for eventh in pygame.event.get():
                if eventh.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(200, 220, 240, 160).collidepoint(smart_get_pos()):
                        antialiasing = False
                        hasset = True
                    elif pygame.Rect(600, 220, 240, 160).collidepoint(smart_get_pos()):
                        antialiasing = True
                        hasset = True
            DISPLAY.fill(WHITE)
            draw_bigtext(200, 220, "a", False)
            draw_bigtext(600, 220, "a", True)
            if lan == "bg":
                DISPLAY.blit(genericfont.render("Искате ли изглаждане на текста?", False, (0, 0, 0)), (180, 90))
                DISPLAY.blit(genericfont.render("Не се препоръчва за", False, (208, 0, 0)), (500, 400))
                DISPLAY.blit(genericfont.render("бавни устройства!", False, (208, 0, 0)), (520, 450))
            else:
                DISPLAY.blit(genericfont.render("Do you want anti-aliased text?", False, (0, 0, 0)), (230, 90))
                DISPLAY.blit(genericfont.render("Not recommended", False, (208, 0, 0)), (540, 400))
                DISPLAY.blit(genericfont.render("for slow devices!", False, (208, 0, 0)), (550, 450))
            smart_display_update()
    if pygame.display.get_surface().get_size() != (1024,600):
        hasset = False
        grey = 128
        while not hasset:
            for eventh in pygame.event.get():
                if eventh.type == pygame.MOUSEBUTTONDOWN:
                    if pygame.Rect(100, 220, 240, 160).collidepoint(smart_get_pos()):
                        fs_scaletype = 0
                    elif pygame.Rect(400, 220, 240, 160).collidepoint(smart_get_pos()):
                        fs_scaletype = 1
                    elif pygame.Rect(700, 220, 240, 160).collidepoint(smart_get_pos()):
                        fs_scaletype = 2
                    elif pygame.Rect(400,450,220,80).collidepoint(smart_get_pos()) and 0 <= fs_scaletype <= 2:
                        hasset = True
            DISPLAY.fill(WHITE)
            if 0 <= fs_scaletype <= 2:
                grey = 0
            else:
                grey = 128
            colors = [0,0,0,0]
            colors[fs_scaletype] = 255
            pygame.draw.rect(DISPLAY,(colors[0],0,0),(100,220,240,160),5)
            pygame.draw.rect(DISPLAY,(colors[1],0,0),(400,220,240,160),5)
            pygame.draw.rect(DISPLAY,(colors[2],0,0),(700,220,240,160),5)
            if lan == "bg":
                DISPLAY.blit(genericfont.render(f"Вашата резолюция ({pygame.display.get_surface().get_size()[0]}x{pygame.display.get_surface().get_size()[1]})", False, (0, 0, 0)), (220, 40))
                DISPLAY.blit(genericfont.render("не съответства на програмата (1024x600)", False, (0, 0, 0)), (140, 80))
                DISPLAY.blit(genericfont.render("Изберете оразмеряване", False, (0, 0, 0)), (320, 140))
                DISPLAY.blit(genericfont.render("никакво", False, (0, 0, 0)), (130,270))
                DISPLAY.blit(genericfont.render("цял екран", False, (0, 0, 0)), (425,270))
                DISPLAY.blit(genericfont.render("цял екран с", False, (0, 0, 0)), (704,260))
                DISPLAY.blit(genericfont.render("изглаждане", False, (0, 0, 0)), (700,295))
                DISPLAY.blit(genericfont.render("Не се препоръчва", False, (208, 0, 0)), (640, 400))
                DISPLAY.blit(genericfont.render("за бавни устройства!", False, (208, 0, 0)), (620, 450))
            else:
                DISPLAY.blit(genericfont.render(f"Your device resolution ({pygame.display.get_surface().get_size()[0]}x{pygame.display.get_surface().get_size()[1]})", False, (0, 0, 0)), (220, 40))
                DISPLAY.blit(genericfont.render("Doesn't match native resolution (1024x600)", False, (0, 0, 0)), (140, 80))
                DISPLAY.blit(genericfont.render("Choose scaling type", False, (0, 0, 0)), (320, 140))
                DISPLAY.blit(genericfont.render("no scaling", False, (0, 0, 0)), (120,270))
                DISPLAY.blit(genericfont.render("fullscreen", False, (0, 0, 0)), (425,270))
                DISPLAY.blit(genericfont.render("fullscreen", False, (0, 0, 0)), (725,260))
                DISPLAY.blit(genericfont.render("smooth", False, (0, 0, 0)), (740,295))
                DISPLAY.blit(genericfont.render("Not recommended", False, (208, 0, 0)), (640, 400))
                DISPLAY.blit(genericfont.render("for slow devices!", False, (208, 0, 0)), (650, 450))
            pygame.draw.rect(DISPLAY,(grey,grey,grey),(400,450,220,80),5)
            DISPLAY.blit(genericfont.render("OK", False, (grey,grey,grey)), (480,470))
            smart_display_update()
    else:
        fs_scaletype = 3
    try:
        fw = open("settings.cfg", "w")
        towrite="error"
        if lan == "en":
            towrite = "1"
        else:
            towrite = "2"
        if antialiasing:
            towrite += "2"
        else:
            towrite += "1"
        towrite += str(fs_scaletype)
        print("saving settings file...")
        fw.write(towrite)
        fw.close()
    except:
        print("ERROR SAVING SETTINGS FILE!")


try:
    print("opening settings file...")
    f = open("settings.cfg", "r")
    f_contents = f.read()
    f.close()
except:
    print("no settings file")
    settings()
else:
    if len(f_contents) == 3:
        if f_contents[:2]=="11":
            lan = "en"
            antialiasing = False
        elif f_contents[:2]=="12":
            lan = "en"
            antialiasing = True
        elif f_contents[:2]=="21":
            lan = "bg"
            antialiasing = False
        elif f_contents[:2]=="22":
            lan = "bg"
            antialiasing = True
        else:
            print("settings file corrupt")
            settings()
    else:
        print("settings file corrupt")
        settings()
    print(f_contents)
    if f_contents[2]=="0":
        fs_scaletype = 0
    elif f_contents[2]=="1":
        fs_scaletype = 1
    elif f_contents[2]=="2":
        fs_scaletype = 2
    elif f_contents[2]=="3":
        fs_scaletype = 3
    else:
        print("settings file corrupt")
        settings()

def download_font():
    global run
    global my_font
    global my_font_m
    global my_font_s
    global my_font_xs
    try:
        URL = "https://github.com/hellgames1/life-manager/raw/main/calibri.ttf"
        response = requests.get(URL,timeout=3)
        response.raise_for_status()
    except requests.exceptions.HTTPError:
        run=False
        text = {"en": "HTTP Error!@Please download \"calibri.ttf\"@manually and place it@in the directory below!",
                "bg": "HTTP Грешка!@Моля изтеглете \"calibri.ttf\"@ръчно и го поставете@в директорията отдолу!"}
        display_message(text[lan])
    except requests.exceptions.ConnectionError:
        run=False
        text = {"en": "Connection error!@Please download \"calibri.ttf\"@manually and place it@in the directory below!",
                "bg": "Грешка с връзката!@Моля изтеглете \"calibri.ttf\"@ръчно и го поставете@в директорията отдолу!"}
        display_message(text[lan])
    except requests.exceptions.Timeout:
        run=False
        text = {"en": "Error - timeout!@Please download \"calibri.ttf\"@manually and place it@in the directory below!",
                "bg": "Грешка - таймаут!@Моля изтеглете \"calibri.ttf\"@ръчно и го поставете@в директорията отдолу!"}
        display_message(text[lan])
    except requests.exceptions.RequestException:
        run=False
        text = {"en": "Weird error!@Please download \"calibri.ttf\"@manually and place it@in the directory below!",
                "bg": "Странна грешка!@Моля изтеглете \"calibri.ttf\"@ръчно и го поставете@в директорията отдолу!"}
        display_message(text[lan])
    else:
        try:
            open("calibri.ttf", "wb").write(response.content)
        except:
            run=False
            text = {"en": "Error saving file!@Please download \"calibri.ttf\"@manually and place it@in the directory below!",
                    "bg": "Грешка при записване на файла!@Моля изтеглете \"calibri.ttf\"@ръчно и го поставете@в директорията отдолу!"}
            display_message(text[lan])
        else:
            if os.path.exists("calibri.ttf") and check_md5("calibri.ttf")==True:
                my_font = pygame.font.Font("calibri.ttf", 72)
                my_font_m = pygame.font.Font("calibri.ttf", 48)
                my_font_s = pygame.font.Font("calibri.ttf", 36)
                my_font_xs = pygame.font.Font("calibri.ttf", 24)
                display_message({"en":"Success!","bg":"Успешно!"}[lan])
            else:
                os.remove("calibri.ttf")
                run=False
                text = {"en": "Error saving file!@Please download \"calibri.ttf\"@manually and place it@in the directory below!",
                        "bg": "Грешка при записване на файла!@Моля изтеглете \"calibri.ttf\"@ръчно и го поставете@в директорията отдолу!"}
                display_message(text[lan])

def open_browser():
    try:
        import webbrowser
        webbrowser.open('https://github.com/hellgames1/life-manager/blob/main/calibri.ttf', new=2)
    except:
        pass
#endregion

############KEYBOARD INITIALIZE#########################
#region
print("Initializing keyboard...")
specificmessage = ["found","открит"]
couldntdelete = False
if os.path.exists("calibri.ttf"):
    if check_md5("calibri.ttf") == False:
        try:
            os.remove("calibri.ttf")
        except:
            couldntdelete = True
        specificmessage = ["correct","правилния"]
try:
    if couldntdelete:
        raise FileNotFoundError()
    my_font = pygame.font.Font("calibri.ttf", 72)
    my_font_m = pygame.font.Font("calibri.ttf", 48)
    my_font_s = pygame.font.Font("calibri.ttf", 36)
    my_font_xs = pygame.font.Font("calibri.ttf", 24)
except FileNotFoundError:
    my_font = pygame.font.SysFont("Calibri", 72)
    my_font_m = pygame.font.SysFont("Calibri", 48)
    my_font_s = pygame.font.SysFont("Calibri", 36)
    my_font_xs = pygame.font.SysFont("Calibri", 24)
    try:
        if couldntdelete:
            raise ModuleNotFoundError()
        else:
            import requests
    except ModuleNotFoundError:
        run=False
        text = {"en": "\"calibri.ttf\" font file not "+specificmessage[0]+"!@Please download \"calibri.ttf\"@and place it in the@directory below!",
                "bg": "\"calibri.ttf\" файлът за шрифта@не е "+specificmessage[1]+"! Моля изтеглете@го и го поставете в@директорията отдолу!"}
        display_message(text[lan],"open_browser()")
    else:
        text = {"en": "\"calibri.ttf\" font file not "+specificmessage[0]+"!@Attempting to download from@hellgames1 github...",
                "bg": "\"calibri.ttf\" файлът за шрифта@не е "+specificmessage[1]+"!@Ще се опитам да го изтегля от@hellgames1 github..."}
        display_message(text[lan],"download_font()")
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
    global temp_rem
    global db_dbname
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
    if which==8:
        if temp_rem == "stopauto" and os.path.exists("autoload.cfg"):
            try:
                os.remove("autoload.cfg")
                display_message(tx[lan]["stoppedauto"])
            except:
                display_message(tx[lan]["couldntstopauto"])
        elif temp_rem == "setauto":
            try:
                fw_autoload = open("autoload.cfg", "w")
                fw_autoload.write(db_dbname)
                fw_autoload.close()
                display_message(tx[lan]["startedauto"]+db_dbname)
            except:
                display_message(tx[lan]["couldntstartauto"])
        else:
            newdb = db.copy()
            newdb["days"][currentday]["reminders"] = temp_rem
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
            if pygame.Rect(key[0], key[1], key[2], key[3]).collidepoint(smart_get_pos()):
                key[5] = True
                last_key = index
                break
        for index,key in enumerate(special_keys):
            if pygame.Rect(key[0], key[1], key[2], key[3]).collidepoint(smart_get_pos()):
                key[5] = True
                last_key = 100+index
                break
    else:
        for index,key in enumerate(digit_keys):
            if pygame.Rect(key[0], key[1], key[2], key[3]).collidepoint(smart_get_pos()):
                key[5] = True
                last_key = index
                break
        for index,key in enumerate(digit_special_keys):
            if pygame.Rect(key[0], key[1], key[2], key[3]).collidepoint(smart_get_pos()):
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
                tempsurface = my_font_s.render(letters[key[4]], antialiasing, (0,0,0))
                DISPLAY.blit(tempsurface,(key[0]+10,key[1]+50-tempsurface.get_size()[1]/2))
            else:
                DISPLAY.blit(my_font.render(letters[key[4]], antialiasing, (0,0,0)),(key[0]+20,key[1]+20))
        for key in special_keys:
            if key[4] == "֍" and not keyboard_switchable:
                continue
            if not (not keyboard_multilingual and len(key)==7):
                if key[5]:
                    pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
                pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)
            if len(key)==7:
                if keyboard_multilingual:
                    tempsurface = my_font_s.render(key[4], antialiasing, (0,0,0))
                    DISPLAY.blit(tempsurface,(key[0]+10,key[1]+(key[3]/2)-tempsurface.get_size()[1]/2))
            else:
                if key[4]=="֍":
                    DISPLAY.blit(img_numswap,(key[0]+20,key[1]+20))
                elif key[4]=="bksp":
                    pygame.draw.line(DISPLAY,(0,0,0),(1000,450),(930,450),3)
                    pygame.draw.polygon(DISPLAY,(0,0,0),((930,434),(930,466),(900,450)))
                else:
                    DISPLAY.blit(my_font.render(key[4], antialiasing, (0,0,0)),(key[0]+20,key[1]+20))
                if key[4]=="shift":
                    pygame.draw.line(DISPLAY,(0,0,0),(22,406),(6,420),3)
                    pygame.draw.line(DISPLAY,(0,0,0),(22,406),(36,420),3)
                    pygame.draw.line(DISPLAY,(0,0,0),(30,420),(36,420),3)
                    pygame.draw.line(DISPLAY,(0,0,0),(13,420),(6,420),3)
                    pygame.draw.line(DISPLAY,(0,0,0),(13,420),(13,435),3)
                    pygame.draw.line(DISPLAY,(0,0,0),(30,420),(30,435),3)
                    pygame.draw.line(DISPLAY,(0,0,0),(13,435),(30,435),3)

    else:
        for key in digit_keys:
            if key[5]:
                pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
            pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)
            DISPLAY.blit(my_font.render(str(key[4]), antialiasing, (0,0,0)),(key[0]+20,key[1]+20))
        for key in digit_special_keys:
            if key[4] == "֍" and not keyboard_switchable:
                continue
            if key[4] == "." and (not keyboard_fraction or "." in tf) and not keyboard_switchable:
                continue
            if key[5]:
                pygame.draw.rect(DISPLAY,(127,127,127),(key[0],key[1],key[2],key[3]))
            pygame.draw.rect(DISPLAY,(0,0,0),(key[0],key[1],key[2],key[3]),5)

            if key[4] != "֍":
                DISPLAY.blit(my_font.render(key[4], antialiasing, (0,0,0)),(key[0]+20,key[1]+20))
            else:
                DISPLAY.blit(img_numswap,(key[0]+20,key[1]+20))
    pygame.draw.rect(DISPLAY, (0, 0, 0), (50,80,900,100), 5)
    textfield_surface = my_font.render(tf, antialiasing, (0, 0, 0))
    DISPLAY.blit(textfield_surface,  (500-(textfield_surface.get_size()[0] / 2),100))
    DISPLAY.blit(my_font.render(blinker, antialiasing, (0, 0, 0)),  (485+(textfield_surface.get_size()[0] / 2),100))
    name_surface = my_font.render(keyboard_entry, antialiasing, (0, 0, 0))
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


    name_surface = my_font.render(tx[lan]["choosecolor"], antialiasing, (0, 0, 0))
    DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 20))

    name_surface = my_font_m.render(colorpicker_displaytext, antialiasing, colorpicker_currentcol)
    DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 170))

    pygame.draw.rect(DISPLAY, (0, 0, 0), (406,500,212,75), 5)
    name_surface = my_font_m.render("OK", antialiasing, (0, 0, 0))
    DISPLAY.blit(name_surface, (512 - (name_surface.get_size()[0] / 2), 537-name_surface.get_size()[1]/2))
def colorpicker_highlight():
    global colorpicker_ok_hl
    global colorpicker_currentcol
    if pygame.Rect(406,500,212,75).collidepoint(smart_get_pos()):
        colorpicker_ok_hl = True
    else:
        for color in colors_pick:
            if pygame.Rect(color[1]).collidepoint(smart_get_pos()):
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
    day = {"wkd": -1, "dt": -1, "mn": -1, "yr": -1, "wksince": -1, "reminders": "", "ints": [], "bools": []}
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
    menus[0].append(["button",920,20,80,72,False,"","medium",False])
    menus[0].append(["image",16,376,-1,-1,False,img_businessman])
    menus[0].append(["image",765,365,-1,-1,False,img_exerciseman])
    menus[0].append(["image",928,24,-1,-1,False,img_gear])

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
                name_surface = my_font.render(item[6], antialiasing, color )
            elif item[7] == "medium":
                name_surface = my_font_m.render(item[6], antialiasing, color )
            elif item[7] == "small":
                name_surface = my_font_s.render(item[6], antialiasing, color )
            elif item[7] == "tiny":
                name_surface = my_font_xs.render(item[6], antialiasing, color )
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
                name_surface = my_font.render(label, antialiasing, (0, 0, 0))
            elif item[7] == "medium":
                name_surface = my_font_m.render(label, antialiasing, (0, 0, 0))
            elif item[7] == "small":
                name_surface = my_font_s.render(label, antialiasing, (0, 0, 0))
            elif item[7] == "tiny":
                name_surface = my_font_xs.render(label, antialiasing, (0, 0, 0))
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
        elif item[0]=="image":
            DISPLAY.blit(item[6],(item[1],item[2]))
def menu_highlight():
    global last_button
    global menu_current
    global calendar_shown
    global calendar_scroll
    for index,button in enumerate(menus[menu_current]):
        if button[0] == "button_context" and globals()[button[9]] == (not button[10]):
            continue
        if button[5] == True:
            iscolliding = pygame.Rect(512-(button[3]/2), button[2], button[3], button[4]).collidepoint(smart_get_pos())
        else:
            iscolliding = pygame.Rect(button[1], button[2], button[3], button[4]).collidepoint(smart_get_pos())
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
            settings()
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
#region
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
editingtimer=0
def load_widgets():
    global db
    global widgets
    global widget_alignments
    global currentday
    global widget_tempsizes
    global boolstart
    global temp_rem
    global line_one
    global line_two
    widget_alignments = db["datealignment"]
    widgets=[["__clock",0,db["positionstyles"][0][0],db["positionstyles"][0][1],(0,0,0),-1]]
    widgets.append(["__date",0,db["positionstyles"][1][0],db["positionstyles"][1][1],(0,0,0),-1])
    widgets.append(["__rem",-12,db["positionstyles"][2][0],db["positionstyles"][2][1],(0,0,0),-1])
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
    temp_rem = db["days"][currentday]["reminders"]
    line_one = []
    line_two = []
    rem_split = temp_rem.split()
    do_one = True
    ind = -1
    while True:
        try:
            ind += 1
            if do_one:
                line_one.append(rem_split[ind])
                if my_font_s.render(" ".join(line_one), False, (0, 0, 0)).get_size()[0] > 360:
                    line_one.pop(len(line_one) - 1)
                    ind -= 1
                    do_one = False
            else:
                line_two.append(rem_split[ind])
                if my_font_s.render(" ".join(line_two), False, (0, 0, 0)).get_size()[0] > 360:
                    line_two.pop(len(line_two) - 1)
                    break
        except IndexError:
            break
    line_one = " ".join(line_one)
    line_two = " ".join(line_two)
    print(widgets)

def draw_awidget(placing_x,placing_y,text,index,style,color,value=-1):
    global widget_selected
    global widget_selected_actual
    global widget_datesize
    global widget_tempsizes
    global istoday
    global editingtimer
    global line_one
    global line_two
    value=str(value)
    if text=="__clock":
        if istoday:
            name_surface = my_font_m.render(datetime.datetime.now().strftime("%H:%M:%S"), antialiasing, (0, 0, 0))
        else:
            name_surface = my_font_m.render("e-00:"+str(round(editingtimer)), antialiasing, (128, 128, 128))
    elif text=="__date":
        if db["days"][currentday]["dt"] == datetime.datetime.today().day and db["days"][currentday]["mn"] == datetime.datetime.today().month and db["days"][currentday]["yr"] == datetime.datetime.today().year:
            name_surface = my_font_m.render(str(current_date) + " " + tx[lan]["months"][current_month-1] + " " + str(current_year), antialiasing, (0, 0, 0))
            istoday=True
        else:
            name_surface = my_font_m.render(str(db["days"][currentday]["dt"]) + " " + tx[lan]["months"][db["days"][currentday]["mn"]-1] + " " + str(db["days"][currentday]["yr"]), antialiasing, (128, 128, 128))
            istoday=False
        widget_datesize = name_surface.get_size()[0]
    elif text == "__rem":
        name_surface = my_font_xs.render(tx[lan]["reminders"], antialiasing, (0, 0, 0))


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
        name_surface = my_font_s.render(line_one, antialiasing, (0, 0, 0))
        DISPLAY.blit(name_surface, (placing_x-name_surface.get_size()[0]/2, placing_y+30))
        name_surface = my_font_s.render(line_two, antialiasing, (0, 0, 0))
        DISPLAY.blit(name_surface, (placing_x-name_surface.get_size()[0]/2, placing_y+60))
        pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - 178, placing_y+2, 360, 116), 5)
    else:
        name_surfacea = my_font_s.render(text, antialiasing, color)
        widget_tempsizes[index][0]=name_surfacea.get_size()[0]
        DISPLAY.blit(name_surfacea, (placing_x - widget_tempsizes[index][0] / 2, placing_y))
        name_surface = my_font_s.render(value, antialiasing, (0, 0, 0))
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
            DISPLAY.blit(my_font_m.render("-", antialiasing, (0, 0, 0)), (placing_x - widget_tempsizes[index][1] / 2 - 50, placing_y + 40))
            if widget_selected_actual==index and widget_selected_type=="int+":
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 40, 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 40, 40), 5)
            DISPLAY.blit(my_font_m.render("+", antialiasing, (0, 0, 0)), (placing_x + widget_tempsizes[index][1] / 2 + 30, placing_y + 40))
        elif style==3:
            if widget_selected_actual==index and widget_selected_type=="int--":
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x - widget_tempsizes[index][1] / 2 - 70, placing_y + 40, 50, 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - widget_tempsizes[index][1] / 2 - 70, placing_y + 40, 50, 40), 5)
            DISPLAY.blit(my_font_s.render("--", antialiasing, (0, 0, 0)), (placing_x - widget_tempsizes[index][1] / 2 - 60, placing_y + 44))
            if widget_selected_actual==index and widget_selected_type=="int++":
                pygame.draw.rect(DISPLAY, (127,127,127), (placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 50, 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 50, 40), 5)
            DISPLAY.blit(my_font_s.render("++", antialiasing, (0, 0, 0)), (placing_x + widget_tempsizes[index][1] / 2 + 28, placing_y + 44))
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
                name_surface = my_font_m.render("√", antialiasing, (0, 0, 0))
                DISPLAY.blit(name_surface, (placing_x - 12, placing_y + 40))
        elif style == 5:
            if value=="True":
                name_surface = my_font_m.render("√", antialiasing, (0, 0, 0))
                DISPLAY.blit(name_surface, (placing_x + name_surfacea.get_size()[0] / 2 + 16, placing_y - 5))
        elif style == 6:
            if value=="True":
                name_surface = my_font_m.render("√", antialiasing, (0, 0, 0))
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
            if pygame.Rect(placing_x - widget_tempsizes[index][1]/2 - 20, placing_y+40, widget_tempsizes[index][1]+40, 40).collidepoint(smart_get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int"
                print("change int number "+str(index-3))
        elif style==1:
            if pygame.Rect(placing_x + widget_tempsizes[index][0] / 2 + 8 , placing_y-5, widget_tempsizes[index][1]+40, 40).collidepoint(smart_get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int"
                print("change int number "+str(index-3))
        elif style==2:
            if pygame.Rect(placing_x - widget_tempsizes[index][1] / 2 - 60, placing_y + 40, 40, 40).collidepoint(smart_get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int-"
                print("minus int number "+str(index-3))
            if pygame.Rect(placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 40, 40).collidepoint(smart_get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int+"
                print("plus int number "+str(index-3))
        elif style==3:
            if pygame.Rect(placing_x - widget_tempsizes[index][1] / 2 - 70, placing_y + 40, 50, 40).collidepoint(smart_get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int--"
                print("minus minus int number "+str(index-3))
            if pygame.Rect(placing_x + widget_tempsizes[index][1] / 2 + 20, placing_y + 40, 50, 40).collidepoint(smart_get_pos()):
                widget_selected=index-3
                widget_selected_actual=index
                widget_selected_type="int++"
                print("plus plus int number "+str(index-3))
        elif style==4:
            if pygame.Rect(placing_x - 20, placing_y+40, 40, 40).collidepoint(smart_get_pos()):
                widget_selected=index-boolstart
                widget_selected_actual=index
                widget_selected_type="bool"
                print("bool int number "+str(index-boolstart))
        elif style==5:
            if pygame.Rect(placing_x + widget_tempsizes[index][0] / 2 + 8 , placing_y-5, 40, 40).collidepoint(smart_get_pos()):
                widget_selected=index-boolstart
                widget_selected_actual=index
                widget_selected_type="bool"
                print("bool int number "+str(index-boolstart))
        elif style==6:
            if pygame.Rect(placing_x - widget_tempsizes[index][0] / 2 - 48 , placing_y-5, 40, 40).collidepoint(smart_get_pos()):
                widget_selected=index-boolstart
                widget_selected_actual=index
                widget_selected_type="bool"
                print("bool int number "+str(index-boolstart))
        elif style==-12:
            if pygame.Rect(placing_x - 178, placing_y + 2, 360, 116).collidepoint(smart_get_pos()):
                print("pressed on reminders")
                widget_selected = 999
                widget_selected_type="rem"

def press_awidget():
    global widget_selected
    global widget_selected_actual
    global widget_selected_type
    global currentday
    global temp_rem
    global istoday
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
        elif widget_selected_type=="rem":
            if istoday:
                display_keyboard(tx[lan]["reminderfor"]+" " + str(current_date) + " " + tx[lan]["months"][current_month-1], "temp_rem", digital=False, switchable=True, begin_with_upper=False,fraction=True, okfunc="okfuncs(8)", default_text=temp_rem, multilingual=True)
            else:
                display_keyboard(tx[lan]["reminderfor"]+" " + str(db["days"][currentday]["dt"]) + " " + tx[lan]["months"][db["days"][currentday]["mn"]-1], "temp_rem", digital=False, switchable=True, begin_with_upper=False,fraction=True, okfunc="okfuncs(8)", default_text=temp_rem, multilingual=True)

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
            if index==1 and pygame.Rect(widget[2]-20,widget[3]+40,40,40).collidepoint(smart_get_pos()):
                if widget_alignments=="left":
                    widget_alignments="center"
                elif widget_alignments=="center":
                    widget_alignments="right"
                elif widget_alignments=="right":
                    widget_alignments="left"

            if pygame.Rect(widget[2]-20,widget[3],40,40).collidepoint(smart_get_pos()):
                widget_selection_offset = [smart_get_pos()[0]-widget[2],smart_get_pos()[1]-widget[3]]
                widget_selected=index

            if index!=0 and index!=1 and pygame.Rect(widget[2] -20, widget[3]-40, 40, 40).collidepoint(smart_get_pos()):
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
        name_surface = my_font_m.render(datetime.datetime.now().strftime("%H:%M:%S"), antialiasing, (0, 0, 0))
    elif text=="__date":
        name_surface = my_font_m.render(str(current_date) + " " + tx[lan]["months"][counter-1] + " " + str(current_year), antialiasing, (0, 0, 0))
        widget_datesize = name_surface.get_size()[0]
        if widgets_visualize:
            DISPLAY.blit(my_font_s.render("↔", antialiasing, (230, 230, 230)), (placing_x -20, placing_y +42))
            pygame.draw.rect(DISPLAY, (230, 230, 230), (placing_x -20, placing_y+40, 40, 40), 5)
    elif text == "__rem":
        name_surface = my_font_xs.render(tx[lan]["reminders"], antialiasing, (0, 0, 0))
    else:
        if widgets_visualize:
            DISPLAY.blit(my_font_s.render("S", antialiasing, (230, 230, 230)), (placing_x -8, placing_y -36))
            pygame.draw.rect(DISPLAY, (230, 230, 230), (placing_x -20, placing_y-40, 40, 40), 5)


    if widgets_visualize:
        if widget_selected==index:
            pygame.draw.rect(DISPLAY, (230, 230, 230), (placing_x - 20, placing_y, 40, 40))
            DISPLAY.blit(my_font_s.render("≡", antialiasing, (255, 255, 255)), (placing_x - 8, placing_y+2))
        else:
            DISPLAY.blit(my_font_s.render("≡", antialiasing, (230, 230, 230)), (placing_x - 8, placing_y + 2))
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
        name_surfacea = my_font_s.render(text, antialiasing, color)
        DISPLAY.blit(name_surfacea, (placing_x - name_surfacea.get_size()[0] / 2, placing_y))
        name_surface = my_font_s.render(defvalue, antialiasing, (0, 0, 0))
        #if name_surface.get_size()[0] < 34:
        #    tempsize = 34
        #else:
        tempsize = name_surface.get_size()[0]
        if style == 4:
            name_surface = my_font_m.render("√", antialiasing, (0, 0, 0))
            DISPLAY.blit(name_surface, (placing_x - 12, placing_y + 40))
        elif style == 5:
            name_surface = my_font_m.render("√", antialiasing, (0, 0, 0))
            DISPLAY.blit(name_surface, (placing_x + name_surfacea.get_size()[0] / 2 + 16, placing_y - 5))
        elif style == 6:
            name_surface = my_font_m.render("√", antialiasing, (0, 0, 0))
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
            DISPLAY.blit(my_font_m.render("-", antialiasing, (0, 0, 0)), (placing_x - tempsize / 2 - 50, placing_y + 40))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x + tempsize / 2 + 20, placing_y + 40, 40, 40), 5)
            DISPLAY.blit(my_font_m.render("+", antialiasing, (0, 0, 0)), (placing_x + tempsize / 2 + 30, placing_y + 40))
        elif style==3:
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x - tempsize / 2 - 70, placing_y + 40, 50, 40), 5)
            DISPLAY.blit(my_font_s.render("--", antialiasing, (0, 0, 0)), (placing_x - tempsize / 2 - 60, placing_y + 44))
            pygame.draw.rect(DISPLAY, (0, 0, 0), (placing_x + tempsize / 2 + 20, placing_y + 40, 50, 40), 5)
            DISPLAY.blit(my_font_s.render("++", antialiasing, (0, 0, 0)), (placing_x + tempsize / 2 + 28, placing_y + 44))
        elif style==4:
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x - 20, placing_y+40, 40, 40),5)
        elif style==5:
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x + name_surfacea.get_size()[0] / 2 + 8 , placing_y-5, 40, 40),5)
        elif style==6:
            pygame.draw.rect(DISPLAY, (0,0,0), (placing_x - name_surfacea.get_size()[0] / 2 - 48 , placing_y-5, 40, 40),5)
#endregion
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
    global editingtimer
    for index,key in enumerate(calendar):
        ypos = calendar_scrolled + key[1]
        if 520 >= ypos >=0 and 80 < smart_get_pos()[1] < 520:
            if pygame.Rect(key[0], ypos , key[2], key[3]).collidepoint(smart_get_pos()) and currentday!=index:
                currentday=index
                if db["days"][currentday]["dt"] == datetime.datetime.today().day and db["days"][currentday]["mn"] == datetime.datetime.today().month and db["days"][currentday]["yr"] == datetime.datetime.today().year:
                    editingtimer=0
                else:
                    editingtimer=60
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
            DISPLAY.blit(my_font_s.render(str(key[4]), antialiasing, (0, 0, 0)), (key[0] + 10, ypos + 10))
    pygame.draw.rect(DISPLAY, (200, 0, 0), (calendar_redbit[0],calendar_redbit[1], 80,80), 5)
    pygame.draw.rect(DISPLAY, (255, 255, 255), (0,0,563,80))
    pygame.draw.rect(DISPLAY, (255, 255, 255), (0,520,563,80))
    DISPLAY.blit(my_font_s.render(tx[lan]["months"][calendar_scrolledmonth-1], antialiasing, (0, 0, 0)), (420, 20))
    dayshowing = my_font_m.render(str(db["days"][currentday]["dt"]) + " " + tx[lan]["months"][db["days"][currentday]["mn"]-1] + " " + str(db["days"][currentday]["yr"]), antialiasing, (0, 0, 0))
    DISPLAY.blit(dayshowing,(792-dayshowing.get_size()[0]/2,0))
    y=60
    if line_one != "":
        displaying=my_font_s.render(tx[lan]["reminders"], antialiasing, (0,0,0))
        DISPLAY.blit(displaying,(670,y))
        y+=30
        displaying=my_font_s.render(line_one, antialiasing, (0,0,0))
        DISPLAY.blit(displaying,(670,y))
        y+=30
    if line_two != "":
        displaying=my_font_s.render(line_two, antialiasing, (0,0,0))
        DISPLAY.blit(displaying,(670,120))
        y+=30
    for index,item in enumerate(db["intnames"]):
        displaying=my_font_s.render(item + " = " + str(db["days"][currentday]["ints"][index]), antialiasing, (db["intcols"][index][0],db["intcols"][index][1],db["intcols"][index][2]))
        DISPLAY.blit(displaying,(670,y))
        y+=30
    for index,item in enumerate(db["boolnames"]):
        if db["days"][currentday]["bools"][index] == True:
            displaying=my_font_s.render(item + " = "+tx[lan]["yes"], antialiasing, (db["boolcols"][index][0],db["boolcols"][index][1],db["boolcols"][index][2]))
        else:
            displaying=my_font_s.render(item + " = "+tx[lan]["no"], antialiasing, (db["boolcols"][index][0],db["boolcols"][index][1],db["boolcols"][index][2]))
        DISPLAY.blit(displaying,(670,y))
        y+=30
#endregion

counter = 1
if os.path.exists("autoload.cfg"):
    try:
        print("found autoload file, reading...")
        f_autoload = open("autoload.cfg", "r")
        f_autoload_contents = f_autoload.read()
        f_autoload.close()
        if ".json" in f_autoload_contents and os.path.exists(f_autoload_contents):
            print("loading autoload database...")
            loaddb(f_autoload_contents,True)
    except:
        pass
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
            widgets[widget_selected][2]=round((smart_get_pos()[0]-widget_selection_offset[0])/10)*10
            widgets[widget_selected][3]=round((smart_get_pos()[1]-widget_selection_offset[1])/10)*10
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
            if editingtimer>0:
                editingtimer-=0.1
            elif editingtimer<0:
                editingtimer=0
            elif editingtimer==0 and not istoday:
                loaddb(db_dbname,True)
                draw_calendar()
                draw_awidget(-1,-1,"__date",-1,-1,-1)
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
            #print(db_nums)
    smart_display_update(True)
    #endregion