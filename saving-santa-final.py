import sys
import time
from tkinter import*


a = 1
b = 0.2
c = 1

player_name = input("Enter your name: ")

print(f"Hello {player_name}! Welcome to Saving Santa!")  

print()
print()
print("     ######################")
print("     |                    |")
print("     |   Saving Santa     |")
print("     |                    |")
print("     ######################")
print()
print()

print("It's the night before chrismas and all through the North Pole")
time.sleep(a)

print("the elves are hard at work, busy in Santa's workshop.")
time.sleep(a)

print("Stockings are hung by chimneys with care,")
time.sleep(a)

print("as the elves wrap the final presents and load up Santa's sleigh.\n")
time.sleep(c)

    
print("Suddenly, a loud crash echoes through the silent night!")
time.sleep(c)

print("The elves gasp as the workshop door flies open with a bang, ")
print("a blast of cold air rushing in.")
time.sleep(c)

print("Standing in the doorway is the shadowy figure of Krampus, ")
print("the evil christmas monster!")
loss_window =Tk()
loss_window.title('Krampus')
loss_canvas = Canvas(loss_window, width=450, height=450)
loss_canvas.pack()
loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//kramp.png')
loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

loss_window.mainloop()
time.sleep(c)

print("His eyes glow red as he lets out a menacing laugh. \n")
time.sleep(c)

print('"Ho ho ho!" mocks Krampus. "You didn\'t think Christmas would go on without a hitch, did you?"\n')
time.sleep(c)

print("With a snap of his sinister fingers, Krampus traps the elves in an icy cage.")
print("Santa steps forward, apalled.\n")
time.sleep(a)

print('"Krampus! What is the meaning of this?" Santa demands.\n')
time.sleep(a)


print('"Isn\'t it obvious, Santa? I\'m taking over Christmas this year!')
print('And you won\'t be able to stop me," Krampus sneers.\n')
time.sleep(a)

print("He grabs Santa in his clawed hand and throws a magical sack over his head.")
print('Santa cries out, struggling against Krampus\'s grasp.\n')
time.sleep(a)

print('"Somebody save me!" Santa calls as Krampus drags him out into the darkness.\n')
time.sleep(a)

print("The elves look around in dismay. Christmas is doomed unless someone can stop")
print("Krampus and save Santa before sunrise!\n")
time.sleep(a)

response = input(f"{player_name}, will you save Santa and stop Krampus from ruining Christmas? Y/N: ")
time.sleep(1.5)

if response.upper() == "Y":
    print(f"{player_name}, you embark on the adventure to save Santa!")
else:
    print("You decide to stay put, and Christmas is lost forever!")
    loss_window =Tk()
    loss_window.title('Game Over')
    loss_canvas = Canvas(loss_window, width=450, height=450)
    loss_canvas.pack()
    loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//sadsanta.png')
    loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

    loss_window.mainloop()
    exit()

print("\nYou set off into the darkness towards Santa's village hoping to pick up his trail.")
time.sleep(3)
print("Twinkling lights glow in the distance marking the cheerful village.")  
time.sleep(3)  
print(f"\nYou arrive to find the elves running around in a panic, {player_name}.")
time.sleep(3)  

print("Head Elf: 'Thank goodness you're here! We have to find Santa!'")
time.sleep(3)  
print("You can:")
time.sleep(2)
print("1. Check Santa's office for clues")  
print("2. Talk to Mrs. Claus")
print("3. Follow reindeer tracks to search the stables")

path = input(f"Which path do you choose {player_name}? 1, 2, or 3: ")

if path == "1":
  print("\nYou head to Santa's office...")
  print("\nNo clues but you overhear noise from the stable...")

elif path == "2":
 print("\nYou enter Santa's house to find Mrs. Claus baking gingerbread...")
 print("\nShe suggests you check the stables...")

elif path == "3":
  print("\nYou discover reindeer tracks leading towards the stables...")
  print("\nYou cautiously enter the stables...")
  
print("\nAlong the way you suddenly find yourself surrounded by three evil elves!")  
time.sleep(a)
print("They snarl and snap pointy candy canes menacingly...")
time.sleep(a) 


approach = input("Do you fight the elves or sneak past? (fight/sneak) ")



if approach == "fight":

 

    # Tkinter pop-up window

    root = Tk()
    root.minsize(height=500, width=900)

    def tab1():
        def tab2():
            label1.destroy()
            button1.destroy()
            label2 = Label(root, text='These elves seem crazed by something sour. What sweet and freshening treat might make them jolly again and turn that frown upside down?', font=('Times_New_Roman',25))
            label2.pack()

            def back():
                label2.destroy()
                button2.destroy()
                tab1()

            button2 = Button(root, text='BACK', font=('Times_New_Roman',25), command=back, activebackground='blue')
            button2.pack(side=BOTTOM)

        label1 = Label(root, text='HINT 1', font=('Times_New_Roman',25))
        label1.pack()
        button1 = Button(root, text='NEXT', font=('Times_New_Roman',25), command=tab2, activebackground='blue')
        button1.pack(side=BOTTOM)

    tab1()
    root.mainloop()

     # Fight path  
    print("Select your weapon:")
    print("1. Peppermint Gun") 
    print("2. Nutcracker Slingshot")
    print("3. Hot Chocolate Bomb")

    weapon = input("Choose 1, 2, or 3:  ")

    if weapon == "1":

        print(f"\n{player_name}, You blast the elves with peppermint and they spin around laughing!")  
        time.sleep(a) 
        print("\nThe elves are friendly now and show you to the stables.")
        time.sleep(a) 
    else:
        print("You lost! Christmas is doomed.")
        time.sleep(a) 
        loss_window =Tk()
        loss_window.title('Game Over')
        loss_canvas = Canvas(loss_window, width=450, height=450)
        loss_canvas.pack()
        loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//sadsanta.png')
        loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

        loss_window.mainloop()
        exit()

else:
    print("\nYou sneak past the elves towards the stables")
    time.sleep(a) 
path = input("Do you go to the Reindeer pen or sled garage? enter reindeer or garage. Pick 1 or 2: ")
time.sleep(a) 

if path == "reindeer":
    print("\nYou approach the reindeer pen and see hoof prints leading towards the woods...")
    time.sleep(a)

elif path == "garage":  
    print("\nYou enter the sled garage and find recent tire tracks from Santa's sled...")
    time.sleep(a)
  
print("\nAs you investigate further, you hear a loud BANG!")


time.sleep(c)  
print("\nKrampus jumps out from the shadows!")
time.sleep(a) 
root = Tk()
root.minsize(height=500, width=900)
def tab1():
        def tab2():
            label1.destroy()
            button1.destroy()
            label2 = Label(root, text='Krampus is a very powerful monster. You might not be able to fight him just yet. Will you take the chance?', font=('Times_New_Roman',25))
            label2.pack()

            def back():
                label2.destroy()
                button2.destroy()
                tab1()

            button2 = Button(root, text='BACK', font=('Times_New_Roman',25), command=back, activebackground='blue')
            button2.pack(side=BOTTOM)

        label1 = Label(root, text='HINT 2', font=('Times_New_Roman',25))
        label1.pack()
        button1 = Button(root, text='NEXT', font=('Times_New_Roman',25), command=tab2, activebackground='blue')
        button1.pack(side=BOTTOM)

tab1()
root.mainloop()

fight_flee = input("Do you fight Krampus or run away? Type 'fight' or 'flee': ")

if fight_flee == "fight":
  print("\nYou fool... you cannot defeat Krampus alone! He captures you!")
  time.sleep(a) 
  loss_window =Tk()
  loss_window.title('Game Over')
  loss_canvas = Canvas(loss_window, width=450, height=450)
  loss_canvas.pack()
  loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//sadsanta.png')
  loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

  loss_window.mainloop()
  exit()
else:
  print("\nYou narrowly escape and go to get help from Mrs. Claus!")
  time.sleep(a)
  print("\nMrs. Claus tries to hide her worry and offers you milk and cookies")
  time.sleep(a)
  print("As you explain what happened, her eyes gleam with determination...")
  time.sleep(a)
  
  help_mrs_claus = input("Will you ask Mrs. Claus to help you face Krampus? Y/N: ")

  if help_mrs_claus == "Y":
    print("\nMrs. Claus nods firmly, grabs a magic staff, and joins your quest!")

  else: 
    print("\nYou thank Mrs. Claus for the cookies but decide to save Santa alone.")
    time.sleep(a)
    print("This was a mistake! Krampus finds you and captures you!")
    time.sleep(a) 

    loss_window =Tk()
    loss_window.title('Game Over')
    loss_canvas = Canvas(loss_window, width=450, height=450)
    loss_canvas.pack()
    loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//sadsanta.png')
    loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

    loss_window.mainloop()
    time.sleep(a)

    exit()

print("\nYou and Mrs. Claus follow sleigh tracks leading into the mountains...")
time.sleep(a)

print("\nYou suddenly spot a gingerbread cottage tucked in the woods!") 
time.sleep(a) 

investigate = input("Do you want to 'approach' the cottage or 'avoid' it? Pick 1 or 2: ")
time.sleep(a) 

if investigate == "2":
  print("\nYou ignore the cottage and follow the sleigh tracks higher into the mountains")
  time.sleep(a) 
  
else:
  print("\nAs you approach, the front door creaks open by itself...")
  time.sleep(a) 
  
  enter = input("Do you want to 'go inside' the mysterious cottage or 'walk away'? Pick 1 or 2: ")
  time.sleep(a) 
  
  if enter == "2":
    print("\nYou decide not to risk going in. The mountain pass beckons...")
    time.sleep(a) 
  
  else:
    print("\nA cackle echoes as the door slams shut behind you! Uh oh...")
    time.sleep(a) 
    
next_move = input("Cast a protection spell or search for exits? Pick 1 or 2: ")

if next_move.lower() == "1":
  print("\nYou cast a shielding spell on you and Mrs. Claus.") 
  time.sleep(a) 
  print("Feeling safer, you search the creepy cottage for a way out.")
  time.sleep(a) 
else:
  print("You search the cottage walls for a hidden exit.")
  time.sleep(a) 
  
print("\nPushing aside a bookshelf, you find a trapdoor leading down...")
time.sleep(a) 

proceed = input("Open the trapdoor and climb down? Y/N >")
time.sleep(a) 

if proceed.upper() == "N":
  print("\nYou turned back and flee the cottage. But outside Krampus waits!")
  time.sleep(a) 
  print("He captures you both! Christmas cheer is lost forever.")
  time.sleep(a) 
  loss_window =Tk()
  loss_window.title('Game Over')
  loss_canvas = Canvas(loss_window, width=450, height=450)
  loss_canvas.pack()
  loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//sadsanta.png')
  loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

  loss_window.mainloop()
  time.sleep(a)

  exit()
  # Game Over
  
else:
  print("\nYou descend down the trapdoor into an icy cave...")
  time.sleep(a) 
  
  print("In the dark depths, you spot Santa tied up!")
  time.sleep(a) 
  untie = input("Quick! Will you untie Santa? Y/N: ")

  if untie.upper() == "N":
    print("\nWhile you hesitated, Krampus returned! You both are captured!") 
    time.sleep(a) 
    loss_window =Tk()
    loss_window.title('Game Over')
    loss_canvas = Canvas(loss_window, width=450, height=450)
    loss_canvas.pack()
    loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//sadsanta.png')
    loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

    loss_window.mainloop()
    time.sleep(a)

    exit()
    # Game over
  
  else: 
    print("\nYou run to untie Santa, but a loud stomp stops you...")
    time.sleep(a) 
    
    print("\nKrampus appears! 'Fools! You fell for my trap.'")
    time.sleep(a) 
    print("\nHe attacks with his sack of sorrows!")
    time.sleep(a) 
# Battle system
print("\n*** Holiday Boss Fight ***")
time.sleep(c) 

root = Tk()
root.minsize(height=500, width=900)
def tab1():
        def tab2():
            label1.destroy()
            button1.destroy()
            label2 = Label(root, text='Beware the choice that shares Krampus affinity for nuts and cracking shells', font=('Times_New_Roman',25))
            label2.pack()

            def back():
                label2.destroy()
                button2.destroy()
                tab1()

            button2 = Button(root, text='BACK', font=('Times_New_Roman',25), command=back, activebackground='blue')
            button2.pack(side=BOTTOM)

        label1 = Label(root, text='HINT 3', font=('Times_New_Roman',25))
        label1.pack()
        button1 = Button(root, text='NEXT', font=('Times_New_Roman',25), command=tab2, activebackground='blue')
        button1.pack(side=BOTTOM)

tab1()
root.mainloop()
print("Choose your weapon:")
print("1. Nutcracker sword")
print("2. Candy cane crossbow") 
print("3. Fruitcake launcher")  

weapon = input("> ")
if weapon == "2": #candy cane
  print("\nYou smashed Krampus with the right weapon!")
  time.sleep(a) 
  print("Christmas cheer overwhelms him until he flees...")
  time.sleep(a) 
  print("\nChristmas is saved! Santa thanks you and offers you a ride on his sleigh.")
  time.sleep(a) 

  win_window =Tk()
  win_window.title('Great choice!')
  win_canvas = Canvas(win_window, width=450, height=450)
  win_canvas.pack()
  win_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//candycane.png')
  win_canvas.create_image(0, 0, anchor=NW, image=win_image)

  win_window.mainloop()
elif weapon == "3":
  print("\nYou smashed Krampus with the right weapon!")
  time.sleep(a) 
  print("Christmas cheer overwhelms him until he flees...")
  time.sleep(a) 
  print("\nChristmas is saved! Santa thanks you and offers you a ride on his sleigh.")
  time.sleep(a) 
  won_window =Tk()
  won_window.title('Great choice!')
  won_canvas = Canvas(won_window, width=450, height=450)
  won_canvas.pack()
  won_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//fruitcake.png')
  won_canvas.create_image(0, 0, anchor=NW, image=won_image)

  won_window.mainloop()
else:
  print("\n You strike Krampus with the nutcracker! ")
  time.sleep(a) 
  print("\n Krampus laughs. 'You cannot stop me!'")
  time.sleep(a) 
  print("\n Krampus captures you all! Christmas is lost...")
  time.sleep(a) 
  
  loss_window =Tk()
  loss_window.title('Game Over')
  loss_canvas = Canvas(loss_window, width=450, height=450)
  loss_canvas.pack()
  loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//sadsanta.png')
  loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

  loss_window.mainloop()
  time.sleep(a)

  exit()
  # Game over
  
