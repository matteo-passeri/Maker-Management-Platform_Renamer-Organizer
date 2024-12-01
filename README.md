# 3D Models Renamer-Organizer (Ex. for Thingiverse)
## for Maker-Management-Platform (MMP)

---

Sites (like Thingiverse) has the downloaded models in a structure folders tree, but MMP wants just a folder with the files inside; so this script flat the folder structure to be use by MMP.
(I use it for every downloaded model to just rename the folders too)

It also improve the name of the folder:

 - Remove the ID at the end, if present (including the ' - ' prefix)
 - Capitalize every first letter of a word
 - Replace with a space, symbols as: '+\_+', '\_', '+', '-'
 - Remove, at the end of the name folder, words as: 'stls', 'model Files', 'print Files'
 - Remove spaces at the beginning or a the end of the name folder


### TODO

 - Remove or substitute letters that break the script (Ex. ideograms)
