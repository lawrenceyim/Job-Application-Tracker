import csv
import datetime
import os
import tkinter


def clear_screen():
    for widget in window.winfo_children():
        widget.destroy()


def exit():
    window.quit()


def display_menu():
    clear_screen()
    label = tkinter.Label(window, text="Menu", font=('Arial', 20))
    label.pack()

    view_application_button = tkinter.Button(window, 
                                            text="View job applications", 
                                            font=('Arial', 20), 
                                            image=pixelVirtual,
                                            compound="c",
                                            height = 60,
                                            width = 400,
                                            command=display_applications)
    view_application_button.pack(pady=10)

    add_application_button = tkinter.Button(window, 
                                            text="Add job application", 
                                            font=('Arial', 20), 
                                            image=pixelVirtual,
                                            compound="c",
                                            height = 60,
                                            width = 400,
                                            command=add_application)
    add_application_button.pack(pady=10)

    update_application_button = tkinter.Button(window, 
                                            text="Update job application", 
                                            font=('Arial', 20), 
                                            image=pixelVirtual,
                                            compound="c",
                                            height = 60,
                                            width = 400)
    update_application_button.pack(pady=10)

    delete_application_button = tkinter.Button(window, 
                                            text="Delete job application", 
                                            font=('Arial', 20), 
                                            image=pixelVirtual,
                                            compound="c",
                                            height = 60,
                                            width = 400,
                                            command=delete_application)
    delete_application_button.pack(pady=10)

    exit_button = tkinter.Button(window, 
                                            text="Exit", 
                                            font=('Arial', 20), 
                                            image=pixelVirtual,
                                            compound="c",
                                            height = 60,
                                            width = 400,
                                            command=exit)
    exit_button.pack(pady=10)


def display_applications():
    clear_screen()
    tkinter.Label(window, text="Applications", font=('Arial', 20)).grid(row=0, column=2)

    back_to_menu_button = tkinter.Button(window, 
                                        text="Return to menu", 
                                        font=('Arial', 20), 
                                        image=pixelVirtual,
                                        compound="c",
                                        height = 60,
                                        width = 200,
                                        command=display_menu)
    back_to_menu_button.grid(row=1, column=2)

    row_count_label = tkinter.Label(window, font=('Arial',20))
    row_count_label.grid(row=2, column=2)

    tkinter.Label(window, text="Company", font=('Arial', 20)).grid(row=3, column=0)
    tkinter.Label(window, text="Title", font=('Arial', 20)).grid(row=3, column=1)
    tkinter.Label(window, text="Applied", font=('Arial', 20)).grid(row=3, column=2)
    tkinter.Label(window, text="Status", font=('Arial', 20)).grid(row=3, column=3)
    tkinter.Label(window, text="Last updated", font=('Arial', 20)).grid(row=3, column=4)


    # csv_table = tkinter.Scrollbar(window,
    #                               orient='vertical')
    # csv_table.pack()

    with open('applications.csv', 'r') as csv_file:
        csv_reader = csv.reader(csv_file)
        row_count = 0
        for line in csv_reader:
            row_count += 1
            tkinter.Label(window, text=line[0], font=('Arial', 20)).grid(row = (row_count + 3), column=0)
            tkinter.Label(window, text=line[1], font=('Arial', 20)).grid(row = (row_count + 3), column=1)
            tkinter.Label(window, text=line[2], font=('Arial', 20)).grid(row = (row_count + 3), column=2)
            tkinter.Label(window, text=line[3], font=('Arial', 20)).grid(row = (row_count + 3), column=3)
            tkinter.Label(window, text=line[4], font=('Arial', 20)).grid(row = (row_count + 3), column=4)

        row_count_label.config(text="Applied: " + str(row_count))
        csv_file.close()

def add_application():
    def validate_data():
        if (company_name_input.compare("end-1c", "==", "1.0") 
                or position_name_input.compare("end-1c", "==", "1.0")):
            response_label.config(text="Please fill out all entries")
        else:
            add_to_storage()
            response_label.config(text="Job application added")
            

    def add_to_storage():
        company_name = company_name_input.get("1.0", "end-1c").strip()
        position_name = position_name_input.get("1.0", "end-1c").strip()
        current_date = datetime.date.today()
        status = "Applied"
        response_date = datetime.date.today()

        with open('applications.csv', 'a') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow([company_name, position_name, current_date, status, response_date])
            csv_file.close()


    clear_screen()
    label = tkinter.Label(window, text="Add application", font=('Arial', 20))
    label.pack()
    back_to_menu_button = tkinter.Button(window, 
                                        text="Return to menu", 
                                        font=('Arial', 20), 
                                        image=pixelVirtual,
                                        compound="c",
                                        height = 60,
                                        width = 400,
                                        command=display_menu)
    back_to_menu_button.pack()

    company_name_label = tkinter.Label(window, text="Company name: ", font=('Arial', 20))
    company_name_label.place(x=250, y=150, height=60, width=300)
    company_name_input = tkinter.Text(window, font=('Arial', 20))
    company_name_input.place(x=550, y=150, height=60, width=600)

    position_name_label = tkinter.Label(window, text="Position name: ", font=('Arial', 20))
    position_name_label.place(x=250, y=250, height=60, width=300)
    position_name_input = tkinter.Text(window, font=('Arial', 20))
    position_name_input.place(x=550, y=250, height=60, width=600)

    add_to_storage_button = tkinter.Button(window, 
                                        text="Add to storage", 
                                        font=('Arial', 20), 
                                        image=pixelVirtual,
                                        compound="c",
                                        height = 60,
                                        width = 400,
                                        command=validate_data)
    add_to_storage_button.place(x=550, y=350)

    response_label = tkinter.Label(window, font=('Arial', 20))
    response_label.place(x=200, y=450, height=60, width = 600)


def delete_application():
    def validate_data():
        if (company_name_input.compare("end-1c", "==", "1.0") 
            or job_title_input.compare("end-1c", "==", "1.0")):
            response_label.config(text="Please fill out all entries")
        else:
            delete_data()

    def delete_data():
        company_name = company_name_input.get("1.0", "end-1c").strip()
        job_title = job_title_input.get("1.0", "end-1c").strip()

        with open('applications.csv', 'r') as input, open ('applications_edited.csv', 'w') as output:
            reader = csv.reader(input)
            writer = csv.writer(output)
            application_deleted = False
            for line in reader:
                if line[0] == company_name and line[1] == job_title:
                    application_deleted = True
                else:
                    writer.writerow(line)

            if application_deleted:
                response_label.config(text="Application deleted")
            else:
                response_label.config(text="No application with that company name and job title found")

        if (os.path.exists("applications.csv")) and os.path.isfile("applications.csv"):
            os.remove("applications.csv")
        if (os.path.exists("applications_edited.csv")) and os.path.isfile("applications_edited.csv"):
            os.rename("applications_edited.csv", "applications.csv")


    clear_screen()

    tkinter.Label(window, text="Delete application", font=('Arial', 20)).grid(row=0, column=2)

    back_to_menu_button = tkinter.Button(window, 
                                        text="Return to menu", 
                                        font=('Arial', 20), 
                                        image=pixelVirtual,
                                        compound="c",
                                        height = 60,
                                        width = 200,
                                        command=display_menu)
    back_to_menu_button.grid(row=1, column=2)

    tkinter.Label(window, text="Company name: ", font=('Arial', 20)).grid(row=2, column=1)

    company_name_input = tkinter.Text(window, font=('Arial', 20), height=1, width=40)
    company_name_input.grid(row=2, column=2, columnspan=2, sticky="w")
    
    tkinter.Label(window, text="Job title: ", font=('Arial', 20)).grid(row=3, column=1)
    
    job_title_input = tkinter.Text(window, font=('Arial', 20), height=1, width=40)
    job_title_input.grid(row=3, column=2, columnspan=2, sticky="w")
    
    delete_button = tkinter.Button(window, 
                                        text="Delete application", 
                                        font=('Arial', 20), 
                                        image=pixelVirtual,
                                        compound="c",
                                        height = 60,
                                        width = 400,
                                        command=validate_data)
    delete_button.grid(row=4, column=2)
    
    response_label = tkinter.Label(window, font=('Arial', 20))
    response_label.grid(row=5, column=1, columnspan=3)


window = tkinter.Tk()
for i in range(5):
    window.grid_columnconfigure(i, minsize=300)
pixelVirtual = tkinter.PhotoImage(width=1, height=1)

window.geometry("1500x1000")
window.title("Job Application Tracker")
display_menu()

window.mainloop()