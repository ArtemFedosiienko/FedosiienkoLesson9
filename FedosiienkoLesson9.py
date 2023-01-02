#Завдання 1
class Car:
    def __init__(self, brand, color, engine_volume):
        self.brand = brand
        self.color = color
        self.engine_volume = engine_volume

    @staticmethod
    def drive_forward():
        print("Їхати вперед")

    @staticmethod
    def drive_backward():
        print("Їхати назад")


class Car2(Car):
    @staticmethod
    def turn_left():
        print("Поворот ліворуч")

    @staticmethod
    def turn_right():
        print("Поворот праворуч")


car = Car2('BMW', 'white', 3.5)
car.turn_left()
car.drive_backward()
car.turn_right()
car.drive_forward()

#Завдання 2
class TextProcessor:
    def __init__(self):
        self._punktuation = '.,!?;:*'

    def __is_punktuation(self, char):
        return char in self._punktuation

    def get_clean_string(self, text):
        clean_text = ""
        for char in text:
            if self.__is_punktuation(char):
                continue
            clean_text += char
        return clean_text


class TextLoader:
    def __init__(self):
        self.__text_processor = TextProcessor()
        self.__clean_string = None

    def set_clean_string(self, text):
        self.__clean_string = self.__text_processor.get_clean_string(text)

    @property
    def clean_string(self):
        print("Clean string is: {}".format(self.__clean_string))
        return self.__clean_string


class DataInterface:
    def __init__(self):
        self.__text_loader = TextLoader()

    def process_texts(self, texts):
        clean_texts = []
        for text in texts:
            self.__text_loader.set_clean_string(text)
            clean = self.__text_loader.clean_string
            clean_texts.append(clean)
        return clean_texts


di = DataInterface()
t = ['Hello, I am Artem *', 'Hey, what is the weather like today ?']
ct = di.process_texts(t)


#Завдання 3
class Parallelogram():
    def __init__(self, l, w):
        self.length = l
        self.width  = w

    def get_area(self):
        return self.length * self.width

parallelogram = Parallelogram(12, 10)
print(parallelogram.get_area())

class Square(Parallelogram):
    def __init__(self, l):
        self.length = l

    def get_area(self):
        return self.length * self.length

square = Square(10)
print(square.get_area())