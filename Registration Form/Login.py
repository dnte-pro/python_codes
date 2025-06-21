import kivy
import re
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button  # You need this for the submit button
from kivy.uix.popup import Popup

class RegistrationApp(App):
    def build(self):

        self.title = "Registration Form"
        layout = BoxLayout(orientation='vertical', padding=30, spacing=10)

        # Adding labels
        head_label = Label(text="Python User Registration App", font_size=26, bold=True, size_hint=(1, None), height=40)

        name_label = Label(text="Name", font_size=18)
        self.name_input = TextInput(multiline=False, font_size=18)

        email_label = Label(text="Email", font_size=18)
        self.email_input = TextInput(multiline=False, font_size=18)

        password_label = Label(text="Password", font_size=18)
        self.password_input = TextInput(password=True, multiline=False, font_size=18)  # Fixed multilineFalse → multiline

        confirm_label = Label(text="Confirm Password", font_size=18)
        self.confirm_input = TextInput(password=True, multiline=False, font_size=18) 

        submit_button = Button(text="Register", font_size=18, on_press=self.register)  # You forgot to define this

        layout.add_widget(head_label)
        layout.add_widget(name_label)
        layout.add_widget(self.name_input)
        layout.add_widget(email_label)
        layout.add_widget(self.email_input)
        layout.add_widget(password_label)
        layout.add_widget(self.password_input)
        layout.add_widget(confirm_label)
        layout.add_widget(self.confirm_input)
        layout.add_widget(submit_button)

        return layout
    
    def register(self, instance):
        name = self.name_input.text
        email = self.email_input.text
        password = self.password_input.text
        confirm_password = self.confirm_input.text
        
        
        # Validating inputs
        if not name.strip() or not email.strip() or not password.strip() or not confirm_password.strip():
            message = "Please fill in all fields."
        elif len(set(name.lower())) == 1:
            message = "Name must not contain the same repeated letters."

        elif len(name) < 4:
            message = "Name must be at least 4 characters long."
        elif not name.isalpha():
            message = "Name must contain only letters."
        elif password != confirm_password:
            message = "Passwords do not match."
        elif len(password) < 8:
            message = "Password must be at least 8 characters long."
        elif not re.match(r"[^@]+@[^@]+\.[^@]+", email):
             message = "Please enter a valid email address."

        else:
            filename = name + ".txt"
            with open(filename, 'w') as file:
                file.write("Name:{}\n".format(name))
                file.write('Email: {}\n'.format(email))
                file.write('Password: {}\n'.format(password))
            message = "Registration successful! Your details have been saved.\nName: {}\nEmail: {}".format(name, email)  # Displaying the message   
         
                

        # Displaying a popup message
        popup = Popup(title='Registration Status',
                      content=Label(text=message),
                      size_hint=(None,None),
                      size=(400, 200))
        popup.open()

if __name__ == '__main__':
    RegistrationApp().run()
