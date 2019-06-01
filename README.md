# Carbon IT recruitment

Repository for the Carbon IT recruitment coding game. The game has been coded using Python 3.7 language. It is executable using this specific version of Python - it won't run on previous versions because of the usage of f-strings.

### Game description

Our game is made of several classes. It has been coded by following OOP paradigm. The game itself is made of a Map, composed with Cells.
A cell can be either:
  - A default **Cell**: empty when there is no fighter on it
  - A **Treasure** cell: same behaviour as a default cell but got a specific amount of treasure that one can collect
  - A **Mountain** cell: default cell that is always considered full - no move can be made on it

Our **Fighters** are made of an initial position and a set of movement:
  - We used a list to store the movements, from which we are going to "pick" moves at each game turn.
  - A Fighter also has an orientation (North, South, East, West). We used an enumeration to store those orientations in order to keep control on the different values of orientations. If a developers needs to add an orientation, he would have to add an entry to the enumeration.
  - Also, in Python an enumeration allows to map values to integers. Therefore, it is easier for us to handle orientation changes: we just have to add or remove 1 and control the final value to know the new orientation of the fighter.

### Game execution

The game can be executed using **Python 3.7+** from the code repository as follows:

```
python main.py [pathToTheGameFile] [-i --interactiveMode]
```

  - The variable pathToTheGameFile should be a string leading to the file from which we can load the game. It defaults to **./test.txt** file that is provided with the code. A second file is provided for testing purpose.
  - The optional -i --interactiveMode tag should be added if you want to follow the game turn after turn. You can disable the interactive mode during the game by entering q when prompted.
  
No additional package is needed.
