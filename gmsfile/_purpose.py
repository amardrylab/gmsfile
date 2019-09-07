class purpose:

	def runtyp(self, purpose='energy'):

		energy=' $contrl runtyp=energy $end\n'

		opt   =' $contrl runtyp=optimize $end\n'+ \
		       ' $statpt opttol=0.0001 nstep=100 $end\n'

		freq  =' $contrl runtyp=hessian $end\n'+ \
		       ' $force method=analytic vibanal=.true. $end\n'+ \
		       ' $statpt opttol=0.0001 nstep=30 $end\n'

		irc   =' $contrl runtyp=irc $end\n'


		card= {
			'ENERGY':energy,
			'OPT'   :opt, 
			'FREQ'  :freq, 
			'IRC'   :irc,
			}
		self.__purpose__= card[purpose.upper()]
