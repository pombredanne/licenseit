import pkg_resources

ENCODING = 'utf-8'

LICENSE = ["APL-1.0", 'Apache-2.0', 'Artistic-2.0', 'BSD+PATENT', 'BSD-2', 'BSD-3',
			'CDDL-1.0', 'ECL-2.0', 'EPL-2.0', 'GNU-2.0', 'GNU-3.0', 'IPA',
			'ISC', 'LGPL-2.0', 'LGPL-2.1', 'MIT', 'MPL-2.0', 'NASA-1.3',
			'OFL-1.1', 'OPL-2.1', 'UCL-1.0']

def get_license(index, author, year):
	global ENCODING
	global LICENSE

	year = bytes(str(year), ENCODING)
	author = bytes(author, ENCODING)

	recourse_package = __name__
	resource_path = '/'.join(('content', LICENSE[index - 1]))

	license = pkg_resources.resource_string(recourse_package, resource_path)
	license = license.replace(b'<YEAR>', year)

	if author:
		license = license.replace(b'<COPYRIGHT HOLDERS>', author)

	return license.decode(ENCODING)