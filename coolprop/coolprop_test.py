#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# In[1]:
#$import refprop as rp



#%%


# Import the things you need
from CoolProp.CoolProp import PropsSI

# Print some information on the currently used version of coolprop
import CoolProp; print(CoolProp.__version__, CoolProp.__gitrevision__)

# Density of carbon dioxide at 100 bar and 25C
D = PropsSI('D', 'T', 298.15, 'P', 100e5, 'CO2');print(D)

# Saturated vapor enthalpy [J/kg] of R134a at 25C
H = PropsSI('H', 'T', 298.15, 'Q', 1, 'R134a');print(H)


#%%


# import the things you need
from CoolProp.HumidAirProp import HAPropsSI

# Enthalpy (J per kg dry air) as a function of temperature, pressure,
#    and relative humidity at STP
h = HAPropsSI('H','T',298.15,'P',101325,'R',0.5); print(h)

# Temperature of saturated air at the previous enthalpy
T = HAPropsSI('T','P',101325,'H',h,'R',1.0); print(T)

# Temperature of saturated air - order of inputs doesn't matter
T = HAPropsSI('T','H',h,'R',1.0,'P',101325); print(T)


#%%


import CoolProp
from CoolProp.Plots import PropertyPlot
plot = PropertyPlot('R290', 'ph')
plot.calc_isolines()
plot.show()


#%%


import coolprop
from CoolProp.Plots import PropertyPlot
ts_plot = PropertyPlot('R290', 'Ts', tp_limits='ORC')
ts_plot.calc_isolines(CoolProp.iQ, num=6)
ts_plot.show()


#%%


import CoolProp
from coolprop.Plots import propertyplot
plot = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR', tp_limits='ACHP')
plot.calc_isolines(CoolProp.iQ, num=11)
plot.calc_isolines(CoolProp.iT, num=25)
plot.calc_isolines(CoolProp.iSmass, num=15)
plot.show()


#%%


import CoolProp
from CoolProp.Plots import PropertyPlot
plot = PropertyPlot('HEOS::R245fa', 'TS', unit_system='EUR', tp_limits='ORC')
plot.calc_isolines(coolprop.iQ, num=11)
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=10, rounding=True)
plot.draw()
plot.isolines.clear()
plot.props[CoolProp.iP]['color'] = 'green'
plot.props[CoolProp.iP]['lw'] = '0.5'
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=10, rounding=False)
plot.show()


#%%


import CoolProp
from CoolProp.Plots import PropertyPlot
ts_plot = PropertyPlot('Water', 'Ts')
ts_plot.calc_isolines(CoolProp.iQ, num=11)
ts_plot.title(r'$T,s$ Graph for Water')
ts_plot.xlabel(r'$s$ [kJ/kg K]')
ts_plot.ylabel(r'$T$ [K]')
ts_plot.grid()
ts_plot.show()


#%%


from CoolProp.Plots import PropertyPlot
plot = PropertyPlot("REFPROP::ISOBUTAN[0.8]&PROPANE[0.2]", 'PH', unit_system='EUR', tp_limits='ACHP')
plot.calc_isolines()
plot.show()


#%%


import CoolProp
state = CoolProp.AbstractState("REFPROP", "ISOBUTAN&PROPANE")
state.set_mass_fractions([0.8,0.2])
from CoolProp.Plots import PropertyPlot
plot = PropertyPlot(state, 'TS', unit_system='EUR', tp_limits='ACHP')
plot.calc_isolines()
plot.show()


#%%


from __future__ import print_function
import CoolProp
from CoolProp.Plots import StateContainer
from tabulate import tabulate

T0 = 300.000; p0 = 200000.000; h0 = 112745.749; s0 = 393.035

cycle_states = StateContainer()
cycle_states[0,'H'] = h0
cycle_states[0]['S'] = s0
cycle_states[0][CoolProp.iP] = p0
cycle_states[0,CoolProp.iT] = T0
cycle_states[1,"T"] = 300.064
print(cycle_states.__dir__)


#%%


import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleCompressionCycle
pp = PropertyPlot('HEOS::R134a', 'PH', unit_system='EUR')
pp.calc_isolines(CoolProp.iQ, num=11)
cycle = SimpleCompressionCycle('HEOS::R134a', 'PH', unit_system='EUR')
T0 = 280
pp.state.update(CoolProp.QT_INPUTS,0.0,T0-10)
p0 = pp.state.keyed_output(CoolProp.iP)
T2 = 310
pp.state.update(CoolProp.QT_INPUTS,1.0,T2+15)
p2 = pp.state.keyed_output(CoolProp.iP)
pp.calc_isolines(CoolProp.iT, [T0-273.15,T2-273.15], num=2)
cycle.simple_solve(T0, p0, T2, p2, 0.7, SI=True)
cycle.steps = 50
sc = cycle.get_state_changes()
pp.draw_process(sc)
import matplotlib.pyplot as plt
plt.close(cycle.figure)
pp.show()


#%%


import CoolProp.CoolProp as CP
fluid = 'Water'
pressure_at_critical_point = CP.PropsSI(fluid,'pcrit')
# Massic volume (in m^3/kg) is the inverse of density
# (or volumic mass in kg/m^3). Let's compute the massic volume of liquid
# at 1bar (1e5 Pa) of pressure
vL = 1/CP.PropsSI('D','P',1e5,'Q',0,fluid); print(vL)
# Same for saturated vapor
vG = 1/CP.PropsSI('D','P',1e5,'Q',1,fluid); print(vG)


#%%


import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots.SimpleCyclesExpansion import SimpleRankineCycle
pp = PropertyPlot('HEOS::Water', 'TS', unit_system='EUR')
pp.calc_isolines(CoolProp.iP        )
pp.calc_isolines(CoolProp.iHmass    )
pp.calc_isolines(CoolProp.iQ, num=11)
cycle = SimpleRankineCycle('HEOS::Water', 'TS', unit_system='EUR')
T0 = 300
pp.state.update(CoolProp.QT_INPUTS,0.0,T0+15)
p0 = pp.state.keyed_output(CoolProp.iP)
T2 = 700
pp.state.update(CoolProp.QT_INPUTS,1.0,T2-150)
p2 = pp.state.keyed_output(CoolProp.iP)
cycle.simple_solve(T0, p0, T2, p2, 0.7, 0.8, SI=True)
cycle.steps = 50
sc = cycle.get_state_changes()
pp.draw_process(sc)
# The same calculation can be carried out in another unit system:
cycle.simple_solve(T0-273.15-10, p0/1e5, T2-273.15+50, p2/1e5-5, 0.7, 0.8, SI=False)
sc2 = cycle.get_state_changes()
pp.draw_process(sc2, line_opts={'color':'blue', 'lw':1.5})
pp.show()


#%%


import CoolProp
from CoolProp.Plots import PropertyPlot
from CoolProp.Plots import SimpleRankineCycle
import matplotlib.pyplot as plt
pp = PropertyPlot('HEOS::R245fa', 'TS', unit_system='EUR', tp_limits='ORC')
pp.calc_isolines(CoolProp.iQ, num=11)
pp.calc_isolines(CoolProp.iP, iso_range=[1,50], num=10, rounding=True)
plot.draw()
plot.isolines.clear()
plot.props[CoolProp.iP]['color'] = 'green'
plot.props[CoolProp.iP]['lw'] = '0.5'
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=10, rounding=False)
cycle = SimpleRankineCycle('HEOS::R245fa', 'TS', unit_system='EUR', tp_limits='ORC')
T0 = 298
pp.state.update(CoolProp.QT_INPUTS,0.0,T0+10)
p0 = pp.state.keyed_output(CoolProp.iP)
T2 = 370
T3 = 330
pp.state.update(CoolProp.QT_INPUTS,1.0,T3)
p2 = pp.state.keyed_output(CoolProp.iP)
cycle.simple_solve(T0, p0, T2, p2, 0.9, 0.9, fluid='R245fa', SI=True)
cycle.steps = 1000
sc = cycle.get_state_changes()

#plt.close(cycle.figure)
#pp.draw_process(sc)
plot.show()
'''
import CoolProp
from CoolProp.Plots import PropertyPlot
plot = PropertyPlot('HEOS::R245fa', 'TS', unit_system='EUR', tp_limits='ORC')
plot.calc_isolines(coolprop.iQ, num=11)
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=10, rounding=True)
plot.draw()
plot.isolines.clear()
plot.props[CoolProp.iP]['color'] = 'green'
plot.props[CoolProp.iP]['lw'] = '0.5'
plot.calc_isolines(CoolProp.iP, iso_range=[1,50], num=10, rounding=False)
plot.show()'''

