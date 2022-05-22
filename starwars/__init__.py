import time

from world import World

def main():
    w = World()

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