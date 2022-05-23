import time
import configmanager

from world import World

def main():
    cfg = configmanager.ConfigManager("config.ini")
    w = World(cfg)

    start_time = time.time()

    while True:
        current_time = time.time()
        delta_time = current_time - start_time

        if delta_time > 0.01:
            start_time = current_time
            w.update()
            print(w.toJSON())

if __name__ == "__main__":
    main()