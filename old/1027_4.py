class SaruInu:
    def __init__(self, character):
        self.character = character

    def ans(self):
        if self.character == "saru":
            return "No"
        return "Yes"
s = input()
test_001 = SaruInu(s)
print(test_001.ans())