import os
import json
import coreapi

print('Loading Schema Document')
# Initialize a client & load the schema document
client = coreapi.Client()
schema = client.get("https://healthsites.io/api/docs/")
print('Schema Document Loaded')

def getHealthFacilities(apiKey,pageNo,location):
    '''
    getHealthFacilities takes three arguments and returns metainfo of health facilities in list format.
    
    Parameters:
    apiKey (string)   -> api-key can be found in the user profile of healthsite (https://healthsites.io/)
    pageNo (string)   -> healthsite.io api requires A page number within the paginated result set.
                         If pageNo is a range, then entered the range as string seperated by comma(,)
                         For example: pageNo = "1,15". Here 1 is the starting pageNo and 15 is the ending pageNo.
    location (string) -> Countary Name of which health facilities want to get.
    
    Returns:
    Function returns a list of dictionary which containes the health facility data.
    
    Function also acts as a helper function for getFacilityData function where all the data is being saved in json formt.
    '''
    pageList = str(pageNo).split(',')
    startPage = int(pageList[0])
    endPage = int(pageList[-1]) + 1
    
    facilityList = []
    
    for i in range(startPage,endPage):
        # Interact with the API endpoint
        action = ["api", "v2", "facilities", "list"]
        params = {
            "api-key": apiKey,
            "page": i,
            "country": location,
#             "extent": ...,
#             "output": ...,
#             "from": ...,
#             "to": ...,
#             "flat-properties": ...,
#             "tag-format": ...,
        }

        result = client.action(schema, action, params=params)

        for facality in result:
            facilityList.append(facality)
            
    return facilityList

def getFacilityData(apiKey,pageNo,location):
    '''
    getFacilityData takes three arguments and returns metainfo of health facilities in a json format file.
    The function uses getHealthFacilities() function to get the list of dictionary which containes the health facility data.
    
    Parameters:
    apiKey (string)   -> api-key can be found in the user profile of healthsite (https://healthsites.io/)
    pageNo (string)   -> healthsite.io api requires A page number within the paginated result set.
                         If pageNo is a range, then entered the range as string seperated by comma(,)
                         For example: pageNo = "1,15". Here 1 is the starting pageNo and 15 is the ending pageNo.
    location (string) -> Countary Name of which health facilities want to get.
    
    Returns:
    Dumps all the data in a json file.
    '''
    
    facilityList = getHealthFacilities(apiKey,pageNo,location)
    
    outputFilename = ''.join([location,'_Facilities.json'])
    
    with open(outputFilename, 'w') as outfile:
        json.dump(facilityList, outfile)
        
    print('%s file has been created with health Facility Data' %(outputFilename))