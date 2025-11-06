import sys
import networkx as nx
import matplotlib.pyplot as plt
import re
import matplotlib.patches as mpatches

def obter_entrada_usuario(mensagem_prompt, token_parada="FIM"):
    print(mensagem_prompt)
    print(f"(Para finalizar, digite '{token_parada}' em uma linha separada e pressione Enter)")
    buffer_linhas = []
    while True:
        try:
            linha = input()
            if linha.strip().upper() == token_parada:
                break
            buffer_linhas.append(linha)
        except EOFError:
            break
    return "\n".join(buffer_linhas)

def extrair_nos_do_dump(saida_dump):
    dispositivos = {}
    regex_padrao = re.compile(r'<(\w+)\s+([\w\d.-]+):')
    for linha in saida_dump.strip().split('\n'):
        correspondencia = regex_padrao.search(linha.strip())
        if correspondencia:
            tipo_completo, nome_dispositivo = correspondencia.groups()
            categoria = 'Desconhecido'
            if 'Host' in tipo_completo:
                categoria = 'Host'
            elif 'Switch' in tipo_completo:
                categoria = 'Switch'
            elif 'Controller' in tipo_completo:
                categoria = 'Controller'
            dispositivos[nome_dispositivo] = categoria
    return dispositivos

def extrair_conexoes_dos_links(saida_links):
    conexoes = []
    regex_padrao = re.compile(r'([\w\d.-]+)-eth\d+\s*<->\s*([\w\d.-]+)-eth\d+')
    for linha in saida_links.strip().split('\n'):
        correspondencia = regex_padrao.search(linha.strip())
        if correspondencia:
            ponta_a, ponta_b = correspondencia.groups()
            conexoes.append((ponta_a, ponta_b))
    return conexoes

def desenhar_grafico_topologia(dispositivos, conexoes):
    if not dispositivos and not conexoes:
        print("Aviso: Não foi possível analisar a topologia. Nenhum dado para exibir.")
        return

    grafo = nx.Graph()

    nomes_dispositivos_encontrados = set(dispositivos.keys())
    for dev_a, dev_b in conexoes:
        nomes_dispositivos_encontrados.add(dev_a)
        nomes_dispositivos_encontrados.add(dev_b)

    for nome in nomes_dispositivos_encontrados:
        if nome not in dispositivos:
            dispositivos[nome] = 'Desconhecido'

    cores_mapa = {
        'Host': 'skyblue',
        'Switch': 'lightgreen',
        'Controller': 'salmon',
        'Desconhecido': 'grey'
    }
    
    lista_cores_nos = [cores_mapa.get(dispositivos[nome], 'grey') for nome in sorted(list(nomes_dispositivos_encontrados))]

    for nome_dispositivo in sorted(list(nomes_dispositivos_encontrados)):
        grafo.add_node(nome_dispositivo)

    for dev_a, dev_b in conexoes:
        if grafo.has_node(dev_a) and grafo.has_node(dev_b):
            grafo.add_edge(dev_a, dev_b)
        else:
            print(f"Alerta: Ignorando conexão com nós ausentes: {dev_a} <-> {dev_b}")

    print("\nIniciando a geração do gráfico da topologia...")
    
    figura, eixo = plt.subplots(figsize=(20, 20))
    posicoes = nx.kamada_kawai_layout(grafo)
    
    nx.draw(
        grafo, posicoes, ax=eixo, with_labels=True, 
        node_color=lista_cores_nos, node_size=1800, 
        font_size=9, font_weight='bold', edge_color='gray'
    )
    
    eixo.set_title("Visualização da Topologia da Rede Mininet", size=20)

    elementos_legenda = [
        mpatches.Patch(color='skyblue', label='Host'),
        mpatches.Patch(color='lightgreen', label='Switch'),
        mpatches.Patch(color='salmon', label='Controller'),
        mpatches.Patch(color='grey', label='Desconhecido')
    ]
    eixo.legend(handles=elementos_legenda, loc='lower right', fontsize=12)

    plt.show()

def main():
    entrada_dump = obter_entrada_usuario("Cole aqui a saída do comando 'dump' do Mininet:")
    entrada_links = obter_entrada_usuario("Agora, cole a saída do comando 'links' do Mininet:")

    dispositivos_mapeados = extrair_nos_do_dump(entrada_dump)
    conexoes_mapeadas = extrair_conexoes_dos_links(entrada_links)

    print("\n--- RESUMO DA ANÁLISE ---")
    print(f"Número de nós identificados: {len(dispositivos_mapeados)}")
    print(f"Número de conexões identificadas: {len(conexoes_mapeadas)}")
    print("-------------------------\n")

    desenhar_grafico_topologia(dispositivos_mapeados, conexoes_mapeadas)

if __name__ == "__main__":
    main()