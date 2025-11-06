import sys
import networkx as nx
import matplotlib.pyplot as plt
import re
import matplotlib.patches as mpatches # Import for creating legend patches

def read_multiline(prompt: str, end_token: str = "FIM") -> str:
    print(prompt)
    print(f"(Cole o texto e finalize com uma linha contendo apenas a palavra {end_token})")
    lines = []
    while True:
        try:
            line = input()
        except EOFError:
            break
        if line.strip() == end_token:
            break
        lines.append(line)
    return "\n".join(lines)

def parse_dump_output(dump_output):
    nodes = {}
    pattern = re.compile(r'<(\w+)\s+([\w\d.-]+):')
    for line in dump_output.strip().split('\n'):
        match = pattern.search(line.strip())
        if match:
            node_type_full, node_name = match.groups()
            node_type = 'Desconhecido'
            if 'Host' in node_type_full:
                node_type = 'Host'
            elif 'Switch' in node_type_full:
                node_type = 'Switch'
            elif 'Controller' in node_type_full:
                node_type = 'Controller'
            nodes[node_name] = node_type
    return nodes

def parse_links_output(links_output):
    links = []
    pattern = re.compile(r'([\w\d.-]+)-eth\d+\s*<->\s*([\w\d.-]+)-eth\d+')
    for line in links_output.strip().split('\n'):
        match = pattern.search(line.strip())
        if match:
            links.append((match.group(1), match.group(2)))
    return links

def visualize_topology(nodes, links):
    if not nodes and not links:
        print("Erro: Não foi possível fazer o parsing da topologia")
        return

    G = nx.Graph()

    all_node_names = set(nodes.keys())
    for a, b in links:
        all_node_names.add(a)
        all_node_names.add(b)

    node_colors = []
    # Create dictionaries to map node types to colors and legend labels
    color_map = {
        'Host': 'skyblue',
        'Switch': 'lightgreen',
        'Controller': 'salmon',
        'Desconhecido': 'grey'
    }
    
    # Ensure all nodes mentioned in links are also in the nodes dictionary with a type
    for node_name in all_node_names:
        if node_name not in nodes:
            nodes[node_name] = 'Desconhecido' # Assign a default type if not found in dump output

    for node_name in sorted(all_node_names):
        G.add_node(node_name)
        node_type = nodes.get(node_name, 'Desconhecido')
        node_colors.append(color_map.get(node_type, 'grey'))

    for a, b in links:
        if G.has_node(a) and G.has_node(b):
            G.add_edge(a, b)
        else:
            print(f"Aviso: pulando um link com pelo menos um nó desconhecido: {(a, b)}")

    print("\nGerando visualização, pode ser demorado.")
    plt.figure(figsize=(20, 20))
    pos = nx.kamada_kawai_layout(G)
    nx.draw(
        G, pos, with_labels=True, node_color=node_colors,
        node_size=1800, font_size=9, font_weight='bold', edge_color='gray'
    )
    plt.title("Visualização de topologia Mininet", size=20)

    # Create legend patches
    legend_patches = [
        mpatches.Patch(color=color_map['Host'], label='Host'),
        mpatches.Patch(color=color_map['Switch'], label='Switch'),
        mpatches.Patch(color=color_map['Controller'], label='Controller'),
        mpatches.Patch(color=color_map['Desconhecido'], label='Desconhecido')
    ]
    plt.legend(handles=legend_patches, loc='lower right', fontsize=12)

    plt.show()

if __name__ == "__main__":
    dump_output = read_multiline("Cole a saída do comando 'dump' do Mininet:", end_token="FIM")
    links_output = read_multiline("Cole a saída do comando 'links' do Mininet:", end_token="FIM")

    nodes = parse_dump_output(dump_output)
    links = parse_links_output(links_output)

    print("\n--- PARSING SUMMARY ---")
    print(f"Realizado o parse de {len(nodes)} nós do comando 'dump'.")
    print(f"Realizado o parse de {len(links)} links do comando 'links'.")
    print("-----------------------")

    visualize_topology(nodes, links)