from spellchecker import SpellChecker

class SpellCheckerApp:
    def __init__(self):
        # Initialize the spell checker object
        self.spell = SpellChecker()

    def correct_text(self, text):
        # Split the input text into words
        words = text.split()
        corrected_words = []

        for word in words:
            # spell.correction may return None; fall back to the original word
            corrected_word = self.spell.correction(word) or word
            if corrected_word and corrected_word.lower() != word.lower():
                print(f"Correcting '{word}' → '{corrected_word}'")
            corrected_words.append(corrected_word)

        # Return the corrected sentence
        return " ".join(corrected_words)

    def run(self):
        print("Spell Checker App")
        while True:
            text = input("Enter text to check (or type 'exit' to quit): ")
            if text.lower() == "exit":
                print("Closing the program...")
                break
            corrected_text = self.correct_text(text)
            print("Corrected text:", corrected_text)

if __name__ == "__main__":
    app = SpellCheckerApp()
    app.run()
