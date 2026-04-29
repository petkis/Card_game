from Cards.Items import Item
from Cards.Type import OptionType


class DummyPlayer:
    def __init__(self):
        self.hp = 10
        self.gold = 0
        self.drawn = 0

    def take_damage(self, x):
        self.hp -= x

    def heal(self, x):
        self.hp += x

    def gain_gold(self, x):
        self.gold += x

    def draw_card(self, x):
        self.drawn += x


def test_item_damage():
    item = Item("dmg", 0, OptionType.Damage, 3)
    p1, p2 = DummyPlayer(), DummyPlayer()

    item.apply(p1, p2)

    assert p2.hp == 7


def test_item_heal():
    item = Item("heal", 0, OptionType.Heal, 5)
    p1, p2 = DummyPlayer(), DummyPlayer()

    item.apply(p1, p2)

    assert p1.hp == 15


def test_item_gold():
    item = Item("gold", 0, OptionType.Money, 10)
    p1, p2 = DummyPlayer(), DummyPlayer()

    item.apply(p1, p2)

    assert p1.gold == 10