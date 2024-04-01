#include <iostream>
#include <string>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <algorithm>
#include <random>

using namespace std;

// Pokemon Class (Base Class):
// o Attributes: name (string), sound (string), type (string), power (int), speed (int).
// o Methods: Constructor, getters for each attribute.
class Pokemon
{
private:
    string name;
    string sound;
    string type;
    int power;
    int speed;

public:
    Pokemon(string n, string s, string t, int p, int sp) : name(n), sound(s), type(t), power(p), speed(sp) {}

    string getName() const
    {
        return name;
    }

    string getSound() const
    {
        return sound;
    }

    string getType() const
    {
        return type;
    }

    int getPower() const
    {
        return power;
    }

    int getSpeed() const
    {
        return speed;
    }
};

// Derived from Pokemon:
// o WildPokemon Class:
// § Inherits all attributes from Pokemon.
// § Additional Attribute: catchRate (int).
// § Methods: Constructor, getter for catchRate, attemptEscape method to simulate escape
// behavior.
// o PalPokemon Class:
// § Inherits all attributes from Pokemon.
// § Represents a Pokémon that has been caught and is now a companion.
class WildPokemon : public Pokemon
{
private:
    int catchRate;

public:
    WildPokemon(string n, string s, string t, int p, int sp, int c) : Pokemon(n, s, t, p, sp), catchRate(c) {}

    int getCatchRate() const
    {
        return catchRate;
    }

    bool attemptEscape() const
    {
        int n = rand() % 100 + 1;
        return n > 50;
    }
};

class PalPokemon : public Pokemon
{
public:
    PalPokemon(string n, string s, string t, int p, int sp) : Pokemon(n, s, t, p, sp) {}
};

// Pokeball Class:
// o Attributes: name (string), efficiency (int).
// o Methods: Constructor, catchPokemon method to attempt catching a WildPokemon, getters for
// attributes.
class Pokeball
{
private:
    string name;
    int efficiency;

public:
    Pokeball(string n) : name(n), efficiency(0)
    {
        // Set default efficiencies based on the type of Pokeball
        if (name == "Normal")
            efficiency = 30;
        else if (name == "Strong")
            efficiency = 50;
        else if (name == "Ultra")
            efficiency = 70;
        else
            efficiency = 0; // Default efficiency for unknown types
    }
    string getName() const
    {
        return name;
    }

    int getEfficiency() const
    {
        return efficiency;
    }

    void setEfficiency(int e)
    {
        efficiency = e;
    }

    bool catchPokemon(const WildPokemon &p) const
    {
        int n = rand() % 100 + 1;
        int catchRate = p.getCatchRate() * efficiency;

        return n <= catchRate;
    }
};

// Berry Class:
// o Attributes: name (string), effectiveness (int).
// o Methods: Constructor, apply effect method that temporarily enhances a Pokéball's efficiency or makes
// a wild Pokémon easier to catch.
class Berry
{
private:
    string name;
    int effectiveness;

public:
    Berry(string n, int e) : name(n), effectiveness(e) {}

    string getName() const
    {
        return name;
    }

    int getEffectiveness() const
    {
        return effectiveness;
    }

    void applyEffect(Pokeball &p) const
    {
        p.setEfficiency(p.getEfficiency() + effectiveness);
    }

    void applyEffect(WildPokemon &p) const
    {
        p = WildPokemon(p.getName(), p.getSound(), p.getType(), p.getPower(), p.getSpeed(), p.getCatchRate() + effectiveness);
    }
};

// Player Class:
// o Attributes: Collection of Pokeballs, optional Berry.
// o Methods: Constructor, method to add Pokeball to the collection, catchPokemon method to attempt to
// catch a wild Pokémon.
// 2. Enable players to augment their inventory with three distinct types of Pokéballs: Normal, Strong, and Ultra.
// 3.1 Stockpile Pokéballs: Players may add five Pokéballs of random types to their inventory in a single action.
// This action is a one-time opportunity.
class Player
{
private:
    vector<Pokeball> pokeballs;
    Berry berry;
    vector<WildPokemon> capturedPokemons;

public:
    Player(Berry b) : berry(b) {}

    void addPokeball(Pokeball p)
    {
        pokeballs.push_back(p);
    }

    void stockpilePokeballs()
    {
        const int MAX_POKEBALLS = 5; // Maximum number of Pokeballs allowed

        if (pokeballs.size() < MAX_POKEBALLS)
        {
            int numToAdd = std::min(static_cast<size_t>(MAX_POKEBALLS - pokeballs.size()), static_cast<size_t>(5));
            for (int i = 0; i < numToAdd; ++i)
            {
                int randomType = rand() % 3; 
                string pokeballType;
                int efficiency;

                switch (randomType)
                {
                case 0:
                    pokeballType = "Normal";
                    efficiency = 1;
                    break;

                case 1:
                    pokeballType = "Strong";
                    efficiency = 2;
                    break;

                case 2:
                    pokeballType = "Ultra";
                    efficiency = 3;
                    break;
                }

                addPokeball(Pokeball(pokeballType));
            }
            cout << "You stocked up " << numToAdd << " random Pokéballs!" << endl;
        }
        else
        {
            cout << "You already have 5 or more Pokéballs. No need to stockpile." << endl;
        }
    }

    bool exploreAndEncounter()
    {
        int encounterChance = rand() % 100 + 1;
        return encounterChance <= 25;
    }

    bool catchPokemon(WildPokemon &p)
    {
        if (pokeballs.empty())
        {
            cout << "No pokeball available." << endl;
            return false;
        }
        else
        {
            if (berry.getName() != "")
            {
                berry.applyEffect(p);
            }
            bool captureResult = pokeballs.back().catchPokemon(p);
            if (captureResult)
            {
                capturedPokemons.push_back(p);
                cout << "You caught " << p.getName() << "!" << endl;

                pokeballs.pop_back();
            }
            else
            {
                cout << "You failed to catch " << p.getName() << "!" << endl;
            }
            return captureResult;
        }
    }
    void displayInventory() const
    {
        cout << "Inventory:" << endl;
        for (const auto &pokeball : pokeballs)
        {
            cout << pokeball.getName() << " (Efficiency: " << pokeball.getEfficiency() << ") " << endl;
        }
    }

    vector<string> displayCapturedPokemons() const
    {
        vector<string> capturedNames;
        cout << "Captured Pokémons:" << endl;
        for (const auto &pokemon : capturedPokemons)
        {
            cout << pokemon.getName() << " ";
            capturedNames.push_back(pokemon.getName());
        }
        cout << endl;
        return capturedNames;
    }
};

// World Class:
// o Attributes: Collection of WildPokemon.
// o Methods: Constructor, method to add WildPokemon to the world, method to simulate player
// exploration and encounters with wild Pokémon.
class World
{
private:
    vector<WildPokemon> wildPokemons;

public:
    void addWildPokemon(WildPokemon p)
    {
        wildPokemons.push_back(p);
    }

    bool allPokemonsCaptured() const
    {
        return wildPokemons.empty();
    }

    void simulateExploration(Player &p)
    {
        int playerChoice = 0; // Initialize playerChoice before the loop

        // Shuffle the wildPokemons vector using a random number generator
        random_device rd;
        mt19937 g(rd());
        shuffle(wildPokemons.begin(), wildPokemons.end(), g);

        int randomPokemonIndex = 0;
        WildPokemon encounteredPokemon = wildPokemons[randomPokemonIndex];

        cout << "Options:" << endl;
        cout << "1. Add Pokeballs to inventory" << endl;
        cout << "2. Explore" << endl;
        cout << "3. Display Pokeballs" << endl;
        cout << "4. Display captured Pokémons" << endl;
        cout << "5. Exit" << endl;

        cout << "Enter your choice: ";
        cin >> playerChoice;

        // Check if the input is valid
        if (cin.fail())
        {
            cout << "Invalid input. Please enter a number." << endl;
            cin.clear();               // Clear the fail state
            cin.ignore(INT_MAX, '\n'); // Ignore invalid input
                                       // Restart the loop
        }

        cout << endl;

        switch (playerChoice)
        {
        case 1:
            p.stockpilePokeballs();
            break;
        case 2:
            if (p.exploreAndEncounter())
            {
                cout << "Encountered a wild " << encounteredPokemon.getName() << endl;
                p.catchPokemon(encounteredPokemon);
                wildPokemons.erase(wildPokemons.begin() + randomPokemonIndex);
            }
            else
            {
                cout << "No wild Pokémons encountered." << endl;
            }
            break;
        case 3:
            p.displayInventory();
            break;
        case 4:
            p.displayCapturedPokemons();
            break;
        case 5:
            cout << "Exiting exploration." << endl;
            break;
        default:
            cout << "Invalid choice." << endl;
            break;
        }
    }

    void displayWildPokemons() const
    {
        cout << "Wild Pokémons remaining in the world:" << endl;
        for (const auto &pokemon : wildPokemons)
        {
            cout << pokemon.getName() << " ";
        }
        cout << endl;
    }
};

// GameTester Class:
// o Methods: Static methods to run tests for different game functionalities, such as catching Pokémon,
// using Pokéballs and Berries, and player-world interactions.
class GameTester
{
public:
    static void testGameplay()
    {
        Berry b("", 0);
        Player player(b);
        player.stockpilePokeballs();
        player.displayInventory();
        player.displayCapturedPokemons();

        World world;
        WildPokemon p1("Pikachu", "Pika Pika", "Electric", 100, 100, 50);
        WildPokemon p2("Charmander", "Char Char", "Fire", 100, 100, 50);
        WildPokemon p3("Squirtle", "Squirt Squirt", "Water", 100, 100, 50);
        WildPokemon p4("Bulbasaur", "Bulba Bulba", "Grass", 100, 100, 50);
        WildPokemon p5("Jigglypuff", "Jiggly Jiggly", "Fairy", 100, 100, 50);

        world.addWildPokemon(p1);
        world.addWildPokemon(p2);
        world.addWildPokemon(p3);
        world.addWildPokemon(p4);
        world.addWildPokemon(p5);

        while (!player.exploreAndEncounter() || !world.allPokemonsCaptured())
        {
            world.simulateExploration(player);
        }

        world.displayWildPokemons(); // Display remaining wild Pokémons in the world
    }
};

int main()
{
    srand(time(NULL)); // Seed the random number generator with the current time

    GameTester::testGameplay();
    return 0;
}
