from PyQt6.QtWidgets import *
from gui import *
import csv
import math


class Logic(QMainWindow, Ui_QTU_Tracker):
    '''App that collects key metric data for keeping track of metrics for the week'''

    def __init__(self):
        '''Function that creates the app and gathers data for computations'''
        super().__init__()
        self.setupUi(self)
        self.frame_2.hide()
        self.frame_3.hide()
        self.frame_4.hide()

        self.var_list = []


        self.submit_button1.clicked.connect(lambda: self.enter_name())
        self.submit_button2.clicked.connect(lambda: self.basic_metrics())
        self.submit_button3.clicked.connect(lambda: self.summary())
        self.Close_button.clicked.connect(lambda: self.close_window())
        self.save_button.clicked.connect(lambda: self.update_data())

    def enter_name(self):
        user_name = self.name_input.text()
        if user_name == '':
            self.guide_1.setText('Enter a valid name')
        else:
            self.var_list.append(user_name)
            self.output_name.setText(f'{user_name}')
            self.frame_2.show()
            self.name_input.setReadOnly(True)
            self.submit_button1.hide()
            self.guide_1.setText('')

    def basic_metrics(self):
        try:
            wanted_aph = float(self.aph_input.text())
            worked_hours = float(self.hoursworked_input.text())
            queue_time_percentage = float(self.QueuePercent_input.text())
            num_cases = ((queue_time_percentage/100)*worked_hours)*wanted_aph
            time_out = (worked_hours-((queue_time_percentage/100)*worked_hours))
            time_in = (queue_time_percentage/100)*worked_hours
            if wanted_aph <= 0 or worked_hours <= 0 or queue_time_percentage <= 0:
                raise ValueError
            elif type(wanted_aph) == str or type(worked_hours) == str or type(queue_time_percentage) == str:
                raise TypeError
            else:
                self.var_list.append(wanted_aph)
                self.var_list.append(worked_hours)
                self.var_list.append(num_cases)
                self.var_list.append(time_out)
                self.var_list.append(time_in)
                self.output_aph.setText(f'{wanted_aph:.2f} per hour')
                self.output_hoursNweek.setText(f'{worked_hours:.2f} hours')
                self.output_timein.setText(f'{(queue_time_percentage/100)*worked_hours:.2f} hours')
                self.output_timeout.setText(f'{(worked_hours-((queue_time_percentage/100)*worked_hours)):.2f} hours')
                self.output_cases.setText(f'{((queue_time_percentage/100)*worked_hours)*wanted_aph:.2f} cases')
                self.frame_3.show()
                self.aph_input.setReadOnly(True)
                self.hoursworked_input.setReadOnly(True)
                self.QueuePercent_input.setReadOnly(True)
                self.submit_button2.hide()
                self.guide_2.setText('')
        except ValueError:
            self.guide_2.setText('Enter a valid integer or float for all fields')
        except TypeError:
            self.guide_2.setText('Enter a valid integer or float for all fields')



    def summary(self):
        try:
            mon = float(self.mon_input.text())
            tue = float(self.tues_input.text())
            wed = float(self.wed_input.text())
            thu = float(self.thurs_input.text())
            fri = float(self.fri_input.text())
            time_used  = (mon + tue + wed + thu + fri)
            time_remaining = self.var_list[4] - time_used
            if mon < 0 or tue < 0 or wed < 0 or thu < 0 or fri < 0:
                raise ValueError
            elif type(mon) == str or type(tue) == str or type(wed) == str or type(thu) == str or type(fri) == str:
                raise TypeError
            else:
                self.var_list.append(time_used)
                self.var_list.append(time_remaining)
                self.output_timeremaining.setText(f'{time_remaining:.2f} hours')
                self.output_timeused.setText(f'{time_used:.2f} hours')
                self.frame_4.show()
                self.mon_input.setReadOnly(True)
                self.tues_input.setReadOnly(True)
                self.wed_input.setReadOnly(True)
                self.thurs_input.setReadOnly(True)
                self.fri_input.setReadOnly(True)
                self.submit_button3.hide()
                self.guide_3.setText('')

        except ValueError:
            self.guide_3.setText('Enter a valid number or a 0 in all unused fields')
        except TypeError:
            self.guide_3.setText('Enter a valid number or a 0 in all unused fields')


    def close_window(self):
        self.close()

    def update_data(self):
        print(self.var_list)

        with open('my_qtu.csv','rU') as csv_file1:
            csv_reader = csv.reader(csv_file1)
            csv_writer = csv.writer(csv_file1)

            for line in csv_reader:
                csv_file1.seek(0)
                if line[0].strip() == self.var_list[0].strip():
                    csv_writer.writerow(self.var_list)
                    return
                csv_file1.seek(0,2)
                csv_writer.writerow(self.var_list)








