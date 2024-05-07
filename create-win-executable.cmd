mkdir win
cd win
python -m venv .
call .\Scripts\activate.bat
cd ..
pip install demjson3 pyinstaller setuptools
python setup.py install
cd win
pyinstaller --onefile ..\cdxj_indexer\main.py
move .\dist\main.exe %~dp0\cdxjIndexer.exe
cd %~dp0
