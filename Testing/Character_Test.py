from Cards.Characters import Character


def test_character_applies_all_abilities():
    calls = []

    def ability1(p, o):
        calls.append("a1")

    def ability2(p, o):
        calls.append("a2")

    char = Character("test", [ability1, ability2])
    char.apply(None, None)

    assert calls == ["a1", "a2"]