# Task Automation for File Organization

## Overview

The File Organization Automation tool is a Python script that helps automate the organization of files within a directory. It sorts files into predefined folders based on their file types or other specified criteria, streamlining file management and reducing manual sorting effort.

## Features

- **Automatic File Sorting**: Moves files into designated folders based on their extensions or criteria.
- **Customizable Rules**: Define and modify sorting rules through a configuration file.
- **Error Handling**: Robust error handling to manage issues like missing directories or invalid files.
- **User-Friendly Interface**: Command-line interface with clear prompts and instructions.

## Installation

1. **Clone the repository**:
    ```bash
    git clone https://github.com/yourusername/file-organization-automation.git
    ```
2. **Navigate to the project directory**:
    ```bash
    cd file-organization-automation
    ```
3. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

## Configuration

1. **Set Up Rules**: Edit the `config.json` file to specify the file types and corresponding directories. Example:
    ```json
    {
        "documents": [".pdf", ".docx", ".txt"],
        "images": [".jpg", ".png", ".gif"],
        "videos": [".mp4", ".avi", ".mov"]
    }
    ```
2. **Adjust Paths**: Ensure the `source_directory` and `destination_directory` are set correctly in the `main.py` file.

## Usage

1. **Run the script**:
    ```bash
    python main.py
    ```
2. **Follow the prompts** to specify the directory to be organized.

## Contributing

Contributions are welcome! To contribute, please open an issue or submit a pull request. For more details, refer to `CONTRIBUTING.md`.


## Contact

For any questions or feedback, please contact rafiakedir22@gmail.com

