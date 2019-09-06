import re

class gms:
	__text__=''
	__purpose__=' $contrl runtyp=energy $end\n'
	__method__=' $contrl scftyp=rfh $end\n'
	__basis__=' $basis gbasis=sto ngauss=3 $end\n'
	
	def __init__(self, infile='mol.xyz'):
		an={
			'H': '     1.0     ',
			'He': '    2.0     ',
			'Li': '    3.0     ',
			'Be': '    4.0     ',
			'B': '     5.0     ',
			'C': '     6.0     ',
			'N': '     7.0     ',
			'O': '     8.0     ',
			'F': '     9.0     ',
			'Ne': '   10.0     ',
			'Na': '   11.0     ',
			'Mg': '   12.0     ',
			'Al': '   13.0     ',
			'Si': '   14.0     ',
			'P' :'    15.0     ',
			'S' :'    16.0     ',
			'Cl': '   17.0     ',
			'Ar': '   18.0     ',
			'K': '    19.0     ',
			'Ca': '   20.0     ',
			'Sc': '   21.0     ',
			'Ti': '   22.0     ',
			'V' :'    23.0     ',
			'Cr': '   24.0     ',
			'Mn': '   25.0     ',
			'Fe': '   26.0     ',
			'Co': '   27.0     ',
			'Ni': '   28.0     ',
			'Cu': '   29.0     ',
			'Zn': '   30.0     ',
			'Ga': '   31.0     ',
			'Ge': '   32.0     ',
			'As': '   33.0     ',
			'Se': '   34.0     ',
			'Br': '   35.0     ',
			'Kr': '   36.0     ',
			'Ru': '   44.0     ',
		}

		self.__text__=''
		data   =' $data\nTitle\nC1\n'
		self.__text__ +=data

		pat=re.compile('\s+')

		f=open(infile, 'r')
		f.readline()
		f.readline()
		for line in f:
			line=line.strip()
			(element,coor)=pat.split(line, 1)
			self.__text__+=element+an[element]+coor+'\n'
		self.__text__+=' $end\n'

		f.close()

	def runtyp(purpose=''):
		__purpose__='$contrl runtyp=energy $end'

	def out(self, outfile="mol.inp"):
		data=''
		data += self.__purpose__
		data +=self.__method__
		data +=self.__basis__
		data +=self.__text__
		f=open(outfile, 'w')
		f.write(data)
		f.close()
