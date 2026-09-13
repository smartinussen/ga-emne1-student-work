# Gjenta en melding

def repeat_message(message: str, repetitions: float = 3):
    for rept in range(repetitions):
        print(message)

repeat_message("Test")
repeat_message("Test", 5)