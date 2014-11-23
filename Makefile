agent:	clean

run:	clean
	python agent.py
	rm -rf *.pyc
grade:	clean
	python grade.py
	rm -rf *.pyc
clean:
	rm -rf *.pyc
	rm -f output.txt
