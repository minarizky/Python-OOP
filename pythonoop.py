class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""

    def __init__(self, start=0):
        """Create a new generator, starting at start."""
        self.start = self.next = start

    def generate(self):
        """Return the next serial number."""
        self.next += 1
        return self.next - 1

    def reset(self):
        """Reset the generator back to the original start number."""
        self.next = self.start

    def __repr__(self):
        """Provide a useful representation when printing this object."""
        return f"<SerialGenerator start={self.start} next={self.next}>"

import random

class WordFinder:
    """Machine for finding random words from a dictionary."""

    def __init__(self, path):
        """Read dictionary and reports number of items read."""
        self.words = self.read_file(path)
        print(f"{len(self.words)} words read")

    def read_file(self, path):
        """Read words from the file and return a list of words."""
        with open(path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

import random

class WordFinder:
    """Machine for finding random words from a dictionary."""

    def __init__(self, path):
        """Read dictionary and reports number of items read."""
        self.words = self.read_file(path)
        print(f"{len(self.words)} words read")

    def read_file(self, path):
        """Read words from the file and return a list of words."""
        with open(path, 'r') as file:
            return [line.strip() for line in file if line.strip()]

    def random(self):
        """Return a random word from the list of words."""
        return random.choice(self.words)

class SpecialWordFinder(WordFinder):
    """Specialized WordFinder that excludes blank lines and comments."""

    def read_file(self, path):
        """Read words from the file, ignoring blanks and comments."""
        with open(path, 'r') as file:
            return [line.strip() for line in file if line.strip() and not line.startswith('#')]

if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # Test SerialGenerator
    serial = SerialGenerator(start=100)
    print(serial.generate())  # 100
    print(serial.generate())  # 101
    print(serial.generate())  # 102
    serial.reset()
    print(serial.generate())  # 100
    print(serial)  # <SerialGenerator start=100 next=101>

    # Test WordFinder
    wf = WordFinder("words.txt")
    print(wf.random())
    print(wf.random())

    # Test SpecialWordFinder
    swf = SpecialWordFinder("special_words.txt")
    print(swf.random())
    print(swf.random())
