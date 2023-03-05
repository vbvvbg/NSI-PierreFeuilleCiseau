import random

choix_possible= ['Pierre','Feuille',"Ciseaux"]

player_points = 0
pc_points = 0

while True:
    player_choice = input('Choisissez Pierre, Feuille, Ciseaux pour commencer la partie : ')
    pc_choice = random.choice(choix_possible)

    if pc_choice == str(player_choice):
        print('PC a choisi ' + pc_choice + ' Il y a égalité , 0 points pour tout le monde')
    else:
        ## CHOIX JOUEUR PIERRE
        if player_choice in ["Pierre", "pierre"]:
            if pc_choice == "Ciseaux":
                print("PC a choisi la Ciseaux et a perdu -- +1 Point pour Joueur / 0 Pour PC")
                player_points += 1
            if pc_choice == "Feuille":
                print("PC a choisi la feuille et a gagné -- +1 Point pour PC / 0 Pour Joueur 1")
                pc_points += 1

        ## CHOIX JOUEUR FEUILLE
        if player_choice in ["Feuille", "feuille"]:
            if pc_choice == "Pierre":
                print("PC a choisi la Pierre et a perdu -- +1 Point pour Joueur / 0 Pour PC")
                player_points += 1
            if pc_choice == "Ciseaux":
                print("PC a choisi la Ciseaux et a gagné -- +1 Points pour PC / 0 Pour Joueur 1")
                pc_points += 1

        ## CHOIX JOUEUR CISEAU
        if player_choice in ["Ciseaux", "ciseau"]:
            if pc_choice == "Feuille":
                print("PC a choisi la Feuille et a perdu -- +1 Point pour Joueur / 0 Pour PC")
                player_points += 1
            if pc_choice == "Pierre":
                print("PC a choisi la Pierre et a gagné -- +1 Points pour PC / 0 Pour Joueur 1")
                pc_points += 1
    print("Votre score : " + str(player_points) + " -- Score ordinateur : " + str(pc_points))