import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MyGridLayout(GridLayout):
    #Initialize infinite keywords
    def __init__(self, **kwargs):
        # Call grid layout constructor
        super(MyGridLayout, self).__init__(**kwargs)
        
        #Set columns
        self.cols = 2
        
        # Add widgets
        self.add_widget(Label(text='Name'))
        # Add Input Box
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        
        # Add widgets
        self.add_widget(Label(text='Favourite Colour:'))
        # Add Input Box
        self.colour = TextInput(multiline=False)
        self.add_widget(self.colour)
        
        # Add widgets
        self.add_widget(Label(text='Favourite Animal:'))
        # Add Input Box
        self.animal = TextInput(multiline=False)
        self.add_widget(self.animal)
        
        # Create a Submit Button
        self.submit = Button(text='Submit', font_size=32)
        #Bind the button
        self.submit.bind(on_press=self.press)
        self.add_widget(self.submit)
    
    def press(self, instance):
        name = self.name.text
        colour = self.colour.text
        animal = self.animal.text
        
        # print(f'Hello {name}, your best colour is {colour}, and the animal you like the most is {animal}')
        # Print it on screen
        self.add_widget(Label(text=f'Hello {name}, your best colour is {colour}, and the animal you like the most is {animal}'))
        
        # Clear the input boxes
        self.name.text = ""
        self.colour.text = ""
        self.animal.text = ""
        
class MyApp(App):
    def build(self):
        return MyGridLayout()
    
if __name__ == "__main__":
    MyApp().run()