import traceback

import PySimpleGUI as sg

import style

sg.theme("LightGrey4")


class InterFace:
    def __init__(self):
        self.make_layout()

    def make_layout(self):
        self.table = sg.Table([], **style.main_table, key="-TABLE-")
        self.frame_table = sg.Frame("ItemList", [[self.table]])

        self.form_price = [
            sg.Text("価格", **style.price_text),
            sg.In(default_text="10000", **style.price_input, key="-PRICE MIN-"),
            sg.Text("〜", **style.price_text),
            sg.In(default_text="30000", **style.price_input, key="-PRICE MAX-"),
            sg.Text("円", **style.price_text),
        ]
        self.form_keyword = [
            sg.Text("キーワード", **style.keyword_text),
            sg.In(default_text="", **style.keyword, key="-KEYWORD-"),
        ]
        self.btn_run_pause = sg.Button("Run", key="-RUN/PAUSE-")
        self.btn_apply = sg.Button("フォーム反映", key="-BTN UPDATE-")
        self.log = sg.Multiline(**style.log, key="-MULTI LOG-")
        self.frame_form = sg.Frame(
            "Form",
            [
                self.form_keyword,
                self.form_price,
                [self.btn_run_pause, self.btn_apply],
            ],
        )

        # fmt:off
        self.layout = [[self.frame_table],
                       [self.frame_form, self.log]]
        # fmt:on

    def show_window(self):
        self.window = sg.Window(
            "mercari app",
            layout=self.layout,
            # no_titlebar=True,
            auto_size_buttons=False,
            keep_on_top=True,
            grab_anywhere=True,
            return_keyboard_events=True,
            resizable=True,
            finalize=True,
        )

    def close_window(self):
        self.window.close()
