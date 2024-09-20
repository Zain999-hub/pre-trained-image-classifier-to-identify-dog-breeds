#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#                                                                             
# PROGRAMMER: Zainab Muhammed Badawi
# DATE CREATED: 7/8/2024                                 
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename. This function inputs: 
#           - The Image Folder as image_dir within get_pet_labels function and 
#             as in_arg.dir for the function call within the main function. 
#          This function creates and returns the results dictionary as results_dic
#          within get_pet_labels function and as results within main. 
#          The results_dic dictionary has a 'key' that's the image filename and
#          a 'value' that's a list. This list will contain the following item
#          at index 0 : pet image label (string).
#
##
# Imports python modules
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py

from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels based on the filenames of the image files.
    Parameters:
     image_dir - The (full) path to the folder of images to be classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a list. 
                    The list contains the following item:
                        index 0 = pet image label (string)
    """
    filename_list = listdir(image_dir)
    results_dic = {}
    
    for filename in filename_list:
        if filename.startswith('.'):
            continue  # skip hidden files and directories
        
        # Extract pet label from filename
        pet_label = ''.join([i if not i.isdigit() else ' ' for i in filename.split('.')[0]])
        pet_label = pet_label.replace('_', ' ').strip().lower()
        
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print("** Warning: Duplicate files exist in directory:", filename)
    
    return results_dic
