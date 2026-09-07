# Regn ut gjennomsnitt


def show_average(score_1: int, score_2: int) -> None:
    average: float = (score_1 + score_2) / 2
    print(f"Gjennomsnittet for {score_1} og {score_2} er {average:.1f}")


show_average(10.45, 45)
show_average(0, 10)
show_average(0, 10)
