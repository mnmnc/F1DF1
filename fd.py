from os import walk
from os import stat


def get_files(mypath):
	f = []
	for (dirpath, dirnames, filenames) in walk(mypath):
		print('Processing:', dirpath)
		for file in filenames:
			fullpath = dirpath + '\\'+ file
			fdict = { 'filename': file, 'path': fullpath, 'size': (stat(fullpath)).st_size, 'modified': (stat(fullpath)).st_mtime }
			f.append(fdict)
	return f



files =  get_files('F:\\')

for file in files:
	siblings = []
	for tmp in files:
		if file['filename'] == tmp['filename']:
			siblings.append(tmp)
	if len(siblings) > 2:
		print('Potential duplication for file', file['filename'])
		for f in siblings:
			print('\tSize:', f['size'], '\tModified:', f['modified'], '\tPath:', f['path'])

