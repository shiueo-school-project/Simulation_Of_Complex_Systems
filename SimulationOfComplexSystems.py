import math
import os
import random
import sys
import threading
import time
import matplotlib.pyplot as plt
import glfw
from PySide6.QtWidgets import (
    QApplication,
    QLabel,
    QWidget,
    QVBoxLayout,
    QLineEdit,
    QHBoxLayout,
    QPushButton,
)
from PySide6.QtCore import Qt, QTimer, QCoreApplication


from utils import global_path, set_variables


class LoadingUI(QWidget):
    def __init__(self, size_x, size_y):
        super().__init__()
        self.size_x = size_x
        self.size_y = size_y
        self.n_a_label = QLabel("A의 수")
        self.n_a_lineedit = QLineEdit()
        self.n_a_lineedit.setPlaceholderText("A의 수")

        self.n_b_label = QLabel("B의 수")
        self.n_b_lineedit = QLineEdit()
        self.n_b_lineedit.setPlaceholderText("B의 수")

        self.p_a_label = QLabel("A가 태어날 확률")
        self.p_a_lineedit = QLineEdit()
        self.p_a_lineedit.setPlaceholderText("A가 태어날 확률")

        self.p_b_label = QLabel("B가 태어날 확률")
        self.p_b_lineedit = QLineEdit()
        self.p_b_lineedit.setPlaceholderText("B가 태어날 확률")

        self.t_g_label = QLabel("굶을 때 버틸 수 있는 시간")
        self.t_g_lineedit = QLineEdit()
        self.t_g_lineedit.setPlaceholderText("굶을 때 버틸 수 있는 시간")

        self.l_a_label = QLabel("A의 수명")
        self.l_a_lineedit = QLineEdit()
        self.l_a_lineedit.setPlaceholderText("A의 수명")

        self.l_b_label = QLabel("B의 수명")
        self.l_b_lineedit = QLineEdit()
        self.l_b_lineedit.setPlaceholderText("B의 수명")

        self.q_r_label = QLabel("자원의 양")
        self.q_r_lineedit = QLineEdit()
        self.q_r_lineedit.setPlaceholderText("자원의 양")

        self.p_p_label = QLabel("A와 B가 충돌했을 때, A가 사라질 확률")
        self.p_p_lineedit = QLineEdit()
        self.p_p_lineedit.setPlaceholderText("A와 B가 충돌했을 때, A가 사라질 확률")

        self.ApplyButton = QPushButton("Apply")
        self.ApplyButton.clicked.connect(lambda: self.Apply_Button())
        self.StopButton = QPushButton("Stop")
        self.StopButton.clicked.connect(lambda: self.Stop_Button())
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.start()
        self.timer.timeout.connect(lambda: self.UPdate())

        self.DRAW_GRAPH_BUTTON = QPushButton("DRAW GRAPH")
        self.DRAW_GRAPH_BUTTON.clicked.connect(lambda: self.draw_graph())

        self.RESET_GRAPH_BUTTON = QPushButton("RESET GRAPH")
        self.RESET_GRAPH_BUTTON.clicked.connect(lambda: self.reset_graph())

        self.running = False

        self.a_quantity = None
        self.b_quantity = None
        self.resources_quantity = None
        self.p_p_die_quantity = None
        self.time_starve = None
        self.a_birth_rate = None
        self.b_birth_rate = None
        self.a_life_length = None
        self.b_life_length = None

        self.a_quantity_list = []
        self.b_quantity_list = []
        self.p_p_list = []
        self.event_list = []

        self.APPLY = False
        self.RESOURCES_X_POS = ""
        self.RESOURCES_Y_POS = ""
        self.A_X_POS = ""
        self.A_Y_POS = ""
        self.A_X_RETURN = ""
        self.A_Y_RETURN = ""
        self.B_X_POS = ""
        self.B_Y_POS = ""
        self.B_X_RETURN = ""
        self.B_Y_RETURN = ""

        self.relative_time = 0

        self.initUI()

    def initUI(self):
        self.a_quantity = 100
        self.b_quantity = 100
        self.resources_quantity = 100
        self.p_p_die_quantity = 100

        self.setWindowTitle("Simulation_Of_Complex_Systems_Control_Panel")
        self.resize(self.size_x, self.size_y)

        EntireLayout = QVBoxLayout()

        n_a_layout = QHBoxLayout()
        n_a_layout.addWidget(self.n_a_label)
        n_a_layout.addWidget(self.n_a_lineedit)

        n_b_layout = QHBoxLayout()
        n_b_layout.addWidget(self.n_b_label)
        n_b_layout.addWidget(self.n_b_lineedit)

        p_a_layout = QHBoxLayout()
        p_a_layout.addWidget(self.p_a_label)
        p_a_layout.addWidget(self.p_a_lineedit)

        p_b_layout = QHBoxLayout()
        p_b_layout.addWidget(self.p_b_label)
        p_b_layout.addWidget(self.p_b_lineedit)

        t_g_layout = QHBoxLayout()
        t_g_layout.addWidget(self.t_g_label)
        t_g_layout.addWidget(self.t_g_lineedit)

        l_a_layout = QHBoxLayout()
        l_a_layout.addWidget(self.l_a_label)
        l_a_layout.addWidget(self.l_a_lineedit)

        l_b_layout = QHBoxLayout()
        l_b_layout.addWidget(self.l_b_label)
        l_b_layout.addWidget(self.l_b_lineedit)

        q_r_layout = QHBoxLayout()
        q_r_layout.addWidget(self.q_r_label)
        q_r_layout.addWidget(self.q_r_lineedit)

        p_p_layout = QHBoxLayout()
        p_p_layout.addWidget(self.p_p_label)
        p_p_layout.addWidget(self.p_p_lineedit)

        choose_layout = QHBoxLayout()
        choose_layout.addWidget(self.ApplyButton)
        choose_layout.addWidget(self.StopButton)
        choose_layout.addWidget(self.DRAW_GRAPH_BUTTON)
        choose_layout.addWidget(self.RESET_GRAPH_BUTTON)

        EntireLayout.addLayout(n_a_layout)
        EntireLayout.addLayout(n_b_layout)
        EntireLayout.addLayout(p_a_layout)
        EntireLayout.addLayout(p_b_layout)
        EntireLayout.addLayout(t_g_layout)
        EntireLayout.addLayout(p_p_layout)
        EntireLayout.addLayout(l_a_layout)
        EntireLayout.addLayout(l_b_layout)
        EntireLayout.addLayout(q_r_layout)
        EntireLayout.addLayout(choose_layout)
        self.setLayout(EntireLayout)

    def Apply_Button(self):
        self.relative_time = 0
        self.running = True
        self.RESOURCES_X_POS = ""
        self.RESOURCES_Y_POS = ""
        self.A_X_POS = ""
        self.A_Y_POS = ""
        self.APPLY = True

        self.resources_quantity = int(self.q_r_lineedit.text())
        self.a_quantity = int(self.n_a_lineedit.text())
        self.b_quantity = int(self.n_b_lineedit.text())
        self.p_p_die_quantity = int(self.p_p_lineedit.text())
        self.a_birth_rate = int(self.p_a_lineedit.text())
        self.b_birth_rate = int(self.p_b_lineedit.text())
        print(self.resources_quantity, self.a_quantity)

        for i in range(self.resources_quantity):
            self.RESOURCES_X_POS = self.RESOURCES_X_POS + " " + str(round(random.uniform(-1, 1), 6))
            self.RESOURCES_Y_POS = self.RESOURCES_Y_POS + " " + str(round(random.uniform(-1, 1), 6))

        for i in range(self.a_quantity):
            self.A_X_POS = self.A_X_POS + " " + str(round(random.uniform(-1, 1), 6))
            self.A_Y_POS = self.A_Y_POS + " " + str(round(random.uniform(-1, 1), 6))
            self.A_X_RETURN = self.A_X_RETURN + " " + "False"
            self.A_Y_RETURN = self.A_Y_RETURN + " " + "False"

        for i in range(self.b_quantity):
            self.B_X_POS = self.B_X_POS + " " + str(round(random.uniform(-1, 1), 6))
            self.B_Y_POS = self.B_Y_POS + " " + str(round(random.uniform(-1, 1), 6))
            self.B_X_RETURN = self.B_X_RETURN + " " + "False"
            self.B_Y_RETURN = self.B_Y_RETURN + " " + "False"

    def Stop_Button(self):
        self.running = False
        self.APPLY = False
        self.RESOURCES_X_POS = ""
        self.RESOURCES_Y_POS = ""
        self.A_X_POS = ""
        self.A_Y_POS = ""
        self.A_X_RETURN = ""
        self.A_Y_RETURN = ""
        self.B_X_POS = ""
        self.B_Y_POS = ""
        self.B_X_RETURN = ""
        self.B_Y_RETURN = ""
        self.relative_time = 0
        self.event_list.clear()

    def reset_graph(self):
        self.a_quantity_list.clear()
        self.b_quantity_list.clear()
        self.p_p_list.clear()

    def draw_graph(self):
        plt.plot(self.a_quantity_list)
        plt.plot(self.b_quantity_list)
        plt.legend("ab")
        plt.show()

    def UPdate(self):
        if self.running:
            self.a_quantity_list.append(self.a_quantity)
            self.b_quantity_list.append(self.b_quantity)
            self.p_p_list.append(self.p_p_lineedit.text())

            A_X = list(map(float, self.A_X_POS.split()))
            A_Y = list(map(float, self.A_Y_POS.split()))
            A_X_RE = list(map(str, self.A_X_RETURN.split()))
            A_Y_RE = list(map(str, self.A_Y_RETURN.split()))
            self.A_X_POS = ""
            self.A_Y_POS = ""
            self.A_X_RETURN = ""
            self.A_Y_RETURN = ""
            for i in range(self.a_quantity):
                if A_X[i] < -1:
                    self.A_X_RETURN = self.A_X_RETURN + " " + "True"
                elif A_X[i] > 1:
                    self.A_X_RETURN = self.A_X_RETURN + " " + "False"
                else:
                    self.A_X_RETURN = self.A_X_RETURN + " " + A_X_RE[i]
                if A_Y[i] < -1:
                    self.A_Y_RETURN = self.A_Y_RETURN + " " + "True"
                elif A_Y[i] > 1:
                    self.A_Y_RETURN = self.A_Y_RETURN + " " + "False"
                else:
                    self.A_Y_RETURN = self.A_Y_RETURN + " " + A_Y_RE[i]

                if A_X_RE[i] == "True":
                    NEW_A_X = A_X[i] + random.uniform(0.03, 0.04)
                else:
                    NEW_A_X = A_X[i] - random.uniform(0.03, 0.04)

                if A_Y_RE[i] == "True":
                    NEW_A_Y = A_Y[i] + random.uniform(0.03, 0.04)
                else:
                    NEW_A_Y = A_Y[i] - random.uniform(0.03, 0.04)
                # print(NEW_A_X, NEW_A_Y)
                self.A_X_POS = self.A_X_POS + " " + str(NEW_A_X)
                self.A_Y_POS = self.A_Y_POS + " " + str(NEW_A_Y)

            ############################################################################################


            B_X = list(map(float, self.B_X_POS.split()))
            B_Y = list(map(float, self.B_Y_POS.split()))
            B_X_RE = list(map(str, self.B_X_RETURN.split()))
            B_Y_RE = list(map(str, self.B_Y_RETURN.split()))
            self.B_X_POS = ""
            self.B_Y_POS = ""
            self.B_X_RETURN = ""
            self.B_Y_RETURN = ""
            for i in range(self.b_quantity):
                if B_X[i] < -1:
                    self.B_X_RETURN = self.B_X_RETURN + " " + "True"
                elif B_X[i] > 1:
                    self.B_X_RETURN = self.B_X_RETURN + " " + "False"
                else:
                    self.B_X_RETURN = self.B_X_RETURN + " " + B_X_RE[i]
                if B_Y[i] < -1:
                    self.B_Y_RETURN = self.B_Y_RETURN + " " + "True"
                elif B_Y[i] > 1:
                    self.B_Y_RETURN = self.B_Y_RETURN + " " + "False"
                else:
                    self.B_Y_RETURN = self.B_Y_RETURN + " " + B_Y_RE[i]

                if B_X_RE[i] == "True":
                    NEW_B_X = B_X[i] + random.uniform(0.03, 0.04)
                else:
                    NEW_B_X = B_X[i] - random.uniform(0.03, 0.04)

                if B_Y_RE[i] == "True":
                    NEW_B_Y = B_Y[i] + random.uniform(0.03, 0.04)
                else:
                    NEW_B_Y = B_Y[i] - random.uniform(0.03, 0.04)
                # (NEW_B_X, NEW_B_Y)
                self.B_X_POS = self.B_X_POS + " " + str(NEW_B_X)
                self.B_Y_POS = self.B_Y_POS + " " + str(NEW_B_Y)

            ############################################################################################
            for i in range(len(A_X)):
                for j in range(len(B_X)):
                    if abs(A_X[i] - B_X[j]) < 0.025 and abs(A_Y[i] - B_Y[j]) < 0.025 and random.randrange(1, 100) % int(
                            100 / int(self.p_p_die_quantity)) == 0:
                        self.event_list.append("a,b collapsed")
                        self.a_quantity = int(self.a_quantity) - 1
                        #print(self.a_quantity, self.b_quantity)
                        break
                '''else:
                    continue
                break'''

            for i in range(len(A_X)):
                for j in range(len(A_X)):
                    if abs(A_X[i] - A_X[j]) < 0.025 and abs(A_Y[i] - A_Y[j]) < 0.025 and random.randrange(1, 100) % int(
                            100 / int(self.a_birth_rate)) == 0 and A_X[i] - A_X[j] != 0 and A_Y[i] - A_Y[j] != 0:
                        self.event_list.append("A birth")
                        self.a_quantity = self.a_quantity + 1
                        self.A_X_POS = self.A_X_POS + " " + str(round(random.uniform(-1, 1), 6))
                        self.A_Y_POS = self.A_Y_POS + " " + str(round(random.uniform(-1, 1), 6))
                        self.A_X_RETURN = self.A_X_RETURN + " " + "False"
                        self.A_Y_RETURN = self.A_Y_RETURN + " " + "False"
                        break
                '''else:
                    continue
                break'''

            for i in range(len(B_X)):
                for j in range(len(B_X)):
                    if abs(B_X[i] - B_X[j]) < 0.025 and abs(B_Y[i] - B_Y[j]) < 0.025 and random.randrange(1, 100) % int(
                            100 / int(self.b_birth_rate)) == 0 and B_X[i] - B_X[j] != 0 and B_Y[i] - B_Y[j] != 0:
                        self.event_list.append("B birth")
                        self.b_quantity = self.b_quantity + 1
                        self.B_X_POS = self.B_X_POS + " " + str(round(random.uniform(-1, 1), 6))
                        self.B_Y_POS = self.B_Y_POS + " " + str(round(random.uniform(-1, 1), 6))
                        self.B_X_RETURN = self.B_X_RETURN + " " + "False"
                        self.B_Y_RETURN = self.B_Y_RETURN + " " + "False"
                        break
                '''else:
                    continue
                break'''

            if self.relative_time % int(self.t_g_lineedit.text()) == 0:
                self.a_quantity = self.a_quantity - 1
                self.b_quantity = self.b_quantity - 1
                self.event_list.append("a_starved_dead")
                self.event_list.append("b_starved_dead")

            print("A_QUANTITY: " + str(self.a_quantity) + "//B_QUANTITY: " + str(self.b_quantity) + "//Event: " + str(set(self.event_list)))
            self.event_list.clear()
            self.relative_time+=1


global app, loaderThread, t


def window_shower(size_x: int, size_y: int):
    global app, t
    app = QApplication(sys.argv)
    loadingWin = LoadingUI(size_x=size_x, size_y=size_y)
    loadingWin.show()
    app.exec()
    sys.exit(0)


global_path.set_abs_path(path=__file__)
window_shower(600, 300)
