run:	clean
	python agent.py
	rm -rf *.pyc
agent:	clean

grade:	clean
	python grade.py
	rm -rf *.pyc
clean:
	rm -rf *.pyc
	rm -f output.txt
