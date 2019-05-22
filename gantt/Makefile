all:    tree

tree.1: tree.mp
	mpost tree
tree: tree.1
	xelatex -shell-escape tree

clean:
	rm -f *.aux *.log *.nav *.out *.pdf *.snm *.toc *.vrb *.sync*
