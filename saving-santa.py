import sys
import time
from tkinter import*

a = 1
b = 0.2
c = 1

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
time.sleep(2)

print("the elves are hard at work, busy in Santa's workshop.")
time.sleep(2)

print("Stockings are hung by chimneys with care,")
time.sleep(2)

print("as the elves wrap the final presents and load up Santa's sleigh.\n")
time.sleep(3)

print("Suddenly, a loud crash echoes through the silent night!")
time.sleep(3)

print("The elves gasp as the workshop door flies open with a bang, ")
print("a blast of cold air rushing in.")
time.sleep(3)

print("Standing in the doorway is the shadowy figure of Krampus, ")
print("the evil christmas monster!")
loss_window =Tk()
loss_window.title('Krampus')
loss_canvas = Canvas(loss_window, width=450, height=450)
loss_canvas.pack()
loss_image = PhotoImage(file='//Users//alaysiahhernton//Desktop//kramp.png')
loss_canvas.create_image(0, 0, anchor=NW, image=loss_image)

loss_window.mainloop()
time.sleep(3)

print("His eyes glow red as he lets out a menacing laugh. \n")
time.sleep(3)

print('"Ho ho ho!" mocks Krampus. "You didn\'t think Christmas would go on without a hitch, did you?"\n')
time.sleep(3)

print("With a snap of his sinister fingers, Krampus traps the elves in an icy cage.")
print("Santa steps forward, apalled.\n")
time.sleep(4)

print('"Krampus! What is the meaning of this?" Santa demands.\n')
time.sleep(2)

print('"Isn\'t it obvious, Santa? I\'m, taking over Christmas this year!')
print('And you won\'t be able to stop me," Krampus sneers.\n')
time.sleep(3)

print("He grabs Santa in his clawed hand and throws a magical sack over his head")
print('Santa cries out, struggling against Krampus\'s grasp.\n')
time.sleep(4)

print('"Somebody save me!" Santa calls as Krampus drags him out into the darkness.\n')
time.sleep(2)

print("The elves look around in dismay. Christmas is doomed unless someone can stop")
print("Krampus and save Santa before sunrise!\n")
time.sleep(3)

response = input("Will you save Santa and stop Krampus from ruining Christmas? (Y/N)")

if response.upper() == "Y":
    print("You embark on the adventure to save Santa!")
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
print("You arrive to find the elves running around in a panic!\n")
time.sleep(3)  

print("Head Elf: 'Thank goodness you're here! We have to find Santa!'")
time.sleep(3)  
print("You can:")
time.sleep(2)

print("1. Check Santa's office for clues")  
print("2. Talk to Mrs. Claus")
print("3. Follow reindeer tracks to search the stables")

path = input("Which path do you choose? 1, 2, or 3: ")

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
time.sleep(3)
print("They snarl and snap pointy candy canes menacingly...")
time.sleep(3) 


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

        print("\nYou blast the elves with peppermint and they spin around laughing!")  
        print("\nThe elves are friendly now and show you to the stables.")
    else:
        print("You lost! Christmas is doomed.")
