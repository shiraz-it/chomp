import tkinter as tk
from Classes.GameMenu import GameMenu


def main():
    root = tk.Tk()
    GameMenu(root)

    root.mainloop()


if __name__ == "__main__":
    main()