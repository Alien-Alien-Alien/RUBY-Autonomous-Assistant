from pathlib import Path


def create_folder(folder_name):

    try:

        Path(folder_name).mkdir(
            exist_ok=True
        )

        return {

            "success": True,

            "message": f"Folder '{folder_name}' created."
        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)
        }


def list_files():

    try:

        current_path = Path(".")

        files = [

            item.name

            for item in current_path.iterdir()
        ]

        return {

            "success": True,

            "files": files
        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)
        }


def delete_folder(folder_name):

    try:

        path = Path(folder_name)

        if path.exists() and path.is_dir():

            path.rmdir()

            return {

                "success": True,

                "message": f"Folder '{folder_name}' deleted."
            }

        return {

            "success": False,

            "message": "Folder does not exist."
        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)
        }
def read_file(file_path):

    try:

        with open(
            file_path,
            "r"
        ) as file:

            content = file.read()

        return {

            "success": True,

            "content": content
        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)
        }

def write_file(
    file_path,
    content
):

    try:

        with open(
            file_path,
            "w"
        ) as file:

            file.write(
                content
            )

        return {

            "success": True,

            "message": f"{file_path} written"
        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)
        }
        
def create_file(file_path):

    try:

        with open(
            file_path,
            "a"
        ):
            pass

        return {

            "success": True,

            "message": f"{file_path} created"
        }

    except Exception as e:

        return {

            "success": False,

            "message": str(e)
        }