# Base class: Animal
class Animal:
    def move(self):
        raise NotImplementedError("Subclass must implement abstract method")

# Subclass: Fish
class Fish(Animal):
    def move(self):
        return "Swimming 🐟"

# Subclass: Bird
class Bird(Animal):
    def move(self):
        return "Flying 🦅"

# Subclass: Snake
class Snake(Animal):
    def move(self):
        return "Slithering 🐍"

# Testing polymorphism
def demonstrate_movement(animal):
    print(animal.move())

if __name__ == "__main__":
    fish = Fish()
    bird = Bird()
    snake = Snake()

    animals = [fish, bird, snake]
    for animal in animals:
        demonstrate_movement(animal)
