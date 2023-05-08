from PIL import Image
from pytesseract import pytesseract
import copy


def convert_img_to_text(image_path=r"20230508_125929.jpg"):
    path_to_tesseract = r"C:\Users\Max\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

    img = Image.open(image_path)

    pytesseract.tesseract_cmd = path_to_tesseract

    text = pytesseract.image_to_string(img)

    return text[:-1]


class Student:

    def __init__(self, first_name, last_name, klasse):
        self.first_name = first_name
        self.last_name = last_name
        self.klasse = klasse
        self.send_to_database()

    def send_to_database(self):
        with open("database.txt", "a") as db:
            db.write(f"{self.first_name} {self.last_name} | {self.klasse}\n")


class Page:

    def __init__(self, image_path):

        big_characters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        self.image_path = image_path
        raw_text:str = self.convert_img_to_text(image_path)

        #print(raw_text.split("\n\n"))

        self.klasse = raw_text.split("\n\n")[0].split(" ")[1]

        students = raw_text.split("\n\n")[1].replace("\n", "").split(",")
        for stdCount, std in enumerate(students):
            std = std.replace(" ", "")
            std = list(std)
            insert_counter = 0
            std_copy = copy.copy(std)
            for count, character in enumerate(std):
                if character in big_characters:
                    std_copy.insert(count + insert_counter, " ")
                    insert_counter = insert_counter + 1

            std = std_copy
            std = "".join(std)

            std = std.removeprefix(" ")
            first_name = std.split(" ")[1]
            last_name = std.split(" ")[0]

            students[stdCount] = f"{first_name} {last_name}"

        self.students = students
        print(self.students)
        self.send_to_database()

    def send_to_database(self):
        for rawStudent in self.students:
            student = Student(rawStudent.split(" ")[0], rawStudent.split(" ")[1], self.klasse)

    def convert_img_to_text(self, image_path=r"20230508_125929.jpg"):
        path_to_tesseract = r"C:\Users\Max\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

        img = Image.open(image_path)

        pytesseract.tesseract_cmd = path_to_tesseract

        text = pytesseract.image_to_string(img)

        return text[:-1]

page = Page("20230508_125929.jpg")

