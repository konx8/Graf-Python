from tkinter import scrolledtext
from tkinter import *
from tkinter.ttk import Combobox

import matplotlib
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt

import top as top

matplotlib.use('TkAgg')
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



G = nx.Graph()

# Main
window = Tk()
window.title("Grafy")
window.geometry("1000x600")

def click1():
    display = Label(window, text=e.get())
    display.grid(row=4, column=0)

    wi1 = int(e.get())
    l_w = [i for i in range(1, wi1+1)]
    combo1['value'] = l_w
    combo1.current(0)

    combo2['value'] = l_w
    combo2.current(0)

def drow(): # rysuj
    button_war.config(state="normal")
    button_Hami.config(state="normal")
    wi1 = int(e.get())
    l_w = [i for i in range(1, wi1+1)]
    nodes = l_w

    G.add_nodes_from(nodes)
    A = nx.to_numpy_matrix(G)
    np.savetxt("am.txt", A, delimiter=' ', fmt='%d')
    nx.draw_networkx(G)
    plt.show()




    # return(A) !!!!!!!!!!!!!!!!!!!

def connect():
    combo_1 = int(combo1.get())
    combo_2 = int(combo2.get())

    G.add_edge(combo_1, combo_2)
    stext.insert(INSERT, combo1.get() + ' z ' + combo2.get() + '\n')

    return G.add_edge(combo_1, combo_2)

def drow_m_s(): # macierz sasiedstwa
    daneMS = stext2.get('1.0', 'end-1c')
    entries = list(map(int, daneMS.split()))
    re = int(e.get())
    daneMS = np.array(entries).reshape(re,re)

    np.savetxt("am.txt", daneMS, delimiter=' ', fmt='%d')
    X = np.loadtxt("am.txt")
    print(X)
    O=nx.from_numpy_matrix(daneMS)
    nx.draw_networkx(O)
    plt.show()

def drow_m_i(): # macierz incydencji
    M_i = int(e_m_i.get())
    daneM_i = int(e.get())
    inciliststr = stext3.get('1.0', 'end-1c')
    ent = list(map(int, inciliststr.split()))
    dane_incy = np.array(ent).reshape(daneM_i, M_i)

    am = (np.dot(dane_incy, dane_incy.T) > 0).astype(int)
    K = nx.from_numpy_matrix(am)
    nx.draw_networkx(K)
    plt.show()

def drow_l_s(): # lista sasiedstwa
    inciliststr = stext4.get('1.0', 'end-1c')
    incidencelist = inciliststr.split('\n')
    P = nx.parse_adjlist(incidencelist, nodetype=int)

    nx.draw_networkx(P)
    plt.show()

def drow_war():
    if nx.is_eulerian(G) == True:
        warunki = Label(window, text="Warunek Eulera spełniony")
        warunki.grid(row=5, column=4)
        button_Eul.config(state="normal")
    else:
        warunki = Label(window, text="Warunek Eulera niespelniony")
        warunki.grid(row=5, column=4)


def drow_Eul():
    warunki.delete(0, 'end')
    def findpath(graph):
        n = len(graph)
        numofadj = list()

        # Find out number of edges each vertex has
        for i in range(n):
            numofadj.append(sum(graph[i]))

            # Find out how many vertex has odd number edges
        startpoint = 0
        numofodd = 0
        for i in range(n - 1, -1, -1):
            if (numofadj[i] % 2 == 1):
                numofodd += 1
                startpoint = i

                # If number of vertex with odd number of edges
        # is greater than two return "No Solution".
        if (numofodd > 2):
            warunki.insert(INSERT, 'Warunki Eulera niespełnione' + '\n')
            return

            # If there is a path find the path
        # Initialize empty stack and path
        # take the starting current as discussed
        stack = list()
        path = list()
        cur = startpoint

        # Loop will run until there is element in the stack
        # or current edge has some neighbour.
        while (stack != [] or sum(graph[cur]) != 0):

            # If current node has not any neighbour
            # add it to path and pop stack
            # set new current to the popped element
            if (sum(graph[cur]) == 0):
                path.append(cur + 1)
                cur = stack.pop(-1)

                # If the current vertex has at least one
            # neighbour add the current vertex to stack,
            # remove the edge between them and set the
            # current to its neighbour.
            else:
                for i in range(n):
                    if graph[cur][i] == 1:
                        stack.append(cur)
                        graph[cur][i] = 0
                        graph[i][cur] = 0
                        cur = i
                        break


        # print the path

        warunki.insert(INSERT, 'Cykl: ' + '\n')
        for ele in path:
              warunki.insert(INSERT, ele)
              warunki.insert(INSERT, '>')
              print()

        warunki.insert(INSERT, cur + 1)
        warunki.insert(INSERT, '\n')

    X = np.loadtxt("am.txt")
    imeg = np.array(X)
    imeg = imeg.astype(np.int)
    imeg = imeg.tolist()

    graph1 = imeg
    findpath(graph1)

def drow_Hami():
    warunki2.delete(0, 'end')
    class Graph():
        def __init__(self, vertices):
            self.graph = [[0 for column in range(vertices)]
                          for row in range(vertices)]
            self.V = vertices

        ''' Check if this vertex is an adjacent vertex  
            of the previously added vertex and is not  
            included in the path earlier '''

        def isSafe(self, v, pos, path):
            # Check if current vertex and last vertex
            # in path are adjacent
            if self.graph[path[pos - 1]][v] == 0:
                return False

            # Check if current vertex not already in path
            for vertex in path:
                if vertex == v:
                    return False

            return True

        # A recursive utility function to solve
        # hamiltonian cycle problem
        def hamCycleUtil(self, path, pos):

            # base case: if all vertices are
            # included in the path
            if pos == self.V:
                # Last vertex must be adjacent to the
                # first vertex in path to make a cyle
                if self.graph[path[pos - 1]][path[0]] == 1:
                    return True
                else:
                    return False

            # Try different vertices as a next candidate
            # in Hamiltonian Cycle. We don't try for 0 as
            # we included 0 as starting point in hamCycle()
            for v in range(1, self.V):

                if self.isSafe(v, pos, path) == True:

                    path[pos] = v

                    if self.hamCycleUtil(path, pos + 1) == True:
                        return True

                    # Remove current vertex if it doesn't
                    # lead to a solution
                    path[pos] = -1

            return False

        def hamCycle(self):
            path = [-1] * self.V

            ''' Let us put vertex 0 as the first vertex  
                in the path. If there is a Hamiltonian Cycle,  
                then the path can be started from any point  
                of the cycle as the graph is undirected '''
            path[0] = 0

            if self.hamCycleUtil(path, 1) == False:
                print ("Solution does not exist\n")
                warunki2.insert(INSERT, 'Warunki Hamiltona niespełnione' + '\n')
                return False

            self.printSolution(path)
            return True

        def printSolution(self, path):
            print ("Cykl Hamiltona:")
            warunki2.insert(INSERT, 'Cykl Hamiltona:' + '\n')
            for vertex in path:
                print (vertex + 1)
                warunki2.insert(INSERT, (vertex + 1))
            print (path[0 + 1])
            warunki2.insert(INSERT, path[0 + 1])
            warunki2.insert(INSERT, '\n')

        # Driver Code

    X = np.loadtxt("am.txt")
    imeg = np.array(X)
    imeg = imeg.astype(np.int)
    imeg = imeg.tolist()
    print (type(imeg))
    print (imeg)
    ca = int(e.get())  # pobieranie danych z Entry przypisanie inta
    ca = int(ca)
    g1 = Graph(ca)
    g1.graph = imeg

    # Print the solution
    g1.hamCycle();

    # Print the solution



#########################################################################################

# Column 0

l_w = Label(window, text="Podaj liczbe wierzcholkow")
l_w.grid(row=0, column=0)

e = Entry(window, width=20)
e.grid(row=1, column=0)

button_z1 = Button(window, text="Zatwierdz", width=10, command=click1)
button_z1.grid(row=2, column=0)

l_wie = Label(window, text="liczba wierzcholkow: ")
l_wie.grid(row=3, column=0)

l_w2 = Label(window, text="wierzcholek: ")
l_w2.grid(row=5, column=0)

combo1=Combobox(window)
combo1.grid(row=6,column=0)

l_w2 = Label(window, text="połącz z wierzcholkiem:\n ")
l_w2.grid(row=7, column=0)

combo2=Combobox(window)
combo2.grid(row=8, column=0)

button_connect = Button(window,text="połacz", width=20, command=connect)
button_connect.grid(row=9, column=0)

l_w2 = Label(window, text="\npołączenia: \n")
l_w2.grid(row=10, column=0)

stext = scrolledtext.ScrolledText(window, width=20, height=10)
stext.grid(row=11,column=0)

button_drow = Button(window, text="Rysuj", width=10, command=drow)
button_drow.grid(row=12, column=0)

# Column 1
l_column1 = Label(window, text="\nMacierz sasiedstwa")
l_column1.grid(row=10, column=1)

stext2 = scrolledtext.ScrolledText(window, width=20, height=10)
stext2.grid(row=11,column=1)

button_drow2 = Button(window, text="Rysuj macierz sasiedstwa", width=20, command=drow_m_s)
button_drow2.grid(row=12, column=1)

# Column 2
l_column1 = Label(window, text="\nMacierz incydencji")
l_column1.grid(row=10, column=2)

stext3 = scrolledtext.ScrolledText(window, width=20, height=10)
stext3.grid(row=11,column=2)

l_column1 = Label(window, text="\nIlosc krawedzi")
l_column1.grid(row=8, column=2)

e_m_i = Entry(window, width=20)
e_m_i.grid(row=9, column=2)

button_drow3 = Button(window, text="Rysuj macierz incydencji", width=20, command=drow_m_i)
button_drow3.grid(row=12, column=2)

# Column 3
l_column1 = Label(window, text="\nLista sasiedstwa")
l_column1.grid(row=10, column=3)

stext4 = scrolledtext.ScrolledText(window, width=20, height=10)
stext4.grid(row=11,column=3)

button_drow4 = Button(window, text="Rysuj liste sasiedstwa", width=20, command=drow_l_s)
button_drow4.grid(row=12, column=3)


# Column 4
l_opcje = Label(window, text="Opcje:\n")
l_opcje.grid(row=0, column=4)

button_war = Button(window, text="Warunek Eulera", state=DISABLED, width=20, command=drow_war)
button_war.grid(row=1, column=4)

button_Eul = Button(window, text="Cykl Eulera", state=DISABLED, width=20, command=drow_Eul)
button_Eul.grid(row=2, column=4)


button_Hami = Button(window, text="Cykl Hamiltona", state=DISABLED, width=20, command=drow_Hami)
button_Hami.grid(row=3, column=4)

warunki = Entry(window, width=20)
warunki.grid(row=6, column=4)
warunki2 = Entry(window, width=20)
warunki2.grid(row=7, column=4)

window.mainloop()