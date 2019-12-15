import os

main = os.environ.get('HOME')

if not os.path.exists(main + '/extras'):
	os.system('git clone https://github.com/ARACADERISE/extras')
	os.system('cd extras/python/yal_lang && python file.py')
else:
	os.system(f'cd {main} && rm -rf extras')
	os.system(f'cd first_yal_project && git clone https://github.com/ARACADERISE/extras && cd extras/python/yal_lang && python file.py')
