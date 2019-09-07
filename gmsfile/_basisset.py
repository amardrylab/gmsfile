class basisset:
	def basis(self, gbasis='sto3g'):
		sto3g =' $basis gbasis=sto ngauss=3 $end\n'
		g321  =' $basis gbasis=N21 ngauss=3 $end\n'

		card={
			'STO3G'  : sto3g,
			'STO-3G' : sto3g,

			'321G'   : g321,
			'3-21G'  : g321,
		}

		self.__basis__ = card[gbasis.upper()]
