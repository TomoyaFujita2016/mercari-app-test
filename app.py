import time
from queue import Queue
from threading import Thread

import PySimpleGUI as sg
from mercari import Mercari

from interface import InterFace

FETCH_INTERVAL = 2
mercari_api = Mercari()
interface = InterFace()


def fetch_items(keyword=None, max_price=None, min_price=None):
    interface.window["-MULTI LOG-"].print("[*]Getting items...")
    interface.window["-MULTI LOG-"].print(f"{keyword}, {min_price}~{max_price}")
    urls = mercari_api.fetch_all_items(
        keyword=keyword, price_min=min_price, price_max=max_price
    )
    items = [[i + 1, url] for i, url in enumerate(urls[:100])]
    interface.window["-TABLE-"].update(values=items)
    interface.window["-MULTI LOG-"].print("[*]Done!")


def update_kwards(values=None):
    if values is None:
        return {
            "keyword": "",
            "max_price": 30000,
            "min_price": 10000,
        }
    return {
        "keyword": values["-KEYWORD-"],
        "max_price": values["-PRICE MAX-"],
        "min_price": values["-PRICE MIN-"],
    }


def main():
    paused = True
    thread = None
    ts = time.time()
    form_data = update_kwards()
    interface.show_window()
    while True:
        event, values = interface.window.read(timeout=10)
        if not event == "__TIMEOUT__":
            print(event, values)
        if event == "-RUN/PAUSE-":
            event = interface.window[event].GetText()

        if event == sg.WIN_CLOSED:
            break
        elif event == "-BTN UPDATE-":
            form_data = update_kwards(values=values)
            interface.window["-MULTI LOG-"].print(f"[*]Data is updated!: {form_data}")
        elif event == "Run":
            paused = False
            element = interface.window["-RUN/PAUSE-"]
            element.update(text="Pause")
        elif event == "Pause":
            paused = True
            element = interface.window["-RUN/PAUSE-"]
            element.update(text="Run")
        # ---------------

        # fetch items-----
        if paused:
            continue
        if time.time() - ts < FETCH_INTERVAL:
            continue
        if thread is not None and thread.is_alive():
            continue
        thread = Thread(target=fetch_items, kwargs=form_data)
        thread.start()
        ts = time.time()
        # ---------------


if __name__ == "__main__":
    main()
