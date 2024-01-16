import tkinter as tk
import webview

def open_webview():
    webview.create_window("Web Viewer", "https://koffeekodes.in/")

def main():
    root = tk.Tk()
    root.title("Tkinter Web Viewer")

    btn = tk.Button(root, text="Open Web Viewer", command=open_webview)
    btn.pack(pady=20)

    root.mainloop()

if __name__ == "__main__":
    main()
