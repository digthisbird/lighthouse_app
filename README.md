# SOLO RPG SUPPORT App
#### Video Demo: <URL>
#### Description:
#####Inspiration:
The main inspiration for this app is the solo RPG journaling game "Lighthouse at the End of the World" by Ken Lowery. I bought the book last summer and have been exicted to sit down an play it. However, when I began reading through it, I realized I didn't have all the tool required to keep track of events and randomization needed. Additionally, laying all that out takes a surprising amount of desk space. Looking online didn't result in a helpful solution, so I decided to try to make an app that would track everything in one place. 
"Lighthouse" uses the Wretched & Alone system, referenced here: https://sealedlibrary.itch.io/wretched-alone-srd

#####Design:
The app is designed to be a companion app to the game, and can be used for other solo journaling RPGs that have the same game mechanics. A user cannot just use the app in lieu of purchasing the game book, which I believe is important to support game designers. The app is merely an emulator of the tools needed and does not give any of the information needed.

I wanted the "table space" to evoke the same high seas imagery the base game does. I looked for old maps through the library of congress, particularly ones of the lower Atlantic, as the game is based on the San Juan del Salvamento Lighthouse off the coast of the Tierra del Fuego. Cards also needed a weathered feel. 


#####Functionality:
Designing the app required taking into account of lot of functionalities with dependent relationships. To start each week, the user must roll a die (d6) to determine how many cards are drawn, then draw the cards one a time, referencing the guide book for what to do with each card pull. Some card pulls ask the player to flip a coin, save a card, or 
The main game flow is as follows: 
1 Roll a d6.
2 Pull cards equal to the number rolled, one by one.
3 Follow the instruction of each card in your journal (external of app).
4 Enter your log for the week.
5 If not dead, restart week.
The user must ensure they are working at the pace they'd like, as there is no back or undo button yet. 


#####Files:
project.py contains the main code and class functions for the program
test_project.py
requirements.txt lists the pip-install libraries needed to run project.py and test_project.py


Background image is a map of Arctic discoveries published by a British cartographer in 1854, accessed from the Library of Congress website: https://www.loc.gov/resource/g9781s.fi000116/
Pixel Art Assests for this app were downloaded from itch.io.
Cards came from the asset pack "Pixel assets- Playing Cards" by user Blueeyedrat: https://blueeyedrat.itch.io/pixel-assets-playing-cards
Dice came from the asset pack "Dice Roll" by user Kicked-in-Teeth: https://kicked-in-teeth.itch.io/dice-roll
The coin asset is a Spanish Doubloon which comes from the Wikipedia entry "Doubloon": https://en.wikipedia.org/wiki/Doubloon 

Issues:
As of right now, the app requires a user to play the entire game in one sitting. The game can be very long and may take multiple days with breaks, depending on the luck of the player. This means the user would have to leave the app open on their desktop

TODO
As of 3/20/2025:
Add an area for 10 tokens that the user can remove tokens from.
Update the dice images to look more weathered.
Create a discard pile.
Add a fullscreen mode.
Make games saveable and add a home screen before starting the game, so users don't have to leave the app open or write down tracking information, allowing them to play the journaling game over many days.



