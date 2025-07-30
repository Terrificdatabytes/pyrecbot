🤖 pyrecbot
pyrecbot is a cross-platform Python automation tool designed to record and replay mouse and keyboard actions. Whether you're on Windows, Linux, or macOS, pyrecbot makes it easy to automate repetitive tasks using simple Python code.

✨ Features
🖱️ Record mouse and keyboard actions

🔁 Replay recorded actions multiple times

💻 Compatible with Windows, Linux, and macOS

⚙️ Ideal for automating repetitive desktop tasks

🐍 Simple and intuitive Python API

📦 Installation
Install pyrecbot using pip:
py -m pip install pyrecbot
🚀 Quick Start
Use the following Python code to record and replay actions:

import pyrecbot.start as bot

# Record one action
bot.record(1)

# Replay the recorded action 5 times
bot.replay(5)
💡 record(n) will record n sets of actions. You can record more by increasing the number.

🛠 Use Cases
Automate repetitive desktop workflows

GUI-based testing and simulations

Keyboard/mouse macro creation

Speed up manual processes in Python scripts

📁 Project Structure
pyrecbot/
├── start.py       # Main logic for recording and replaying
├── __init__.py    # Module initializer
├── utils/         # Helper functions (if available)
📃 License
This project is licensed under the MIT License.
See the LICENSE file for full terms.

🤝 Contributing
Found a bug? Have a feature idea?
Issues and pull requests are welcome!

👉 Visit: https://github.com/terrificdatabytes/pyrecbot/issues

Built with ❤️ by @terrificdatabytes
