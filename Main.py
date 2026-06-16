from tkinter import *
from tkinter.ttk import *
import pandas as pd
from tkinter import messagebox
import random

def filter():

    df = pd.read_csv("pokemon.csv")

    df_filtered = df[df['#'] <= 18]

    df_filtered = df_filtered[df_filtered['Name'].apply(lambda x: len(x.split()) == 1)]

    df_filtered = df_filtered[['Name', 'Type 1', 'HP', 'Attack']]

    df_filtered.rename(columns={'Type 1': 'Element'}, inplace=True)

    df_filtered.insert(0, '', range(len(df_filtered)))

    df_filtered.to_csv("filtered_pokemon_data.csv", index=False)

    print("Filtered data exported successfully.")

class Pokemon:
    def __init__(self, name, Element, hp, attack):
        self.name = name
        self.Element = Element
        self.hp = hp
        self.attack = attack

def Pokemon_info(file_name):
    pokemon_instances = []
    with open(file_name, 'r') as file:
        next(file)
        for line in file:
            data = line.strip().split(',')
            name = data[1]
            Element = data[2]
            hp = int(data[3])
            attack = int(data[4])
            pokemon = Pokemon(name, Element, hp, attack)
            pokemon_instances.append(pokemon)
    return pokemon_instances
poke = Pokemon_info("filtered_pokemon_data.csv")
poke1 = poke[0]
poke2 = poke[6]
poke3 = poke[3]
poke4 = poke[9]
poke5 = poke[12]
poke6 = poke[15]
Epoke = Pokemon_info("filtered_pokemon_data.csv")
Epokemon_dict = {}
Epoke_indices = [1, 2, 7, 8, 4, 5, 10, 11, 13, 14, 16, 17]
for i, index in enumerate(Epoke_indices):
    key = f"Epoke{i+1}"
    Epokemon_dict[key] = Epoke[index]
Score1 = 0
Score2 = 0
evolutions = {
    "Bulbasaur": "Epoke1",
    "Ivysaur": "Epoke2",
    "Charmander": "Epoke5",
    "Charmeleon": "Epoke6",
    "Squirtle": "Epoke3",
    "Wartortle": "Epoke4",
    "Caterpie": "Epoke7",
    "Metapod": "Epoke8",
    "Weedle": "Epoke9",
    "Kakuna": "Epoke10",
    "Pidgey": "Epoke11",
    "Pidgeotto": "Epoke12"
}

def evolution_1():
    global listbox
    global window
    window = Tk()
    window.title("Pokemon")
    window.geometry("350x350")
    window.configure(bg="silver")

    label = Label(window, text="Player 1 chooses Pokemon!", font=("", 10), background="silver")
    label.grid(row=0, column=0, padx=50, columnspan=3)

    label1 = Label(window, background="silver")
    label1.grid(row=1, column=1, padx=10)

    listbox = Listbox(window, height=15, width=25)
    listbox.grid(row=1, column=0)
    for poke_instance in [poke1, poke2, poke3, poke4, poke5, poke6]:
        listbox.insert(END, poke_instance.name)

    button = Button(window, text="Choose!", command=Choice1_2)
    button.grid(row=2, column=1, sticky=N)

    window.mainloop()

def evolved1():
    global selected2
    evolutions = {
        "Bulbasaur": "Epoke1",
        "Ivysaur": "Epoke2",
        "Charmander": "Epoke5",
        "Charmeleon": "Epoke6",
        "Squirtle": "Epoke3",
        "Wartortle": "Epoke4",
        "Caterpie": "Epoke7",
        "Metapod": "Epoke8",
        "Weedle": "Epoke9",
        "Kakuna": "Epoke10",
        "Pidgey": "Epoke11",
        "Pidgeotto": "Epoke12"
    }
    evolved_key = evolutions.get(selected2.name)
    if evolved_key:
        selected2 = Epokemon_dict[evolved_key]
        print(f"{selected2.name} has evolved! New stats - HP: {int(selected2.hp * 0.7)}, Attack: {selected2.attack}")

def evolved2():
    global selected1
    evolutions = {
        "Bulbasaur": "Epoke1",
        "Ivysaur": "Epoke2",
        "Charmander": "Epoke5",
        "Charmeleon": "Epoke6",
        "Squirtle": "Epoke3",
        "Wartortle": "Epoke4",
        "Caterpie": "Epoke7",
        "Metapod": "Epoke8",
        "Weedle": "Epoke9",
        "Kakuna": "Epoke10",
        "Pidgey": "Epoke11",
        "Pidgeotto": "Epoke12"
    }
    evolved_key = evolutions.get(selected1.name)
    if evolved_key:
        selected1 = Epokemon_dict[evolved_key]
        print(f"{selected1.name} has evolved! New stats - HP: {int(selected1.hp * 0.7)}, Attack: {selected1.attack}")

def evolution_2():
    global listbox1
    global window1
    window1 = Tk()
    window1.title("Pokemon")
    window1.geometry("350x350")
    window1.configure(bg="silver")

    label = Label(window1, text="Player 2 chooses Pokemon!", font=("", 10), background="silver")
    label.grid(row=0, column=0, padx=50, columnspan=3)

    label1 = Label(window1, background="silver")
    label1.grid(row=1, column=1, padx=10)

    listbox1 = Listbox(window1, height=15, width=25)
    listbox1.grid(row=1, column=0)
    for poke_instance in [poke1, poke2, poke3, poke4, poke5, poke6]:
        listbox1.insert(END, poke_instance.name)

    button = Button(window1, text="Choose!", command=Choice2_2)
    button.grid(row=2, column=1, sticky=N)

    window1.mainloop()



def Choice1():
    global selected1
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        if index == 0:
            selected1 = poke1
        elif index == 1:
            selected1 = poke2
        elif index == 2:
            selected1 = poke3
        elif index == 3:
            selected1 = poke4
        elif index == 4:
            selected1 = poke5
        elif index == 5:
            selected1 = poke6

        print("Player1 chose:", selected1.name)
        print("HP:", selected1.hp)
        print("Attack:", selected1.attack)
        window.destroy()
        player2()

def Choice2():
    global selected2
    selected_index1 = listbox1.curselection()
    if selected_index1:
        index = selected_index1[0]
        if index == 0:
            selected2 = poke1
        elif index == 1:
            selected2 = poke2
        elif index == 2:
            selected2 = poke3
        elif index == 3:
            selected2 = poke4
        elif index == 4:
            selected2 = poke5
        elif index == 5:
            selected2 = poke6

        print("Player1 chose:", selected2.name)
        print("HP:", selected2.hp)
        print("Attack:", selected2.attack)
        window1.destroy()
        battle()

def Choice1_2():
    global selected1
    selected_index = listbox.curselection()
    if selected_index:
        index = selected_index[0]
        if index == 0:
            selected1 = poke1
        elif index == 1:
            selected1 = poke2
        elif index == 2:
            selected1 = poke3
        elif index == 3:
            selected1 = poke4
        elif index == 4:
            selected1 = poke5
        elif index == 5:
            selected1 = poke6

        print("Player1 chose:", selected1.name)
        print("HP:", selected1.hp)
        print("Attack:", selected1.attack)
        window.destroy()
        evolved1()
        battle()


def Choice2_2():
    global selected2
    selected_index1 = listbox1.curselection()
    if selected_index1:
        index = selected_index1[0]
        if index == 0:
            selected2 = poke1
        elif index == 1:
            selected2 = poke2
        elif index == 2:
            selected2 = poke3
        elif index == 3:
            selected2 = poke4
        elif index == 4:
            selected2 = poke5
        elif index == 5:
            selected2 = poke6

        print("Player1 chose:", selected2.name)
        print("HP:", selected2.hp)
        print("Attack:", selected2.attack)
        window1.destroy()
        evolved2()
        battle()


def player1():
    global listbox
    global window
    window = Tk()
    window.title("Pokemon")
    window.geometry("350x350")
    window.configure(bg="silver")

    label = Label(window, text="Player 1 chooses Pokemon!", font=("", 10), background="silver")
    label.grid(row=0, column=0, padx=50, columnspan=3)

    label1 = Label(window, background="silver")
    label1.grid(row=1, column=1, padx=10)

    listbox = Listbox(window, height=15, width=25)
    listbox.grid(row=1, column=0)
    for poke_instance in [poke1, poke2, poke3, poke4, poke5, poke6]:
        listbox.insert(END, poke_instance.name)

    button = Button(window, text="Choose!", command=Choice1)
    button.grid(row=2, column=1, sticky=N)

    window.mainloop()


def player2():
    global listbox1
    global window1
    window1 = Tk()
    window1.title("Pokemon")
    window1.geometry("350x350")
    window1.configure(bg="silver")

    label = Label(window1, text="Player 2 chooses Pokemon!", font=("", 10), background="silver")
    label.grid(row=0, column=0, padx=50, columnspan=3)

    label1 = Label(window1, background="silver")
    label1.grid(row=1, column=1, padx=10)

    listbox1 = Listbox(window1, height=15, width=25)
    listbox1.grid(row=1, column=0)
    for poke_instance in [poke1, poke2, poke3, poke4, poke5, poke6]:
        listbox1.insert(END, poke_instance.name)

    button = Button(window1, text="Choose!", command=Choice2)
    button.grid(row=2, column=1, sticky=N)

    window1.mainloop()

def battle():
    player1_turn = True
    player1_health = (selected1.hp * 5)
    player2_health = (selected2.hp * 5)
    Pattack1 = (selected1.attack)
    Eattack1= (selected1.attack)
    Pattack2 = (selected2.attack)
    Eattack2= (selected2.attack)
    Pdamage1 = random.randint(int((0.75 * Pattack1)), Pattack1)
    Pdamage2 = random.randint(int((0.75 * Pattack2)), Pattack2)
    elemental_strength = {
        'Water': 'Fire',
        'Fire': 'Grass',
        'Grass': 'Water',
        'Bug': 'Normal',
        'Normal': 'Bug'
    }

    def is_elementally_stronger(attacker, defender):
        return elemental_strength.get(attacker.Element) == defender.Element

    def physical_attack():
        nonlocal player2_health, player1_turn
        if player1_turn:
            player2_health -= Pattack1
            update_health_bars()
            player1_turn = False
            toggle_buttons()

    def elemental_attack():
        nonlocal player2_health, player1_turn
        if player1_turn:
            damage = random.randint(int(0.5 * Eattack1), Eattack1)
            if is_elementally_stronger(selected1, selected2) and random.random() < 0.8:
                damage *= 2
                messagebox.showinfo("Critical!", "Critical damage")
            player2_health -= damage
            update_health_bars()
            player1_turn = False
            toggle_buttons()

    def physical_attack_player2():
        nonlocal player1_health, player1_turn
        if not player1_turn:
            player1_health -= Pattack2
            update_health_bars()
            player1_turn = True
            toggle_buttons()

    def elemental_attack_player2():
        nonlocal player1_health, player1_turn
        if not player1_turn:
            damage = random.randint(int(0.5 * Eattack2), Eattack2)
            if is_elementally_stronger(selected2, selected1) and random.random() < 0.8:
                damage *= 2
                messagebox.showinfo("Critical!", "Critical damage")
            player1_health -= damage
            update_health_bars()
            player1_turn = True
            toggle_buttons()

    def update_health_bars():
        bar["value"] = player1_health
        bar1["value"] = player2_health
        health_label.config(text=f"Health: {player1_health}")
        health_label2.config(text=f"Health: {player2_health}")
        global Score1, Score2
        if player1_health <= 0:
            messagebox.showinfo("Game Over", "Player1 has lost!, now player1 chooses a new pokemon while player2 evolves.")
            window2.destroy()
            Score2 += 1
            if Score2 == 3:
                messagebox.showinfo("Game Over", "Player2 won")
            else:
                evolution_1()


        if player2_health <= 0:
            messagebox.showinfo("Game Over", "Player2 has lost!, now player2 chooses a new pokemon while player1 evolves.")
            window2.destroy()
            Score1 += 1
            if Score1 == 3:
                messagebox.showinfo("Game Over", "Player1 won")
            else:
                evolution_2()
        if player1_turn:
            damage_dealt = Pattack1
        else:
            damage_dealt = Pattack2
        if damage_dealt :
            messagebox.showinfo("Attack Result", f"Damage dealt: {damage_dealt}")


    def toggle_buttons():
        if player1_turn:
            button.config(state=NORMAL)
            button1.config(state=NORMAL)
            button2.config(state=DISABLED)
            button3.config(state=DISABLED)
        else:
            button.config(state=DISABLED)
            button1.config(state=DISABLED)
            button2.config(state=NORMAL)
            button3.config(state=NORMAL)

    window2 = Tk()
    window2.title("Pokemon")
    window2.geometry("500x250")
    window2.configure(bg="silver")

    label = Label(window2, text=f"Player1: {selected1.name}", background="silver", font=("", 10))
    label.grid(row=0, column=0)

    label1 = Label(window2, text=f"Score1: {int(Score1)}", background="silver", font=("", 10))
    label1.grid(row=1, column=0)

    label2 = Label(window2, text=f"Player2: {selected2.name}", background="silver", font=("", 10))
    label2.grid(row=0, column=2, )

    label3 = Label(window2, text=f"Score2: {int(Score2)}", background="silver", font=("", 10))
    label3.grid(row=1, column=2,)

    bar = Progressbar(window2, orient=HORIZONTAL, length=170, maximum=player1_health, value=player1_health)
    bar.grid(row=2, column=0, columnspan=2, sticky=W, padx=20)

    bar1 = Progressbar(window2, orient=HORIZONTAL, length=170, maximum=player2_health, value=player2_health)
    bar1.grid(row=2, column=2, columnspan=2, sticky=E, padx=20)

    health_label = Label(window2, text=f"Health: {player1_health}", background="silver", font=("", 10))
    health_label.grid(row=3, column=0, sticky=W)

    health_label2 = Label(window2, text=f"Health: {player2_health}", background="silver", font=("", 10))
    health_label2.grid(row=3, column=2, sticky=E)

    button = Button(window2, text="physical attack", command=physical_attack)
    button.grid(row=4, column=0)

    button1 = Button(window2, text="elemental attack", command=elemental_attack)
    button1.grid(row=4, column=1, sticky=W)

    button2 = Button(window2, text="physical attack", command=physical_attack_player2)
    button2.grid(row=4, column=2)

    button3 = Button(window2, text="elemental attack", command=elemental_attack_player2)
    button3.grid(row=4, column=3)

    toggle_buttons()
    window2.mainloop()

player1()
