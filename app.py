import tkinter as tk
from tkinterdnd2 import DND_FILES, TkinterDnD
from PIL import ImageTk, Image
from tensorflow import keras

from keras.applications.resnet import ResNet50 ,preprocess_input
import numpy as np
import keras.utils as image


file_path =""
my_model = keras.models.load_model("ressfinal.h5")
def on_drop(event):
    
        global file_path
        file_path = event.data
        text_field.insert(tk.END, f"image déposé: {file_path}\n")
        image1 = Image.open(file_path)
        resized_image = image1.resize((224,224))
        photo = ImageTk.PhotoImage(resized_image)
        image_label.configure(image=photo)
        image_label.image = photo
       

  

def button_click(button_number):
    #text_field.insert(tk.END, f"Button {button_number} clicked\n")

        image1 = image.load_img(file_path,target_size =(224,224))
        image_array=image.img_to_array(image1)

        image_array_expand_dims = np.expand_dims(image_array,axis=0)
        image_array_expand_dims=image_array_expand_dims*1./255
        

       
        result = my_model.predict(image_array_expand_dims)

        print(result)

        result_cocci.config(text=int(result[0][0]%100*100))
        result_salmo.config(text=int(result[0][1]%100*100))
        result_ncd.config(text=int(result[0][2]%100*100))
        result_healthy.config(text=int(result[0][3]%100*100))
        print(file_path)

window = TkinterDnD.Tk()
window.title("Chiken diseases predictor")
#  window.iconphoto(True, tk.PhotoImage(file="1..ico"))
window.geometry("900x590")  # Fixed width and height
window.resizable(False, False)  # Disable window resizing

# Dark theme colors
bg_color = "#1e1e1e"  # Background color
fg_color = "#ffffff"  # Foreground color
button_color = "#ff5555"  # Button color
button_text_color = "#ffffff"  # Button text color

container = tk.Frame(window, padx=20, pady=20, bg=bg_color)
container.pack(fill="both", expand=True)

label = tk.Label(container, text="Glisser votre image ici", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove",height=5)
label.pack(pady=20, fill="both")


text_field = tk.Text(container, height=5, font=("Helvetica", 12, "bold"), bg=bg_color, fg=fg_color)
text_field.pack(pady=10, fill="both")


image_frame = tk.Frame(container,bg=bg_color, highlightthickness=2, highlightbackground="#8a8a8a",width=224,height=224)
image_frame.pack(side=tk.LEFT, padx=10)
image_frame.pack_propagate(False)


name_frame = tk.Frame(container, bg=bg_color,width=100,height=180)
name_frame.pack(side=tk.LEFT,pady=20,padx=20)
name_frame.pack_propagate(False)

result_frame = tk.Frame(container, bg=bg_color,width=100,height=180)
result_frame.pack(side=tk.LEFT,pady=20)
result_frame.pack_propagate(False)


button_frame = tk.Frame(container, bg=bg_color,width=224,height=224)
button_frame.pack(side=tk.RIGHT, padx=10)
button_frame.pack_propagate(False)

#Créer le Label pour afficher l'image
image_label = tk.Label(image_frame)
image_label.pack(side=tk.LEFT )



label_cocci = tk.Label(name_frame, text="cocci", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove")
label_cocci.pack(pady=7,fill=tk.BOTH)

label_salmo = tk.Label(name_frame, text="healthy", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove")
label_salmo.pack(pady=7,fill=tk.BOTH)

label_ncd = tk.Label(name_frame, text="ncd", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove")
label_ncd.pack(pady=7,fill=tk.BOTH)

label_healthy = tk.Label(name_frame, text="salmo", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove")
label_healthy.pack(pady=7,fill=tk.BOTH)




result_cocci = tk.Label(result_frame,text="97%", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove")
result_cocci.pack(pady=7,fill=tk.BOTH)

result_salmo = tk.Label(result_frame,text="1%", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove")
result_salmo.pack(pady=7,fill=tk.BOTH)

result_ncd = tk.Label(result_frame, text="0%",font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove")
result_ncd.pack(pady=7,fill=tk.BOTH)

result_healthy = tk.Label(result_frame,text="2%", font=("Helvetica", 16, "bold"), bg=bg_color, fg=fg_color, relief="groove")
result_healthy.pack(pady=7,fill=tk.BOTH)




button1 = tk.Button(button_frame, text="Prédire", font=("Helvetica", 12, "bold"), fg=button_text_color, bg=button_color, command=lambda: button_click(1))
button1.pack(pady=10,fill=tk.BOTH)


logo_image = Image.open("aa.png")
resized_image_log = logo_image.resize((150, 150))  # Adjust the size as needed
logo =  ImageTk.PhotoImage(resized_image_log)
logo_lable = tk.Label(button_frame,image =logo)
logo_lable.pack(fill=tk.BOTH,pady=10)

label.drop_target_register(DND_FILES)
label.dnd_bind('<<Drop>>', on_drop)

window.configure(bg=bg_color)
window.tk_setPalette(background=bg_color, foreground=fg_color)

window.mainloop()
