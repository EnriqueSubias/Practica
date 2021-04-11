
test:
	for t in *.in; do ./aqueducte.py $$t > sortida; diff -q `basename $$t .in`.pa.ans sortida; done
singletest:
	./aqueducte.py test5-1.in > sortida; diff -q test5-1.pa.ans sortida
