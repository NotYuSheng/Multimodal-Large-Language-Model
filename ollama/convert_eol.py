import os

def convert_eol(file_path):
    # Determine the EOL character based on the operating system
    if os.name == 'nt':  # Windows
        eol = '\r\n'
    elif os.name == 'posix':  # Unix/Linux/MacOS (modern)
        eol = '\n'
    else:
        raise OSError("Unsupported operating system.")

    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Replace all possible EOL characters with the chosen one
    content = content.replace('\r\n', '\n').replace('\r', '\n').replace('\n', eol)

    # Write the content back to the file
    with open(file_path, 'w') as file:
        file.write(content)

    print(f"Converted EOL characters in {file_path} to {repr(eol)}")

# EOL conversion for the following files
convert_eol('/app/ollama-build.sh')
convert_eol('/app/ollama-startup.sh')
