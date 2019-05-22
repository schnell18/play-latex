all:    circle-cluster

circle-cluster-1.asy: circle-cluster.tex
	xelatex circle-cluster

circle-cluster-1.pdf: circle-cluster-1.asy
	asy circle-cluster-1.asy

circle-cluster: circle-cluster-1.pdf circle-cluster.tex
	xelatex -shell-escape circle-cluster.tex

clean:
	rm -f *.aux *.log *.nav *.out *.pdf *.snm *.toc *.vrb *.sync* *.fdb_latexmk *.asy *.pre
