import reverse


class TestReverse:
    def test_reversed(self):
        assert reverse.reverse("My name is V Tadimeti") == "Tadimeti V is name My"
