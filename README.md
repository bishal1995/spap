API Documentation.

1) For getting user detail after login

### [GET]  '127.0.0.1:8080/user/info/'

    + Header
        Authorization : Token sfd78g5sfd67g5sd5fg76sdf5g5gdfgddsfg57s6df5gsd75fg

2) For registering a species

## [PUT] - "127.0.0.1:8080/regspecies/plantae/"  -- For saving ( registering ) a species

    + Header
        Authorization : Token sfd78g5sfd67g5sd5fg76sdf5g5gdfgddsfg57s6df5gsd75fg

+ Request  200 (application/json)

        {
            "plantae" : "<plantae_id">,             # Species ID to be selected from dropdown,API "127.0.0.1:8080/plantaelist/?from=20" return registered species of pk 20 - 30
            "images" : "<images_media_id>",         # Image Id that we recieve after sucessfully saving a image to "127.0.0.1/media/plantaeImg/"
            "beat" : "<beat_id>",                   # Beat ID to be selected from dropdown 
            "state" : "<state>",                    # eg : "ASSAM" ,  to be selected from a state list , may use ASSAM as default 
            "district" : "<district>",              # eg : "CACHAR" ,  to be selected from a district list , may use CACHAR as default
            "latitude" : "12.121212",               # latitude , after decimal should contain only 6 digit
            "longitude" : "12.121212",              # longitude , after decimal should contain only 6 digit
            "ptype" : "<ptype>",                    # Options - 'SB' :Seed Bearing,'IG': indigenous tree,'IP':Indigenous patch(the one with multiple location)
            "patch" : "[                            # Patch cordinates array ,  this field will not be present in seed bearing and indigenous tree
                        [12.121212 , 12.121212],    # patch field will only be present in the indigenous   patch tree
                        [12.121212 , 12.121212],  
                        [12.121212 , 12.121212],  
                        [12.121212 , 12.121212],  
                        [12.121212 , 12.121212],  
                        [12.121212 , 12.121212],  
                        [12.121212 , 12.121212],  
                        [12.121212 , 12.121212],  
                        [12.121212 , 12.121212],  
                        [12.121212 , 12.121212],
                      ]"                       
        }