if(!settings.multipleView) settings.batchView=false;
settings.tex="xelatex";
defaultfilename="circle-cluster-1";
if(settings.render < 0) settings.render=4;
settings.outformat="";
settings.inlineimage=true;
settings.embed=true;
settings.toolbar=false;
viewportmargin=(2,2);

real r = 2.6cm;
for (int i = 0; i < 360; i += 10)
draw(circle(dir(i)*r, r));
