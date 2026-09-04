from nicegui import ui


def update() -> None:
    """Runs every time a switch changes. Same logic as the original if/else,
    but the result goes into a label instead of print()."""
    if has_username.value and accepted_rules.value and not is_blocked.value:
        message.text = 'You are authorized! Access will commence'
    else:
        message.text = 'You do not qualify to access the game'


ui.label('Kontroll av tilgang til GTA7').classes('text-xl font-bold')

# Each switch replaces one boolean variable. ON == True
with ui.row():
    has_username = ui.switch('Has username', value=True, on_change=update)
    accepted_rules = ui.switch('Accepted rules', value=True, on_change=update)
    is_blocked = ui.switch('Is blocked', value=False, on_change=update)

message = ui.label()
update()  # show the correct text before the user touches anything

ui.run()
