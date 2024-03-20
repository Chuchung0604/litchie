# -*- coding: utf-8 -*-
"""
Created on Wed May  4 17:04:01 2022

@author: ccchen
"""

import main
import os
# CESM1-BGC, CESM1-CAM5, CMCC-CM, CNRM-CM5, CSIRO-Mk3-6-0, FGOALS-g2,
# GFDL-ESM2G, GFDL-ESM2M, immcm4, IPSL-CM5A-LR, IPSL-CM5A_MR, IPSL-CM5B-LR,
# MIROC5, MIROC-ESM, MIROC-ESM-CHEM, MPIESM_LR, MPI-ESM-MR, MRI-CGCM3, NorESM1-M

#models = ["MIROC5", "bcc-csm1-1","CCSM4","MIROC-ESM","MIROC-ESM-CHEM","FGOALS-g2"]   
models1 = ["bcc-csm1-1", "bcc-csm1-1-m", "BNU-ESM", "CanESM2", "CCSM4","CESM1-BGC", "CESM1-CAM5", 
          "CMCC-CM", "CNRM-CM5", "CSIRO-Mk3-6-0", "FGOALS-g2","GFDL-ESM2G", "GFDL-ESM2M"] 
models2 = ["immcm4", "IPSL-CM5A-LR", "IPSL-CM5A-MR", "IPSL-CM5B-LR", "MIROC5", "MIROC-ESM", 
           "MIROC-ESM-CHEM", "MPI-ESM-LR", "MPI-ESM-MR", "MRI-CGCM3", "NorESM1-M"] 

for model in models1:
    
    for year in range(2026,2056):
    #for year in yearLst:
        os.makedirs("Output2022oct/%s"%(model),exist_ok = True)
        main.writeReadMe("rcp85", model)
        main.runOneYear("rcp85",model,year)