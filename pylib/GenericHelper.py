from rich import print


class GenericHelper:

    @staticmethod
    def yesno(self, prompt):
        while True:
            response = input(prompt + " (y/n): ").lower()
            if response in "nN":
                print("Exiting.")
            elif response in "yY":
                return True
            else:
                print("Invalid response. Please enter 'yes' or 'no'.")
