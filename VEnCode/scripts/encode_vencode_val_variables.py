# Note: index are FANTOM5 cel types and columns are ENCODE cell types

index_promoter_order = ['CD34 cells differentiated to erythrocyte lineage', 'Hepatocyte', 'promyelocytes',
                        'Adipocyte - perirenal', 'migratory langerhans cells', 'chorionic membrane cells',
                        'Dendritic Cells - monocyte immature derived', 'Macrophage - monocyte derived',
                        'CD14+ monocyte derived endothelial progenitor cells', 'Mast cell', 'mature adipocyte',
                        'Placental Epithelial Cells', 'Sertoli Cells', 'Hair Follicle Dermal Papilla Cells',
                        'Smooth Muscle Cells - Umbilical Vein', 'immature langerhans cells', 'tenocyte',
                        'Alveolar Epithelial Cells', 'Synoviocyte', 'Smooth muscle cells - airway',
                        'CD14+ CD16+ Monocytes', 'Preadipocyte - perirenal', 'Adipocyte - breast',
                        'Preadipocyte - omental', 'Preadipocyte - breast', 'Corneal Epithelial Cells',
                        'salivary acinar cells', 'Fibroblast - Mammary', 'Fibroblast - Lymphatic',
                        'Keratinocyte - epidermal', 'Sebocyte', 'Chondrocyte', 'gamma delta positive T cells',
                        'amniotic membrane cells', 'Pericytes', 'Adipocyte - subcutaneous', 'Myoblast',
                        'Dendritic Cells - plasmacytoid', 'CD19+ B Cells', 'Mesenchymal stem cells - umbilical',
                        'granulocyte macrophage progenitor', 'common myeloid progenitor CMP', 'CD34+ Progenitors',
                        'CD133+ stem cells - cord blood derived', 'CD34+ stem cells - adult bone marrow derived',
                        'CD133+ stem cells - adult bone marrow derived', 'Amniotic Epithelial Cells',
                        'Hair Follicle Outer Root Sheath Cells', 'Neural stem cells', 'Urothelial cells',
                        'Endothelial Cells - Vein', 'Fibroblast - Choroid Plexus',
                        'mesenchymal precursor cell - bone marrow', 'mesenchymal precursor cell - cardiac',
                        'mesenchymal precursor cell - adipose', 'Keratinocyte - oral', 'nasal epithelial cells',
                        'Mammary Epithelial Cell', 'Small Airway Epithelial Cells', 'Mallassez-derived cells',
                        'Gingival epithelial cells', 'Renal Glomerular Endothelial Cells',
                        'Smooth Muscle Cells - Tracheal', 'Smooth Muscle Cells - Bladder',
                        'Intestinal epithelial cells (polarized)', 'Smooth Muscle Cells - Umbilical artery',
                        'Olfactory epithelial cells', 'Nucleus Pulposus Cell', 'Mesenchymal stem cells - hepatic',
                        'Mesothelial Cells', 'Mesenchymal Stem Cells - Wharton Jelly', 'Trabecular Meshwork Cells',
                        'Hepatic Stellate Cells (lipocyte)', 'Multipotent Cord Blood Unrestricted Somatic Stem Cells',
                        'Iris Pigment Epithelial Cells', 'Neurons', 'Smooth Muscle Cells - Uterine',
                        'Oligodendrocyte - precursors', 'Smooth Muscle Cells - Intestinal', 'Osteoblast',
                        'Endothelial Cells - Microvascular', 'Endothelial Cells - Artery',
                        'Endothelial Cells - Thoracic', 'Schwann Cells', 'Fibroblast - Villous Mesenchymal',
                        'Smooth Muscle Cells - Esophageal', 'Smooth Muscle Cells - Bronchial', 'Renal Mesangial Cells',
                        'Astrocyte - cerebellum', 'Pancreatic stromal cells', 'Keratocytes',
                        'Fibroblast - Conjunctival', 'Mesenchymal Stem Cells - amniotic membrane',
                        'Prostate Stromal Cells', 'Smooth Muscle Cells - Colonic',
                        'Smooth Muscle Cells - Brain Vascular', 'Retinal Pigment Epithelial Cells',
                        'Ciliary Epithelial Cells', 'Astrocyte - cerebral cortex', 'Lens Epithelial Cells',
                        'Fibroblast - Pulmonary Artery', 'Endothelial Cells - Umbilical vein',
                        'Endothelial Cells - Lymphatic', 'Meningeal Cells', 'Mesenchymal Stem Cells - Vertebral',
                        'Renal Proximal Tubular Epithelial Cell', 'Renal Cortical Epithelial Cells']

index_enhancer_order = ['Basophils', 'Natural Killer Cells', 'immature langerhans cells',
                        'gamma delta positive T cells', 'Dendritic Cells - plasmacytoid', 'CD34+ Progenitors',
                        'Keratinocyte - oral', 'Mast cell', 'CD4+CD25+CD45RA- memory regulatory T cells', 'Hepatocyte',
                        'CD19+ B Cells', 'CD133+ stem cells - cord blood derived',
                        'CD34 cells differentiated to erythrocyte lineage', 'mature adipocyte', 'Neural stem cells',
                        'Preadipocyte - perirenal', 'CD133+ stem cells - adult bone marrow derived',
                        'migratory langerhans cells', 'Neurons', 'CD14+ monocyte derived endothelial progenitor cells',
                        'Urothelial cells', 'amniotic membrane cells', 'salivary acinar cells',
                        'Macrophage - monocyte derived', 'Tracheal Epithelial Cells', 'Endothelial Cells - Vein',
                        'Smooth Muscle Cells - Bladder', 'CD34+ stem cells - adult bone marrow derived',
                        'Hair Follicle Dermal Papilla Cells', 'chorionic membrane cells',
                        'Intestinal epithelial cells (polarized)', 'Placental Epithelial Cells',
                        'Adipocyte - perirenal', 'Alveolar Epithelial Cells', 'Amniotic Epithelial Cells', 'Myoblast',
                        'nasal epithelial cells', 'mesenchymal precursor cell - bone marrow',
                        'Oligodendrocyte - precursors', 'Endothelial Cells - Microvascular', 'Adipocyte - subcutaneous',
                        'Prostate Epithelial Cells', 'Keratinocyte - epidermal', 'Small Airway Epithelial Cells',
                        'Gingival epithelial cells', 'Mallassez-derived cells', 'mesenchymal precursor cell - cardiac',
                        'Multipotent Cord Blood Unrestricted Somatic Stem Cells',
                        'mesenchymal precursor cell - adipose', 'Smooth Muscle Cells - Intestinal', 'Mesothelial Cells',
                        'Synoviocyte', 'Renal Mesangial Cells', 'Mammary Epithelial Cell',
                        'Mesenchymal Stem Cells - amniotic membrane', 'Hair Follicle Outer Root Sheath Cells',
                        'Preadipocyte - subcutaneous', 'Skeletal muscle cells differentiated into Myotubes',
                        'Endothelial Cells - Artery', 'Endothelial Cells - Thoracic',
                        'Retinal Pigment Epithelial Cells', 'Olfactory epithelial cells',
                        'Mesenchymal stem cells - hepatic', 'Iris Pigment Epithelial Cells',
                        'Smooth Muscle Cells - Umbilical artery', 'Fibroblast - Conjunctival', 'Osteoblast',
                        'Endothelial Cells - Lymphatic', 'Endothelial Cells - Umbilical vein', 'Renal Epithelial Cells',
                        'tenocyte', 'Pericytes', 'Renal Cortical Epithelial Cells',
                        'Renal Proximal Tubular Epithelial Cell', 'Astrocyte - cerebral cortex',
                        'Smooth Muscle Cells - Brachiocephalic', 'Adipocyte - omental', 'Adipocyte - breast',
                        'Preadipocyte - breast', 'Preadipocyte - omental', 'Astrocyte - cerebellum',
                        'Smooth Muscle Cells - Uterine', 'Preadipocyte - visceral',
                        'Mesenchymal Stem Cells - Wharton Jelly', 'Ciliary Epithelial Cells',
                        'Hepatic Stellate Cells (lipocyte)', 'Pancreatic stromal cells',
                        'Skeletal Muscle Satellite Cells', 'Lens Epithelial Cells',
                        'Mesenchymal Stem Cells - Vertebral', 'Smooth Muscle Cells - Esophageal',
                        'Fibroblast - Pulmonary Artery', 'Fibroblast - Aortic Adventitial', 'Perineurial Cells',
                        'Meningeal Cells', 'Smooth Muscle Cells - Brain Vascular', 'Prostate Stromal Cells',
                        'Smooth Muscle Cells - Colonic', 'Smooth Muscle Cells - Bronchial', 'Anulus Pulposus Cell',
                        'Nucleus Pulposus Cell', 'CD14+ CD16- Monocytes', 'CD14+ CD16+ Monocytes']

columns_promoter_order = ['osteoblast', 'trophoblast cell', 'CD14-positive monocyte',
                          'common myeloid progenitor, CD34-positive',
                          'CD1c-positive myeloid dendritic cell', 'naive B cell', 'hepatocyte', 'foreskin keratinocyte',
                          'epithelial cell of esophagus', 'bronchial epithelial cell', 'hepatic stellate cell',
                          'foreskin fibroblast', 'endothelial cell of umbilical vein',
                          'lung microvascular endothelial cell',
                          'dermis blood vessel endothelial cell',
                          'dermis microvascular lymphatic vessel endothelial cell',
                          'astrocyte of the hippocampus', 'foreskin melanocyte', 'epidermal melanocyte',
                          'skeletal muscle myoblast', 'T-helper 17 cell', 'regulatory T cell',
                          'astrocyte of the spinal cord',
                          'keratinocyte', 'dedifferentiated amniotic fluid mesenchymal stem cell',
                          'mammary epithelial cell',
                          'renal cortical epithelial cell', 'fibroblast of lung', 'astrocyte',
                          'amniotic epithelial cell',
                          'fibroblast of villous mesenchyme', 'cardiac fibroblast', 'fibroblast of dermis',
                          'fibroblast of mammary gland', 'choroid plexus epithelial cell',
                          'iris pigment epithelial cell',
                          'cardiac muscle cell', 'fibroblast of pulmonary artery',
                          'fibroblast of the aortic adventitia',
                          'fibroblast of peridontal ligament', 'fibroblast of gingiva', 'epithelial cell of prostate',
                          'retinal pigment epithelial cell', 'fibroblast of skin of scalp',
                          'fibroblast of skin of upper back',
                          'fibroblast of skin of right quadriceps', 'fibroblast of skin of right biceps',
                          'epithelial cell of proximal tubule', 'kidney epithelial cell', 'brain pericyte',
                          'smooth muscle cell of the brain vasculature', 'glomerular endothelial cell',
                          'pulmonary artery endothelial cell', 'stromal cell of bone marrow',
                          'brain microvascular endothelial cell', 'non-pigmented ciliary epithelial cell',
                          'fibroblast of the conjunctiva', 'astrocyte of the cerebellum', 'skeletal muscle cell',
                          'fibroblast of skin of abdomen', 'fibroblast of skin of left quadriceps',
                          'fibroblast of skin of left biceps', 'T-helper 1 cell', 'B cell', 'T-helper 2 cell',
                          'naive thymus-derived CD4-positive, alpha-beta T cell', 'CD4-positive, alpha-beta T cell',
                          'CD8-positive, alpha-beta T cell', 'T-cell', 'natural killer cell']

columns_enhancer_order = ['osteoblast', 'trophoblast cell', 'common myeloid progenitor, CD34-positive',
                          'foreskin melanocyte', 'foreskin keratinocyte', 'epithelial cell of esophagus',
                          'bronchial epithelial cell', 'renal cortical epithelial cell', 'CD14-positive monocyte',
                          'CD1c-positive myeloid dendritic cell', 'skeletal muscle myoblast', 'naive B cell', 'B cell',
                          'endothelial cell of umbilical vein', 'lung microvascular endothelial cell',
                          'dermis blood vessel endothelial cell',
                          'dermis microvascular lymphatic vessel endothelial cell', 'epidermal melanocyte',
                          'hepatic stellate cell', 'foreskin fibroblast', 'fibroblast of villous mesenchyme',
                          'astrocyte of the hippocampus', 'keratinocyte', 'mammary epithelial cell',
                          'epithelial cell of prostate', 'retinal pigment epithelial cell',
                          'dedifferentiated amniotic fluid mesenchymal stem cell', 'pulmonary artery endothelial cell',
                          'glomerular endothelial cell', 'kidney epithelial cell', 'epithelial cell of proximal tubule',
                          'stromal cell of bone marrow', 'brain pericyte',
                          'smooth muscle cell of the brain vasculature', 'astrocyte of the cerebellum',
                          'fibroblast of the conjunctiva', 'skeletal muscle cell', 'fibroblast of skin of abdomen',
                          'fibroblast of skin of left quadriceps', 'fibroblast of skin of left biceps',
                          'brain microvascular endothelial cell', 'non-pigmented ciliary epithelial cell',
                          'fibroblast of skin of scalp', 'fibroblast of skin of upper back',
                          'fibroblast of skin of right quadriceps', 'fibroblast of skin of right biceps',
                          'astrocyte of the spinal cord', 'fibroblast of lung', 'astrocyte', 'fibroblast of gingiva',
                          'fibroblast of peridontal ligament', 'amniotic epithelial cell',
                          'choroid plexus epithelial cell', 'iris pigment epithelial cell',
                          'fibroblast of the aortic adventitia', 'cardiac fibroblast', 'cardiac muscle cell',
                          'fibroblast of pulmonary artery', 'fibroblast of mammary gland', 'fibroblast of dermis',
                          'hepatocyte', 'CD4-positive, alpha-beta T cell', 'T-helper 17 cell', 'regulatory T cell',
                          'CD8-positive, alpha-beta T cell', 'naive thymus-derived CD4-positive, alpha-beta T cell',
                          'T-cell', 'natural killer cell', 'T-helper 1 cell', 'T-helper 2 cell']

index_promoter_matching = ['Amniotic Epithelial Cells', 'Astrocyte - cerebellum', 'CD14+ CD16+ Monocytes',
                           'CD19+ B Cells',
                           'Ciliary Epithelial Cells', 'common myeloid progenitor CMP', 'Endothelial Cells - Artery',
                           'Endothelial Cells - Lymphatic', 'Endothelial Cells - Microvascular',
                           'Endothelial Cells - Umbilical vein', 'Fibroblast - Conjunctival', 'Fibroblast - Mammary',
                           'Fibroblast - Pulmonary Artery', 'Fibroblast - Villous Mesenchymal',
                           'Hepatic Stellate Cells (lipocyte)', 'Hepatocyte', 'Iris Pigment Epithelial Cells',
                           'Keratinocyte - epidermal', 'Mammary Epithelial Cell', 'Myoblast', 'Osteoblast', 'Pericytes',
                           'Renal Cortical Epithelial Cells', 'Renal Glomerular Endothelial Cells',
                           'Renal Proximal Tubular Epithelial Cell', 'Retinal Pigment Epithelial Cells',
                           'Smooth Muscle Cells - Brain Vascular']

columns_promoter_matching = ['amniotic epithelial cell', 'astrocyte of the cerebellum', 'CD14-positive monocyte',
                             'B cell',
                             'non-pigmented ciliary epithelial cell', 'common myeloid progenitor, CD34-positive',
                             'pulmonary artery endothelial cell',
                             'dermis microvascular lymphatic vessel endothelial cell',
                             'brain microvascular endothelial cell', 'endothelial cell of umbilical vein',
                             'fibroblast of the conjunctiva', 'fibroblast of mammary gland',
                             'fibroblast of pulmonary artery',
                             'fibroblast of villous mesenchyme', 'hepatic stellate cell', 'hepatocyte',
                             'iris pigment epithelial cell', 'keratinocyte', 'mammary epithelial cell',
                             'skeletal muscle myoblast', 'osteoblast', 'brain pericyte',
                             'renal cortical epithelial cell',
                             'glomerular endothelial cell', 'epithelial cell of proximal tubule',
                             'retinal pigment epithelial cell', 'smooth muscle cell of the brain vasculature']

index_enhancer_matching = ['Amniotic Epithelial Cells', 'Astrocyte - cerebellum', 'CD14+ CD16+ Monocytes',
                           'CD19+ B Cells', 'CD34+ Progenitors', 'Ciliary Epithelial Cells',
                           'Endothelial Cells - Artery', 'Endothelial Cells - Lymphatic',
                           'Endothelial Cells - Microvascular', 'Endothelial Cells - Umbilical vein',
                           'Fibroblast - Aortic Adventitial', 'Fibroblast - Conjunctival',
                           'Fibroblast - Pulmonary Artery', 'Hepatic Stellate Cells (lipocyte)', 'Hepatocyte',
                           'Iris Pigment Epithelial Cells', 'Keratinocyte - epidermal', 'Mammary Epithelial Cell',
                           'Myoblast', 'Natural Killer Cells', 'Osteoblast', 'Pericytes', 'Prostate Epithelial Cells',
                           'Renal Cortical Epithelial Cells', 'Renal Proximal Tubular Epithelial Cell',
                           'Retinal Pigment Epithelial Cells', 'Smooth Muscle Cells - Brain Vascular']

columns_enhancer_matching = ['amniotic epithelial cell', 'astrocyte of the cerebellum', 'CD14-positive monocyte',
                             'B cell', 'common myeloid progenitor, CD34-positive',
                             'non-pigmented ciliary epithelial cell', 'pulmonary artery endothelial cell',
                             'dermis microvascular lymphatic vessel endothelial cell',
                             'brain microvascular endothelial cell', 'endothelial cell of umbilical vein',
                             'fibroblast of the aortic adventitia', 'fibroblast of the conjunctiva',
                             'fibroblast of pulmonary artery', 'hepatic stellate cell', 'hepatocyte',
                             'iris pigment epithelial cell', 'keratinocyte', 'mammary epithelial cell',
                             'skeletal muscle myoblast', 'natural killer cell', 'osteoblast', 'brain pericyte',
                             'epithelial cell of prostate', 'renal cortical epithelial cell',
                             'epithelial cell of proximal tubule', 'retinal pigment epithelial cell',
                             'smooth muscle cell of the brain vasculature']

index_promoter_order_200bp = index_promoter_order.copy()
index_promoter_order_200bp.append("Basophils")