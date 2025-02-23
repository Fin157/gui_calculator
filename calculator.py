from tkinter import StringVar

# A class that manages all the operations done on a specific listenable string
class Calculator:
    string_mappings = { # Maps some significant chars used visually to their corresponding equivalents in Python
        ":": "/",
        "×": "*",
        ",": "."
    }
    operator_chars = ["+", "-", "×", ":"] # A list of binary operators that work slightly 
                                          # differently than the rest of the characters
    is_error = False # Indicates if the last calculation was attempted on an invalid expression

    def __init__(self, character_limit: int):
        self.character_limit = character_limit

    # Appends the specified string value to the specified listenable string
    def append_to(self, target: StringVar, s: str):
        previous_expr = target.get()

        # Proceed only if the calculator is in the valid state currently and
        # if the character limit hasn't been reached yet
        if self.is_error or len(previous_expr) >= self.character_limit:
            return

        # Make sure to replace the last operator with the new one if necessary (to avoid doubling operators)
        if len(previous_expr) > 0 and s in self.operator_chars and previous_expr[-1] in self.operator_chars:
            previous_expr = previous_expr[:-1]

        target.set(previous_expr + s)

    # Removes the last character of the target listenable string's value
    def remove_last_char(self, target: StringVar):
        # Clear the whole expression instead if there has been an error (to avoid leaving residues of the
        # "custom error message" behind)
        if self.is_error:
            self.clear_expression(target)
        # Otherwise just remove the last character
        else:
            target.set(target.get()[:-1])

    # Empties the whole target listenable string's value
    def clear_expression(self, target: StringVar):
        target.set("")
        # Reset the error flag (clearing the expression always removes the error)
        self.is_error = False

    # Evaluates the expression saved in the target listenable string and replaces its value by the result
    def calculate(self, target: StringVar):
        expression = target.get()

        # Replace any mapped characters with their equivalent used when evaling
        for key in self.string_mappings:
            expression = expression.replace(key, self.string_mappings[key])

        # Make sure to catch exceptions if the expression isn't valid
        # and in case of any caught, just write out our universal error message
        try:
            eval_result = eval(expression)
        except:
            eval_result = "What the fuck man?" # This is our universal error message.
            self.is_error = True # Switch the error flag to signal that the current expression was invalid

        eval_result_str = str(eval_result)

        # Replace any mapped characters with their equivalent used visually
        for key in self.string_mappings:
            eval_result_str = eval_result_str.replace(self.string_mappings[key], key)

        target.set(eval_result_str)