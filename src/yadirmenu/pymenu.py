#! /usr/bin/python3
# -*- coding: utf-8 -*-
import sys

from tkinter import Button, Tk, W

WIDTH = 30
HEIGHT = 1
BG = "white"
FG = "black"
FOCUS_COLOR = "#444"
XPOZ = 400
YPOZ = 100


class Action:

    def __init__(self, tag, bf_obj, menu_tk_obj):
        self.tag = tag
        self.bf_obj = bf_obj
        self.menu_tk_obj = menu_tk_obj

    def do_action(self, event):  # pylint: disable=W0613
        self.menu_tk_obj.return_tag = self.tag
        self.bf_obj.root.quit()


class MenuButton:

    def __init__(
        self, root, text, cmd, w, h, bg="white",
            fg="blue", highlight_bg="black"
    ):
        self.but = Button(
            root,
            text=text,
            width=w,
            height=h,
            bg=bg,
            fg=fg,
            highlightcolor=highlight_bg,
            highlightthickness=2,
            anchor=W,
        )
        self.cmd = cmd
        self.but.bind("<Button-1>", self.cmd)
        self.but.pack()


class ButtonsFabric:

    def __init__(
        self,
        xpoz=100,
        ypoz=100,
        width=20,
        height=4,
        bg="green",
        fg="red",
        focus_color=FOCUS_COLOR,
    ):
        self.use_return = True
        self.buttons = []
        self.button_cur = 0
        self.root = Tk()
        self.title = "PyMenu"
        self.root.title(self.title)
        self.root.geometry(f"+{xpoz}+{ypoz}")
        self.width = width
        self.height = height
        self.bg = bg
        self.fg = fg
        self.focus_color = focus_color
        self.keys = {}
        self.bind_keys = [
            "1",
            "2",
            "3",
            "4",
            "5",
            "6",
            "7",
            "8",
            "9",
            "0",
            "q",
            "w",
            "e",
            "r",
            "t",
            "y",
            "u",
            "i",
            "o",
            "p",
            "a",
            "s",
            "d",
            "f",
            "g",
            "h",
            "j",
            "k",
            "l",
            "z",
            "x",
            "c",
            "v",
            "b",
            "n",
            "m",
        ]
        self.bind_keys_cnt = 0
        self.key_symbpol_pressed = ""
        self.keys["Up"] = self.key_up
        self.keys["Down"] = self.key_down
        self.keys["Escape"] = self.key_esc
        self.keys["Return"] = self.key_return

    def key_up(self):
        self.button_cur -= 1
        if self.button_cur == -1:
            self.button_cur = len(self.buttons) - 1
        self.buttons[self.button_cur].but.focus_set()

    def key_down(self):
        self.button_cur += 1
        if self.button_cur == len(self.buttons):
            self.button_cur = 0
        self.buttons[self.button_cur].but.focus_set()

    def key_esc(self):
        sys.exit(0)

    def key_return(self):
        self.buttons[self.button_cur].but.event_generate("<Button-1>")

    def key_symbol(self):
        symbol_index = self.bind_keys.index(self.key_symbpol_pressed)
        self.button_cur = symbol_index
        self.buttons[self.button_cur].but.focus_set()
        if not self.use_return:
            self.buttons[self.button_cur].but.event_generate("<Button-1>")

    def add_button(self, text, cmd):
        key = self.bind_keys[self.bind_keys_cnt]
        self.bind_keys_cnt += 1
        text = f"{key}        {text}"
        btn = MenuButton(
            self.root,
            text,
            cmd,
            self.width,
            self.height,
            bg=self.bg,
            fg=self.fg,
            highlight_bg=self.focus_color,
        )
        self.buttons.append(btn)
        self.keys[key] = self.key_symbol

    def key(self, event):
        self.key_symbpol_pressed = event.keysym
        try:
            self.keys[event.keysym]()
        except KeyError:
            pass

    def finalize(self):
        self.root.title(self.title)
        self.buttons[self.button_cur].but.focus_set()
        self.root.bind_all("<Key>", self.key)
        self.root.mainloop()


def main():

    class Menu:
        return_tag = "0"

    menu_obj = Menu()
    bf = ButtonsFabric(xpoz=XPOZ, ypoz=YPOZ, width=WIDTH,
                       height=HEIGHT, bg=BG, fg=FG)
    bf.use_return = False
    bf.title = "Test title"
    action_obj = Action("1", bf, menu_obj)
    bf.add_button("Tag = 1", action_obj.do_action)
    action_obj = Action("2", bf, menu_obj)
    bf.add_button("Tag = 2", action_obj.do_action)
    bf.finalize()
    print(f"Pressed tad = {menu_obj.return_tag}")
    sys.exit(0)


if __name__ == "__main__":
    main()
    sys.exit()
