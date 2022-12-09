from tkinter import *
import area
import perimeter


class GUI:
    def __init__(self, window):
        self.window = window
        
        self.frame_shape = Frame(self.window)
        self.label_shape = Label(self.frame_shape, text='Shape\t')
        self.radio_1 = IntVar()
        self.radio_1.set(0)
        self.radio_circle = Radiobutton(self.frame_shape, text='Circle', variable=self.radio_1, value=1)
        self.radio_rectangle = Radiobutton(self.frame_shape, text='Rectangle', variable=self.radio_1, value=2)
        self.radio_square = Radiobutton(self.frame_shape, text='Square', variable=self.radio_1, value=3)
        self.radio_triangle = Radiobutton(self.frame_shape, text='Triangle', variable=self.radio_1, value=4)
        self.label_shape.pack(side='left', padx=5)
        self.radio_circle.pack(side='left')
        self.radio_rectangle.pack(side='left')
        self.radio_square.pack(side='left')
        self.radio_triangle.pack(side='left')
        self.frame_shape.pack(anchor='w', pady=10)
        
        self.frame_operation = Frame(self.window)
        self.label_operation = Label(self.frame_operation, text='Operation\t')
        self.radio_2 = IntVar()
        self.radio_2.set(0)
        self.radio_perimeter = Radiobutton(self.frame_operation, text='Perimeter', variable=self.radio_2, value=1)
        self.radio_area = Radiobutton(self.frame_operation, text='Area', variable=self.radio_2, value=2)
        self.label_operation.pack(side='left', padx=5)
        self.radio_perimeter.pack(side='left')
        self.radio_area.pack(side='left')
        self.frame_operation.pack(anchor='w', pady=10)

        self.frame_first = Frame(self.window)
        self.label_first = Label(self.frame_first, text='First number')
        self.entry_first = Entry(self.frame_first, width=40)
        self.label_first.pack(padx=5, side='left')
        self.entry_first.pack(padx=30, side='left')
        self.frame_first.pack(anchor='w', pady=10)

        self.frame_second = Frame(self.window)
        self.label_second = Label(self.frame_second, text='Second number')
        self.entry_second = Entry(self.frame_second, width=40)
        self.label_second.pack(padx=5, side='left')
        self.entry_second.pack(padx=15, side='left')
        self.frame_second.pack(anchor='w', pady=10)
        
        self.frame_third = Frame(self.window)
        self.label_third = Label(self.frame_third, text='Third number')
        self.entry_third = Entry(self.frame_third, width=40)
        self.label_third.pack(padx=5, side='left')
        self.entry_third.pack(padx=15, side='left')
        self.frame_third.pack(anchor='w', pady=10)


        self.frame_result = Frame(self.window)
        self.label_result = Label(self.frame_result)
        self.label_result.pack(pady=10)
        self.frame_result.pack()

        self.frame_button = Frame(self.window)
        self.button_compute = Button(self.frame_button, text='COMPUTE', command=self.compute)
        self.button_compute.pack(pady=10)
        self.frame_button.pack()

    def compute(self):
        try:
            first_num = self.entry_first.get()
            second_num = self.entry_second.get()
            third_num = self.entry_third.get()
            shape = self.radio_1.get()
            operation = self.radio_2.get()

            if operation == 1:
                if shape == 1:
                    self.label_result.config(text=f'Equation is 2 *{first_num} * pi. Perimeter of the circle = {perimeter.circle(first_num)}')
                elif shape == 2:
                    self.label_result.config(text=f'Equation is 2 * {first_num} + 2 * {second_num}. Perimeter of the rectangle = {perimeter.rectangle(first_num, second_num)}')
                elif shape == 3:
                    self.label_result.config(text=f'Equation is 4 * {first_num}. Perimeter of the square = {perimeter.square(first_num)}')
                elif shape == 4:
                    self.label_result.config(text=f'Equation is {first_num} + {second_num} + {third_num}. Perimeter of the triangle = {perimeter.triangle(first_num, second_num, third_num)}')
                  
            elif operation == 2:
                if shape == 1:
                    self.label_result.config(text=f'Equation is ({first_num} * {first_num}) * pi. Area of the circle = {area.circle(first_num):.2f}')
                elif shape == 2:
                    self.label_result.config(text=f'Equation is {first_num} * {second_num}. Area of the square = {area.rectangle(first_num, second_num):.2f}')
                elif shape == 3:
                    self.label_result.config(text=f'Equation is {first_num} * {first_num}. Area of the square = {area.square(first_num):.2f}')
                elif shape == 4:
                    self.label_result.config(text=f'Equation is 1/2 * {first_num} * {second_num}. Area of the triangle = {area.triangle(first_num, second_num):.2f}')
                  
        except ValueError:
            self.label_result.config(text='Enter numeric values')
        except ZeroDivisionError:
            self.label_result.config(text='Cannot divide by 0 (change second number value)')
        except:
            self.label_result.config(text='Error occurred! Check input values')
