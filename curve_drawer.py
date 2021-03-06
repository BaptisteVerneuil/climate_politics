import matplotlib.pyplot as plt


   ###########################################
   #    Primary energy supply of crude oil   #
   ###########################################

# From https://www.climate-transparency.org/wp-content/uploads/2020/11/EU28-CT-2020-WEB.pdf
# Data obtained through http://www.graphreader.com
x = [1990, 1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
# In PJ/year
y_coal = [19098.592,17937.834,17051.756,15824.805,15229.282,14895.298,15085.807,14474.878,13806.299,13074.308,13449.435,13521.127,13521.127,13660.223,13746.479,13746.479,13746.479,13562.895,12633.533,11271.491,11719.505,11948.372,12306.298,12051.855,11421.467,10905.122,10202.7,9664.608,9242.767,7211.268]
y_coal_and_oil = [44603.622,44089.021,42690.238,41533.862,41030.559,41324.915,41915.493,41239.437,41239.437,40232.918,39948.077,40104.905,40395.907,41006.85,40611.613,40339.693,40761.535,39675.571,38239.922,35164.494,35927.343,35449.322,34593.996,33709.568,33049.053,32729.157,32308.24,31948.935,31105.252, 29746.479]
y_oil = [y_coal_and_oil[i] - y_coal[i] for i in range(len(y_coal))]
plt.plot(x, y_oil, label = "Primary energy supply of crude oil")

value_2019_oil_demand = y_oil[-1]


   ########################################################################
   #    Final energy consumption of Crude oil consumption for transport   #
   ########################################################################

# Final energy consumption of Crude oil consumption for transport
# From https://www.climate-transparency.org/wp-content/uploads/2020/11/EU28-CT-2020-WEB.pdf
# Data retrieved with http://www.graphreader.com
x_transport = [1990, 1991,1992,1993,1994,1995,1996,1997,1998,1999,2000,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011,2012,2013,2014,2015,2016,2017,2018,2019]
# In PJ/year
y_transport = [10776.173, 10753.766,11029.192,11143.564,11226.036,11336.872,11707.421,11839.08,12291.363,12560.032,12524.177,12650.086,12799.079,12982.696,13212.996,13222.287,13383.513,13521.43,13113.948,12665.016,12580.27,12482.883,12107.556,11980.436,12122.145,12316.207,12560.154,12797.709,12897.084, 12942.238]
plt.plot(x_transport, y_transport, label = "Final energy consumption of Crude oil consumption for transport")

value_2005 = y_transport[15]
value_2019 = y_transport[-1]



   ###########################################
   #               Scenario 1 :              #
   ###########################################

# In this scenario, we consider that the oil consumption for the transport sector will stagnate
# We also consider that the oil consumption from other sectors than transport will have a 20% decrease, 
# which is the necessary average decrease to fulfill the Paris Agreement

share_transport_sector = 0.655
reduction_other_sector = 0.8

plt.plot([2019, 2030], [value_2019, value_2019], linestyle='--', label = "Scenarios 1 projection for oil consumption for transport")
# No decrease for transport consumption

y_values = [value_2019_oil_demand, (value_2019_oil_demand*share_transport_sector + value_2019_oil_demand*(1-share_transport_sector)*reduction_other_sector)]
plt.plot([2019, 2030], y_values, linestyle='--', label = "Scenario 1 projection for oil demand")
# -7% decrease for global oil consumption


   ############################################
   #               Scenario 2/3 :             #
   ############################################

# In this scenario, we consider that the oil consumption for the transport sector will decrease according the European Commission "Baseline scenario" (-19%).
# We also consider that the oil consumption from other sectors than transport will have :
#  - a 20% decrease for the scenario 2, which is the necessary average decrease to fulfill the Paris Agreement
#  - a 40% decrease for the scenario 3, which is the necessary average decrease to the EU new commitments (-55% in 2030 emissions compared to 1990)

value_2030_baseline = value_2005 * (1-0.19)
plt.plot([2019, 2030], [value_2019, value_2030_baseline], linestyle='--', label = "Scenario 2/3 projection for oil consumption for transport")
# -17,25% between 2019 and 2030 for trasport consumption

y_values = [value_2019_oil_demand, (value_2019_oil_demand*share_transport_sector*(value_2030_baseline/value_2019) + value_2019_oil_demand*(1-share_transport_sector)*(0.80))]
plt.plot([2019, 2030], y_values, linestyle='--', label = "Scenario 2 projection for oil demand")
# -18.2% decrease for global oil consumption

y_values = [value_2019_oil_demand, (value_2019_oil_demand*share_transport_sector*(value_2030_baseline/value_2019) + value_2019_oil_demand*(1-share_transport_sector)*(0.60))]
plt.plot([2019, 2030], y_values, linestyle='--', label = "Scenario 3 projection for oil demand")
# -25.1% decrease for global oil consumption



   ################################################
   #               Supply scenarios :             #
   ################################################

# Best scenario : 
# 1% decrease (from https://theshiftproject.org/wp-content/uploads/2020/09/Study_Risk-supply-Europe_TSP-with-Rystad-Data.pdf)
oil_supply_2030_best_case = value_2019_oil_demand*0.99 

# Worst case scenario : 
# - 8% decrease for production of EU supppliers
# - Constant ratio oil_supply/GDP for both EU and China
# GDP projection data retrieved from https://ec.europa.eu/assets/epsc/pages/espas/chapter1.html, retrieved with http://www.graphreader.com

decrease_production = 0.08 

GDP_EU_2019 = 15841
GDP_EU_2030 = 24364
GDP_CHINA_2019 = 14106
GDP_CHINA_2030 = 33869
share_EU_2019 = GDP_EU_2019/(GDP_EU_2019 + GDP_CHINA_2019) # 52,9%
share_EU_2030 = GDP_EU_2030/(GDP_EU_2030 + GDP_CHINA_2030) # 41,8%
decrease_worst_case = (1-decrease_production) * share_EU_2030/share_EU_2019 
# -27.2% decrease for global oil supply

y = [oil_supply_2030_best_case, value_2019_oil_demand*decrease_worst_case]
scatter = plt.scatter([2030, 2030], y)
plt.fill_between([2019, 2030], [value_2019_oil_demand, oil_supply_2030_best_case], [value_2019_oil_demand, value_2019_oil_demand*decrease_worst_case], label = "Range of oil supply scenarios", alpha=0.5)


   ################################################
   #               Graph parameters :             #
   ################################################

# labelling
plt.gca().annotate('Best case 2030\nsupply scenario', (2030-5, y[0]+800))
plt.gca().annotate('Worst case 2030\nsupply scenario', (2030-5.8, y[1]-2600))
plt.xlabel("years")
plt.ylabel("Crude oil in PJ/year")
plt.legend(prop={'size': 7})

# Setting axes scale
plt.xlim(1990, 2035)
plt.ylim(0, 30000)

# Displaying the figure
plt.show()