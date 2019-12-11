import os

main_path = os.envrion.get('HOME')

if not os.path.exists(main_path + '/extras'):
  os.system('cd && git clone https://github.com/ARACADERISE/extras')

os.system('cd extras/python/yal_lang && python file.py')
