"""
Simple Python Project
A basic Python script to get started.
"""


def greet(name: str) -> str:
    """
    Greet a person by name.
    
    Args:
        name: The person's name
        
    Returns:
        A greeting message
    """
    return f"Hello, {name}! Welcome to this Python project."


def main():
    """Main entry point of the application."""
    print("=" * 50)
    print("Welcome to the Simple Python Project")
    print("=" * 50)
    
    # Example: greet the user
    name = input("Enter your name: ")
    message = greet(name)
    print(message)
    
    print("\nProject structure:")
    print("  - src/main.py: Main application code")
    print("  - requirements.txt: Project dependencies")
    print("  - README.md: Project documentation")
    print("=" * 50)


if __name__ == "__main__":
    main()
