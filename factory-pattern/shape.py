from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

class Rectangle(Shape):
    def draw(self):
        print("2(l+b)")

class Circle(Shape):
    def draw(self):
        print("2πr")

class ShapeFactory:
    @staticmethod
    def get_shape(shape_type: str) -> Shape:
        if shape_type == "rectangle":
            return Rectangle()
        elif shape_type == "circle":
            return Circle()
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")

def main():
    shape = ShapeFactory.get_shape("circle")
    shape.draw()

if __name__ == "__main__":
    main()
