#! /bin/zsh
source .venv/bin/activate
python3 -m twine upload dist/*
