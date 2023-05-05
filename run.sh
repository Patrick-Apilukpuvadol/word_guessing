# Check if python is installed 
python3 -m venv venv

# Check if venv already exists
source venv/bin/activate
pip3 install -r requirements.txt
clear
python3 hangman.py