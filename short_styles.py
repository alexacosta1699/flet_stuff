"""Python Dictionary hack in Flet"""

import flet as ft

# alternative and much better way of setting styling properties is returning a 
# dictionay containing the styling properties
def box_style() -> dict:
    return{
        "width":100,
        "height":100,
        "bgcolor":"teal",
        "border_radius":6,
    }

def logic_box_style(theme: ft.Page.theme_mode) -> dict:
    return {
        "width":100,
        "height":100,
        "bgcolor":"teal" if theme == "dark" else "pink",
        "border_radius":6, 
    }

def main(page: ft.Page):
    page.horizontal_alignment = "center"
    page.vertical_alignment = "center"
    page.theme_mode = "light"
    # page.theme_mode = "dark"

    # typical control flow
    # styling properties can get long - making the code un-readable
    page.add(
        ft.Container(
            width=100, 
            height=100, 
            bgcolor="teal", 
            border_radius=6
            )
        )
    # you can un-pack the dict's properties directly into the container call
    page.add(
        ft.Container(**box_style())
    )

    # an additional benefit is performing logic on the style - see the logic_box_style function
    # we will use the page theme L/D mode to show this
    page.add(
        ft.Container(**logic_box_style(page.theme_mode))
    )
    page.update()

if __name__ == "__main__":
    ft.app(target=main)