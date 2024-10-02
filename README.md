# PyBrowser

This is a simple Python web browser built using PyQt5 and PyQtWebEngine. It allows you to open multiple tabs, navigate web pages, and perform basic browser actions like back, forward, refresh, and go home. 

## Features
- Multiple tabs support
- Navigation controls: Back, Forward, Refresh, Home
- Address bar for direct URL input
- New tab functionality with the default page set to Google

## Requirements

This project requires the following Python packages:
- PyQt5
- PyQtWebEngine
- requests

You can install these packages automatically by running:
```bash
pip install -r requirements.txt
```

## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/python-web-browser.git
   cd python-web-browser
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the browser:
   ```bash
   python main.py
   ```

## Usage

- **Back Button:** Takes you back to the previous page in your browsing history.
- **Forward Button:** Takes you forward to the next page in your browsing history.
- **Refresh Button:** Reloads the current page.
- **Home Button:** Takes you to the homepage (default is Google).
- **Address Bar:** Enter a URL and press Enter to navigate.
- **New Tab Button:** Opens a new tab with Google loaded by default.

## File Structure

```
.
├── main.py             # Main Python file that launches the browser
├── util.py             # Utility functions
├── requirements.txt    # Dependencies for the project
└── README.md           # Project documentation
```

## Contributing

We welcome contributions! Please see the [CONTRIBUTING.md](CONTRIBUTING.md) file for guidelines.

## License

This project is licensed under the MIT License.
