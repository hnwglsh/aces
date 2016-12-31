from aces.materials.POSCAR import structure as material
class structure(material):
	def getPOSCAR(self):
		return self.directContcar()
		#generated from minimized Bi4I4 tilt cell
		return """POSCAR file written by OVITO
1.0
        4.4448437691         0.0000000000         0.0000000000
        2.2224218396         7.8117603831         0.0000000000
        0.0000000000         2.9140218290        10.6656807255
   Bi    I
    4    4
Direct
     0.785974920         0.380735666         0.573405504
     0.164426789         0.623831928         0.839674532
     0.769837260         0.413011134         0.288448513
     0.148288980         0.656107605         0.554717600
     0.517726481         0.917232454         0.780036151
     0.416537434         0.119610682         0.348086953
     0.124091707         0.704502106         0.199127942
     0.810172141         0.332341015         0.928995073
"""
	def directContcar(self):
		return """Bi  I 
 1.0000000000000000
     1.2100935260191532    4.2769506840430891   -0.0000000000002100
    -6.9113483941381544    4.2651169123495434   -0.0693201522270231
    -2.8949119255432874    0.8190681722870106   10.6394026495327889
    Bi    I
   4   4
Cartesian
  5.3710962420928592  0.7899993138004117  0.1436195283796707
 -4.7433324006001136  3.6517121378367969  2.8903912576196218
  3.0585140192273870  1.4443067826475851  7.7490113919129584
 -7.0559147016282306  4.3060196287987855 10.4957834084168393
  0.7403966147082210  2.1001803062913327  2.3048554208558620
 -2.4252150981847973  2.9958385737917417  8.3345475372193807
 -6.3902670151061267  4.1176853897580532  6.7091683613127611
  4.7054486842779610  0.9783333778457488  3.9302339690377104
  """