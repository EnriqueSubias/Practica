
test:
	for t in *.in; do ./aqueducte.py $$t > sortida; diff -q `basename $$t .in`.pa.ans sortida; done
