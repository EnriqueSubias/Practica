
test:
	for t in t*.in; do ./aqueducte.py $$t > sortida; diff -q `basename $$t .in`.pa.ans sortida; done

test_recursive:
	for t in t*.in; do ./aqueducte_recursive.py $$t > sortida; diff -q `basename $$t .in`.pa.ans sortida; done
