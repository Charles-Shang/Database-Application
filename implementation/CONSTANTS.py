# database
user = "root"
password = "cs348group11"
host = "cs348project.ceggb9lnr3wd.us-west-1.rds.amazonaws.com"
port = "3306"
sample_database_name = "productiondb"
TABLES = [
    "Access" "Actor",
    "Acts",
    "Celebrity",
    "Director",
    "Director_famousMovie",
    "Employee",
    "Movie",
    "Movie_category",
    "Permission",
    "Permits",
    "Person",
    "RateBy",
    "Rating",
    "Unique_id" "User",
]

# project
app_title = """

                                                                                                         
          ____       ,----..                                                                             
        ,'  , `.    /   /   \                   ,---,     ,---,.            .---.     ,---,. ,-.----.    
     ,-+-,.' _ |   /   .     :         ,---. ,`--.' |   ,'  .' |           /. ./|   ,'  .' | \    /  \   
  ,-+-. ;   , ||  .   /   ;.  \       /__./| |   :  : ,---.'   |       .--'.  ' ; ,---.'   | ;   :    \  
 ,--.'|'   |  ;| .   ;   /  ` ;  ,---.;  ; | :   |  ' |   |   .'      /__./ \ : | |   |   .' |   | .\ :  
|   |  ,', |  ': ;   |  ; \ ; | /___/ \  | | |   :  | :   :  |-,  .--'.  '   \' . :   :  |-, .   : |: |  
|   | /  | |  || |   :  | ; | ' \   ;  \ ' | '   '  ; :   |  ;/| /___/ \ |    ' ' :   |  ;/| |   |  \ :  
'   | :  | :  |, .   |  ' ' ' :  \   \  \: | |   |  | |   :   .' ;   \  \;      : |   :   .' |   : .  /  
;   . |  ; |--'  '   ;  \; /  |   ;   \  ' . '   :  ; |   |  |-,  \   ;  `      | |   |  |-, ;   | |  \  
|   : |  | ,      \   \  ',  /     \   \   ' |   |  ' '   :  ;/|   .   \    .\  ; '   :  ;/| |   | ;\  \ 
|   : '  |/        ;   :    /       \   `  ; '   :  | |   |    \    \   \   ' \ | |   |    \ :   ' | \.' 
;   | |`-'          \   \ .'         :   \ | ;   |.'  |   :   .'     :   '  |--"  |   :   .' :   : :-'   
|   ;/               `---`            '---"  '---'    |   | ,'        \   \ ;     |   | ,'   |   |.'     
'---'                                                 `----'           '---"      `----'     `---'       
                                                                                                         
"""
app_name = "MOVIEWER"

import textFormatter as tf

menus = [
    ["Top movies", ["tm", "<n>"]],
    ["Top actors", ["ta", "<n>"]],
    ["Top categories with movies", ["tc", "<n>", "<m>"]],
    ["Search a key word", ["search", "<movie/celebrity>"]],
    ["Functional Filtering", ["fsp"]],
    [
        f"List {tf.pink('fsp')} sub-options",
        ["list", "<region|year|category|letter|sortedBy|n>"],
    ],
    ["Graph diagrams", ["graph"]],
    ["Home page", ["home"]],
    [
        "Navigate a certain entry",
        ["navigate", "<movie|celebrity|director|actor>", "<id>"],
    ],
    ["Account login", ["login"]],
    ["Account register", ["register"]],
    ["My Profile", ["me"]],
    ["Command example", ["help", "<option>"]],
    ["Quit", ["q"]],
]

menus_user = [
    ["Top movies", ["tm", "<n>"]],
    ["Top actors", ["ta", "<n>"]],
    ["Top categories with movies", ["tc", "<n>", "<m>"]],
    ["Search a key word", ["search", "<movie/celebrity>"]],
    ["Functional Filtering", ["fsp"]],
    [
        f"List {tf.pink('fsp')} sub-options",
        ["list", "<region|year|category|letter|sortedBy|n>"],
    ],
    ["Graph diagrams", ["graph"]],
    ["Home page", ["home"]],
    [
        "Navigate a certain entry",
        ["navigate", "<movie|celebrity|director|actor|rating>", "<id>"],
    ],
    ["Account login", ["login"]],
    ["Account logout", ["logout"]],
    ["Account register", ["register"]],
    ["Rate a movie", ["rate", "<movie_id>"]],
    ["Modify", ["modify", "<rating>", "<update|delete>", "<rating_id>"]],
    ["My Profile", ["me"]],
    ["Command example", ["help", "<option>"]],
    ["Quit", ["q"]],
]


menus_employee = [
    ["Search a key word", ["search", "<movie/celebrity>"]],
    ["Top movies", ["tm", "<n>"]],
    ["Top actors", ["ta", "<n>"]],
    ["Top categories with movies", ["tc", "<n>", "<m>"]],
    ["Functional Filtering", ["fsp"]],
    [
        f"List {tf.pink('fsp')} sub-options",
        ["list", "<region|year|category|letter|sortedBy|n>"],
    ],
    ["Graph diagrams", ["graph"]],
    ["Home page", ["home"]],
    [
        "Navigate a certain entry",
        ["navigate", "<movie|celebrity|director|actor|rating>", "<id>"],
    ],
    ["Account login", ["login"]],
    ["Account logout", ["logout"]],
    ["Account register", ["register"]],
    ["Modify", ["modify", "<movie|rating>", "<update|delete>", "<rating_id>"]],
    ["My Profile", ["me"]],
    ["Command example", ["help", "<option>"]],
    ["Quit", ["q"]],
]

# User
from string import ascii_letters, digits

pwd_valid_chars = ascii_letters + digits + "_"

# info template
celebrity_template = """
\x1b[1;33;40mID:\x1b[0m %s\t\x1b[1;33;40mName:\x1b[0m %s
\x1b[1;33;40mNationality:\x1b[0m %s\t\x1b[1;33;40mBirth:\x1b[0m %s
\x1b[1;33;40mSummary:\x1b[0m
%s
"""

director_template = """
\x1b[1;33;40mID:\x1b[0m %s\t\x1b[1;33;40mName:\x1b[0m %s
\x1b[1;33;40mNationality:\x1b[0m %s\t\x1b[1;33;40mBirth:\x1b[0m %s\t\x1b[1;33;40mGraduation:\x1b[0m %s
\x1b[1;33;40mDirected Movie(s):\x1b[0m %s
\x1b[1;33;40mFamous Movie(s):\x1b[0m %s
\x1b[1;33;40mSummary:\x1b[0m
%s
"""

actor_template = """
\x1b[1;33;40mID:\x1b[0m %s\t\x1b[1;33;40mName:\x1b[0m %s
\x1b[1;33;40mNationality:\x1b[0m %s\t\x1b[1;33;40mBirth:\x1b[0m %s\t\x1b[1;33;40mOrganization:\x1b[0m %s
\x1b[1;33;40mActed Movie(s):\x1b[0m %s
\x1b[1;33;40mSummary:\x1b[0m
%s
"""

movie_template = """
\x1b[1;33;40mID:\x1b[0m %s\t\x1b[1;33;40mName:\x1b[0m %s\t\x1b[1;33;40mYear:\x1b[0m %s\t\x1b[1;33;40mRating:\x1b[0m %s
\x1b[1;33;40mRegion:\x1b[0m %s\t\x1b[1;33;40mCategory:\x1b[0m %s
\x1b[1;33;40mDirector:\x1b[0m %s\t\x1b[1;33;40mActor:\x1b[0m %s
\x1b[1;33;40mIntroduction:\x1b[0m
%s
"""

rating_template = """
\x1b[1;33;40mID:\x1b[0m %s\t\x1b[1;33;40mValue:\x1b[0m %s\t\x1b[1;33;40mMovie:\x1b[0m %s\t\x1b[1;33;40mTime:\x1b[0m %s
\x1b[1;33;40mComment:\x1b[0m
%s
"""
