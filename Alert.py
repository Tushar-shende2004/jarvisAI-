import os
from winotify import Notification, audio
from os import getcwd

def Alert(Text):
    icon_path = r"D:\J.A.R.V.I.S-main\J.A.R.V.I.S-main\generated_image.png"
    toast = Notification(
        app_id="🟢 J.A.R.V.I.S.",
        title=Text,
        duration="long",
        icon=icon_path
    )

    toast.set_audio(audio.Default, loop=False)


    toast.add_actions(label="Click me", launch="https://www.google.com")
    toast.add_actions(label="Dismiss", launch="https://www.google.com")


    toast.show()

