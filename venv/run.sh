# Check if python is installed 
python3 -m venv venv.venv

# Check if venv already exists
source WORD_GUESSING/venv.venv/bin/activate
pip3 install -r requirements.txt
python3 hangman.py