def get_media_type(filename):
    """
    Determine the media type based on the file extension.

    Parameters:
    filename (str): The name of the file.

    Returns:
    str: The media type.
    """
    # Define the mapping of file extensions to media types
    media_types = {
        '.gif': 'image/gif',
        '.jpg': 'image/jpeg',
        '.jpeg': 'image/jpeg',
        '.png': 'image/png',
        '.pdf': 'application/pdf',
        '.txt': 'text/plain',
        '.zip': 'application/zip'
    }

    # Strip any leading or trailing whitespace and convert the filename to lowercase
    filename = filename.strip().lower()

    # Extract the file extension
    if '.' in filename:
        ext = '.' + filename.rsplit('.', 1)[-1]
    else:
        ext = ''

    # Return the appropriate media type or default to application/octet-stream
    return media_types.get(ext, 'application/octet-stream')

def main():
    # Prompt the user for the name of the file
    filename = input("Enter the name of the file: ")

    # Get and print the media type
    media_type = get_media_type(filename)
    print(media_type)

# Call the main function
if __name__ == "__main__":
    main()
