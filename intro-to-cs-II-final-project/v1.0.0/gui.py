from tkinter import *
from modules import *

class gui: 
    def __init__(self, window) -> None: 
        '''
        Method to display header text and radio buttons and to create all future frames
        '''

        self.window = window

        # Display header text
        self.headerFrame = Frame(self.window)
        self.headerTitle = Label( 
            self.headerFrame, 
            text = 'Understanding Basic Searching & Sorting Algorithms', 
            font = ('System', 20)
        ).pack(side = 'top', pady = 10) 
        self.headerSubheading = Label(
            self.headerFrame, 
            text = 'A guided introduction to linear search, binary search, bubble sort, selection sort, and insertion sort algorithms',
            font = ('System', 10)
        ).pack(side = 'top', pady = 5)
        self.headerSearchDescription = Label(
            self.headerFrame, 
            text = 'A search algorithm finds a target value in an array', 
            font = ('System', 14)
        ).pack(side = 'top', pady = 10)
        self.header = Label(
            self.headerFrame, 
            text = 'A sort algorithm arranges the items of an array in a specific order', 
            font = ('System', 14)
        ).pack(side = 'top')
        self.headerFrame.pack(side = 'top', pady = 5)

        # Create radio buttons for each algorithm
        self.algorithmSelectFrame = Frame(self.window)
        self.radioSelection = IntVar(value = 0)
        self.algorithmSelectLabel = Label(
            self.algorithmSelectFrame, 
            text = 'Select an option:', 
            font = ('System', 12)
        ).pack(side = 'top', pady = 10)
        self.radioLinearSearch = Radiobutton(
            self.algorithmSelectFrame, 
            text = 'Linear Search',
            font = ('System', 11), 
            variable = self.radioSelection, 
            value = 1, 
            command = lambda: self.algorithmSelection(1)
        )
        self.radioLinearSearch.pack(side = 'left', pady = 5, padx = 10)
        self.radioBinarySearch = Radiobutton(
            self.algorithmSelectFrame, 
            text = 'Binary Search',
            font = ('System', 11), 
            variable = self.radioSelection, 
            value = 2, 
            command = lambda: self.algorithmSelection(2)
        )
        self.radioBinarySearch.pack(side = 'left', pady = 5, padx = 10)
        self.radioBubbleSort = Radiobutton(
            self.algorithmSelectFrame, 
            text = 'Bubble Sort',
            font = ('System', 11), 
            variable = self.radioSelection, 
            value = 3, 
            command = lambda: self.algorithmSelection(3)
        )
        self.radioBubbleSort.pack(side = 'left', pady = 5, padx = 10)
        self.radioSelectionSort = Radiobutton(
            self.algorithmSelectFrame, 
            text = 'Selection Sort',
            font = ('System', 11), 
            variable = self.radioSelection, 
            value = 4, 
            command = lambda: self.algorithmSelection(4)
        )
        self.radioSelectionSort.pack(side = 'left', pady = 5, padx = 10)
        self.radioInsertionSort = Radiobutton(
            self.algorithmSelectFrame, 
            text = 'Insertion Sort',
            font = ('System', 11), 
            variable = self.radioSelection, 
            value = 5, 
            command = lambda: self.algorithmSelection(5)
        )
        self.radioInsertionSort.pack(side = 'left', pady = 5, padx = 10)
        self.algorithmSelectFrame.pack(side = 'top')
    
        # Create all future frames
        self.algorithmSelectionFrame = None
        self.algorithmSelectionContinueFrame = None
        self.algorithmDescriptionFrame = None
        self.algorithmDescriptionContinueFrame = None
        self.getInputFrame = None
        self.getInputErrorFrame = None
        self.getTargetFrame = None
        self.getTargetErrorFrame = None
        self.searchAlgorithmOutputFrame = None
        self.sortAlgorithmOutputFrame = None

    def algorithmSelection(self, algorithm) -> None:
        '''
        Method to update radio buttons, reset the GUI, and display the description of an algorithm upon selection
        '''

        # Update radio buttons
        self.radioLinearSearch.config(state = DISABLED if algorithm == 1 else NORMAL)
        self.radioBinarySearch.config(state = DISABLED if algorithm == 2 else NORMAL)
        self.radioBubbleSort.config(state = DISABLED if algorithm == 3 else NORMAL)
        self.radioSelectionSort.config(state = DISABLED if algorithm == 4 else NORMAL)
        self.radioInsertionSort.config(state = DISABLED if algorithm == 5 else NORMAL)

        # Destroy all frames if a different algorithm is selected (resets GUI)
        self.frame = [
            self.algorithmSelectionFrame,
            self.algorithmSelectionContinueFrame,
            self.algorithmDescriptionFrame,
            self.algorithmDescriptionContinueFrame,
            self.getInputFrame,
            self.getInputErrorFrame,
            self.getTargetFrame,
            self.getTargetErrorFrame,
            self.searchAlgorithmOutputFrame,
            self.sortAlgorithmOutputFrame
        ]

        for frame in self.frame: 
            if frame:
                frame.destroy()

        # Display algorithm introduction 
        self.algorithmSelectionFrame = Frame(self.window)
        if algorithm == 1: 
            self.algorithmSelectionText = 'A linear search algorithm finds a target value in an array by sequentially checking each element until the target is found or the array ends'
        elif algorithm == 2: 
            self.algorithmSelectionText = 'A binary search algorithm finds a target value in a sorted array by repeatedly halving the search range until the target is found or the range is empty'
        elif algorithm == 3: 
            self.algorithmSelectionText = 'A bubble sort algorithm sorts an array by repeatedly comparing and swapping adjacent elements until the array is sorted'
        elif algorithm == 4: 
            self.algorithmSelectionText = 'A selection sort algorithm sorts an array by finding the smalles element in the unsorted portion of the array and swapping it with the first element in the unsorted portion'
        else: 
            self.algorithmSelectionText = 'An insertion sort algorithm sorts an array by repeatedly taking one element and inserting it into its correct position relative to the already sorted portion of the array'
        self.algorithmSelectionLabel = Label(
            self.algorithmSelectionFrame, 
            text = self.algorithmSelectionText,
            font = ('System', 12),
            wraplength = 550
        ).pack(side = 'top')
        self.algorithmSelectionFrame.pack(side = 'top', pady = 5)

        # Display continue checkbox
        self.algorithmSelectionContinueFrame = Frame(self.window)
        self.algorithmSelectionContinueVar = IntVar() 
        self.algorithmSelectionContinueCheckbox = Checkbutton(
            self.algorithmSelectionContinueFrame, 
            text = 'Continue', 
            font = ('System', 12),
            variable = self.algorithmSelectionContinueVar, 
            command = lambda: self.algorithmDescription(algorithm) if self.algorithmSelectionContinueVar.get() else None
        )
        self.algorithmSelectionContinueCheckbox.pack()
        self.algorithmSelectionContinueFrame.pack(side = 'top')

    def algorithmDescription(self, algorithm) -> None:
        '''
        Method to display the algorithm details
        '''

        # Destroy previous checkbox
        self.algorithmSelectionContinueCheckbox.destroy()
        self.algorithmSelectionContinueFrame.destroy()
        
        # Display algorithm details (runtimes, pros, and cons)
        if algorithm == 1: 
            self.algorithmDescriptionRuntimesString = 'RUNTIMES \n Best Case: O(1) \n Average Case: O(n) \n Worst Case: O(n)'
            self.algorithmDescriptionProsString = 'PROS \n Easy implementation \n Works on sorted and unsorted arrays'
            self.algorithmDescriptionConsString = 'CONS \n Inefficient searching \n Does not utilize sorted data'

        elif algorithm == 2: 
            self.algorithmDescriptionRuntimesString = 'RUNTIMES \n Best Case: O(1) \n Average Case: O(log n) \n Worst Case: O(log n)'
            self.algorithmDescriptionProsString = 'PROS \n Fast searching on large datasets \n Efficient with sorted data'
            self.algorithmDescriptionConsString = 'CONS \n Requires sorted array \n More complex implementation'

        elif algorithm == 3: 
            self.algorithmDescriptionRuntimesString = 'RUNTIMES \n Best Case: O(n) \n Average Case: O(n^2) \n Worst Case: O(n^2)'
            self.algorithmDescriptionProsString = 'PROS \n Simple to understand \n Useful for small datasets'
            self.algorithmDescriptionConsString = 'CONS \n Inefficient for large datasets \n Poor performance'

        elif algorithm == 4: 
            self.algorithmDescriptionRuntimesString = 'RUNTIMES \n Best Case: O(n^2) \n Average Case: O(n^2) \n Worst Case: O(n^2)'
            self.algorithmDescriptionProsString = 'PROS \n Easy to implement \n No extra memory needed'
            self.algorithmDescriptionConsString = 'CONS \n Always performs O(n^2) comparisons \n Inefficient for large datasets'

        elif algorithm == 5: 
            self.algorithmDescriptionRuntimesString = 'RUNTIMES \nBest Case: O(n)\n Average Case: O(n^2) \n Worst Case: O(n^2)'
            self.algorithmDescriptionProsString = 'PROS \n Simple implementation \n Efficient for small or nearly sorted datasets'
            self.algorithmDescriptionConsString = 'CONS \n Inefficient for large or unsorted datasets \n Slower than advanced algorithms'

        self.algorithmDescriptionFrame = Frame(self.window)

        self.algorithmDescriptionRuntimes = Frame(self.algorithmDescriptionFrame)
        self.algorithmDescriptionRuntimesLabel = Label(
            self.algorithmDescriptionRuntimes,
            text = self.algorithmDescriptionRuntimesString,
            font = ('System', 11),
            wraplength = 300
        )
        self.algorithmDescriptionRuntimesLabel.pack()
        self.algorithmDescriptionRuntimes.pack(side='left', padx = 20)

        self.algorithmDescriptionPros = Frame(self.algorithmDescriptionFrame)
        self.algorithmDescriptionProsLabel = Label(
            self.algorithmDescriptionPros,
            text = self.algorithmDescriptionProsString,
            font = ('System', 11),
            wraplength = 300
        )
        self.algorithmDescriptionProsLabel.pack()
        self.algorithmDescriptionPros.pack(side='left', padx = 20)

        self.algorithmDescriptionCons = Frame(self.algorithmDescriptionFrame)
        self.algorithmDescriptionConsLabel = Label(
            self.algorithmDescriptionCons,
            text = self.algorithmDescriptionConsString,
            font = ('System', 11),
            wraplength = 300
        )
        self.algorithmDescriptionConsLabel.pack()
        self.algorithmDescriptionCons.pack(side='right', padx = 20)

        self.algorithmDescriptionFrame.pack(side='top')

        # Display continue checkbox
        self.algorithmDescriptionContinueFrame = Frame(self.window)
        self.algorithmDescriptionContinueVar = IntVar() 
        self.algorithmDescriptionContinueCheckbox = Checkbutton(
            self.algorithmDescriptionContinueFrame, 
            text = 'Continue', 
            font = ('System', 12),
            variable = self.algorithmDescriptionContinueVar, 
            command = lambda: self.getInput(algorithm) if self.algorithmDescriptionContinueVar.get() else None
        )
        self.algorithmDescriptionContinueCheckbox.pack()
        self.algorithmDescriptionContinueFrame.pack(side = 'top', pady = 15)

    def getInput(self, algorithm) -> None:
        '''
        Method to get input from user
        '''

        # Destroy previous checkbox and detail frames
        self.algorithmDescriptionContinueFrame.destroy()

        # Display input frame
        self.getInputFrame = Frame(self.window)
        self.getInputLabel = Label(
            self.getInputFrame,
            text = 'Enter a list of 3 - 10 numbers:',
            font = ('System', 11),
        )
        self.getInputLabel.pack(side = 'left', padx = 10)
        self.getInputEntry = Entry(
            self.getInputFrame,
            width = 20
        )
        self.getInputEntry.pack(side = 'left', padx = 10)
        self.getInputCheckboxVar = IntVar()
        self.getInputCheckbox = Checkbutton(
            self.getInputFrame, 
            text = 'Enter',
            font = ('System', 12),
            variable = self.getInputCheckboxVar, 
            command = lambda: self.inputCheck(algorithm) if self.getInputCheckboxVar.get() else None
        )
        self.getInputCheckbox.pack(side = 'left', padx = 10)
        self.getInputFrame.pack(side = 'top', pady = 15)
        self.getInputFrame.update_idletasks()

        # Initialize input error frame
        self.getInputErrorFrame = Frame(self.window)
        self.getInputErrorLabel = Label(self.getInputErrorFrame)
        self.getInputErrorLabel.config(text = '')

    def inputCheck(self, algorithm) -> None:
        '''
        Method to check if input is valid (exception handling)
        ''' 

        # Check if input is valid
        try:
            self.inputEntryValue = self.getInputEntry.get()
            array = [
                int(num) if num.isdigit() else float(num) 
                for num in self.inputEntryValue.split()
            ] # convert input to numbers
            if len(array) > 10: # cut list if input is too long
                array = array[0:10]
            elif len(array) < 3 : # raise error if input is too short
                raise ValueError
            self.getInputEntry.config(state='disabled')
            self.getInputCheckbox.config(state='disabled') # disable entry and checbox
            if algorithm == 1 or algorithm == 2:  
                self.getTarget(algorithm, array)
            else: 
                self.sortAlgorithmOutput(algorithm, array) # send input to next method based on algorithm

        # Clear input and display error message
        except ValueError:
            self.getInputEntry.delete(0, END)
            self.getInputErrorLabel.config(text = 'Enter a valid list')
            self.getInputErrorLabel.pack(side = 'bottom', pady = 10)
            self.getInputErrorFrame.pack(side = 'top')
            self.getInputCheckboxVar.set(0)
            self.getInputCheckbox.config(state = 'normal')

    def getTarget(self, algorithm, array) -> None: 
        '''
        Method to get target value if a search algorithm is selected
        ''' 

        # Destroy input error frame if it exists
        if self.getInputErrorFrame:
            self.getInputErrorFrame.destroy()

        # Display target frame
        self.getTargetFrame = Frame(self.window)
        self.getTargetLabel = Label(
                self.getTargetFrame,
                text = 'Enter the target value:',
                font = ('System', 12)
            ).pack(side = 'left', pady = 5)
        self.getTargetEntry = Entry(
            self.getTargetFrame,
            width = 10
        )
        self.getTargetEntry.pack(side = 'left', padx = 10)
        self.getTargetCheckboxVar = IntVar()
        self.getTargetCheckbox = Checkbutton(
            self.getTargetFrame, 
            text = 'Enter',
            font = ('System', 12),
            variable = self.getTargetCheckboxVar, 
            command = lambda: self.targetCheck(algorithm, array) if self.getTargetCheckboxVar.get() else None
        )
        self.getTargetCheckbox.pack(side = 'left', padx = 10)
        self.getTargetFrame.pack(side = 'top', pady = 15)
        self.getInputFrame.update_idletasks()

        # Initialize target error frame
        self.getTargetErrorFrame = Frame(self.window)
        self.getTargetErrorLabel = Label(self.getTargetErrorFrame)
        self.getTargetErrorLabel.config(text = '')

    def targetCheck(self, algorithm, array) -> None: 
        '''
        Method to check if target value is valid (exception handling)
        ''' 

        # Check if target is valid
        try:
            self.targetInputValue = self.getTargetEntry.get()
            target = [
                int(num) if num.isdigit() else float(num) 
                for num in self.targetInputValue.split()
            ] # convert list to numbers
            if len(target) != 1: # raise error if target is too long
                raise ValueError
            target = target[0] 
            self.getTargetEntry.config(state='disabled')
            self.getTargetCheckbox.config(state='disabled') # disable entry and checkbox
            self.searchAlgorithmOutput(algorithm, array, target)

        # Clear target and display error message
        except ValueError:
            self.getTargetEntry.delete(0, END)
            self.getTargetErrorLabel.config(text = 'Enter a valid target value')
            self.getTargetErrorLabel.pack(side = 'bottom', pady = 10)
            self.getTargetErrorFrame.pack(side = 'top')
            self.getTargetCheckboxVar.set(0)
            self.getTargetCheckbox.config(state = 'normal')

    def searchAlgorithmOutput(self, algorithm, array, target) -> None: 
        '''
        Method to call proper function from modules file and output results
        ''' 

        # Destroy target error frame if it exists
        if self.getTargetErrorFrame: 
            self.getTargetErrorFrame.destroy()

        # Call function from modules.py based on algorithm
        if algorithm == 1: 
            self.output = linearSearch(array, target)
        else: 
            self.output = binarySearch(array, target)

        # Display output from function
        self.searchAlgorithmOutputFrame = Frame(self.window)
        for line in self.output:
            Label(
                self.searchAlgorithmOutputFrame, 
                text = line, 
                font = ('Courier', 11)
            ).pack(side = 'top')
        self.searchAlgorithmOutputFrame.pack(side = 'top', pady = 15)
    
    def sortAlgorithmOutput(self, algorithm, array) -> None:
        '''
        Method to call proper function from modules file and output results
        ''' 

        # Destroy input error frame if it exists
        if self.getInputErrorFrame:
            self.getInputErrorFrame.destroy()

        # Call function from modules.py based on algorithm
        if algorithm == 3: 
            self.output = bubbleSort(array)
        elif algorithm == 4:
            self.output = selectionSort(array)
        else: 
            self.output = insertionSort(array)

        # Display output from function
        self.sortAlgorithmOutputFrame = Frame(self.window)
        for line in self.output: 
            Label(
                self.sortAlgorithmOutputFrame, 
                text = line, 
                font = ('Courier', 11)
            ).pack(side = 'top')
        self.sortAlgorithmOutputFrame.pack(side = 'top', pady = 15)