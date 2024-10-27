class Campaign:
    def __init__(self, yen):
        self.yen = yen

    def discount(self):
        if self.yen >= 1000:
            return self.yen - 100
        return self.yen

n = int(input())

campaign = Campaign(n)
print(campaign.discount())