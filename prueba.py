from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    md_bg_color: self.theme_cls

    MDFlatButton:
        style: "elevated"
        pos_hint: {"center_x": .5, "center_y": .5}

        MDIconButton:
            icon: "plus"

        MDTextButton:
            text: "Button"
'''


class Example(MDApp):
    def build(self):
        self.theme_cls.theme_style = "Dark"
        self.theme_cls.primary_palette = "Pink"  # "Purple", "Red"
        return Builder.load_string(KV)


Example().run()
