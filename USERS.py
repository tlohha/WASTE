from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class WasteManagementApp(App):
    def build(self):
        # Main layout
        layout = BoxLayout(orientation='vertical', padding=10, spacing=10)

        # User ID input
        self.user_id_input = TextInput(hint_text="Enter User ID", multiline=False)
        layout.add_widget(Label(text="User ID:"))
        layout.add_widget(self.user_id_input)

        # Waste type input
        self.waste_type_input = TextInput(hint_text="Enter Waste Type", multiline=False)
        layout.add_widget(Label(text="Waste Type:"))
        layout.add_widget(self.waste_type_input)

        # Submit button
        submit_button = Button(text="Submit Request", size_hint=(1, 0.5))
        submit_button.bind(on_press=self.submit_request)
        layout.add_widget(submit_button)

        # Message label
        self.message_label = Label(text="", color=(1, 0, 0, 1))
        layout.add_widget(self.message_label)

        return layout

    def submit_request(self, instance):
        # Get inputs
        user_id = self.user_id_input.text.strip()
        waste_type = self.waste_type_input.text.strip()

        if user_id and waste_type:
            # Display success message
            self.message_label.text = f"Request submitted: {waste_type} by User {user_id}."
            self.message_label.color = (0, 1, 0, 1)  # Green
        else:
            # Display error message
            self.message_label.text = "Error: Please fill all fields."
            self.message_label.color = (1, 0, 0, 1)  # Red


# Run the app
if __name__ == "__main__":
    WasteManagementApp().run()
