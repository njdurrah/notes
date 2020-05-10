class Skyline:
    def __init__(self):
        self.grid = []
        self.front = []
        self.side = []
        self.rows = 0
        self.cols = 0

    def get_skyline(self):
        file = input("Text filename: ")
        temp = ''
        with open(file, 'r') as f:
            temp = f.read()
        for char in temp:
            if char == '[':
                newline = []
            if char.isdigit():
                newline.append(int(char))
            if char == ']':
                self.grid.append(newline)

        print(self.grid)

    def get_peaks(self):
        self.front = [max(i) for i in self.grid]
        self.side = [max(i) for i in zip(*self.grid)]
        self.rows = len(self.front)
        self.cols = len(self.side)

if __name__ == '__main__':
    skyline = Skyline()
    skyline.get_skyline()
    print("Got skyline")
    print(skyline.grid)
    skyline.get_peaks()
    print(skyline.front)
    print(skyline.side)

    def maxincrease():
        incr = 0
        for i in range(skyline.rows):
            for j in range(skyline.cols):
                incr += min(skyline.front[i], skyline.side[j]) - skyline.grid[i][j]

        return incr

    print ("Can increase by " + str(maxincrease()))
