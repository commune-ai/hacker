
class LeonardoMachine:
    def __init__(self):
        self.golden_ratio = 1.618033988749895

    def calculate_proportion(self, dimension):
        return dimension * self.golden_ratio

    def design_masterpiece(self, base_dimension):
        height = self.calculate_proportion(base_dimension)
        return f"A masterpiece of {base_dimension} x {height:.2f}"

if __name__ == "__main__":
    machine = LeonardoMachine()
    print(machine.design_masterpiece(10))
