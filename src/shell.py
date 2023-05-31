import subprocess

class ShelllInterface:
    def run(self):
        while True:
            user_input = input("Enter your prompt (type 'exit' to quit): ")
            if user_input.lower() == 'exit':
                break
            response = self.process_input(user_input)
            print(response)

    @staticmethod
    def process_input(user_input):
        # Process the user input and generate a response
        # Here, we are simply returning a static prompt as an example
        return f"You entered: {user_input}"


if __name__ == '__main__':
    terminal = ShelllInterface()
    terminal.run()
