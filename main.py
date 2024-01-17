import requests
import tkinter as tk


def get_data():
    country_name=entr_box.get()
    if country_name: 
     url=f"https://restcountries.com/v3.1/name/{entr_box.get()}"
     response=requests.get(url)
     if response.status_code==200:
        country_data=response.json()[0]
        country_info(country_data)
     else:
       error_screen(f"Error:{response.status_code}")
    else:
        error_screen(text="Please Enter Country Name") 
# ------------------------------------------------------------------------
def country_info(country_data):
   
   result_screen=tk.Toplevel(window)
   result_screen.geometry("700x500")
   result_screen.configure(bg="#81de76")

   info=f"Name:{country_data['name']['common']}\n"\
   f"Capital:{country_data['capital'][0]}\n"\
   f"Continent:{country_data['continents'][0]}\n"\
   f"Area:{country_data['area']}\n"\
   f"Population:{country_data['population']}"

   result=tk.Label(result_screen,text=info,bg="black",fg="white",font=('Helvetica',16,'bold'))
   result.pack(pady=43,padx=43)
# -------------------------------------------------------------------------

def error_screen(msg_error):
    not_valid=tk.Toplevel(window)
    not_valid.geometry("700x500")
    not_valid.configure(bg="##81de76")

    error=tk.Label(not_valid,text=msg_error,bg="black",fg="white")
    error.pack(pady=43,padx=43)
    
# ------------------------------------------------------------------------

window = tk.Tk()
window.geometry("700x500")
window.configure(bg="#81de76")
heading_label = tk.Label(window,text="COUNTRY APP",background="black",foreground="#107195", width=200,font=('Helvetica',16,'bold'))
heading_label.pack(pady=10,padx=10)

main_frame=tk.Frame(window,bg="#6caddf",width=300,height=300)
main_frame.pack(pady=30,padx=30)

entr_label=tk.Label(main_frame,text="Enter Country Name",bg="#8cd9ff",fg="white",font=('Helvetica',14,'bold'))
entr_label.pack(pady=32.3,padx=32.3)
entr_box=tk.Entry(main_frame,width=50,bg='white',fg="black")
entr_box.pack(pady=38,padx=39)

search=tk.Button(main_frame,text='Get country info',background="#8cd9ff",fg="white",command=get_data)
search.pack(pady=42,padx=42)


window.mainloop()