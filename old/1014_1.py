class Rain:
    def __init__(self):
        self.n = None

    def loops(self, n):
        self.n = n
        l = [input() for _ in range(n)]
        if l.count("Rain") >= 4:
            return "Yes"
        return "No"

rain = Rain()
print(rain.loops(7))

