import os

main = os.environ.get('HOME')

if not os.path.exists(main + '/extras'):
	os.system('git clone https://github.com/ARACADERISE/extras')
	os.system('cd extras/python/yal_lang && python file.py')
else:
	os.system(f'cd {main}/extras/python/yal_lang && python file.py')
