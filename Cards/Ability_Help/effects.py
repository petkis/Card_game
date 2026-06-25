def gain_gold(amount):
    return lambda player, opponent: player.gain_gold(amount)


def deal_damage(amount):
    return lambda player, opponent: opponent.take_damage(amount)


def heal(amount):
    return lambda player, opponent: player.heal(amount)