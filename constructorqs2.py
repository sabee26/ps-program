class student:
    def __init__(self):
        self.name=""
        self.regno=""
    def display(self):
        print("name of the student: ", self.name)
        print("regno of the student: ", self.regno)
computerscience=student()
mechanical=student()
computerscience.name="sabeena"
computerscience.regno="cs-001"
mechanical.name="pavitharan"
mechanical.regno="ME-001"

mechanical.display()
computerscience.display()