def html_tag(msg):
	def wrap_text(tag):
		print('<{0}>{1}</{0}>'.format(msg,tag))
	return wrap_text


h_t = html_tag('h1')
h_t('luckie')

h_t1= html_tag('p')
h_t1("I once loved and then I never loved, one way to say, I Kind of forgot what love means from myself to any other")