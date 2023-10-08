import customtkinter
import requests
import json

app = customtkinter.CTk()
app.title("IP Location Finder")
app.geometry("450x300")

ip_entry = customtkinter.CTkEntry(
    app, placeholder_text="Enter IP Address", width=180, height=40)
ip_entry.pack(pady=20, padx=20)


def get_location():
    ip = ip_entry.get()

    url = f"http://ip-api.com/json/{ip}"
    response = requests.get(url)
    location_data = json.loads(response.text)

    country = location_data['country']
    city = location_data['city']

    location_label.configure(text=f"country: {country}\ncity: {city}")


get_location_button = customtkinter.CTkButton(
    app, text="Get Location", width=100, height=40, command=get_location, bg_color="blue")
get_location_button.pack(pady=10)

location_label = customtkinter.CTkLabel(app, text="")
location_label.pack(pady=5)


app.mainloop()
