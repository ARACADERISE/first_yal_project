import os

if not os.path.exists('extras'):
  os.system('cd && git clone https://github.com/ARACADERISE/extras')

os.system('cd extras/python/yal_lang && python file.py')
