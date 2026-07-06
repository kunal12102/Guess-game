from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
import random

Window.clearcolor = (0.08, 0.08, 0.12, 1)


class GuessGame(BoxLayout):

    def __init__(self, **kwargs):
        super().__init__(
            orientation="vertical",
            spacing=20,
            padding=30,
            **kwargs
        )

        self.secret = random.randint(1, 10)
        self.score = 0

        self.title = Label(
            text="🎮 Guess The Number",
            font_size=34,
            bold=True,
            size_hint=(1, .2)
        )

        self.add_widget(self.title)

        self.score_label = Label(
            text="⭐ Score : 0",
            font_size=22,
            size_hint=(1, .1)
        )

        self.add_widget(self.score_label)

        self.entry = TextInput(
            hint_text="Enter a number (1-10)",
            multiline=False,
            input_filter="int",
            halign="center",
            font_size=26,
            size_hint=(1, .15),
            background_color=(0.15, 0.15, 0.2, 1),
            foreground_color=(1, 1, 1, 1),
            cursor_color=(1, 1, 1, 1)
        )

        self.add_widget(self.entry)

        self.button = Button(
            text="GUESS",
            font_size=24,
            bold=True,
            size_hint=(1, .15),
            background_normal="",
            background_color=(0.2, 0.6, 1, 1)
        )

        self.button.bind(on_press=self.check)
        self.add_widget(self.button)

        self.result = Label(
            text="Good Luck! 🍀",
            font_size=24,
            size_hint=(1, .3)
        )

        self.add_widget(self.result)

    def check(self, instance):

        if self.entry.text == "":
            self.result.text = "⚠ Enter a number!"
            return

        guess = int(self.entry.text)

        if guess == self.secret:
            self.score += 1
            self.result.text = "🎉 Correct!"
        else:
            self.result.text = f"❌ Wrong!\nNumber was {self.secret}"

        self.score_label.text = f"⭐ Score : {self.score}"

        self.secret = random.randint(1, 10)
        self.entry.text = ""


class GuessApp(App):

    def build(self):
        self.title = "Guess Game"
        return GuessGame()


GuessApp().run()