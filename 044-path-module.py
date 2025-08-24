from pathlib import Path

# Get the current working directory
current_dir = Path.cwd()
print(f"Current directory: {current_dir}")

# Create a new directory
new_dir = current_dir / "test123"
new_dir.mkdir(exist_ok=True)

# Create a file within the new directory
file_path = new_dir / "test_file.txt"
file_path.write_text("Hello from pathlib!")


# Read content from the file
content = file_path.read_text()
print(f"File content: {content}")

# Check if the file exists
if file_path.exists():
    print("File exists.")
