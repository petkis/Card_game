from Cards.Characters import Character


def test_character_applies_one_ability():
    calls = []

    def ability(player, opponent):
        calls.append("ability")

    character = Character("Test character", [ability])

    character.apply(None, None)

    assert calls == ["ability"]


def test_character_applies_all_abilities_in_order():
    calls = []

    def ability1(player, opponent):
        calls.append("a1")

    def ability2(player, opponent):
        calls.append("a2")

    character = Character("Test character", [ability1, ability2])

    character.apply(None, None)

    assert calls == ["a1", "a2"]


def test_character_ability_can_affect_player():
    class DummyPlayer:
        def __init__(self):
            self.gold = 0

        def gain_gold(self, amount):
            self.gold += amount

    player = DummyPlayer()
    opponent = DummyPlayer()

    character = Character(
        "Gain gold",
        [
            lambda p, o: p.gain_gold(3)
        ]
    )

    character.apply(player, opponent)

    assert player.gold == 3
    assert opponent.gold == 0


def test_character_ability_can_affect_opponent():
    class DummyPlayer:
        def __init__(self):
            self.hp = 10

        def take_damage(self, amount):
            self.hp -= amount

    player = DummyPlayer()
    opponent = DummyPlayer()

    character = Character(
        "Deal damage",
        [
            lambda p, o: o.take_damage(4)
        ]
    )

    character.apply(player, opponent)

    assert opponent.hp == 6
    assert player.hp == 10