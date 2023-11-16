# Import pip and requests to download the resource URL content if the url is valid
import pip
import requests

# Define a function with one parameter for the url that takes a url from user input and determines whether it is a valid resource url or not.
def validate_url(url):
    
    # Define lists for valid resource protocols and file extensions
    valid_protocols = ["http", "https", "ftp"]
    valid_fileinfo = ["html", "csv", "docx"]

    """
    Seperate the url into useful components and
    identify their place in the list for later use:
        1. Resource Protocol = url_prot[0]
        2. Resource File Extension = url_finfo[1]
        3. Resource File Name = filename[1]
    """
    url_prot = url.split("://", 1)
    url_finfo = url.rsplit(".", 1)
    filename = url.rsplit("/", 1)

    # Check if the url protocol is valid
    if url_prot[0] in valid_protocols:
        # Check if the url file extension is valid
        if url_finfo[1] in valid_fileinfo:
            """
            Lines of code 33-42 adapted from 'user5305519' at 
            'https://stackoverflow.com/questions/51521658/using-python-requests-to-download-csv-file-after-authentication'
            """

            # Store the url content in a variable and set stream to True to prepare for download to a file
            r = requests.get(url, stream=True)

            # Download the file to a file with File Name = filename[1]
            with open(filename[1], 'wb') as handle:
                for chunk in r.iter_content(chunk_size=128):
                    handle.write(chunk)

            # Notify the user when the download is finished
            print("–"*20)
            print("Download complete for %s!" % filename)
            print("Validity Check:")
            return True
        # If the url file extension is invalid, return false
        else:
            print("–"*20)
            print("URL file extension is invalid or unsupported")
            print("Validity Check:")
            return False
    # If the url protocol is invalid, return false
    else:
        print("–"*20)
        print("URL protocol is invalid or unsupported")
        print("Validity Check:")
        return False 

if __name__ == '__main__':
	url = input("Enter an Url: ")
	print(validate_url(url))
