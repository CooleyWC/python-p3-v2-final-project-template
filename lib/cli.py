# lib/cli.py

from helpers import (
    list_ensembles,
    exit_program,
    add_ensemble,
    view_ensemble,
    update_ensemble,
    delete_ensemble
)


def main():
    while True:
        main_menu()
        choice = input("> ")
        if choice == "M" or choice == "m":
            list_ensembles()
            ensembles()
        elif choice == "E" or choice == "e":
            exit_program()
        else:
            print("Invalid choice")


def main_menu():
    print("Welcome to Will Cooley's Music School")
    print("Type M or m to see the ensembles")
    print("Type E or e to exit the program")

def ensembles():
    selected_ensemble = None
    while True:
        ensembles_menu()
        choice = input("> ")
        if choice.isdigit():
            selected_ensemble = int(choice)
            view_ensemble(selected_ensemble)
            ensemble_options(selected_ensemble)
        elif choice == "C" or choice == "c":
            add_ensemble()    
        elif choice == "B" or choice == "b":
            break
        elif choice == "E" or choice == "e":
            exit_program()
        else:
            print('Invalid Choice')

def ensembles_menu():
    print("Type the number of the Ensemble to view its details")
    print("Type C or c to add a new ensemble")
    print("Type B or b to go back to the main menu")
    print("Type E or e to exit the program")

def ensemble_options(selected_ensemble):
    while True:
        ensemble_options_menu()
        choice = input("> ")
        if choice == "U" or choice == "u":
            update_ensemble(selected_ensemble)
            list_ensembles()
            break
        elif choice == "D" or choice == "d":
            delete_ensemble(selected_ensemble)
        elif choice == "B" or choice ==  "b":
            break
        elif choice == "E" or choice =="e":
            exit_program()
        else:
            print('Invalid Choice')
        

def ensemble_options_menu():
    print("Type U or u to update this ensemble")
    print("Type D or d to delete this ensemble")
    print("Type B or b to go back to ensemble menu")
    print("Type E or e to exit the program")




    





if __name__ == "__main__":
    main()
