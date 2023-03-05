from tkinter import *
import tkinter.messagebox

import random
 
# Initalisation des variables pour sauvgrader le score 
player_points = 0
pc_points = 0

window = Tk()
window.geometry("450x250")
window.resizable(width=False, height=False)
window.title("NSI - Ghassen D. -- Pierre/Feuille/Ciseau !")

frame = Frame(window, width=450, height=210)
frame.pack()

img_pierre = PhotoImage(file="images/Pierre.png")
pierre = Label(frame, image=img_pierre)
pierre.place(x=30, y=100)

img_feuille = PhotoImage(file="images/Feuille.png")
feuille = Label(frame, image=img_feuille)
feuille.place(x=180, y=100)

img_ciseau = PhotoImage(file="images/Ciseaux.png")
ciseau = Label(frame, image=img_ciseau)
ciseau.place(x=330, y=100)

msg_acceuil = Label(frame, text="Bienvenue, vous jouez contre l'ordinateur, Cliquez sur une case pour jouer !")
msg_acceuil.place(relx=.5, rely=.1, anchor="center")

score_msg = StringVar()
score_msg.set("Votre score : " + str(player_points) + " -- Score Ordintaeur : " + str(pc_points))

msg_score = Label(frame, textvariable=score_msg)
msg_score.place(relx=.5, rely=.3, anchor="center")

def compter_pts(player_choice):
    global player_points, pc_points, score_msg

    # Game Status var. 0 if equality 1 if player win, 2 if comp. win
    game_status = 0

    choix_possible = ['Pierre', 'Feuille', "Ciseaux"]
    pc_choice = random.choice(choix_possible)

    if pc_choice == str(player_choice):
        print('PC a choisi ' + pc_choice + ' Il y a égalité , 0 points pour tout le monde')
    else:
        ## CHOIX JOUEUR PIERRE
        if player_choice in ["Pierre", "pierre"]:
            if pc_choice == "Ciseaux":
                print("PC a choisi la Ciseaux et a perdu -- +1 Point pour Joueur / 0 Pour PC")
                game_status = 1
                player_points += 1
            if pc_choice == "Feuille":
                print("PC a choisi la feuille et a gagné -- +1 Point pour PC / 0 Pour Joueur 1")
                game_status = 2
                pc_points += 1

        ## CHOIX JOUEUR FEUILLE
        if player_choice in ["Feuille", "feuille"]:
            if pc_choice == "Pierre":
                print("PC a choisi la Pierre et a perdu -- +1 Point pour Joueur / 0 Pour PC")
                game_status = 1
                player_points += 1
            if pc_choice == "Ciseaux":
                print("PC a choisi la Ciseaux et a gagné -- +1 Points pour PC / 0 Pour Joueur 1")
                game_status = 2
                pc_points += 1

        ## CHOIX JOUEUR CISEAU
        if player_choice in ["Ciseaux", "ciseau"]:
            if pc_choice == "Feuille":
                print("PC a choisi la Feuille et a perdu -- +1 Point pour Joueur / 0 Pour PC")
                game_status = 1
                player_points += 1
            if pc_choice == "Pierre":
                print("PC a choisi la Pierre et a gagné -- +1 Points pour PC / 0 Pour Joueur 1")
                game_status = 2
                pc_points += 1
    print("Votre score : " + str(player_points) + " -- Score ordinateur : " + str(pc_points))
    score_msg.set("Votre score : " + str(player_points) + " -- Score ordinateur : " + str(pc_points))
    
    if game_status == 0:
        tkinter.messagebox.showwarning("Egalité ..", "Il y'a eu égalité ! Ordinateur a choisi : " + pc_choice + " et vous : " + player_choice)
    elif game_status == 1:
        tkinter.messagebox.showinfo("VICTOIRE !", "Bravo, vous avez gagné ! Ordinateur a choisi : " + pc_choice + " et vous : " + player_choice)
    elif game_status == 2:
        tkinter.messagebox.showerror("Zuut, c'est perdu !", "Zut, vous avez perdu ! Ordinateur a choisi : " + pc_choice + " et vous : " + player_choice)
        

pierre.bind('<Button-1>', lambda event: compter_pts("Pierre"))
feuille.bind('<Button-1>', lambda event: compter_pts("Feuille"))
ciseau.bind('<Button-1>', lambda event: compter_pts("Ciseaux"))

frame.mainloop()
