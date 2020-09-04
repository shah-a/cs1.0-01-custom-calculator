# Ali Shah
# 2020-09-03
# CS1.0 Assignment 1: Custom Calculator

#This program asks user to input time and distance, then calculates speed of travel
#Calculator assumes constant values and an ideal physics world

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
]

for _ in range(len(art)):
    print(art[_])

print(
    "Oh my! Is that a giant helium balloon?!\n"
    "Are you stuck up there??\n"
)

name = input("What's your name?: ")
time = float(input(f"How long have you been floating like that, {name}? (minutes): ")) * 60
distance = float(input("How far have you travelled since you got stuck? (meters): "))
speed = distance/time

print("\nThat means you've been travelling at " + "{:.2f}".format(speed) + "m/s!")
print("Let's get you down :)\n")