from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class MainApp(App):
    # App initialization and widget setup
    def build(self):
        self.icon = "calculator.png"
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None

        # Main vertical layout
        main_layout = BoxLayout(orientation = "vertical")

        # Display input/output field
        self.solution = TextInput(background_color = "black", foreground_color = "white",
                                  multiline=False, halign="right", font_size=55, readonly=True)

        # Add solution field to layout
        main_layout.add_widget(self.solution)
        # Define button layout
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "+"],
            [".", "0", "C", "-"],
        ]

        # Create and add number/operator buttons
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text = label, font_size=30, background_color="grey",
                    pos_hint = {"center_x": 0.5, "center_y": 0.5}
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)

            main_layout.add_widget(h_layout)

        # Create equals button
        equal_button = Button(
            text = "=", font_size=30, background_color="grey",
            pos_hint = {"center_x": 0.5, "center_y": 0.5}
        )
        equal_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equal_button)

        return main_layout

    # Handle button presses (numbers, operators, C)
    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            self.solution.text = ""
        else:
            # Prevent multiple operators in a row
            if current and (self.last_was_operator and button_text in self.operators):
                return
            # Prevent starting with an operator
            elif current == "" and button_text in self.operators:
                return
            else:
                # Append button text
                new_text = current + button_text
                self.solution.text = new_text

        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    # Calculate the solution when '=' is pressed
    def on_solution(self, instance):
        text = self.solution.text

        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution


if __name__ == "__main__":
    app = MainApp()
    app.run()