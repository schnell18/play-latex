all:    tree

tree.1: tree.mp
	mpost tree
tree: tree.1
	xelatex -shell-escape tree
	rm -fr tree.1

clean:
	rm -f tree.1 *.aux *.log *.nav *.out *.pdf *.snm *.toc *.vrb *.sync*
