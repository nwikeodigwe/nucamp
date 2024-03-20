wizard="Wizard"
elf="Elf"
human="Human"

wizard_hp = 70
elf_hp = 100
human_hp = 150
dragon_hp = 300

wizard_damage = 150
elf_damage = 100    
human_damage = 20

while True:
    print("1. Wizard")
    print("2. Elf")
    print("3. Human")
    print("4. Exit")

    input_character = input("Choose your character: ")
    if input_character == "1":
        character = wizard
        my_hp = wizard_hp
        my_damage = wizard_damage
    elif input_character == "2":
        character = elf
        my_hp = elf_hp
        my_damage = elf_damage
    elif input_character == "3":
        character = human
        my_hp = human_hp
        my_damage = human_damage
    elif input_character == "4":
        break
    else:
        print("Unknown character")

    print("You chose the character: " + character)
    print("Health: " + str(my_hp))
    print("Damage: " + str(my_damage))
    
    while True:
        dragon_hp = dragon_hp - my_damage
        print("The dragon received " + str(my_damage) + " damage")
        print("Dragon health: " + str(dragon_hp))
        if dragon_hp <= 0:
            print("The dragon lost the battle")
            break
        my_hp = my_hp - 20
        print("The dragon strikes back with 20 damage")
        print("Character health: " + str(my_hp))
        if my_hp <= 0:
            print(character + "lost the battle")
            break