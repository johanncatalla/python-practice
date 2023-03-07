import tkinter as tk
from tkinter import messagebox
from tkinter import filedialog as fd
import re
import os

# creates the class MainApplication to create object to call when running the program
class MainApplication(tk.Frame):

    def __init__(self): # create GUI widgets using tkinter

        # creates the root container
        self.root = tk.Tk()
        
        # set window size and default title of the root
        self.root.geometry("800x800")
        self.root.title("New File")

        # Set flag to check if the file exists in the directory
        global open_status_name
        self.open_status_name = False

        # set falg to check if the text cursor has selected text
        global selected
        self.selected = False

        # creating C.R.U.D file menu
        # create menu bar and place it in root
        self.menu_bar = tk.Menu(self.root)
        self.root.config(menu=self.menu_bar)

        # Adding FILE menu containing that has the functions "Open File...", "New Text File", "Save", "Save as...", and "Delete file"
        self.file_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.file_menu.add_command(label="Open File...", command=self.open_text_file)
        # adds separator to organize the file menu relative to the functionality of its commands
        self.file_menu.add_separator()
        self.file_menu.add_command(label="New Text File", command=self.new_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Save", command=self.save_file)
        self.file_menu.add_command(label="Save as...", command=self.save_as_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Delete File", command=self.delete_file)     
        
        # Add second menu called ACTION menu
        self.action_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.action_menu.add_command(label="Close window", command=self.on_closing)

        # Add third menu called EDIT menu containing the functions "cut", "copy", and "paste"
        self.edit_menu = tk.Menu(self.menu_bar, tearoff=0)
        self.edit_menu.add_command(label="Cut", command=lambda: self.cut_text(False))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Copy", command=lambda: self.copy_text(False))
        self.edit_menu.add_separator()
        self.edit_menu.add_command(label="Paste", command=lambda: self.paste_text(False))
        

        # Add cascade and set labels for menus
        self.menu_bar.add_cascade(label="File", menu=self.file_menu)
        self.menu_bar.add_cascade(label="Actions", menu=self.action_menu)
        self.menu_bar.add_cascade(label="Edit", menu=self.edit_menu)
        
        # TOP FRAME/SCROLL FRAME
        # creating top frame for text widget and scrollbar
        self.text_scroll_Frame = tk.Frame(self.root, width=800, height=400, padx=20)
        # packs the scroll Frame in the root
        self.text_scroll_Frame.pack(fill='x')

        # Creates the text widget in the first frame
        self.txt_editor = tk.Text(
            self.text_scroll_Frame,
            font=("Century Gothic", 10),
            width=400,
            height=20
        )

        # binds the text editor into keypress event to allow shortcuts for open file, save, new file, and delete file
        self.txt_editor.bind("<KeyPress>", self.shortcut)

        # creating scrollbar for text widget
        self.txt_scrollbar = tk.Scrollbar(self.text_scroll_Frame, command=self.txt_editor.yview) 
        self.txt_editor.config(yscrollcommand=self.txt_scrollbar.set) #bounds the scrollbar to the text editor

        # packs the text editor and its scrollbar
        self.txt_scrollbar.pack(side=tk.RIGHT, fill='y') 
        self.txt_editor.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # EDITOR FRAME
        # Create middle frame for options    
        self.editor_Frame = tk.Frame(self.root, width=800, height=400)
        
        # Modify frame columns to cater to the grid function
        self.editor_Frame.columnconfigure(0, weight=1)
        self.editor_Frame.columnconfigure(1, weight=1)
        self.editor_Frame.pack(fill='x', padx=20)
        
        # Creates the label widget inside the editor frame 
        self.label = tk.Label(
            self.editor_Frame, 
            text="Enter text or ", 
            font=('Arial', 10)
        )
        # adds the label in the first row and first column in the editor frame using the grid function
        self.label.grid(row=1, column=1, sticky=tk.E, padx=74,)
        
        # Creates the button frame as shortcut for uploading a file
        self.open_button = tk.Button(
            self.editor_Frame,
            text="Open file",
            command=self.open_text_file
        )
        self.open_button.grid(row=1, column=1, sticky=tk.E) # grids the button besides the label
      
        # creating another label
        self.label = tk.Label(
            self.editor_Frame, 
            text="Search: ", 
            font=('Arial', 10)
        )
        self.label.grid(row=1, column=0, sticky=tk.W)

        # Creating the search bar using the entry function 
        self.entry = tk.Entry(
            self.editor_Frame, 
            width=30,
            font=('Arial', 10)
        )
        self.entry.grid(row=1, column=0, sticky=tk.W, padx=52) # grids the search bar besides the label 
        
        # Create Options for ignorecase and case sensitive search
        self.options_list = ["Ignore Case", "Case Sensitive"]
        # Using the StringVar function to interact with the values of the option menu later 
        self.value_inside = tk.StringVar(self.editor_Frame)
        self.value_inside.set("Ignore Case") #sets the default value of the option menu to Ignore Case
        
        # Creates the option menu that will contain "Ignore Case" and "Case Sensitive" to modify search functionality later
        self.option_menu = tk.OptionMenu(self.editor_Frame, self.value_inside, *self.options_list)
        self.option_menu.grid(column=0, row=1, sticky=tk.E, padx=40)
        
        # BUTTONS INSIDE EDITOR FRAME

        # Creates the button that is bound to the fucntion that searches text
        self.search_button = tk.Button(
            self.editor_Frame, 
            text="Search", 
            font=('Arial', 10), 
            command=self.search_txt 
        )
        # grids the button to the second row, columm 1 of the editor frame, and modifies sticky to West and East to occupy the whole columnn
        self.search_button.grid(row=2, column=0, sticky=tk.W+tk.E)
        
        # Creates button that is bound to the function that clears the content of the second text editor 
        self.clear_search = tk.Button(
            self.editor_Frame,
            text="Clear Searches",
            font=('Arial', 10),
            command=self.destroy
        )
        # grids the button to the second row, column 2 of the editor frame, and modifies sticky to West and East to occupy the whole columnn
        self.clear_search.grid(row=2, column=1, sticky=tk.W+tk.E)

        # DISPLAY FRAME
        # Creates a frame for the second text editor and scrollbar 
        self.display_frame = tk.Frame(self.root, width=800, height=200)
        self.display_frame.pack(fill='x', padx=20)

        # creates another text editor to display result
        self.display_text = tk.Text(
            self.display_frame, 
            font=("Century Gothic", 10),
            width=400,
            height=20
        )
        
        # creating the scrollbar for the text editor
        self.display_scroll = tk.Scrollbar(self.display_frame, command=self.display_text.yview)
        self.display_text.config(yscrollcommand=self.display_scroll.set)
        
        # packs the scrollbar and the text editor in the display frame
        self.display_scroll.pack(side=tk.RIGHT, fill='y')
        self.display_text.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # create button to export results
        self.export_button = tk.Button(
            self.root,
            text="Export Searches",
            font=('Arial', 8),
            command= self.save_export
        )
        self.export_button.place(x=20,y=745)
        # creates a status bar at the bottom right of the root container
        self.status_bar = tk.Label(self.root, text="Ready       ", anchor=tk.E)
        self.status_bar.pack(fill='x', side=tk.BOTTOM, ipady=5)

        # Triggers when closing window then display yes or no prompt 
        # to make sure if the user intends to close the window
        self.root.protocol(
            "WM_DELETE_WINDOW", 
            self.on_closing
        )

        # starts the GUI event loop
        self.root.mainloop()
    
    # SEARCH FUNCTION
    # creating the search functionality using regex
    def search_txt(self):

        # getting the text from the Text editor
        self.text_editor_input = self.txt_editor.get("1.0", tk.END)
        # cleaning the text using regex sub fuction to remove unnecessary spaces and lines
        self.clean_text_input = re.sub('[ \n]+', ' ', self.text_editor_input)

        # gettting the text from the Entry widget
        self.entry_input = self.entry.get()
        # Cleaning the text using regex sub function to remove unnecessary spaces
        self.clean_entry_input = re.sub(' +', ' ', self.entry_input)
        
        # transforming the string of keywords into list to iterate later
        self.lst_entry_input = self.clean_entry_input.split(' ')
        
        # Adding the "|" metacharacter between each keyword on list using join function to search more than one keyword
        self.keywords = r'\b[^.?!]*(?:' + '|'.join(self.lst_entry_input) + r')(?=[\s@*&\^%$#.,;:\/\'-\?!]|$)'

        # Getting the value of the option menu whether it is ignorecase or case sensitive to modify the search functionality
        self.option_value = self.value_inside.get()

        # Conditional that changes the behavior of the search functionality depending on the value of the option menu
        if self.option_value == "Ignore Case":
            # compiling the keyword pattern with the sentence pattern to create a main regex pattern 
            self.pattern = re.compile(r'\b[^.?!]*\b{0}\b[^.?!]*[ .?!]'.format(self.keywords), re.IGNORECASE) # So the search can be Insensitive
        else: 
            self.pattern = re.compile(r'\b[^.?!]*\b{0}\b[^.?!]*[ .?!]'.format(self.keywords)) # or it can be Sensitive
        
        # Executing the findall function with the main regex pattern to get a list of searches
        self.list_searches = self.pattern.findall(self.clean_text_input)

        # Transforming the list of results into string with lines in between for readability
        self.string_searches = "\n\n".join(self.list_searches)
        
        # Inserting the string of results to the text editor in the display frame
        self.display_text.insert('1.0', f"\nMatches:\n\n{self.string_searches}\n\n------END OF RESULTS------\n\n")

        # Iterator that inserts match count per keyword to the text editor
        for string in self.lst_entry_input:
            if self.option_value == "Ignore Case":
                self.res = len(re.findall(string, self.string_searches, re.IGNORECASE))
            else:
                self.res = len(re.findall(string, self.string_searches))
            self.display_text.insert('1.0', f"Number of matches for \"{string}\": {self.res}\n")
        

        # storing the number of matches to return number of sentence matches then inserting to the text widget
        self.num_matches = len(self.list_searches)
        self.display_text.insert('1.0', f"Sentence matches: {self.num_matches}\n")
    
    # Keyboard shortcuts that calls the functions of open file, save file, new file, dlete file
    def shortcut(self, event):
        # checks if the user presses certain key combinations
        # "Ctrl + s" saves the file
        if event.state == 4 and event.keysym == "s": 
            self.save_file()
        # "Ctrl + o" opens a file
        elif event.state == 4 and event.keysym == "o":
            self.open_text_file()
        # "Ctrl + n" creates a new file
        elif event.state == 4 and event.keysym == "n":
            self.new_file()
        # "Ctrl + d" deletes the opened file
        elif event.state == 4 and event.keysym == "d":
            self.delete_file()

    # create functions for edit menu options 
    def cut_text(self,e): # cuts text
        global selected
        if self.txt_editor.selection_get():
            # Grabs the selected text from the text editor
            self.selected = self.txt_editor.selection_get()
            # Deletes the selected text from the text editor
            self.txt_editor.delete("sel.first", "sel.last")

    def copy_text(self,e): # copies text
        if self.txt_editor.selection_get():
            # Grabs the selected text from the text editor
            self.selected = self.txt_editor.selection_get()

    def paste_text(self,e): # pastes text
        if self.selected:
            # Finds the position of the text cursor
            self.position = self.txt_editor.index(tk.INSERT)
            # inserts the grabbed text at the position of the cursor
            self.txt_editor.insert(self.position, self.selected)

    # function that triggers when clicking clear search button
    def destroy(self):
        self.display_text.delete('1.0', tk.END)

    # function that triggers when clicking "Open File" button to select a file that will be inserted to the text widget
    def open_text_file(self):

        # Grabs file using the "askopenfilename" function from the filedialog module
        # Filetypes can be .txt, .html, .py, or All Files
        self.f = fd.askopenfilename(
            initialdir="D:/Downloads/", 
            title='Open File', 
            filetypes=(('.txt files', '*.txt'), ('HTML Files', '*.html'),('Python Files', '*.py'), ('All Files', '*.*'))
        )
        # Check to see if the user opened a file in the file dialog
        if self.f:
            # Make filename global to access it later
            global open_status_name
            self.open_status_name = self.f
            
            # Delete previous texxt
            self.txt_editor.delete('1.0', tk.END)
            
            # Update status bars
            self.extract_filename = re.search(r"[^/\\]+$", self.open_status_name).group(0)
            self.status_bar.config(text=f"{self.f}       ")            
            self.root.title(f"{self.extract_filename}")

            # Open the file
            self.text_file = open(self.f, 'r')
            self.text = self.text_file.read()

            # Add file to text widget
            self.txt_editor.insert('1.0', self.text)

            # close the opened file
            self.text_file.close()

    # Function that triggers when clicking the "New File" option in the "File" menu
    def new_file(self):
        # Deletes previous text
        self.txt_editor.delete('1.0', tk.END)
        # Updates the title and status bar
        self.root.title('New File')
        self.status_bar.config(text="New File       ")

        # Since the new file is still not saved in the directory, sets the text editor flag to False
        # so that when we click the "Delete File" option in the "File Menu", the previous file will not be deleted
        global open_status_name
        self.open_status_name = False        
    
    #Function that triggers when clicking the "Save file" in the "File" menu
    def save_file(self):
        # checks the text editor flag if the file exists in the directory
        if self.open_status_name:
            # Save the file
            self.w_file = open(self.open_status_name, 'w')
            # updates the file to whatever the input is in the text editor
            self.w_file.write(self.txt_editor.get(1.0, tk.END))
            # Close the file 
            self.w_file.close()

            #updates the status bar
            self.status_bar.config(text=f"Saved: {self.open_status_name}       ")

        # if the file is not in the directory, calls the "Save File as..." function
        else:
            self.save_as_file() 
    
    # save the search result to directory 
    def save_export(self):
        # Saves the file as... using the "asksaveasfilename" function from the filedialog module
        # Filetypes can be .txt, .html, .py, or All Files
        self.text_file = fd.asksaveasfilename(
            defaultextension=".*", 
            initialdir="D:/Downloads/", 
            title="Export Search Results", 
            filetypes=(('.txt files', '*.txt'), ('HTML Files', '*.html'),('Python Files', '*.py'), ('All Files', '*.*'))
        )
        # checks if the user opened a file in the file dialog
        if self.text_file:
            # Updade Status Bars
            self.name = self.text_file
            self.status_bar.config(text=f"Saved: {self.name}       ")
            self.name = self.name.replace("D:/Downloads/", "")
            self.root.title(f"{self.name}")
            
            # Save the file
            self.w_file = open(self.text_file, 'w')
            self.w_file.write(self.display_text.get(1.0, tk.END))
            # Close the file 
            self.w_file.close()
        else:
            pass

    # Function that triggers when the "Save as File..." option is clicked in the "File" menu
    # Saves the File as...
    def save_as_file(self):
        # Saves the file as... using the "asksaveasfilename" function from the filedialog module
        # Filetypes can be .txt, .html, .py, or All Files
        self.text_file = fd.asksaveasfilename(
            defaultextension=".*", 
            initialdir="D:/Downloads/", 
            title="Save File as", 
            filetypes=(('.txt files', '*.txt'), ('HTML Files', '*.html'),('Python Files', '*.py'), ('All Files', '*.*'))
        )
        # checks if the user opened a file in the file dialog
        if self.text_file:
            # Updade Status Bars
            self.name = self.text_file
            self.status_bar.config(text=f"Saved: {self.name}       ")
            self.name = self.name.replace("D:/Downloads/", "")
            self.root.title(f"{self.name}")
            
            # Save the file
            self.w_file = open(self.text_file, 'w')
            self.w_file.write(self.txt_editor.get(1.0, tk.END))
            # Close the file 
            self.w_file.close()
        else:
            pass
        
        # sets the flag into the file name of the saved file to allow some functionalities in the "File" menu to work
        self.open_status_name = self.text_file
        
    # Function that Deletes the file from the directory
    def delete_file(self):
        # check if there is a file opened or the file exists in the directory
        if self.open_status_name:
            # checks if the path exists
            if os.path.exists(self.open_status_name):
                # calls the on_deletion function
                self.on_deletion()
        # if the text editor flag is False, shows a message that the file does not exist
        else:
            messagebox.showinfo(
                title = "File not found",
                message = "The file you are trying to delete does not exist"
            )
    
    # Deletes the file from the directory
    def on_deletion(self):
        
        # regex that takes tha file name from the directory
        self.extract_filename = re.search(r"[^/\\]+$", self.open_status_name).group(0)
        #regex that takes the directory from the file name
        self.directory_path = re.search(r"^(.*)/[^/]+$", self.open_status_name).group(1)

        # message prompt to ask the user if they really intend to delete the file
        if messagebox.askyesno(title="Delete?", message=f"Do you really want to delete \"{self.extract_filename}\" from {self.directory_path}?"):
            # deletes the file that is opened
            os.remove(self.open_status_name)
            # Confirmation message that the file is deleted
            messagebox.showinfo(title="Message", message=f"Successfuly deleted \"{self.extract_filename}\" from {self.directory_path}.")
            # Creates a new file
            self.new_file()
            
    # Function that triggers the messagebox when closing the window
    def on_closing(self):
        # checks if the user intends to close the window
        if messagebox.askyesno(title="Close?", message=f"Do you really want to close Text Editor?"):
            self.root.destroy()

# checks if the file is being run as a script or as a module
if __name__=="__main__":
    # calls the main application
    MainApplication()

    