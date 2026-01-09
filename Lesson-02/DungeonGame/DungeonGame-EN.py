# === SCENES ===

def scene_Thor(name):

    while True:
        print("Thor's Island is very large. On the other side of the island, there is a harbor. There stands an old lady who promises to help you find the Three Souls Scarab. \n"
              "You can also choose to continue by submarine, or you can relax at a café.")
        print()
        try:
            choice_Thor = int(input(f"What will {name} choose? \n"
                                   "[1] Submarine\n"
                                   "[2] Old lady\n"
                                   "[3] Café\n"
                                   "\n"
                                   f"{name} chooses option number: "))
            if choice_Thor == 1:
                fish = input("The submarine captain asks: 'What is your favorite fish?': ")
                print()
                print(f"After a brief introduction, {name} travels in a submarine with the captain who knows the way... Hey, did I see your favorite fish? The {fish}?\n"
                      f"You admit you saw that fish. The captain suggests sailing after a school of {fish}.\n"
                      f"NAAANUUNAANUUU\n"
                      f"What was that? Are we under attack?\n"
                      f"{name} quickly grabs the only diving gear left and leaves the submarine... leaving the captain to drown.\n"
                      f"Once on land, {name} runs towards the inhabited part of the island, but suddenly {name} falls into a deep pit...\n"
                      f"..It's very dark...")
                result = scene_Basilisk(name)
                return result

            elif choice_Thor == 2:
                print()
                print(f'You walk to the harbor, heading to the lady who promises to help find the Three Souls Scarab. "Come with me to my house," says the old lady. {name} follows her without thinking.\n'
                      f'The old lady’s house is not very clean. There are potions on the table, the counter, and even on the floor. Only a few candles are burning. In the middle of the house is a large cauldron.\n'
                      f'"If you give me a bag of gold, I will take you to the place of the Three Souls Scarab," says the lady. {name} gives a bag of gold. The lady throws a Cerberus bone, night moss, and a whisper feather into the cauldron.\n'
                      f'She pours the potion into a bottle. "If you drink this bottle, it will take you to the place of the Three Souls Scarab." {name} drinks it in one gulp, feels dizzy, and faints.\n'
                      f'\n'
                      f'{name} wakes up, but not where {name} expected...')
                result = scene_Cerberus(name)
                return result

            elif choice_Thor == 3:
                print()
                print(f"{name} decides to relax at the café. There, {name} is offered a drink. {name} drinks it and feels a little drunk.\n"
                      f"{name} decides to continue traveling toward an old ship.")
                result = scene_Kraken(name)
                return result
            else:
                print("=== YOU MUST MAKE A CHOICE. ENTER 1, 2 OR 3! ===")
        except ValueError:
            print("=== YOU MUST MAKE A CHOICE. ENTER 1, 2 OR 3! ===")


def scene_Basilisk(name):
    while True:
        print(
            f'{name} opens the door. A gurgling sound fills the room, followed by a "Hisssssss....."\n'
            f'A wet Basilisk crawls toward {name}! It has a mouth full of sharp teeth and tries to attack!\n')
        next_step = input("Press enter to see what you can do!")

        try:
            choice_Basilisk = int(input("The Basilisk is a large snake-like creature. You look around. Skeletons of humans and animals are everywhere.\n"
                                        "You also see a soldier's skeleton. His sword and shield are still in good condition.\n"
                                        "Across the room, there is a rope. You could climb it, but the Basilisk has a long neck and can catch you quickly.\n"
                                        "\n"
                                        "Do you choose the sword and shield or climb the rope?\n"
                                        "\n"
                                        "[1] Sword and shield\n"
                                        "[2] Climb the rope"))
            if choice_Basilisk == 1:
                print()
                print(
                    f"{name} quickly grabs the sword and shield. First, {name} cuts off part of the Basilisk's tail. The Basilisk reacts quickly and moves toward {name}.\n"
                    f"{name} tries to defend against the Basilisk with the shield... but it is in vain.\n"
                    f"The Basilisk grabs {name} by the legs.\n"
                    f"{name} screams and tries to crawl away, but there is no escape.\n"
                    f"{name} is eaten alive and will never find the Three Souls Scarab.\n"
                    f"\n"
                    f"RIP {name}")
                return "dead"
            elif choice_Basilisk == 2:
                print()
                print(f"{name} runs to the rope and narrowly escapes the Basilisk! Once at the top, {name} takes a deep breath and looks around.\n"
                      f"{name} finds themselves in another room, this time full of treasures! {name} can't believe it... the Three Souls Scarab lies there!\n"
                      f"{name} will live forever...\n")
                return "crown"
            else:
                print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")
        except ValueError:
            print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")


def scene_Cerberus(name):
    while True:
        print()
        print(f"{name} starts sweating.. it is very hot here! {name} looks around. It is dark, but the lava lights up the darkness in this cave.\n"
              f"{name} quickly removes all clothing, the heat is unbearable!\n"
              f"Naked, {name} tries to find a way out. It looks like a labyrinth! {name} suddenly hears the sound of panting dogs but is only thinking of escaping to a cooler place.\n")
        next_step = input(f"Press enter to see what happens in this labyrinth...")
        try:
            choice_Cerberus = int(input(f"{name} thought they found the exit, but then a beast appears... It is CERBERUS! A three-headed monstrous dog with a long snake tail!\n"
                                        f"Cerberus approaches... he wants to EAT {name}!\n"
                                        f"What will {name} do?\n"
                                        "\n"
                                        f"[1] Run back into the labyrinth and hope Cerberus doesn't find you\n"
                                        f"[2] See no way out and sacrifice yourself\n"
                                        f"[3] Throw a rock at Cerberus\n"
                                        "\n"
                                        f"{name} chooses option number: "))

            if choice_Cerberus == 1:
                print()
                print(f"{name} runs back into the labyrinth.. but Cerberus quickly catches up. {name} slips and Cerberus tears {name} apart..")
                return "dead"

            elif choice_Cerberus == 2:
                print()
                print(f"{name} sees no way out in this lava cave labyrinth... {name} is very scared and sacrifices themselves. Cerberus approaches. 6 eyes look at {name}, but Cerberus does nothing.\n"
                      f"{name} feels relieved and now wants to leave the lava cave. Cerberus guides {name} to the exit. {name} steps onto the surface. Sand everywhere... It looks like a desert. {name} sees an oasis and walks towards it.\n"
                      f"{name} drinks water from the oasis and suddenly sees a sarcophagus half buried. {name} opens it and finds an artifact. Hmm.. looks like a scarab?..\n"
                      f"{name} examines it carefully.\n"
                      f"IT IS THE THREE SOULS SCARAB!! ")
                print()
                print(f"{name} jumps around! {name} is so happy the Three Souls Scarab is found.. or was it an illusion?")
                return "crown"
            elif choice_Cerberus == 3:
                print()
                print(f"{name} throws a rock at Cerberus. But it doesn’t work. Cerberus tears {name} apart..")
                return "dead"
            else:
                print("=== YOU MUST MAKE A CHOICE. ENTER 1, 2 OR 3! ===")
        except ValueError:
            print("=== YOU MUST MAKE A CHOICE. ENTER 1, 2 OR 3! ===")


def scene_Kraken(name):
    while True:
        print()
        print(f"After a long journey, {name} arrives at an old ship. {name} boards the ship. {name} senses someone is present.\n"
              f"Suddenly the old ship moves! {name} gets scared and tries to escape, but it's too late.\n"
              f"Large tentacles wrap around the ship. {name} cannot move.")
        print()
        next_step = input("Press enter to see what you can do")
        print()
        try:
            choice_Kraken = int(input(f"{name} luckily has a magic wand with 2 spells. {name} only remembers their names but not what they do.\n"
                                      f"{name} has to guess which spell to use:\n"
                                      "[1] Abyssus Ignis!!!\n"
                                      "[2] Tentaculi Vinculum!!!\n"
                                      "\n"
                                      f"{name} chooses spell number: "))
            if choice_Kraken == 1:
                print()
                print(f"{name} shouts: ABYSSUS IGNIS!!. Instead of banishing the Kraken, {name} vanishes themselves.\n"
                      f"{name} ends up inside the Kraken's stomach... not smart.. {name} suffocates inside..")
                return "dead"
            elif choice_Kraken == 2:
                print()
                print(f"{name} shouts: TENTACULI VINCULUM!!. The Kraken relaxes and sinks into the water.. Now {name} can safely investigate the old ship.\n"
                      f"On the deck, {name} finds a treasure chest and opens it.. {name} grabs the Three Souls Scarab! What a find!")
                return "crown"
            else:
                print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")
        except ValueError:
            print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")


# == CHECK DEAD OR WON
def check_Result(result):
    if result == "dead":
        print("You are dead")
        return True
    elif result == "crown":
        print("Congratulations! You won!")
        return True
    return False


def start_DungeonGame():
    print("Welcome to the Dungeon Game!")
    name = input("Brave adventurer, what is your name?: ")
    print()
    print(f"Hello {name}! Welcome to the beginning of your journey!\n"
          f'You have decided to search for the "Three Souls Scarab"! This is a large artifact of shiny obsidian, wings of fire with sandy golden accents.\n'
          f'The artifact can protect you from enemies. You find it so special that you go on a world adventure to obtain it.\n'
          f"This will not be an easy journey. There is a chance you might not survive. So think carefully about the path you take.")
    print()
    input("Press enter to start your journey!")
    print()

    while True:
        try:
            boat_choice = int(input(f"It is a beautiful sunny day. {name} has arrived at the harbor and walks past a few boats.\n"
                                    f"\n"
                                    f"The first boat is a papyrus boat, heading to the Realm of Anubis.\n"
                                    f"The second boat is a Trireme, a Greek warship that will take you to the Temple of Medusa.\n"
                                    f"The third boat is the Knarr, a large Viking ship that sails directly to Muspel’s Fireland.\n"
                                    f"\n"
                                    f"Which boat do you choose?\n"
                                    f"\n"
                                    f"[1] Realm of Anubis\n"
                                    f"[2] Temple of Medusa\n"
                                    f"[3] Fireland of Muspel\n"
                                    f"\n"
                                    f"{name} chooses boat number: "))
            if boat_choice == 1:
                print()
                print(f"{name} has chosen to travel to the Realm of Anubis...\n")
                input("Press enter to see what happens next...\n")
                print(f'"{name.upper()}! HOLD ON!" Shouts the captain. The papyrus boat is attacked by sea monsters.\n'
                      f"There should be weapons in the chest. You rush to the chest and see a harpoon and... the catch of the day: a huge fat mermaid. Nothing else is left...\n"
                      f"\nHow will you make the sea monsters leave the boat alone?\n")
                input("Press enter to make your choice\n")
                while True:
                    choice_item = int(input(f"What will {name} do?\n"
                                            "[1] Throw the harpoon at the sea monsters...\n"
                                            "[2] Try to throw the fat mermaid into the sea...\n"
                                            "\n"
                                            f"{name} chooses option number: "))
                    if choice_item == 1:
                        print()
                        print(f"{name} quickly throws the harpoon at the sea monsters. They still cling to the boat. Part of the boat breaks off.\n"
                              f"Because the boat is now unbalanced, it runs aground at the Lion’s Cave of Sechmet. The captain is furious. He cannot leave this land.\n"
                              f"He tries to attack you, but you quickly run into the cave to hide.\n")
                        input("Press enter to see what happens as you go deeper into the cave...\n")
                        print(f"{name} sees a staircase and spirals downwards. There are 2 closed cellar doors. The left door has a symbol of a snake-like creature.\n"
                              f"The right door has a symbol of a dog-like creature.\n")
                        input("Press enter to choose a door...\n")
                        while True:
                            try:
                                animal_choice = int(input(f"Which door does {name} choose?\n"
                                                          "[1] Door with the snake-like symbol\n"
                                                          "[2] Door with the dog-like symbol\n"
                                                          f"{name} chooses door number: "))
                                if animal_choice == 1:
                                    print("You choose the door with the snake-like symbol")
                                    result = scene_Basilisk(name)
                                    if check_Result(result):
                                        return
                                elif animal_choice == 2:
                                    print("You choose the door with the dog-like symbol")
                                    result = scene_Cerberus(name)
                                    if check_Result(result):
                                        return
                                else:
                                    print("Choose a symbol!")
                            except ValueError:
                                print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")
                    elif choice_item == 2:
                        print(f"{name} decides to throw the catch of the day: the fat mermaid into the water so the sea monsters will follow it.\n"
                              f"Luckily, the boat is not damaged, but soon the captain sees dark clouds forming. A storm begins and he decides to stop at Thor's Island.\n")
                        result = scene_Thor(name)
                        if check_Result(result):
                            return
                    else:
                        print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")

            elif boat_choice == 2:
                print("You sail toward the Temple of Medusa. The captain of the Greek warship advises not to stop at the temple.\n"
                      "Medusa could appear at any moment. If you look at her, you turn to stone!\n"
                      "It is decided to continue sailing to Thor's Island.")
                result = scene_Thor(name)
                if check_Result(result):
                    return

            elif boat_choice == 3:
                print()
                print("You sail to Muspel’s Fireland.")
                print()
                while True:
                    try:
                        drink_choice = int(input("Once you arrive at Muspel’s Fireland, you notice a 'burnt' smell.\n"
                                                 "Suddenly, a fire troll approaches and offers you 2 drinks: a nasty drink and a tasty drink.\n"
                                                 "\n"
                                                 f"Which drink does {name} choose?\n"
                                                 "[1] Nasty drink\n"
                                                 "[2] Tasty drink\n"
                                                 f"{name} chooses drink number: "))
                        if drink_choice == 1:
                            print("You drink the nasty drink... Ugh, it feels bad. You need to vomit and rush to the bathroom.\n"
                                  "The captain decides to go to Thor's Island to drop you off, not wanting vomit or mess on the ship.")
                            result = scene_Thor(name)
                            if check_Result(result):
                                return

                        elif drink_choice == 2:
                            print("You drink the tasty drink. That was delicious! You decide to continue sailing toward the Battlefield of Teutates.")
                            while True:
                                try:
                                    fairy_choice = int(input("The battlefield is still 'fresh'. A recent war took place. Many casualties lie on the field.\n"
                                                             "Some are alive, some are dead.\n"
                                                             "\n"
                                                             f"Suddenly, a small fairy flies toward {name}. She looks like Tinkerbell!\n"
                                                             "The fairy is very sad and is looking for a home.\n"
                                                             f"\nWhat does {name} offer?\n"
                                                             "[1] Invite the fairy to travel with you\n"
                                                             "[2] Let the fairy live in a big flower\n"
                                                             f"{name} chooses option number: "))
                                    if fairy_choice == 1:
                                        print(f"The fairy travels with {name}. During the journey, {name} asks which direction to take.\n"
                                              "The fairy points to a small island. Smoke rises from it, but that does not matter.\n"
                                              f"Once on the island, the fairy flies away.\n"
                                              f"{name} walks on the island, but suddenly {name} falls into a deep dark hole...")
                                        result = scene_Cerberus(name)
                                        if check_Result(result):
                                            return
                                    elif fairy_choice == 2:
                                        print("You let the fairy live in a big flower. That is a nice home for her.\n"
                                              f"{name} wants to continue sailing toward an old abandoned ship.")
                                        result = scene_Kraken(name)
                                        if check_Result(result):
                                            return
                                    else:
                                        print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")
                                except ValueError:
                                    print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")
                        else:
                            print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")
                    except ValueError:
                        print("=== YOU MUST MAKE A CHOICE. ENTER 1 OR 2! ===")
            else:
                print()
                print("=== YOU MUST CHOOSE A BOAT: ENTER 1, 2 OR 3! ===")
                print()
        except ValueError:
            print()
            print("=== YOU MUST CHOOSE A BOAT: ENTER 1, 2 OR 3! ===")
            print()


# Start game
start_DungeonGame()
