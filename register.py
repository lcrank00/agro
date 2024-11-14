import tkinter as tk
import tkinter.messagebox as messagebox

# Function to validate user input (replace with more robust validation)
def validate_input(name, phone_number):
    if not name.strip():
        return False, "Please enter your name."
    if not phone_number.isdigit() or len(phone_number) != 10:
        return False, "Please enter a valid 10-digit phone number."
    # You can add more validation checks here, such as for district, block, etc.
    return True, ""

def handle_register_button_click():
    name = name_entry.get().strip()
    phone_number = phone_number_entry.get().strip()

    # Validate user input
    is_valid, error_message = validate_input(name, phone_number)
    if not is_valid:
        messagebox.showerror("Error", error_message)
        return

    # Simulate successful registration (replace with actual registration logic)
    messagebox.showinfo("Success", "Registration successful!")
    # Clear entry fields for new registration
    name_entry.delete(0, tk.END)
    phone_number_entry.delete(0, tk.END)

# Create the main application window
root = tk.Tk()
root.title("AGRO - Registration")

# Create a frame to hold registration fields
registration_frame = tk.Frame(root)
registration_frame.pack(padx=10, pady=10)

# Label and entry for name
name_label = tk.Label(registration_frame, text="Name:")
name_label.pack()
name_entry = tk.Entry(registration_frame)
name_entry.pack()

# Label and entry for phone number
phone_number_label = tk.Label(registration_frame, text="Phone Number:")
phone_number_label.pack()
phone_number_entry = tk.Entry(registration_frame)
phone_number_entry.pack()

# Registration button
register_button = tk.Button(registration_frame, text="Register", command=handle_register_button_click)
register_button.pack()

root.mainloop()
