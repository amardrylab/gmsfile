import re

def xyztogms(infile='mol.xyz', outfile='mol.inp'):
	an={
		'H': '     1.0     ',
		'C': '     6.0     ',
		'N': '     7.0     ',
		'O': '     8.0     ',
	}

	text=''
	runtype=' $contrl runtyp=energy $end\n'
	scftype=' $contrl scftyp=rhf $end\n'
	basis  =' $basis gbasis=sto ngauss=3 $end\n'
	data   =' $data\nTitle\nC1\n'
	text+=runtype+scftype+basis+data

	pat=re.compile('\s+')

	f=open(infile, 'r')
	f.readline()
	f.readline()
	for line in f:
		(element,coor)=pat.split(line, 1)
		text+=element+an[element]+coor


	text+=' $end\n'

	g=open(outfile, 'w')
	g.write(text)
	g.close()
