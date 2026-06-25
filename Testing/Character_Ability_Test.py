import pytest

from Cards.Ability import Ability
from Cards.Characters import Character


class FakePlayer:
    def __init__(self):
        self.hp = 30
        self.gold = 0
        self.damage_taken = 0

    def gain_gold(self, amount):
        self.gold += amount

    def take_damage(self, amount):
        self.hp -= amount
        self.damage_taken += amount

    def heal(self, amount):
        self.hp += amount


def test_ability_runs_when_condition_is_true():
    player = FakePlayer()
    opponent = FakePlayer()

    ability = Ability(
        condition=lambda player, opponent: True,
        ability=lambda player, opponent: player.gain_gold(2)
    )

    ability.use_ability(player, opponent)

    assert player.gold == 2


def test_ability_does_not_run_when_condition_is_false():
    player = FakePlayer()
    opponent = FakePlayer()

    ability = Ability(
        condition=lambda player, opponent: False,
        ability=lambda player, opponent: player.gain_gold(2)
    )

    ability.use_ability(player, opponent)

    assert player.gold == 0


def test_ability_can_affect_opponent():
    player = FakePlayer()
    opponent = FakePlayer()

    ability = Ability(
        condition=lambda player, opponent: True,
        ability=lambda player, opponent: opponent.take_damage(3)
    )

    ability.use_ability(player, opponent)

    assert opponent.hp == 27
    assert opponent.damage_taken == 3


def test_ability_condition_can_check_player_health():
    player = FakePlayer()
    opponent = FakePlayer()
    player.hp = 10

    ability = Ability(
        condition=lambda player, opponent: player.hp <= 10,
        ability=lambda player, opponent: player.heal(5)
    )

    ability.use_ability(player, opponent)

    assert player.hp == 15


def test_character_apply_uses_single_ability():
    player = FakePlayer()
    opponent = FakePlayer()

    character = Character(
        description="Merchant: Gain 2 gold",
        cost=0,
        abilities=[
            Ability(
                condition=lambda player, opponent: True,
                ability=lambda player, opponent: player.gain_gold(2)
            )
        ]
    )

    character.apply(player, opponent)

    assert player.gold == 2


def test_character_apply_uses_multiple_abilities():
    player = FakePlayer()
    opponent = FakePlayer()

    character = Character(
        description="Battle Priest: Gain 1 gold and heal 3 hp",
        cost=3,
        abilities=[
            Ability(
                condition=lambda player, opponent: True,
                ability=lambda player, opponent: player.gain_gold(1)
            ),
            Ability(
                condition=lambda player, opponent: True,
                ability=lambda player, opponent: player.heal(3)
            )
        ]
    )

    character.apply(player, opponent)

    assert player.gold == 1
    assert player.hp == 33


def test_character_does_not_apply_ability_if_condition_is_false():
    player = FakePlayer()
    opponent = FakePlayer()

    character = Character(
        description="Weak Merchant: Gain 2 gold only if hp below 10",
        cost=0,
        abilities=[
            Ability(
                condition=lambda player, opponent: player.hp < 10,
                ability=lambda player, opponent: player.gain_gold(2)
            )
        ]
    )

    character.apply(player, opponent)

    assert player.gold == 0


def test_character_str_returns_description():
    character = Character(
        description="Soldier: Deal 3 damage",
        cost=0,
        abilities=[]
    )

    assert str(character) == "Soldier: Deal 3 damage"


def test_character_stores_cost():
    character = Character(
        description="Knight: Deal 4 damage",
        cost=4,
        abilities=[]
    )

    assert character.cost == 4