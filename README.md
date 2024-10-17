# Examination of PDGFRβ reactivity and KLF4 expression following cerebral ischemia

This repository was organised by Daniel Manrique-Castano, former postdoctoral fellow and current research data curation officer at the Digital Research Alliance of Canada.

**Website:** https://daniel-manrique.github.io/
**GitHub:** https://github.com/daniel-manrique
**Contact:** dmanriquecastano .at gmail.com

This repository hosts **Quarto** and **Python** notebooks (data handling and statistical models) associated with the research article "XXX". Raw/processed data and outputs are available in our **Open Science Framework (OSF) repository** (https:doi.org/10.17605/OSF.IO/74MQN).

## Files

Naming conventions for notebooks (taking as example *Confocal_20x_ROIs_Ki67-Pdgfrb_Coloc.qmd*)

Confocal: Imaging type (available strings = Confocal, Widefield).
20x: Objective magnification (Available strings = 5x, 10x, 20x, 40x).
ROIs: Region of interest (Available strings = ROIs [regions of interest], Whole [whole brain], Ipsilateral [ischemic hemisphere]).
Ki67-Pdgfrb: Marker stained/analysed (available strings = multiple, depending on experiment).
Coloc: Analysis performed in notebook (available strings = multiple, depending on each experiment).


### Confocal imaging analysis

**Confocal_20x_ROIs_Ki67-Pdgfrb_Coloc.qmd:** [Quarto notebook, R code] Analysis of Ki67/PDGFRβ colocalization in defined ROIs of PDGFRβ_TdTomato mice.

**Confocal_20x_ROIs_Klf4-Pdgfrb_Coloc.qmd:** [Quarto notebook, R code] Analysis of KLF4/PDGFRβ colocalization in defined ROIs of PDGFRβ_TdTomato mice.

**Confocal_40x_ROIs_Pdgfrb_Morpho_Analysis.qmd:** [Quarto notebook, R code] Morphological analysis of PDGFRβ-positive cells in defined ROIs of PDGFRβ_TdTomato mice.

**Confocal_40x_ROIs_Pdgfrb_Morpho_BatchScript.qmd:** [Quarto notebook, Python code] Extraction of morphological features from PDGFRβ-positive cells in defined ROIs of PDGFRβ_TdTomato mice.


### Flow Cytometry analysis

**FlowCytometry_Pdgfrb_Analysis.qmd:** [Quarto notebook, R code] Analysis of FACS-sorted PDGFRβ-positive cells from the ischemic core of PDGFRβ_TdTomato mice.

**FlowCytometry_Pdgfrb_Processing.qmd:** [Quarto notebook, R code] Processing of .FCS (FACS-derived files) for the analysis of PDGFRβ-positive cells from the ischemic core of PDGFRβ_TdTomato mice.


### Widefield imaging analysis

**Widefield_10x_Ipsilateral_KO_CD31-ColIV_Inten.qmd:** [Quarto notebook, R code] Analysis of CD31/ColIV intensity in the ischemic hemisphere of PDGFRβ_KLF4-KO brains and corresponding controls.

**Widefield_10x_Ipsilateral_KO_Fish_Pdgfrb.qmd:** [Quarto notebook, R code] Analysis of PDGFRβ by Fluorescence in situ hybridization (FISH) from PDGFRβ_KLF4-KO brains and corresponding controls.

**Widefield_10x_Ipsilateral_KO_Klf4_Exp.qmd:** [Quarto notebook, R code] Analysis of KLF4 expression in the ischemic hemisphere of PDGFRβ_KLF4-KO brains and corresponding controls.

**Widefield_10x_Ipsilateral_Ki67-Pdgfrb_Coloc.qmd:** [Quarto notebook, R code] Analysis of Ki67/PDGFRβ colocalization in the ischemic hemisphere of PDGFRβ_TdTomato mice.

**Widefield_10x_Ipsilateral_Ki67_PPA.qmd:** [Quarto notebook, R code] Point Pattern Analysis (PPA) of Ki67-positive cells in the ischemic hemisphere of PDGFRβ_TdTomato mice.

**Widefield_10x_Ipsilateral_Klf4_Exp.qmd:** [Quarto notebook, R code] Analysis of KLF4 expression in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains.

**Widefield_10x_ROIs_CD31-Pdgfrb_Coloc.qmd:** [Quarto notebook, R code] Analysis of perivascular and parenchymal PDGFRβ-positive cells in defined ROIs of PDGFRβ_TdTomato mouse brains.

**Widefield_10x_ROIs_Gfap-Pdgfrb_Covariance.qmd:** [Quarto notebook, R code] Analysis of GFAP/PDGFRβ covariance in defined ROIs of PDGFRβ_TdTomato mouse brains.

**Widefield_10x_ROIs_Gfap-Pdgfrb_Handling.qmd:** [Quarto notebook, R code] Creation of point patterns from GFAP/PDGFRβ single cells detections in defined ROIs of PDGFRβ_TdTomato mouse brains.

**Widefield_10x_ROIs_Flox-Cre_Fish_Pdgfrb.qmd:** [Quarto notebook, R code] Analysis of PDGFRβ by Fluorescence in situ hybridization (FISH) in ROIs of KLF4-Flox and PDGFRβ-Cre mouse brains.

**Widefield_10x_ROIs_KO_CD31-ColIV_Coloc.qmd:** [Quarto notebook, R code] Analysis of CD31/ColIV-stained sections in defined ROIs of PDGFRβ_KLF4-KO mouse brains and corresponding controls.
 
**Widefield_10x_ROIs_KO_Pdgfrb_TDA.ipynb:** [Jupyter notebook, Python code] Topological Data Analysis (TDA) of PDGFRβ-positive cells in defined ROIs of PDGFRβ_KLF4-KO mouse brains and corresponding controls. 

**Widefield_20x_ROIs_KO_Picosirius.qmd:** [Quarto notebook, R code] Analysis of Picosirius staining in defined ROIs of PDGFRβ_KLF4-KO mouse brains and corresponding controls.

**Widefield_20x_ROIs_Pdgfrb_Haralick.qmd:** [Quarto notebook, R code] Analysis of Haralick features of PDGFRβ-positive cells in defined ROIs of PDGFRβ_TdTomato mouse brains.

**Widefield_20x_ROIs_Pdgfrb_Haralick_BatchScript.qmd:** [Quarto notebook, Python code] Extraction of Haralick features from PDGFRβ-positive cells in defined ROIs of PDGFRβ_TdTomato mouse brains.

**Widefield_20x_ROIs_Pdgfrb_TDA.ipynb:** [Jupyter notebook, Python code] Topological Data Analysis (TDA) of PDGFRβ-positive cells in defined ROIs of PDGFRβ_TdTomato mouse brains. 

**Widefield_5x_Ipsilateral_EarlyKO_Pdgfrb-Gfap.qmd:** [Quarto notebook, R code] Analysis of GFAP/PDGFRβ expression in the ischemic hemisphere of PDGFRβ_KLF4-KO mouse brains and corresponding controls.

**Widefield_5x_Ipsilateral_Gfap-Pdgfrb_Covariance.qmd:** [Quarto notebook, R code] Analysis of GFAP/PDGFRβ covariance (PPA) in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains.

**Widefield_5x_Ipsilateral_Gfap-Pdgfrb_Covariance_str.qmd:** [Quarto notebook, R code] Analysis of GFAP/PDGFRβ covariance (PPA) in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains with striatal-only lesions.

**Widefield_5x_Ipsilateral_Gfap-Pdgfrb_Handling.qmd:** [Quarto notebook, R code] Creation of point patterns from GFAP/PDGFRβ single cells detections in the ipsilateral hemipshere of PDGFRβ_TdTomato mouse brains.

**Widefield_5x_Ipsilateral_Gfap_Convex.qmd:** [Quarto notebook, R code] Analysis of GFAP convex hull in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains.

**Widefield_5x_Ipsilateral_Gfap_IntDen.qmd:** [Quarto notebook, R code] Analysis of GFAP integrated density (IntDen) in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains.

**Widefield_5x_Ipsilateral_KO_Structure.qmd:** [Quarto notebook, R code] Analysis of hemispheric shrinkage/atrophy in the ischemic hemisphere of PDGFRβ_KLF4-KO mouse brains.

**Widefield_5x_Ipsilateral_Pdgfrb_IntDen.qmd:** [Quarto notebook, R code] Analysis of PDGFRβ integrated density (IntDen) in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains.

**Widefield_5x_Ipsilateral_Pdgfrb_LowHigh.qmd:** [Quarto notebook, R code] Analysis of PDGFRβ_Low and PDGFRβ_High-expressing cells in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains.

**Widefield_5x_Ipsilateral_Pdgfrb_LowHigh_Str.qmd:** [Quarto notebook, R code] Analysis of PDGFRβ_Low and PDGFRβ_High-expressing cells in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains with striatal-only lesions.

**Widefield_5x_Ipsilateral_Pdgfrb_Shrinkage.qmd:** [Quarto notebook, R code] Analysis of hemispheric shrinkage/atrophy in the ischemic hemisphere of PDGFRβ_TdTomato mouse brains.


## Additional files

**PDGFR-B_Reactivity_SupplementaryTables.qmd:** [Quarto notebook, R code] Contains supplementary tables showcasing the results of the fitted models. 

**references.bib** [.bib file] Bibliography filed used ti generate citation/references in all Quarto notebooks. 

**science.csl** [Citation Style Language file] This files contains the Science Journal citation style implemented in the notebooks. Please note this is style is not associated to the journal the original research article is publish in. 


## Supplementary material

Please refer to the OSF repository https:doi.org/10.17605/OSF.IO/74MQN to access the Raw/processed data to run the notebooks in this repository.