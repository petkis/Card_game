from Cards.Items import Item
from Cards.Type import OptionType


class DummyPlayer:
    def __init__(self):
        self.hp = 10
        self.gold = 0
        self.drawn_items = 0

    def take_damage(self, amount):
        self.hp -= amount

    def heal(self, amount):
        self.hp += amount

    def gain_gold(self, amount):
        self.gold += amount

    def draw_items(self, amount):
        self.drawn_items += amount


def test_item_damage():
    item = Item("Deal 3 damage", 0, OptionType.Damage, 3)
    player = DummyPlayer()
    opponent = DummyPlayer()

    item.apply(player, opponent)

    assert opponent.hp == 7
    assert player.hp == 10


def test_item_heal():
    item = Item("Heal 5", 0, OptionType.Heal, 5)
    player = DummyPlayer()
    opponent = DummyPlayer()

    item.apply(player, opponent)

    assert player.hp == 15
    assert opponent.hp == 10


def test_item_gold():
    item = Item("Gain 10 gold", 0, OptionType.Money, 10)
    player = DummyPlayer()
    opponent = DummyPlayer()

    item.apply(player, opponent)

    assert player.gold == 10
    assert opponent.gold == 0


def test_item_draw():
    item = Item("Draw 2 items", 0, OptionType.Draw, 2)
    player = DummyPlayer()
    opponent = DummyPlayer()

    item.apply(player, opponent)

    assert player.drawn_items == 2
    assert opponent.drawn_items == 0