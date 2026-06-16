from modules.automation.files import (

    create_folder,

    list_files,

    delete_folder
)

print(

    create_folder(
        "demo_folder"
    )
)

print(

    list_files()
)

print(

    delete_folder(
        "demo_folder"
    )
)