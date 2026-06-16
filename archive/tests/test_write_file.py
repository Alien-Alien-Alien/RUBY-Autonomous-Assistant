from modules.automation.files import (

    write_file,

    read_file
)

print(

    write_file(

        "demo.txt",

        "hello from assistant"
    )
)

print(

    read_file(

        "demo.txt"
    )
)