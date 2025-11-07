import requests, ctypes, getpass, os

MessageBox = ctypes.windll.user32.MessageBoxW
MessageBox(None, "BOCCHI WAS HERE!!! ♪(´▽｀)", "HAHAHAHAHAHAHAHAHAHAHAHA", 0)

image_url = "https://raw.githubusercontent.com/lainonz/bocchi.exe/main/bocchi.jpg"
temp_image_path = "C:/Users/{}/zzz.jpg".format(getpass.getuser())

response = requests.get(image_url)
with open(temp_image_path, "wb") as file:
    file.write(response.content)

SPI_SETDESKWALLPAPER = 0x0014
ctypes.windll.user32.SystemParametersInfoW(SPI_SETDESKWALLPAPER, 0, temp_image_path, 3)

os.remove(temp_image_path)

for a in range(100):
    file_name = "bocchi_{}.txt".format(a+1)
    try:
        file_path = os.path.join("C:/Users/{}/Desktop".format(getpass.getuser()), file_name)
        with open(file_path, "w") as file:
            file.write("BOCCHI WAS HERE!")
    except:
        file_path = os.path.join("C:/Users/{}/OneDrive/Desktop".format(getpass.getuser()), file_name)
        with open(file_path, "w") as file:

            file.write("BOCCHI WAS HERE!")
