# Path testing program for the numberutil module
# Batandwa Mgutsi
# 08/06/2020

"""
>>> import numberutil
>>> numberutil.aswords(120)
'one hundred and twenty'
>>> numberutil.aswords(151)
'one hundred and fifty one'
>>> numberutil.aswords(0)
'zero'
>>> numberutil.aswords(100)
'one hundred'
>>> numberutil.aswords(150)
'one hundred and fifty'

"""
import doctest
doctest.testmod(verbose=True)
