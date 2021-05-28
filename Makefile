
test_iterative:
	for t in *.in; do ./aqueducte.py $$t > sortida; diff -q `basename $$t .in`.ap.ans sortida; done

test_recursive:
	for t in *.in; do ./aqueducte_recursive.py $$t > sortida; diff -q `basename $$t .in`.ap.ans sortida; done
