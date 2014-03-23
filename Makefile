# oroboros makefile

RM = rm -rf
PY = python
CD = cd
PYDOC = epydoc
RST = buildhtml.py

all:

clean:
	$(RM) build dist MANIFEST

cleanpy:
	$(RM) oroboros/*.pyc oroboros/core/*.pyc oroboros/gui/*.pyc oroboros/cli/*.pyc oroboros/irc/*.pyc

cleandoc:
	$(RM) doc *.html

cleanhome:
	$(RM) ~/.oroboros

mrproper: clean cleanpy cleandoc cleanhome

doc:
	$(PYDOC) --config epydoc.cfg

rst:
	$(RST) --config docutils.cfg

dist: mrproper doc rst
	$(PY) setup.py sdist --formats=bztar

rpm: mrproper
	$(PY) setup.py bdist_rpm --use-bzip2 --group=Sciences/Astronomy

upload: mrproper doc rst
	$(PY) setup.py sdist --formats=bztar upload

install:
	$(PY) setup.py install

# end.
