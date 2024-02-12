There are two usage in this script: Location Selection and Array Interaction Simulation.
For the Location Selection Part:
  Step 1. Download all the geo files (.nc / .shp / .tif) and input it inside the corrspounding directory.
  Step 2. Use the Scripts under the directory "gisfile_plot&detacheck", where you can check the data of the geo files and plot.
  Step 3. Use the Scripts under the directory "Location Selection", where you can process three selection sectors: Economic Sector, Restriction Sector, and Technical Sector via scripts separately, under its directory.
      Economic Sector: 
        1. Coastline_BufferArea.py: Build the buffer area for coastline and output a new Geo file，so that we can check the distance to the coastline in QGIS.
        2. V.C Data_Preprocess.py: A Pre-process code for vessel density analysis, used to create three thresholds, so that we can divide the Ocean-area into 4 levels based on vessel density.
        3. VesselDensity_limitation.py: Be used to do vessel density analysis and output a new Geo file.
      Restriction Sector:
        1. Active licences for Oil and Gas EE_buffer.py: Be used to build the buffer area for Oil and Gas EE device already installed and output a new Geo file.
        2. Pipelines_buffer.py: Be used to build the buffer area for Pipelines already installed and output a new Geo file.
        3. Power Cables_buffer.py: Be used to build the buffer area for Power Cables already installed and output a new Geo file.
      Technical Sector:
        1. mean mwd 2010to2020.py and yearly mwd calculation.py: Be used to set thresholds for mean wave period, reshape the wave data file and output a new Geo file.
        2. mean swh 2010to2020.py and yearly swh calculation.py: Be used to set thresholds for significant wave height, reshape the wave data file and output a new Geo file.
        3. mean wave_power 2010to2020.py and yearly wave_power calculation.py: Be used to set thresholds for wave power, reshape the wave data file and output a new Geo file.
        4. Accessibility @2010to2020.py: Be used to set thresholds for Accessibility, reshape the wave data file and output a new Geo file.
        5. Bathymetry_limitation.py: Be used to set thresholds for Bathymetry, reshape the Bathymetry file and output a new Geo file.
        6. MVI@2020.py: Be used to set thresholds for MVI(a factor) and output a new Geo file.
  Step 4. Use the Scripts under the directory "Sensitivit Analysis", where you can check the sensitivity of five factors that affect the Technical Sector: mwd, swh, Accessibility, Bathymetry, and MVI.

For the Array Interaction Simulation Part:
  Step 1. Use the Scripts under the directory "Array Generation", where you can generate a array.
  Step 2. Use the Scripts "wavenum_calculator.py" under the directory "Array Interaction", where you can compute the wave properties, includes wave number, Angular frequency, wave lenght.
  Step 3. Use the Scripts under the directory "PointAbsorber_AEP", where you can compute the annual energy production of WECs that without interaction effect.
  Step 4. Use the Scripts "Array_Interaction_total_k.py" or "Array_Interaction_fixed_k.py" under the directory "Array Interaction", where you can do the q_factor simulation, economic analysis and WECs' displacement calculation.
