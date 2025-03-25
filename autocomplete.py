import readline
from difflib import get_close_matches

# Expanded dataset with Python, Java, and C++ code snippets
CODE_SNIPPETS = {
    # Python Snippets
    "print": "print('Hello, World!')",
    "for loop": "for i in range(10):\n    print(i)",
    "if condition": "if x > 0:\n    print('Positive')",
    "function": "def my_function():\n    return 'Hello'",
    "class": "class MyClass:\n    def __init__(self, name):\n        self.name = name",
    
    # Java Snippets
    "java print": "System.out.println(\"Hello, World!\");",
    "java for loop": "for (int i = 0; i < 10; i++) {\n    System.out.println(i);\n}",
    "java if condition": "if (x > 0) {\n    System.out.println(\"Positive\");\n}",
    "java function": "public static String myFunction() {\n    return \"Hello\";\n}",
    "java class": "public class MyClass {\n    private String name;\n    public MyClass(String name) {\n        this.name = name;\n    }\n}",
    
    # C++ Snippets
    "cpp print": "std::cout << \"Hello, World!\" << std::endl;",
    "cpp for loop": "for (int i = 0; i < 10; i++) {\n    std::cout << i << std::endl;\n}",
    "cpp if condition": "if (x > 0) {\n    std::cout << \"Positive\" << std::endl;\n}",
    "cpp function": "std::string myFunction() {\n    return \"Hello\";\n}",
    "cpp class": "class MyClass {\n    private:\n        std::string name;\n    public:\n        MyClass(std::string name) : name(name) {}\n};"
}

def complete(text, state):
    """Auto-complete function for user input."""
    matches = get_close_matches(text, CODE_SNIPPETS.keys(), n=5, cutoff=0.4)
    return matches[state] if state < len(matches) else None

# Configure auto-completion
readline.parse_and_bind("tab: complete")
readline.set_completer(complete)

def main():
    while True:
        try:
            user_input = input("Start typing a code snippet: ")
            if user_input in CODE_SNIPPETS:
                print("\nSuggested Code:\n", CODE_SNIPPETS[user_input])
            else:
                print("\nNo exact match found. Try again.")
        except KeyboardInterrupt:
            print("\nExiting...")
            break

if __name__ == "__main__":
    main()
