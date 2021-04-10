
test:
	for t in *.in; do python aqueducte.py $$t > sortida; diff -q `basename $$t .in`.ans sortida; done
