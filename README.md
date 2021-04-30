# GameOfLife

A [Conway's Game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life) simple implementation using Python, PyQT5, QTDesigner and convolution 
to manage the state succession mechanism.

## Motivation
This is a programming assignment for the HCI 2020-2021 course where it will be implemented the Game of Life, along with a
complete and polished Graphical User Interface to control the simulation with various features that will be described later.\
This project focuses on **functionality**, **code hygene**, **correctness**, **completeness** and **extra features** using interface programming **best practices** (such as MVC) so the application's overall look it's not a central aspect.

## Screenshots
![Screenshot from 2021-03-08 20-31-30](https://user-images.githubusercontent.com/22282000/110372918-2e26d280-804f-11eb-8a93-22b47eeded4e.png)
![Screenshot from 2021-03-08 20-32-07](https://user-images.githubusercontent.com/22282000/110372927-2ff09600-804f-11eb-974f-a0636db863da.png)


## Tech/framework used
Python 3.5+ language

<b>Built and tested with</b>
- [PyQT5](https://www.riverbankcomputing.com/software/pyqt/) v. 5.15.2
- [QTDesigner](https://build-system.fman.io/qt-designer-download) v. 5.5.1
- scipy v. 1.4.1
- numpy v. 1.18.5
- qimage2ndarray v. 1.8.3

## Features implemented
* A working visual simulation
* Start/pause/clear controls
* Variable framerate
* Drawing/editing of state
### Extra features
* Zoom slider
* Cell history

## Installation
Simply install the necessary libraries and run _main.py_


## How to use?
Left click on the blank board to add a population to a cell (black cell).\
Right click to bring back the cell to white.\
Left click and mouse movement to define a continuous sequence of black cells.\
Play button to start the simulation then is possible to pause.\
Clear button to revert the board to a blank state.

## Credits
Credits to GTRONIK for the Aqua Style Sheet for QT Applications. 
https://github.com/GTRONICK/QSS

