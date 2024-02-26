<h1 align="left">python-template</h1>

<p align="left">
  Here you should add general information about the project
  <br> 
</p>

## 📝 Table of Contents

- [📝 Table of Contents](#-table-of-contents)
- [🧐 About ](#-about-)
- [👨‍💻 Description ](#-description-)
- [🏁 Getting Started ](#-getting-started-)
  - [Installing](#installing)
  - [Usage](#usage)
- [✍️ Authors ](#️-authors-)

## 🧐 About <a name = "about"></a>

With this program, you have the opportunity to play a game of dice with an AI opponent. The levels available are categorized as simple, moderate and arduous for your preference. Before being granted access to the scoreboard summary screen after launching it up, inputting your name is necessary.

As you play the game, the dice will be rolled in alternating turns. The sum of each roll adds to your score during that particular round. You have two options: either hold onto your current points and let the AI take over or continue rolling for an opportunity at a higher tally. However, if you happen to land on a 1, then all points acquired from that turn are lost instantaneously as it signals an end to any further rolls within said turn.

The match will persist until either party has accumulated a sum of 100 points or surpasses that number. Should you achieve victory, accolades shall be bestowed upon your conquest!

If you want to start another round, there are two options that await - either restart the game or simply exit. Take pleasure in your decision!

## 👨‍💻 Description <a name = "description"></a>

The class dedicated to games involves a dice game, where participants take turns rolling the die and earning points based on their results. The objective is for someone to reach or exceed 100 points before concluding the game. By invoking the method labeled play_game, this initiates gameplay while taking into account a difficulty parameter that identifies what number rolls would be considered as ones by each level of complexity; intricate levels having lesser values assigned in comparison with simpler counterparts. Additionally, there exists an option within the class allowing instantaneous victory accessible through using cheat codes if desired.

The games2 course is an additional game that functions using text, and it pits the player against a computer to determine who can reach a set score first. The gameplay consists of rolling dice and adding up scores while competing with another opponent. This continues until one person reaches their predetermined top point limit. To initialize the game, there's a technique called 'game_play' which chooses difficulty levels based on users’ preferences for maximum scoring per turn parameterization needs during playtime sessions.

## 🏁 Getting Started <a name = "getting_started"></a>

### Installing

Install Python: If you don't have Python already installed on your computer, go to https://www.python.org/downloads/ and download the version that is compatible with your system. Follow the installation instructions provided by the installer.

Create a new Python project in your IDE: Open your favorite Integrated Development Environment (IDE) and create a new Python project

Download the game files: Provide them with a link to download the game files or attach the files in an email.

Extract the files: Instruct them to extract the files from the downloaded folder to a location of their choice.

Run the main file: Instruct them to navigate to the extracted folder and double-click on the main file to run the game.

Play the game: Once the game is launched, they can follow the on-screen instructions to play the game.

Make sure to provide them with any additional information or requirements they may need to run the game, such as the version of Python needed or any dependencies required.

### Usage

In the initial block of code, there are two distinct categories - Die and games. The former being a class that consists solely of one function, roll(). This single method generates an arbitrary integer within the range 1 through 6 when called upon. Games on the other hand is designed for multiple players to engage in rolling dice together. Within this category lies three functions: __init__, play_game, and scoreboard creator.The first mentioned function initializes all aspects necessary to begin gameplay such as creating participants (players), setting up Dice instances for each player,and establishing a scoreboard to keep track of progress throughout the game's duration.Next comes into play,the ‘play_game’ procedure – which acts as our primary gaming loop until someone reaches or surpasses 100 points mark.Finally,a new winner will be declared at endgame based off total score achieved during said rounds played thus far by any given participant .

Within the subsequent set of code, there exists a solitary class named games2. This game is designed for singular players and entails competing against an AI opponent. Upon instantiation within the __init__ method, Die comes into play as well. Through utilization of name in tandem with user input collection capabilities, users are able to interactively provide their own distinct names which can then be returned later on during gameplay if necessary or desired by means unavailable through any other channels outside this particular function's scope alone. The progression of gameplay itself is categorized based upon varying levels of difficulty that end up dictating what maximum scores will ultimately result from each individual turn taken throughout said stages; all skills implemented therein such as rolling dice between both human player(s) and computer-based challengers operate under these conditions until either contender successfully accumulates 100 total points individually before one another signaling conclusion beyond doubt towards respective victors!

## ✍️ Authors <a name = "authors"></a>

- [Robel] [Brian] - Idea & Initial work
