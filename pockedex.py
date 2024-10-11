from tkinter import *
from PIL import Image, ImageTk

Pokemons=["Pikachu","Charizard","Bulbasaur","Squirtle","Eevee","Jigglypuff","Meowth","Mewtwo","Snorlax","Gengar"]
PokeType=["⚡Electric", "🔥Fire-🪽Flying", "🌿Grass-💀Poison","💧Water","⚪Normal","🧚Fairy-⚪Normal", "⚪Normal", "🌀Psychic", "⚪Normal", "👻Ghost-💀Poison"]
PokeInfo=[
    "INFO :\nWhen it is angered, it immediately discharges the energy stored in the pouches in its cheeks.\n\n",
    "INFO :\nIf Charizard becomes truly angered, the flame at the tip of its tail burns in a light blue shade.\n\n",
    "INFO :\nFor some time after its birth, it uses the nutrients that are packed into the seed on its back in order to grow.\n\n",
    "INFO :\nAfter birth, its back swells and hardens into a shell. It sprays a potent foam from its mouth.\n\n",
    "INFO :\nIts ability to evolve into many forms allows it to adapt smoothly and perfectly to any environment.\n\n",
    "INFO :\nWhen its huge eyes waver, it sings a mysteriously soothing melody that lulls its enemies to sleep.\n\n",
    "INFO :\nAll it does is sleep during the daytime. At night, it patrols its territory with its eyes aglow.\n\n",
    "INFO :\nIts DNA is almost the same as Mew’s. However, its size and disposition are vastly different.\n\n",
    "INFO :\nThis gluttonous Pokémon eats constantly, apart from when it’s asleep. It devours nearly 900 pounds of food per day.\n\n",
    "INFO :\nTo steal the life of its target, it slips into the prey’s shadow and silently waits for an opportunity.\n\n"]
PokeStat=[
    "STATS :\nSpeed: 6/15\nDefence: 3/15\nAttack: 4/15\nHP: 3/15",
    "STATS :\nSpeed: 6/15\nDefence: 5/15\nAttack: 5/15\nHP: 5/15",
    "STATS :\nSpeed: 3/15\nDefence: 3/15\nAttack: 3/15\nHP: 3/15",
    "STATS :\nSpeed: 3/15\nDefence: 4/15\nAttack: 3/15\nHP: 3/15",
    "STATS :\nSpeed: 4/15\nDefence: 3/15\nAttack: 4/15\nHP: 4/15",
    "STATS :\nSpeed: 2/15\nDefence: 2/15\nAttack: 3/15\nHP: 7/15",
    "STATS :\nSpeed: 6/15\nDefence: 3/15\nAttack: 3/15\nHP: 3/15",
    "STATS :\nSpeed: 8/15\nDefence: 6/15\nAttack: 7/15\nHP: 7/15",
    "STATS :\nSpeed: 2/15\nDefence: 4/15\nAttack: 7/15\nHP: 10/15",
    "STATS :\nSpeed: 7/15\nDefence: 4/15\nAttack: 4/15\nHP: 4/15"]


def showStats():
    selected_pokemon=pokeListBox.get(ACTIVE)
    match selected_pokemon:
        case "Pikachu" : modify("assets/Pikachu.png",0)
        case "Charizard" : modify("assets/Charizard.png",1)
        case "Bulbasaur" : modify("assets/Bulbasaur.png",2)
        case "Squirtle" : modify("assets/Squirtle.png",3)
        case "Eevee" : modify("assets/Eevee.png",4)
        case "Jigglypuff" : modify("assets/Jigglypuff.png",5)
        case "Meowth" : modify("assets/Meowth.png",6)
        case "Mewtwo" : modify("assets/Mewtwo.png",7)
        case "Snorlax" : modify("assets/Snorlax.png",8)
        case "Gengar" : modify("assets/Gengar.png",9)


def modify(img,indx):
    pokeName.config(text=Pokemons[indx])

    original_image = Image.open(img)
    resized_image = original_image.resize((200, 200), Image.LANCZOS)
    pokePic = ImageTk.PhotoImage(resized_image)
    
    pokeRend.config(image=pokePic)
    pokeRend.image = pokePic

    typeLabel.config(text="\nType: "+PokeType[indx]+"\n")

    description.config(text=PokeInfo[indx])

    stats.config(text=PokeStat[indx])




root = Tk()
root.geometry("800x400")
root.title("POKEDEX")
root.iconbitmap("assets/pokemon.ico")

#pokemon list============================================================
pokeList = Canvas(root, width=300, height=400, bg="#880808")
pokeList.pack(side=LEFT, expand=False)

frame = Frame(pokeList, bg="#880808")
pokeList.create_window((0, 0), window=frame, anchor="nw", width=300, height=400)

pokeListBox=Listbox(frame, width=40, height=10, font=('Helvetica', '16'))
for i in range(len(Pokemons)):
    pokeListBox.insert(i+1, Pokemons[i])
pokeListBox.pack(side=TOP, padx=20, pady=30)

showInfoButton=Button(frame, text="showinfo", font=('Helvetica', '12'), command=showStats)
showInfoButton.pack(side=BOTTOM, pady=25)

#pokemon picture + name==================================================
pokemon = Canvas(root, width=250, height=400, bg="#D2042D")
pokemon.pack(side=LEFT)

frame2 = Frame(pokemon, bg="#D2042D")
pokemon.create_window((0, 0), window=frame2, anchor="nw", width=250, height=400)

original_image = Image.open("assets/Pikachu.png")
resized_image = original_image.resize((200, 200), Image.LANCZOS)

pokePic = ImageTk.PhotoImage(resized_image)

pokeRend = Label(frame2, image=pokePic, bg="#D2042D")
pokeRend.pack(side=TOP, pady=60)

pokeName=Label(frame2, text="Pikachu", font=('Helvetica', '20'), bg="#D2042D", fg="white")
pokeName.pack(side=BOTTOM, pady=20)

#pokemon stats===========================================================
pokeStat = Canvas(root, width=250, height=400, bg="#DC143C")
pokeStat.pack(side=LEFT)

frame3 = Frame(pokeStat, bg="#DC143C")
pokeStat.create_window((0, 0), window=frame3, anchor="nw", width=250, height=400)

typeLabel = Label(frame3, text="\nType: ⚡Electric\n", bg="#DC143C", fg="white", font=('Helvetica', '14'))
typeLabel.pack()

description = Label(frame3, text="INFO :\nWhen it is angered, it immediately discharges the energy stored in the pouches in its cheeks.\n\n", wraplength=200, bg="#DC143C", fg="white", font=('Helvetica', '14'))
description.pack()

stats = Label(frame3, text="STATS :\nSpeed: 6/15\nDefence: 3/15\nAttack: 4/15\nHP: 3/15", bg="#DC143C", fg="white", font=('Helvetica', '14'))
stats.pack()



root.mainloop()