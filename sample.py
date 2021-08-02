import sys

if sys.version_info[0] >= 3:
    import PySimpleGUI as sg
else:
    import PySimpleGUI27 as sg

import time

"""
 Timer Desktop Widget Creates a floating timer that is always on top of other windows You move it by grabbing anywhere on the window Good example of how to do a non-blocking, polling program using SimpleGUI Can be used to poll hardware when running on a Pi

 While the timer ticks are being generated by PySimpleGUI's "timeout" mechanism, the actual value
  of the timer that is displayed comes from the system timer, time.time().  This guarantees an
  accurate time value is displayed regardless of the accuracy of the PySimpleGUI timer tick. If
  this design were not used, then the time value displayed would slowly drift by the amount of time
  it takes to execute the PySimpleGUI read and update calls (not good!)     

 NOTE - you will get a warning message printed when you exit using exit button.
 It will look something like: invalid command name \"1616802625480StopMove\"
"""


# ----------------  Create Form  ----------------
sg.ChangeLookAndFeel("Black")
sg.SetOptions(element_padding=(0, 0))

layout = [
    [sg.Text("")],
    [
        sg.Text(
            "", size=(8, 2), font=("Helvetica", 20), justification="center", key="text"
        )
    ],
    [
        sg.Button("Pause", key="button", button_color=("white", "#001480")),
        sg.Button("Reset", button_color=("white", "#007339"), key="Reset"),
        sg.Exit(button_color=("white", "firebrick4"), key="Exit"),
    ],
]

window = sg.Window(
    "Running Timer",
    layout,
    no_titlebar=True,
    auto_size_buttons=False,
    keep_on_top=True,
    grab_anywhere=True,
)

# ----------------  main loop  ----------------
current_time = 0
paused = False
start_time = int(round(time.time() * 100))
while True:
    # --------- Read and update window --------
    if not paused:
        event, values = window.read(timeout=10)
        current_time = int(round(time.time() * 100)) - start_time
    else:
        event, values = window.read()
    if event == "button":
        event = window[event].GetText()
    # --------- Do Button Operations --------
    if event == sg.WIN_CLOSED or event == "Exit":  # ALWAYS give a way out of program
        break
    if event == "Reset":
        start_time = int(round(time.time() * 100))
        current_time = 0
        paused_time = start_time
    elif event == "Pause":
        paused = True
        paused_time = int(round(time.time() * 100))
        element = window["button"]
        element.update(text="Run")
    elif event == "Run":
        paused = False
        start_time = start_time + int(round(time.time() * 100)) - paused_time
        element = window["button"]
        element.update(text="Pause")

    # --------- Display timer in window --------
    window["text"].update(
        "{:02d}:{:02d}.{:02d}".format(
            (current_time // 100) // 60, (current_time // 100) % 60, current_time % 100
        )
    )
