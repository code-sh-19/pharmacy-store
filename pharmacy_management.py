import tkinter as tk
import tksheet
import csv


root = tk.Tk()
root.title("Pharmacy Management System")
pagenum = 1


def main_page(root):
    def btn_add():
        with open('pharmdata.csv', mode='a', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows([''])
        file.close()
        main_frame.grid_forget()
        edit_page(root)

    main_frame = tk.Frame(root, bg="black")
    label1 = tk.Label(main_frame, text="Dashboard", fg="white", bg="black")
    btn_medicine_list = tk.Button(main_frame, text="Medicine List", command=changepage, bg="white", fg="black")
    btn_add_item = tk.Button(main_frame, text="Add Item", command=btn_add, bg="white", fg="black")

    label1.grid(row=0, columnspan=2, pady=10)
    btn_medicine_list.grid(row=1, columnspan=2, pady=10, padx=20)
    btn_add_item.grid(row=2, columnspan=2, pady=10, padx=20)
    main_frame.grid()


def changepage():
    global pagenum, root
    print("from c ", pagenum)
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        medicine_page(root)
        pagenum = 2
    elif pagenum == 2:
        main_page(root)
        pagenum = 1
    elif pagenum == 3:
        medicine_page(root)
        pagenum = 2
    else:
        main_page(root)
        pagenum = 1


def changepage1():
    global pagenum, root
    print("from c1 ", pagenum)
    for widget in root.winfo_children():
        widget.destroy()
    if pagenum == 1:
        medicine_page(root)
        pagenum = 2
    elif pagenum == 2:
        edit_page(root)
        pagenum = 3
    else:
        medicine_page(root)
        pagenum = 2


def medicine_page(root):
    name_var = tk.StringVar()

    def search():
        search_frame = tk.Toplevel(list_frame)
        search_frame.title("Search Results")
        word = name_var.get()
        search_label = tk.Label(search_frame,text="Search Results for {}".format(word))

        res = []
        with open('pharmdata.csv', mode='r') as file:
            rows = list(csv.reader(file))
        file.close()
        # print(rows)
        for row in rows:
            for col in row:
                if word in col.lower():
                    # print(row)
                    res.append(row)

        search_label.grid(row=0)
        sheet1 = tksheet.Sheet(search_frame)
        sheet1.grid(row=1)
        sheet1.set_sheet_data([[f"{col}" for col in row] for row in res])

        sheet1.enable_bindings(("single_select",

                               "row_select",

                               "column_width_resize",

                               "arrowkeys",

                               "rc_select",

                               "copy",

                               "right_click_popup_menu"
                               ))
        search_frame.grid()

    list_frame = tk.Frame(root, bg="grey")
    label2 = tk.Label(list_frame, text="List of Medicines", bg="grey")
    btn_back_to_main = tk.Button(list_frame, text="Back", command=changepage)
    btn_edit_list = tk.Button(list_frame, text="Edit List", command=changepage1)
    btn_search = tk.Button(list_frame, text="Search", command=search)
    search_input = tk.Entry(list_frame, textvariable=name_var)

    label2.grid(row=0, columnspan=2, pady=10)
    btn_back_to_main.grid(row=1, column=0)
    btn_edit_list.grid(row=2, column=0)
    btn_search.grid(row=1, column=1)
    search_input.grid(row=2, column=1)

    sheet = tksheet.Sheet(list_frame)
    sheet.grid(row=3, columnspan=2)
    with open('pharmdata.csv', 'rt')as f1:
        data = csv.reader(f1)
        sheet.set_sheet_data([[f"{col}" for col in row] for row in data])
    # table enable choices listed below:
    sheet.enable_bindings(("single_select",

                           "row_select",

                           "column_width_resize",

                           "arrowkeys",

                           "rc_select",

                           "copy",

                           "right_click_popup_menu"
                           ))
    f1.close()
    list_frame.grid()


def edit_page(root):
    def save():
        print("Saving the info")
        data = sheet1.get_sheet_data(return_copy=True, get_header=False, get_index=False)
        with open('pharmdata.csv', mode='w', newline='') as file:
            writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            writer.writerows(data)
        file.close()
        print(data)

    edit_list_frame = tk.Frame(root, bg="grey")
    label3 = tk.Label(edit_list_frame, text="List of Medicines(Edit Mode)", bg="grey")
    btn_back_to_list_view = tk.Button(edit_list_frame, text="Back", command=changepage)
    btn_save = tk.Button(edit_list_frame, text="Save", command=save)

    label3.grid(row=0)
    btn_back_to_list_view.grid(row=1)
    btn_save.grid(row=2)

    sheet1 = tksheet.Sheet(edit_list_frame)
    sheet1.grid(row=3)
    with open('pharmdata.csv', 'rt')as f2:
        data = csv.reader(f2)
        sheet1.set_sheet_data([[f"{col}" for col in row] for row in data])
    # table enable choices listed below:
    sheet1.enable_bindings(("single_select",

                            "row_select",

                            "column_width_resize",

                            "arrowkeys",

                            "right_click_popup_menu",

                            "rc_select",

                            "rc_insert_row",

                            "rc_insert_row_below",

                            "rc_delete_row",

                            "copy",

                            "cut",

                            "paste",

                            "delete",

                            "undo",

                            "edit_cell"
                            ))
    f2.close()
    edit_list_frame.grid()

print(pagenum)

main_page(root)
root.mainloop()


