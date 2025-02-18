from tkinter import StringVar

class Calculator:
    string_mappings = {
        ":": "/",
        "×": "*",
        ",": "."
    }
    operation_chars = ["+", "-", "×", ":"]
    is_error = False

    def append_to(self, target: StringVar, s: str):
        if self.is_error:
            return

        previous_expr = target.get()

        if len(previous_expr) > 0 and s in self.operation_chars and previous_expr[-1] in self.operation_chars:
            previous_expr = previous_expr[:-1]

        target.set(previous_expr + s)

    def remove_last_char(self, target: StringVar):
        if self.is_error:
            self.clear_expression(target)
        else:
            target.set(target.get()[:-1])

    def clear_expression(self, target: StringVar):
        target.set("")
        self.is_error = False

    def calculate(self, target: StringVar):
        # Construct the whole expression to be evaluated
        expression = target.get()

        # Replace any mapped characters with their equivalent used when evaling
        for key in self.string_mappings:
            expression = expression.replace(key, self.string_mappings[key])

        try:
            eval_result = eval(expression)
        except:
            eval_result = "What the fuck man?" # This is our universal error message.
            self.is_error = True

        eval_result_str = str(eval_result)

        if (eval_result_str.isnumeric() and float(eval_result_str).is_integer()):
            eval_result_str = str(int(float(eval_result_str)))
        # eval_result_str = str(int(eval_result)) if str(eval_result).isnumeric() and float(eval_result).is_integer() else str(eval_result)
        # eval_result_str = str(eval_result)

        # Replace any mapped characters with their equivalent used visually
        for key in self.string_mappings:
            eval_result_str = eval_result_str.replace(self.string_mappings[key], key)

        target.set(eval_result_str)