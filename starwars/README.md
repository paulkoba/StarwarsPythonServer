# Starwars server

This folder contains server for the Starwars game that was written by Paul Koba as an assignment for OOP course at KNU.

According to the assignment description, the server should implement 10 patterns. The following patterns are implemented:

1. Singleton pattern - implemented as a metaclass; used in world, strategies
2. Factory method pattern - creation of border strategies
3. Strategy pattern - borderstrategy.py; manage what happens to the object when they go over the boundary of the world
4. Dependency injection pattern - world containts configuration as a member of the class
5. Adapter pattern - ConfigManager class is adapter over configparser.ConfigParser
6. Decorator pattern - astroids are given positions and velocities using AstroidDecorator class
7. Template method pattern - used in iterators in the world class
8. Facade pattern - worldfacade is used to manage the world instead of directly accessing the world class
9. Iterator pattern - used in the world class to iterate over all objects / objects of a certain type
10. Observer pattern - used in the world class to notify observers about ticks