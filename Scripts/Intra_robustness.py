#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""intra_robustness.py: Functions for generating intra robustness data """

import Classes_2

# region "Global Variables"
complete_primary_non_include_list = {"Adipocyte - breast": "pre", "Adipocyte - omental": "pre",
                                     "Adipocyte - perirenal": "pre", "Adipocyte - subcutaneous": "pre",
                                     "Endothelial Cells - Vein": "Umbilical",
                                     "Renal Epithelial Cells": "Cortical",
                                     "Skeletal Muscle Cells": ["satellite", "differentiated"]}
complete_primary_exclude_list = ["mesenchymal precursor cell - ovarian", "Osteoblast - differentiated",
                                 "Peripheral Blood Mononuclear Cells", "Whole blood"]
complete_primary_jit_exclude_list = {"CD14+ CD16- Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD14+ CD16+ Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD14- CD16+ Monocytes": ("CD14+ Monocytes", "CD16"),
                                     "CD4+CD25+CD45RA- memory regulatory T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25+CD45RA+ naive regulatory T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25-CD45RA- memory conventional T cells": ("CD4+ T Cells", "CD25"),
                                     "CD4+CD25-CD45RA+ naive conventional T cells": ("CD4+ T Cells", "CD25")}

complete_primary_cell_list = ["Adipocyte - breast", "Adipocyte - omental", "Adipocyte - perirenal",
                              "Adipocyte - subcutaneous", "Alveolar Epithelial Cells", "Amniotic Epithelial Cells",
                              "amniotic membrane cells", "Anulus Pulposus Cell", "Astrocyte - cerebellum",
                              "Astrocyte - cerebral cortex", "Basophils", "Bronchial Epithelial Cell",
                              "Cardiac Myocyte", "CD133+ stem cells - adult bone marrow derived",
                              "CD133+ stem cells - cord blood derived",
                              "CD14+ monocyte derived endothelial progenitor cells", "CD14+ Monocytes",
                              "CD14+ CD16- Monocytes", "CD14+ CD16+ Monocytes", "CD14- CD16+ Monocytes",
                              "CD19+ B Cells", "CD34 cells differentiated to erythrocyte lineage", "CD34+ Progenitors",
                              "CD34+ stem cells - adult bone marrow derived", "CD4+ T Cells",
                              "CD4+CD25+CD45RA- memory regulatory T cells", "CD4+CD25+CD45RA+ naive regulatory T cells",
                              "CD4+CD25-CD45RA- memory conventional T cells",
                              "CD4+CD25-CD45RA+ naive conventional T cells", "CD8+ T Cells", "Chondrocyte",
                              "chorionic membrane cells", "Ciliary Epithelial Cells", "common myeloid progenitor CMP",
                              "Corneal Epithelial Cells", "Dendritic Cells - monocyte immature derived",
                              "Dendritic Cells - plasmacytoid", "Endothelial Cells - Aortic",
                              "Endothelial Cells - Artery", "Endothelial Cells - Lymphatic",
                              "Endothelial Cells - Microvascular", "Endothelial Cells - Thoracic",
                              "Endothelial Cells - Umbilical vein", "Endothelial Cells - Vein", "Eosinophils",
                              "Esophageal Epithelial Cells", "Fibroblast - Aortic Adventitial", "Fibroblast - Cardiac",
                              "Fibroblast - Choroid Plexus", "Fibroblast - Conjunctival", "Fibroblast - Dermal",
                              "Fibroblast - Gingival", "Fibroblast - Lung", "Fibroblast - Lymphatic",
                              "Fibroblast - Mammary", "Fibroblast - Periodontal Ligament",
                              "Fibroblast - Pulmonary Artery", "Fibroblast - skin", "Fibroblast - Villous Mesenchymal",
                              "gamma delta positive T cells", "Gingival epithelial cells",
                              "granulocyte macrophage progenitor", "Hair Follicle Dermal Papilla Cells",
                              "Hair Follicle Outer Root Sheath Cells", "Hepatic Sinusoidal Endothelial Cells",
                              "Hepatic Stellate Cells (lipocyte)", "Hepatocyte", "immature langerhans cells",
                              "Intestinal epithelial cells (polarized)", "Iris Pigment Epithelial Cells",
                              "Keratinocyte - epidermal", "Keratinocyte - oral", "Keratocytes", "Lens Epithelial Cells",
                              "Macrophage - monocyte derived", "Mallassez-derived cells", "Mammary Epithelial Cell",
                              "Mast cell", "mature adipocyte", "Melanocyte", "Meningeal Cells",
                              "mesenchymal precursor cell - adipose", "mesenchymal precursor cell - bone marrow",
                              "mesenchymal precursor cell - cardiac", "Mesenchymal stem cells - adipose",
                              "Mesenchymal Stem Cells - amniotic membrane", "Mesenchymal Stem Cells - bone marrow",
                              "Mesenchymal stem cells - hepatic", "Mesenchymal stem cells - umbilical",
                              "Mesenchymal Stem Cells - Vertebral", "Mesenchymal Stem Cells - Wharton Jelly",
                              "Mesothelial Cells", "migratory langerhans cells",
                              "Multipotent Cord Blood Unrestricted Somatic Stem Cells", "Myoblast",
                              "nasal epithelial cells", "Natural Killer Cells", "Neural stem cells", "Neurons",
                              "Neutrophil", "Nucleus Pulposus Cell", "Olfactory epithelial cells",
                              "Oligodendrocyte - precursors", "Osteoblast", "Pancreatic stromal cells", "Pericytes",
                              "Perineurial Cells", "Placental Epithelial Cells",
                              "Preadipocyte - breast", "Preadipocyte - omental", "Preadipocyte - perirenal",
                              "Preadipocyte - subcutaneous", "Preadipocyte - visceral", "promyelocytes",
                              "Prostate Epithelial Cells", "Prostate Stromal Cells", "Renal Cortical Epithelial Cells",
                              "Renal Epithelial Cells", "Renal Glomerular Endothelial Cells", "Renal Mesangial Cells",
                              "Renal Proximal Tubular Epithelial Cell", "Retinal Pigment Epithelial Cells",
                              "salivary acinar cells", "Schwann Cells", "Sebocyte", "Sertoli Cells",
                              "Skeletal Muscle Cells", "Skeletal muscle cells differentiated into Myotubes",
                              "Skeletal Muscle Satellite Cells", "Small Airway Epithelial Cells",
                              "Smooth muscle cells - airway", "Smooth Muscle Cells - Aortic",
                              "Smooth Muscle Cells - Bladder", "Smooth Muscle Cells - Brachiocephalic",
                              "Smooth Muscle Cells - Brain Vascular", "Smooth Muscle Cells - Bronchial",
                              "Smooth Muscle Cells - Carotid", "Smooth Muscle Cells - Colonic",
                              "Smooth Muscle Cells - Coronary Artery", "Smooth Muscle Cells - Esophageal",
                              "Smooth Muscle Cells - Internal Thoracic Artery", "Smooth Muscle Cells - Intestinal",
                              "Smooth Muscle Cells - Prostate", "Smooth Muscle Cells - Pulmonary Artery",
                              "Smooth Muscle Cells - Subclavian Artery", "Smooth Muscle Cells - Tracheal",
                              "Smooth Muscle Cells - Umbilical artery", "Smooth Muscle Cells - Umbilical Vein",
                              "Smooth Muscle Cells - Uterine", "Synoviocyte", "tenocyte", "Trabecular Meshwork Cells",
                              "Tracheal Epithelial Cells", "Urothelial cells"]

three_donors_cell_list = ["Adipocyte - omental", "Adipocyte - subcutaneous", "Alveolar Epithelial Cells",
                          "Amniotic Epithelial Cells", "amniotic membrane cells", "Astrocyte - cerebellum",
                          "Astrocyte - cerebral cortex", "Basophils", "Cardiac Myocyte", "CD14+CD16- Monocytes",
                          "CD14+CD16+ Monocytes", "CD14-CD16+ Monocytes",
                          "chorionic membrane cells", "Ciliary Epithelial Cells", "Corneal Epithelial Cells",
                          "Dendritic Cells - plasmacytoid",
                          "Endothelial Cells - Artery", "Endothelial Cells - Lymphatic",
                          "Endothelial Cells - Microvascular", "Endothelial Cells - Umbilical vein",
                          "Endothelial Cells - Vein", "Eosinophils", "Esophageal Epithelial Cells",
                          "Fibroblast - Aortic Adventitial", "Fibroblast - Choroid Plexus",
                          "Fibroblast - Lung", "Fibroblast - Lymphatic", "Fibroblast - Mammary",
                          "Fibroblast - Villous Mesenchymal", "Gingival epithelial cells",
                          "granulocyte macrophage progenitor", "Hair Follicle Dermal Papilla Cells",
                          "Hepatic Sinusoidal Endothelial Cells", "Hepatic Stellate Cells (lipocyte)", "Hepatocyte",
                          "Keratinocyte - epidermal", "Keratocytes", "Lens Epithelial Cells",
                          "Macrophage - monocyte derived", "Mallassez-derived cells", "Mammary Epithelial Cell",
                          "Meningeal Cells", "mesenchymal precursor cell - adipose",
                          "mesenchymal precursor cell - bone marrow", "Mesenchymal stem cells - hepatic",
                          "Mesothelial Cells", "migratory langerhans cells",
                          "Myoblast", "Natural Killer Cells", "Neurons", "Nucleus Pulposus Cell", "Osteoblast",
                          "Pericytes", "Placental Epithelial Cells", "Preadipocyte - omental",
                          "Preadipocyte - subcutaneous", "Preadipocyte - visceral", "Prostate Epithelial Cells",
                          "Prostate Stromal Cells", "Renal Epithelial Cells", "Renal Mesangial Cells",
                          "Renal Proximal Tubular Epithelial Cell",
                          "salivary acinar cells", "Schwann Cells", "Sebocyte",
                          "Skeletal muscle cells differentiated into Myotubes - multinucleated",
                          "Skeletal Muscle Satellite Cells", "Small Airway Epithelial Cells",
                          "Smooth Muscle Cells - Brachiocephalic",
                          "Smooth Muscle Cells - Brain Vascular", "Smooth Muscle Cells - Carotid",
                          "Smooth Muscle Cells - Colonic", "Smooth Muscle Cells - Coronary Artery",
                          "Smooth Muscle Cells - Internal Thoracic Artery", "Smooth Muscle Cells - Prostate",
                          "Smooth Muscle Cells - Pulmonary Artery", "Smooth Muscle Cells - Subclavian Artery",
                          "Smooth Muscle Cells - Tracheal",
                          "Smooth Muscle Cells - Umbilical Vein", "Synoviocyte",
                          "tenocyte", "Trabecular Meshwork Cells", "Tracheal Epithelial Cells"]
four_donors_cell_list = ["Smooth Muscle Cells - Umbilical Artery", "Retinal Pigment Epithelial Cells",
                         "Smooth Muscle Cells - Aortic", "Mesenchymal Stem Cells - umbilical",
                         "Endothelial Cells - Aortic", "Mesenchymal Stem Cells - adipose", "Urothelial Cells",
                         "mature adipocyte", "Mesenchymal Stem Cells - bone marrow", "Olfactory epithelial cells"]
# endregion "Global variables"

# region "Setup Variables"
cell_list = complete_primary_cell_list
vens_to_take = 20
combinations_number = 4
threshold = 90

# endregion "Global variables"

if __name__ == "__main__":
    initialize_promoters = Classes_2.Promoters("hg19.cage_peak_phase1and2combined_tpm.osc.txt",
                                               cell_list,
                                               celltype_exclude=complete_primary_exclude_list,
                                               not_include=complete_primary_non_include_list,
                                               partial_exclude=complete_primary_jit_exclude_list,
                                               sample_types="primary cells",
                                               second_parser=None)
    """ All cell types 
    # use: cell_list = complete_primary_cell_list
    initialize_promoters.codes_to_csv("codes_all_cells.csv", "list", "/Figure 2/Test codes/")
    initialize_promoters.celltypes_to_csv("celltypes_all.csv", "list", "/Figure 2/Test codes/")
    """

    """ 3 Donors
    # use: cell_list = three_donors_cell_list
    initialize_promoters.codes_to_csv("codes_3_donors.csv", "list", "/Figure 2/Test codes/")
    initialize_promoters.celltypes_to_csv("celltypes_3_donors.csv", "list", "/Figure 2/Test codes/")
    """

    """ 4 Donors
    # use: cell_list = four_donors_cell_list
    initialize_promoters.codes_to_csv("codes_4_donors.csv", "list", "/Figure 2/Test codes/")
    initialize_promoters.celltypes_to_csv("celltypes_4_donors.csv", "list", "/Figure 2/Test codes/")
    """

    initialize_promoters.intra_individual_robustness(combinations_number, vens_to_take, threshold=threshold)
# TODO: run intra for cancer cell lines: All, 3 donors, 4 donors, etc..
# TODO: run intra for All cell lines (I only have old 156 celltypes file)
