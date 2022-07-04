print("hellgames1 Bitmap Tool")
try:
    from PIL import Image
except ModuleNotFoundError:
    print("ERROR: Python Image Library (PIL) required!")
else:
    print("File must be in PNG format with Indexed 2 color mode (can be set in Photoshop in Image -> Mode)")
    print("Enter name of file (without png extension): ",end="")
    name = input()
    try:
        im = Image.open(name+'.png') # Can be many different formats.
        pix = im.load()
    except:
        print("ERROR: Couldn't load file!")
    else:
        stri = f"img_a_{name} = [({im.size[0]},{im.size[1]}),"
        last = 1
        counter = 0
        for y in range(im.size[1]):
            for x in range(im.size[0]):
                current = pix[x,y]
                if last != current:
                    stri += str(counter)+","
                    counter = 1
                else:
                    counter+=1
                last = current
        stri += str(counter)+"]"
        print("")
        print(stri)
        print("")
        try:
            import subprocess
            from platform import system
            if system() == "Windows":
                subprocess.check_call('echo ' + stri + '|clip', shell=True)
                print("Copied to clipboard!")
            else:
                raise Exception("")
        except:
            print("Couldn't copy to clipboard!") # Get the RGBA Value of the a pixel of an image


#######DECODING FUNCTION AND EXAMPLE CODE FOR PYGAME########
"""
import pygame
DISPLAY = pygame.display.set_mode((500, 500))

img_a_gear = [(64,64),27,10,53,12,51,13,51,14,50,4,6,4,50,3,7,4,38,2,10,3,7,4,9,3,24,6,7,4,8,3,8,6,21,8,4,6,8,6,3,9,19,19,8,19,17,5,2,12,10,12,2,5,15,5,4,9,14,8,5,5,13,5,7,4,20,4,7,4,13,4,44,4,12,4,44,4,12,5,42,4,14,4,42,4,15,4,40,4,16,5,16,6,16,5,17,4,13,12,13,4,18,4,11,16,11,4,18,4,10,18,10,4,17,4,10,6,8,6,10,3,17,4,9,5,12,5,9,4,16,4,8,5,14,5,8,4,11,8,9,4,16,4,9,9,3,10,8,4,18,4,8,10,1,10,9,4,18,4,9,16,13,3,20,3,13,10,14,4,20,4,14,8,14,4,20,4,14,8,14,4,20,4,14,8,14,4,20,4,14,8,14,4,20,4,14,8,14,4,20,4,14,9,14,3,19,4,13,16,9,4,18,4,9,10,1,10,8,4,17,5,8,10,3,9,9,4,16,4,9,8,10,5,8,5,14,4,9,4,16,4,9,5,11,6,9,4,16,4,10,6,7,7,9,4,18,4,10,18,10,4,18,4,11,15,11,4,19,4,13,12,13,4,17,5,16,5,17,5,16,4,40,4,15,4,42,4,14,4,42,4,13,4,44,4,12,4,33,1,10,4,13,4,7,4,19,5,7,4,14,5,5,8,14,8,5,5,15,5,2,12,10,12,2,5,17,19,8,7,1,11,19,9,4,5,8,5,4,9,21,6,8,3,8,3,8,6,24,3,9,3,8,3,9,3,38,4,6,4,50,4,6,4,50,14,50,13,52,12,53,10,27]

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
    
image_example = generate_image_from_array(img_a_gear)

while True:
    DISPLAY.fill((255,255,255))
    DISPLAY.blit(image_example, (100, 100))
    pygame.display.update()

"""