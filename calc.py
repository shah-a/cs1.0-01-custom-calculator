# Ali Shah
# 2020-09-03
# CS1.0 Assignment 1: Custom Calculator

# This program asks user to input time and distance, then calculates approximate speed of travel
# Calculator assumes ideal physics world and constant values

# ASCII art by Daniel C. Au, taken from:
# https://asciiart.website/index.php?art=objects/balloons

art = [
"     ,;|%;Oo,",
"   ,|||%%;;OOo,",
"  ;||| CS10 OOo;",
"  ;|||%%%;;;OOo;",
"   '|||%%;;OOo'",
"    \\'||%;OO'/",
"     \\ |  | /",
"      \\|__|/",
"      |6:|6|",
"      `;;|;'",
"         |",
"        ,'",
"        ',",
"          ;   help!",
"          |o /",
"       `\\ /\\",
"         |  `",
"         '",
"\n-------------------\n"
] #ascii art, indexed line-by-line in list for easy printing

for _ in range(len(art)): #for loop to print ascii art
    print(art[_])

print(
    "Oh my! Is that a giant helium balloon?!\n"
    "Are you stuck up there??\n"
)

# Next few lines assign username, time-of-flight, and distance travelled to "name", "time", and "distance" variables respectively
# Note: time is multiplied by 60 to convert minutes to seconds (SI unit)
name = input("What's your name?: ")
time = float(input(f"How long have you been floating like that, {name}? (minutes): ")) * 60 #str input cast as float
distance = float(input("How far have you travelled since you got stuck? (meters): ")) #str input cast as float
speed = distance/time #speed calculation formula; SI unit intended (m/s)

#speed *= 3.600 #convert m/s to km/h; if used, change print statement label below
#speed *= 2.237 #convert m/s mph; if used, change print statement label below

print("\nThat means you've been travelling at " + "{:.2f}".format(speed) + "m/s!") #speed printed to 2 decimal places
print("Let's get you down :)\n")
