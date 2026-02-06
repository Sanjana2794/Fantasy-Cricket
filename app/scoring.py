def batting_points(runs, balls, fours, sixes):
    points = runs // 2

    if runs >= 50:
        points += 5
    if runs >= 100:
        points += 10

    strike_rate = (runs / balls) * 100 if balls > 0 else 0
    if 80 <= strike_rate <= 100:
        points += 2
    elif strike_rate > 100:
        points += 4

    points += fours * 1 + sixes * 2
    return points


def bowling_points(wkts, runs_given, overs):
    points = wkts * 10

    if wkts >= 3:
        points += 5
    if wkts >= 5:
        points += 10

    economy = runs_given / overs if overs > 0 else 0
    if 3.5 <= economy <= 4.5:
        points += 4
    elif 2 <= economy < 3.5:
        points += 7
    elif economy < 2:
        points += 10

    return points


def fielding_points(catches, stumpings, runouts):
    return (catches + stumpings + runouts) * 10
