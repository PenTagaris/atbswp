import re

def is_phone_number_re(text):
	phone_num_regex = re.compile(r'(\d{3})-(\d{3}-\d{4})')
	mo = phone_num_regex.search(text)
	if mo:
		print('Phone number found: {0}'.format(mo.group(0)))
		print('Area code: {0}'.format(mo.group(1)))
		print('Phone number: {0}'.format(mo.group(2)))
	else:
		print('Nothing here!')

pos_test = ('My number is 415-555-4242')
neg_test = ('My number is unlisted')
is_phone_number_re(pos_test)
is_phone_number_re(neg_test)
