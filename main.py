from ga import run_genetic_algorithm
from graph_utils import create_random_graph
from gui_app import QoSRoutingApp

#kadir deliceli


if __name__ == "__main__":
    app = QoSRoutingApp()
    app.mainloop()


"""
# UI yapsız deneme

G = create_random_graph(250, 0.03 ,
            edge_file="C:\\Users\\dkadi\\OneDrive - Bartın Üniversitesi\\Masaüstü\\Bilgisayar Ağları\\BSM307_317_Guz2025_TermProject_EdgeData.csv",
            demand_file="C:\\Users\\dkadi\\OneDrive - Bartın Üniversitesi\\Masaüstü\\Bilgisayar Ağları\\BSM307_317_Guz2025_TermProject_DemandData.csv",
            node_file="C:\\Users\\dkadi\\OneDrive - Bartın Üniversitesi\\Masaüstü\\Bilgisayar Ağları\\BSM307_317_Guz2025_TermProject_NodeData.csv"
        )
print(G)

agırlık = {
    "delay" : 0.4,
    "reliability" : 0.3,
    "resource": 0.3
}

best_path, best_cost = run_genetic_algorithm(
                G, 8, 44, 950 , agırlık
            )
print(best_path)
print(best_cost)

"""