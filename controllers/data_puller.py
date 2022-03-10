import PySimpleGUI as sg
import lil_helpers as lil_h

sg.theme('Black')  # Let's set our own color theme

# STEP 1 define the layout
layout = [ 
            [sg.Text('Welcome to RegTech Data Puller')],
            [sg.Text('Please Input the Path to S3:')],
            [sg.Input(key='-PATH-')],
            [sg.Text('Please input the OMS or leave empty if none:')],
            [sg.Input(key='-OMS-')],
            [sg.Text('Please select the type of data you want to pull:')],
            [sg.Checkbox('Raw Data')],
            [sg.Checkbox('FCA Data')],
            [sg.Checkbox('Pre Enriched Data')],
            [sg.Checkbox('Comparison Test Fails')],
            [sg.Checkbox('Assurance Test Fails')],
            [sg.Text('Please select a start date and an end date of the range. (End date is excluesive)')],
            [sg.Input(key='-STARTDATE-'), sg.CalendarButton('Start Date',  target='-STARTDATE-', format='%Y-%m', default_date_m_d_y=(1,None,2020),)],
            [sg.Input(key='-ENDDATE-'), sg.CalendarButton('End Date',  target='-ENDDATE-', format='%Y-%m', default_date_m_d_y=(1,None,2020),)],
            [sg.Button('Pull Data'), sg.Button('Exit')]
         ]

#STEP 2 - create the window
window = sg.Window('My new window', layout)

# STEP3 - the event loop
while True:
    event, values = window.read()   # Read the event that happened and the values dictionary
    print(event, values)
    if event == sg.WIN_CLOSED or event == 'Exit':     # If user closed window with X or if user clicked "Exit" button then exit
        break
    if event == 'Pull Data':
        # Connect to the server and the users corresponding folder
        main_folder_path = values['-PATH-']
        oms = values['-OMS-']
        controller_settings={}
        controller_settings["Pull Raw Data?"] = values[0]
        controller_settings["Pull FCA Data?"] = values[1]
        controller_settings["Pull Pre Enriched Data?"] = values[2]
        controller_settings["Pull Comparison Test Fails?"] = values[3]
        controller_settings["Pull Assurance Test Fails?"] = values[4]
        
        print(lil_h.date_gap_to_dic(values['-STARTDATE-'],values['-ENDDATE-']))
        
        
        
        # print(controller_settings)
window.close()