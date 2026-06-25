def always(player, opponent):
    return True

def health_over_X(amount):
    return lambda player, opponent: player.hp > amount

def health_under_X(amount):
    return lambda player, opponent: player.hp < amount

def opponent_health_under_X(amount):
    return lambda player, opponent: opponent.hp < amount

def opponent_less_healt():
    return lambda player, opponent: opponent.hp < player.hp

def opponent_NOT_less_healt():
    return lambda player, opponent: opponent.hp >= player.hp