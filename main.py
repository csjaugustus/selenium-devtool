from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import tkinter as tk
from tkinter import ttk
import traceback
import time
import json

by_dic = {
    "ID" : By.ID,
    "NAME" : By.NAME,
    "XPATH" : By.XPATH,
    "LINK_TEXT" : By.LINK_TEXT,
    "PARTIAL_LINK_TEXT" : By.PARTIAL_LINK_TEXT,
    "TAG_NAME" : By.TAG_NAME,
    "CLASS_NAME" : By.CLASS_NAME,
    "CSS_SELECTOR" : By.CSS_SELECTOR,
}


def main():
    def run_code(driver):
        code = textbox.get("1.0", tk.END)
        try:
            exec(code)
        except:
            print(traceback.format_exc())

    def find_el():
        if cb_var.get():
            results = driver.find_elements(by_dic[attr_var.get()], value_entry.get())
            print(results)
        else:
            result = driver.find_element(by_dic[attr_var.get()], value_entry.get())
            print(result)

    def click_el():
        result = driver.find_element(by_dic[attr_var.get()], value_entry.get())
        result.click()

    def send_keys():
        result = driver.find_element(by_dic[attr_var.get()], value_entry.get())
        result.send_keys("example")

    driver = webdriver.Chrome()

    root = tk.Tk()

    root.title("Selenium Devtool")
    root.resizable(False, False)
    root.tk.call("source", "sun-valley.tcl")
    root.tk.call("set_theme", "light")

    # Sandbox Exec
    sandbox_label = tk.Label(root, text="Sandbox Exec")
    textbox = tk.Text(root, height=10, width=80)
    sb_exc_bn = ttk.Button(root, text="Run", command=lambda x=driver: run_code(driver))

    sandbox_label.grid(row=0, column=0, columnspan=3)
    textbox.grid(row=1, column=1, padx=10, pady=10)
    sb_exc_bn.grid(row=2, column=1, padx=10, pady=10)

    # Find Element
    find_label = tk.Label(root, text="Find Element(s)")
    cb_var = tk.BooleanVar(value=False)
    cb = ttk.Checkbutton(root, text="Find All", variable=cb_var, style="Switch.TCheckbutton")
    by_label = tk.Label(root, text="Find by:")
    attr_var = tk.StringVar(value="- Select Attribute -")
    attrs = ["ID", "NAME", "XPATH", "LINK_TEXT", "PARTIAL_LINK_TEXT", "TAG_NAME", "CLASS_NAME", "CSS_SELECTOR"]
    attr_menu = tk.OptionMenu(root, attr_var, *attrs)
    value_label = tk.Label(root, text="Enter value:")
    value_entry = ttk.Entry(root, width=50)
    find_element_bn = ttk.Button(root, text="Find", command=find_el)
    click_element_bn = ttk.Button(root, text="Click", command=click_el)
    send_keys_bn = ttk.Button(root, text="Send Keys", command=send_keys)

    find_label.grid(row=3, column=1, padx=10, pady=10)
    cb.grid(row=3, column=2, padx=10, pady=10)
    by_label.grid(row=4, column=0, padx=10, pady=10)
    attr_menu.grid(row=4, column=1, padx=10, pady=10)
    value_label.grid(row=5, column=0, padx=10, pady=10)
    value_entry.grid(row=5, column=1, padx=10, pady=10)
    find_element_bn.grid(row=6, column=1, padx=10, pady=10)
    click_element_bn.grid(row=7, column=1, padx=10, pady=10)
    send_keys_bn.grid(row=8, column=1, padx=10, pady=10)

    # Center Window
    root.update()
    root.minsize(root.winfo_width(), root.winfo_height())
    x_cordinate = int((root.winfo_screenwidth() / 2) - (root.winfo_width() / 2))
    y_cordinate = int((root.winfo_screenheight() / 2) - (root.winfo_height() / 2))
    root.geometry("+{}+{}".format(x_cordinate, y_cordinate - 20))

    root.mainloop()

if __name__ == "__main__":
    main()
