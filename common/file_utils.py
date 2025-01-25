
class TxtProcess():
    def __init__(self):
        pass

    def get_lines(self, path):
        with open(path, 'r') as f:
            lines = []
            for line in f:
                lines.append(line)
            return lines


