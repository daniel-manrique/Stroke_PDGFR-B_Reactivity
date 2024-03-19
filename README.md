# Examination of PDGFR-B reactivity following experimental brain ischemia

This repository contains code notebooks (Quarto and Python) associated with the research on PDGFR-B reactivity following brain ischemia. 


## Folders

Folders are listed in alphabetic order.

**ProData:** Contains processed data sets used for analysis and visualization. These data frames are generated from raw data available at the **RawData** folder, or the Open Science Framework (OSF) repository if the files are too heavy. The precise handling of the data is show in specific notebooks.


## Notebooks

The notebooks are listed according to the suggested execution order to follow the research pipeline described in the research article (XXXXXX)


**Widefield_5x_Shrinkage.qmd:** Contains data handling and statistical modeling for the analysis of brain shrinkage. 
**Widefield_5x_Pdgfrb-IntDen.qmd:** Contains data handling and statistical modeling for the analysis of PDGFR-β integrated density.  

**Widefield_5x_Pdgfrb-LowHigh.qmd:** Contains data handling and statistical modeling for the proportion of reactive (PDGFR-β_high) cells in cortico-striatal lesions.  

**Widefield_5x_Pdgfrb-LowHigh_Str.qmd:** Contains data handling and statistical modeling for the proportion of reactive (PDGFR-β_high) cells in striatal (only regions).  

**Widefield_5x_Gfap-IntDen.qmd:** Contains data handling and statistical modeling for the analysis of GFAP integrated density. 

**Widefield_5x_Gfap-Convex.qmd:** Contains data handling and statistical modeling for the analysis of GFAP convex hull in the ischemic hemisphere. 

**Widefield_5x_Pdgfrb-Gfap_Covariance.qmd:** Contains data and point pattern analysis for PDGFR-β and its covariance for GFAP. This notebook process the data from cortico-striatal lesions.  

**Widefield_5x_Pdgfrb-Gfap_Covariance_Str.qmd:** Contains data and point pattern analysis for PDGFR-β and its covariance for GFAP. This notebook process the data from striatal (only) lesions.

**Widefield_10x_Pdgfrb-Gfap_Covariance.qmd:** Contains data and point pattern analysis for PDGFR-β and its covariance for GFAP. 

**Widefield_10x_CD31-Pdgfrb_Coloc.qmd:** Contains data handling and statistical modeling for the analysis of PDGFR-β and CD31 colocalization in specific brain ROIs. 

**Confocal_40x_Pdgfrb_Morphology.qmd**: Contains data handling and statistical modeling for the analysis features extracted with **Confocal_40x_ROIs_Pdgfrb_MorphologicalAnalysis_skimage.py**. 

**Confocal_40x_ROIs_Pdgfrb_MorphologicalAnalysis_skimage.py:** Python script to extract morphological features from selected cells. 

**Widefield_10x_Pdgfra-Pdgfrb_Coloc.qmd:** Contains data handling and statistical modeling for the analysis of PDGFR-α and PDGFR-β colocalization in the ipsilateral hemisphere. 

**Widefield_20x_ROIs_Pdgfrb_Area-Haralick.qmd:** Contains data handling and statistical modeling for the analysis of the area and Haralick features of PDGFR-β cells in specific ROIs. 

**Widefield_10x_Klf4_Detections.qmd:** Contains data and point pattern analysis for KLF4 spatial and intensity analysis.

**Widefield_20x_Klf4_Detections.qmd:** Contains data analysis for KLF4/PDGFR-β colocalization in defined ROIs.

## Support files

**.bib files** These are files associated to each notebook containing cited bibliography. 
**science.csl** This files contains the Science Journal citation style implemented in the notebooks. Please note this is style is not associated to the journal the original research article is publish in. 