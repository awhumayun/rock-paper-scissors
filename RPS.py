# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

def player(previous_play, opponent_history=[], play_statistics={}):
    opponent_history.append(previous_play if previous_play else 'R')
    
    guess = 'P'

    if len(opponent_history) > 4:
        last_five_plays = "".join(opponent_history[-5:])
        play_statistics[last_five_plays] = play_statistics.get(last_five_plays, 0) + 1      
        potential_plays = ["".join(opponent_history[-4:] + [v]) for v in ['R', 'P', 'S']]

        if sub_statistics := {key: play_statistics.get(key, 0) for key in potential_plays if key in play_statistics}:
            guess = max(sub_statistics, key=sub_statistics.get)[-1]

    return {'P': 'S', 'R': 'P', 'S': 'R'}.get(guess, 'R')
