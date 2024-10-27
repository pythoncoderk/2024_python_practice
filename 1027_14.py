class Pass:
    def __init__(self, password):
        self.password = password
    
    def ans(self):
        if self.password == "paiza":
            return "Yes"
        return "No"
s = input()
password = Pass(s)
print(password.ans())