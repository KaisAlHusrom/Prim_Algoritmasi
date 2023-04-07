# prim algoritmasi kullanark minimum agirligi bulayacak algoritma
def prim_algoritma(graph):
    # Prim's Algorithm in Python

    INF = 9999999

    # grafiğin dikeylerin sayısı
    N = len(graph)

    selected_node = [0 for i in range(N)]

    # loop sonlandirabilmek icin bir degisken tanimliyoruz
    no_edge = 0
    sum = 0

    selected_node[0] = True

    while (no_edge < N - 1):

        minimum = INF
        a = 0
        b = 0
        for m in range(N):
            if selected_node[m]:
                for n in range(N):
                    if ((not selected_node[n]) and graph[m][n]):
                        # seçilmemiş ve kenar var
                        if minimum > graph[m][n]:
                            minimum = graph[m][n]
                            a = m
                            b = n
        sum += graph[a][b]
        print(
            f"({a}, {b}) konumndaki sayi: {graph[a][b]}, {graph[a]} kumenin minimum agirligidir")
        selected_node[b] = True
        no_edge += 1
    # agirligin toplami yazdiriyoruz
    print(f"Toplam: {sum}")


def main():
    print("Prim algoritmasi icinde kullanmak istedigin matrisi yaziniz")
    boyut = int(input("Matrisin boyutu x*x, X= "))
    graph = [[0 for i in range(boyut)] for j in range(boyut)]
    for i in range(boyut):
        for j in range(boyut):
            graph[i][j] = int(input(f"({i + 1}, {j + 1}) elemani giriniz\n"))

    prim_algoritma(graph=graph)


main()
