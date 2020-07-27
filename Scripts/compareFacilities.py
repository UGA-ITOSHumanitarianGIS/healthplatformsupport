import os
import json
import pandas as pd
from pandas import DataFrame as df

def getFacilityName(healthFacility):
    '''
    Parameter:
    healthFacility (DataFrame) --> A dataframe of health facility
    
    Returns:
    healthFacilityList (list) - list of health facility names in lower case.
    '''
    healthFacilityList = [each_facility.lower() for each_facility in healthFacility['FacilityName'].to_list()]
    
    return healthFacilityList

def compareByNames(kaggleSRC, healthsiteSRC):
    '''
    Parameters:
    kaggleSRC     (string) --> path for kaggle health facility csv file. 
    healthsiteSRC (string) --> path for healthsite health facility excel file.
    
    Creates a excel file which has matched health facilities. The comparision is done by facility names.
    '''
    
    kaggleHealthFacility = pd.read_csv(kaggleSRC)
    healthsiteFacility = pd.read_excel(healthsiteSRC)
    
    kaggleFacility = getFacilityName(kaggleHealthFacility)
    
    matchFacility = []
    for i in range(len(healthsiteFacility)):
        try:
            if healthsiteFacility.iloc[i,:]['name'].lower() in kaggleFacility:
                matchFacility.append(healthsiteFacility.iloc[i,:])
        except:
            pass
        
    print("%d health facilities are matched by facility names."%(len(matchFacility)))
    print("")
    
    df(matchFacility).to_excel('compared_facilities_byName.xlsx',index=False)    

    print("Matched Facilities are stored in compared_facilities_byName.xlsx file.")
    
def main():
    print("Enter the Kaggle Health Facility file(csv) path.")
    kagglePath = str(input())
    print("")
    print("Enter the healthsite.io Health Facility file(csv) path.")
    healthsitePath = str(input())
    print("")
    
    compareByNames(kagglePath,healthsitePath)
    
if __name__ == "__main__":
    main()