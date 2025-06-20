python3 -m venv venv

source venv/bin/activate

pip install -r requirements.txt // not there any

pip install gitpython

pip install tree-sitter tree-sitter-languages

CFLAGS="-std=c11" python parse_repo.py