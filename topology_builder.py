import networkx as nx
import matplotlib.pyplot as plt
import re

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
    for link in links:
        all_node_names.add(link[0])
        all_node_names.add(link[1])

    node_colors = []
    for node_name in all_node_names:
        G.add_node(node_name)
        node_type = nodes.get(node_name, 'Desconhecido') 
        
        if node_type == 'Host':
            node_colors.append('skyblue')
        elif node_type == 'Switch':
            node_colors.append('lightgreen')
        elif node_type == 'Controller':
            node_colors.append('salmon')
        else:
            node_colors.append('grey') 

    for link in links:
        if G.has_node(link[0]) and G.has_node(link[1]):
            G.add_edge(link[0], link[1])
        else:
            print(f"Aviso: pulando um link com pelo menos um nó desconhecido: {link}")

    print("\nGerando visualização, pode ser demorado.")
    plt.figure(figsize=(20, 20))
    
    pos = nx.kamada_kawai_layout(G)
    
    nx.draw(G, pos, with_labels=True, node_color=node_colors, 
            node_size=1800, font_size=9, font_weight='bold', edge_color='gray')
            
    plt.title("Visualização de topologia mininet", size=20)
    plt.show()

if __name__ == "__main__":
    dump_output = """
    <Host h1: h1-eth0:10.0.0.1 pid=3251>
    <Host h2: h2-eth0:10.0.0.2 pid=3253>
    <Host h3: h3-eth0:10.0.0.3 pid=3255>
    <Host h4: h4-eth0:10.0.0.4 pid=3257>
    <Host h5: h5-eth0:10.0.0.5 pid=3259>
    <Host h6: h6-eth0:10.0.0.6 pid=3261>
    <Host h7: h7-eth0:10.0.0.7 pid=3263>
    <Host h8: h8-eth0:10.0.0.8 pid=3265>
    <Host h9: h9-eth0:10.0.0.9 pid=3267>
    <Host h10: h10-eth0:10.0.0.10 pid=3269>
    <Host h11: h11-eth0:10.0.0.11 pid=3271>
    <Host h12: h12-eth0:10.0.0.12 pid=3273>
    <Host h13: h13-eth0:10.0.0.13 pid=3275>
    <Host h14: h14-eth0:10.0.0.14 pid=3277>
    <Host h15: h15-eth0:10.0.0.15 pid=3279>
    <Host h16: h16-eth0:10.0.0.16 pid=3281>
    <Host h17: h17-eth0:10.0.0.17 pid=3283>
    <Host h18: h18-eth0:10.0.0.18 pid=3285>
    <Host h19: h19-eth0:10.0.0.19 pid=3287>
    <Host h20: h20-eth0:10.0.0.20 pid=3289>
    <Host h21: h21-eth0:10.0.0.21 pid=3291>
    <Host h22: h22-eth0:10.0.0.22 pid=3293>
    <Host h23: h23-eth0:10.0.0.23 pid=3295>
    <Host h24: h24-eth0:10.0.0.24 pid=3297>
    <Host h25: h25-eth0:10.0.0.25 pid=3299>
    <Host h26: h26-eth0:10.0.0.26 pid=3303>
    <Host h27: h27-eth0:10.0.0.27 pid=3305>
    <Host h28: h28-eth0:10.0.0.28 pid=3307>
    <Host h29: h29-eth0:10.0.0.29 pid=3309>
    <Host h30: h30-eth0:10.0.0.30 pid=3311>
    <Host h31: h31-eth0:10.0.0.31 pid=3313>
    <Host h32: h32-eth0:10.0.0.32 pid=3315>
    <Host h33: h33-eth0:10.0.0.33 pid=3317>
    <Host h34: h34-eth0:10.0.0.34 pid=3319>
    <Host h35: h35-eth0:10.0.0.35 pid=3321>
    <Host h36: h36-eth0:10.0.0.36 pid=3323>
    <Host h37: h37-eth0:10.0.0.37 pid=3325>
    <Host h38: h38-eth0:10.0.0.38 pid=3327>
    <Host h39: h39-eth0:10.0.0.39 pid=3329>
    <Host h40: h40-eth0:10.0.0.40 pid=3331>
    <Host h41: h41-eth0:10.0.0.41 pid=3333>
    <Host h42: h42-eth0:10.0.0.42 pid=3335>
    <Host h43: h43-eth0:10.0.0.43 pid=3337>
    <Host h44: h44-eth0:10.0.0.44 pid=3339>
    <Host h45: h45-eth0:10.0.0.45 pid=3341>
    <Host h46: h46-eth0:10.0.0.46 pid=3343>
    <Host h47: h47-eth0:10.0.0.47 pid=3345>
    <Host h48: h48-eth0:10.0.0.48 pid=3347>
    <Host h49: h49-eth0:10.0.0.49 pid=3349>
    <Host h50: h50-eth0:10.0.0.50 pid=3351>
    <Host h51: h51-eth0:10.0.0.51 pid=3353>
    <Host h52: h52-eth0:10.0.0.52 pid=3355>
    <Host h53: h53-eth0:10.0.0.53 pid=3357>
    <Host h54: h54-eth0:10.0.0.54 pid=3359>
    <Host h55: h55-eth0:10.0.0.55 pid=3361>
    <Host h56: h56-eth0:10.0.0.56 pid=3363>
    <Host h57: h57-eth0:10.0.0.57 pid=3365>
    <Host h58: h58-eth0:10.0.0.58 pid=3367>
    <Host h59: h59-eth0:10.0.0.59 pid=3369>
    <Host h60: h60-eth0:10.0.0.60 pid=3371>
    <Host h61: h61-eth0:10.0.0.61 pid=3373>
    <Host h62: h62-eth0:10.0.0.62 pid=3375>
    <Host h63: h63-eth0:10.0.0.63 pid=3377>
    <Host h64: h64-eth0:10.0.0.64 pid=3379>
    <Host h65: h65-eth0:10.0.0.65 pid=3381>
    <Host h66: h66-eth0:10.0.0.66 pid=3383>
    <Host h67: h67-eth0:10.0.0.67 pid=3385>
    <Host h68: h68-eth0:10.0.0.68 pid=3387>
    <Host h69: h69-eth0:10.0.0.69 pid=3389>
    <Host h70: h70-eth0:10.0.0.70 pid=3391>
    <Host h71: h71-eth0:10.0.0.71 pid=3393>
    <Host h72: h72-eth0:10.0.0.72 pid=3395>
    <Host h73: h73-eth0:10.0.0.73 pid=3397>
    <Host h74: h74-eth0:10.0.0.74 pid=3399>
    <Host h75: h75-eth0:10.0.0.75 pid=3401>
    <Host h76: h76-eth0:10.0.0.76 pid=3403>
    <Host h77: h77-eth0:10.0.0.77 pid=3405>
    <Host h78: h78-eth0:10.0.0.78 pid=3407>
    <Host h79: h79-eth0:10.0.0.79 pid=3409>
    <Host h80: h80-eth0:10.0.0.80 pid=3411>
    <Host h81: h81-eth0:10.0.0.81 pid=3413>
    <Host h82: h82-eth0:10.0.0.82 pid=3415>
    <Host h83: h83-eth0:10.0.0.83 pid=3417>
    <Host h84: h84-eth0:10.0.0.84 pid=3419>
    <Host h85: h85-eth0:10.0.0.85 pid=3421>
    <Host h86: h86-eth0:10.0.0.86 pid=3423>
    <Host h87: h87-eth0:10.0.0.87 pid=3425>
    <Host h88: h88-eth0:10.0.0.88 pid=3427>
    <Host h89: h89-eth0:10.0.0.89 pid=3429>
    <Host h90: h90-eth0:10.0.0.90 pid=3431>
    <Host h91: h91-eth0:10.0.0.91 pid=3433>
    <Host h92: h92-eth0:10.0.0.92 pid=3435>
    <Host h93: h93-eth0:10.0.0.93 pid=3437>
    <Host h94: h94-eth0:10.0.0.94 pid=3439>
    <Host h95: h95-eth0:10.0.0.95 pid=3441>
    <Host h96: h96-eth0:10.0.0.96 pid=3443>
    <Host h97: h97-eth0:10.0.0.97 pid=3445>
    <Host h98: h98-eth0:10.0.0.98 pid=3447>
    <Host h99: h99-eth0:10.0.0.99 pid=3449>
    <Host h100: h100-eth0:10.0.0.100 pid=3451>
    <Host h101: h101-eth0:10.0.0.101 pid=3453>
    <Host h102: h102-eth0:10.0.0.102 pid=3455>
    <Host h103: h103-eth0:10.0.0.103 pid=3457>
    <Host h104: h104-eth0:10.0.0.104 pid=3459>
    <Host h105: h105-eth0:10.0.0.105 pid=3461>
    <Host h106: h106-eth0:10.0.0.106 pid=3463>
    <Host h107: h107-eth0:10.0.0.107 pid=3465>
    <Host h108: h108-eth0:10.0.0.108 pid=3467>
    <Host h109: h109-eth0:10.0.0.109 pid=3469>
    <Host h110: h110-eth0:10.0.0.110 pid=3471>
    <Host h111: h111-eth0:10.0.0.111 pid=3473>
    <Host h112: h112-eth0:10.0.0.112 pid=3475>
    <Host h113: h113-eth0:10.0.0.113 pid=3477>
    <Host h114: h114-eth0:10.0.0.114 pid=3479>
    <Host h115: h115-eth0:10.0.0.115 pid=3481>
    <Host h116: h116-eth0:10.0.0.116 pid=3483>
    <Host h117: h117-eth0:10.0.0.117 pid=3485>
    <Host h118: h118-eth0:10.0.0.118 pid=3487>
    <Host h119: h119-eth0:10.0.0.119 pid=3489>
    <Host h120: h120-eth0:10.0.0.120 pid=3491>
    <Host h121: h121-eth0:10.0.0.121 pid=3493>
    <Host h122: h122-eth0:10.0.0.122 pid=3495>
    <Host h123: h123-eth0:10.0.0.123 pid=3497>
    <Host h124: h124-eth0:10.0.0.124 pid=3499>
    <Host h125: h125-eth0:10.0.0.125 pid=3501>
    <OVSSwitch s1: lo:127.0.0.1,s1-eth1:None,s1-eth2:None,s1-eth3:None,s1-eth4:None,s1-eth5:None pid=3506>
    <OVSSwitch s2: lo:127.0.0.1,s2-eth1:None,s2-eth2:None,s2-eth3:None,s2-eth4:None,s2-eth5:None,s2-eth6:None pid=3509>
    <OVSSwitch s3: lo:127.0.0.1,s3-eth1:None,s3-eth2:None,s3-eth3:None,s3-eth4:None,s3-eth5:None,s3-eth6:None pid=3512>
    <OVSSwitch s4: lo:127.0.0.1,s4-eth1:None,s4-eth2:None,s4-eth3:None,s4-eth4:None,s4-eth5:None,s4-eth6:None pid=3515>
    <OVSSwitch s5: lo:127.0.0.1,s5-eth1:None,s5-eth2:None,s5-eth3:None,s5-eth4:None,s5-eth5:None,s5-eth6:None pid=3518>
    <OVSSwitch s6: lo:127.0.0.1,s6-eth1:None,s6-eth2:None,s6-eth3:None,s6-eth4:None,s6-eth5:None,s6-eth6:None pid=3521>
    <OVSSwitch s7: lo:127.0.0.1,s7-eth1:None,s7-eth2:None,s7-eth3:None,s7-eth4:None,s7-eth5:None,s7-eth6:None pid=3524>
    <OVSSwitch s8: lo:127.0.0.1,s8-eth1:None,s8-eth2:None,s8-eth3:None,s8-eth4:None,s8-eth5:None,s8-eth6:None pid=3527>
    <OVSSwitch s9: lo:127.0.0.1,s9-eth1:None,s9-eth2:None,s9-eth3:None,s9-eth4:None,s9-eth5:None,s9-eth6:None pid=3530>
    <OVSSwitch s10: lo:127.0.0.1,s10-eth1:None,s10-eth2:None,s10-eth3:None,s10-eth4:None,s10-eth5:None,s10-eth6:None pid=3533>
    <OVSSwitch s11: lo:127.0.0.1,s11-eth1:None,s11-eth2:None,s11-eth3:None,s11-eth4:None,s11-eth5:None,s11-eth6:None pid=3536>
    <OVSSwitch s12: lo:127.0.0.1,s12-eth1:None,s12-eth2:None,s12-eth3:None,s12-eth4:None,s12-eth5:None,s12-eth6:None pid=3539>
    <OVSSwitch s13: lo:127.0.0.1,s13-eth1:None,s13-eth2:None,s13-eth3:None,s13-eth4:None,s13-eth5:None,s13-eth6:None pid=3542>
    <OVSSwitch s14: lo:127.0.0.1,s14-eth1:None,s14-eth2:None,s14-eth3:None,s14-eth4:None,s14-eth5:None,s14-eth6:None pid=3545>
    <OVSSwitch s15: lo:127.0.0.1,s15-eth1:None,s15-eth2:None,s15-eth3:None,s15-eth4:None,s15-eth5:None,s15-eth6:None pid=3548>
    <OVSSwitch s16: lo:127.0.0.1,s16-eth1:None,s16-eth2:None,s16-eth3:None,s16-eth4:None,s16-eth5:None,s16-eth6:None pid=3551>
    <OVSSwitch s17: lo:127.0.0.1,s17-eth1:None,s17-eth2:None,s17-eth3:None,s17-eth4:None,s17-eth5:None,s17-eth6:None pid=3554>
    <OVSSwitch s18: lo:127.0.0.1,s18-eth1:None,s18-eth2:None,s18-eth3:None,s18-eth4:None,s18-eth5:None,s18-eth6:None pid=3557>
    <OVSSwitch s19: lo:127.0.0.1,s19-eth1:None,s19-eth2:None,s19-eth3:None,s19-eth4:None,s19-eth5:None,s19-eth6:None pid=3560>
    <OVSSwitch s20: lo:127.0.0.1,s20-eth1:None,s20-eth2:None,s20-eth3:None,s20-eth4:None,s20-eth5:None,s20-eth6:None pid=3563>
    <OVSSwitch s21: lo:127.0.0.1,s21-eth1:None,s21-eth2:None,s21-eth3:None,s21-eth4:None,s21-eth5:None,s21-eth6:None pid=3566>
    <OVSSwitch s22: lo:127.0.0.1,s22-eth1:None,s22-eth2:None,s22-eth3:None,s22-eth4:None,s22-eth5:None,s22-eth6:None pid=3569>
    <OVSSwitch s23: lo:127.0.0.1,s23-eth1:None,s23-eth2:None,s23-eth3:None,s23-eth4:None,s23-eth5:None,s23-eth6:None pid=3572>
    <OVSSwitch s24: lo:127.0.0.1,s24-eth1:None,s24-eth2:None,s24-eth3:None,s24-eth4:None,s24-eth5:None,s24-eth6:None pid=3575>
    <OVSSwitch s25: lo:127.0.0.1,s25-eth1:None,s25-eth2:None,s25-eth3:None,s25-eth4:None,s25-eth5:None,s25-eth6:None pid=3578>
    <OVSSwitch s26: lo:127.0.0.1,s26-eth1:None,s26-eth2:None,s26-eth3:None,s26-eth4:None,s26-eth5:None,s26-eth6:None pid=3581>
    <OVSSwitch s27: lo:127.0.0.1,s27-eth1:None,s27-eth2:None,s27-eth3:None,s27-eth4:None,s27-eth5:None,s27-eth6:None pid=3584>
    <OVSSwitch s28: lo:127.0.0.1,s28-eth1:None,s28-eth2:None,s28-eth3:None,s28-eth4:None,s28-eth5:None,s28-eth6:None pid=3587>
    <OVSSwitch s29: lo:127.0.0.1,s29-eth1:None,s29-eth2:None,s29-eth3:None,s29-eth4:None,s29-eth5:None,s29-eth6:None pid=3590>
    <OVSSwitch s30: lo:127.0.0.1,s30-eth1:None,s30-eth2:None,s30-eth3:None,s30-eth4:None,s30-eth5:None,s30-eth6:None pid=3593>
    <OVSSwitch s31: lo:127.0.0.1,s31-eth1:None,s31-eth2:None,s31-eth3:None,s31-eth4:None,s31-eth5:None,s31-eth6:None pid=3596>
    <Controller c0: 127.0.0.1:6653 pid=3244>
    """

    # --- Paste your 'links' command output here ---
    links_output = """
    s1-eth1<->s2-eth6 (OK OK)
    s1-eth2<->s8-eth6 (OK OK)
    s1-eth3<->s14-eth6 (OK OK)
    s1-eth4<->s20-eth6 (OK OK)
    s1-eth5<->s26-eth6 (OK OK)
    s2-eth1<->s3-eth6 (OK OK)
    s2-eth2<->s4-eth6 (OK OK)
    s2-eth3<->s5-eth6 (OK OK)
    s2-eth4<->s6-eth6 (OK OK)
    s2-eth5<->s7-eth6 (OK OK)
    s3-eth1<->h1-eth0 (OK OK)
    s3-eth2<->h2-eth0 (OK OK)
    s3-eth3<->h3-eth0 (OK OK)
    s3-eth4<->h4-eth0 (OK OK)
    s3-eth5<->h5-eth0 (OK OK)
    s4-eth1<->h6-eth0 (OK OK)
    s4-eth2<->h7-eth0 (OK OK)
    s4-eth3<->h8-eth0 (OK OK)
    s4-eth4<->h9-eth0 (OK OK)
    s4-eth5<->h10-eth0 (OK OK)
    s5-eth1<->h11-eth0 (OK OK)
    s5-eth2<->h12-eth0 (OK OK)
    s5-eth3<->h13-eth0 (OK OK)
    s5-eth4<->h14-eth0 (OK OK)
    s5-eth5<->h15-eth0 (OK OK)
    s6-eth1<->h16-eth0 (OK OK)
    s6-eth2<->h17-eth0 (OK OK)
    s6-eth3<->h18-eth0 (OK OK)
    s6-eth4<->h19-eth0 (OK OK)
    s6-eth5<->h20-eth0 (OK OK)
    s7-eth1<->h21-eth0 (OK OK)
    s7-eth2<->h22-eth0 (OK OK)
    s7-eth3<->h23-eth0 (OK OK)
    s7-eth4<->h24-eth0 (OK OK)
    s7-eth5<->h25-eth0 (OK OK)
    s8-eth1<->s9-eth6 (OK OK)
    s8-eth2<->s10-eth6 (OK OK)
    s8-eth3<->s11-eth6 (OK OK)
    s8-eth4<->s12-eth6 (OK OK)
    s8-eth5<->s13-eth6 (OK OK)
    s9-eth1<->h26-eth0 (OK OK)
    s9-eth2<->h27-eth0 (OK OK)
    s9-eth3<->h28-eth0 (OK OK)
    s9-eth4<->h29-eth0 (OK OK)
    s9-eth5<->h30-eth0 (OK OK)
    s10-eth1<->h31-eth0 (OK OK)
    s10-eth2<->h32-eth0 (OK OK)
    s10-eth3<->h33-eth0 (OK OK)
    s10-eth4<->h34-eth0 (OK OK)
    s10-eth5<->h35-eth0 (OK OK)
    s11-eth1<->h36-eth0 (OK OK)
    s11-eth2<->h37-eth0 (OK OK)
    s11-eth3<->h38-eth0 (OK OK)
    s11-eth4<->h39-eth0 (OK OK)
    s11-eth5<->h40-eth0 (OK OK)
    s12-eth1<->h41-eth0 (OK OK)
    s12-eth2<->h42-eth0 (OK OK)
    s12-eth3<->h43-eth0 (OK OK)
    s12-eth4<->h44-eth0 (OK OK)
    s12-eth5<->h45-eth0 (OK OK)
    s13-eth1<->h46-eth0 (OK OK)
    s13-eth2<->h47-eth0 (OK OK)
    s13-eth3<->h48-eth0 (OK OK)
    s13-eth4<->h49-eth0 (OK OK)
    s13-eth5<->h50-eth0 (OK OK)
    s14-eth1<->s15-eth6 (OK OK)
    s14-eth2<->s16-eth6 (OK OK)
    s14-eth3<->s17-eth6 (OK OK)
    s14-eth4<->s18-eth6 (OK OK)
    s14-eth5<->s19-eth6 (OK OK)
    s15-eth1<->h51-eth0 (OK OK)
    s15-eth2<->h52-eth0 (OK OK)
    s15-eth3<->h53-eth0 (OK OK)
    s15-eth4<->h54-eth0 (OK OK)
    s15-eth5<->h55-eth0 (OK OK)
    s16-eth1<->h56-eth0 (OK OK)
    s16-eth2<->h57-eth0 (OK OK)
    s16-eth3<->h58-eth0 (OK OK)
    s16-eth4<->h59-eth0 (OK OK)
    s16-eth5<->h60-eth0 (OK OK)
    s17-eth1<->h61-eth0 (OK OK)
    s17-eth2<->h62-eth0 (OK OK)
    s17-eth3<->h63-eth0 (OK OK)
    s17-eth4<->h64-eth0 (OK OK)
    s17-eth5<->h65-eth0 (OK OK)
    s18-eth1<->h66-eth0 (OK OK)
    s18-eth2<->h67-eth0 (OK OK)
    s18-eth3<->h68-eth0 (OK OK)
    s18-eth4<->h69-eth0 (OK OK)
    s18-eth5<->h70-eth0 (OK OK)
    s19-eth1<->h71-eth0 (OK OK)
    s19-eth2<->h72-eth0 (OK OK)
    s19-eth3<->h73-eth0 (OK OK)
    s19-eth4<->h74-eth0 (OK OK)
    s19-eth5<->h75-eth0 (OK OK)
    s20-eth1<->s21-eth6 (OK OK)
    s20-eth2<->s22-eth6 (OK OK)
    s20-eth3<->s23-eth6 (OK OK)
    s20-eth4<->s24-eth6 (OK OK)
    s20-eth5<->s25-eth6 (OK OK)
    s21-eth1<->h76-eth0 (OK OK)
    s21-eth2<->h77-eth0 (OK OK)
    s21-eth3<->h78-eth0 (OK OK)
    s21-eth4<->h79-eth0 (OK OK)
    s21-eth5<->h80-eth0 (OK OK)
    s22-eth1<->h81-eth0 (OK OK)
    s22-eth2<->h82-eth0 (OK OK)
    s22-eth3<->h83-eth0 (OK OK)
    s22-eth4<->h84-eth0 (OK OK)
    s22-eth5<->h85-eth0 (OK OK)
    s23-eth1<->h86-eth0 (OK OK)
    s23-eth2<->h87-eth0 (OK OK)
    s23-eth3<->h88-eth0 (OK OK)
    s23-eth4<->h89-eth0 (OK OK)
    s23-eth5<->h90-eth0 (OK OK)
    s24-eth1<->h91-eth0 (OK OK)
    s24-eth2<->h92-eth0 (OK OK)
    s24-eth3<->h93-eth0 (OK OK)
    s24-eth4<->h94-eth0 (OK OK)
    s24-eth5<->h95-eth0 (OK OK)
    s25-eth1<->h96-eth0 (OK OK)
    s25-eth2<->h97-eth0 (OK OK)
    s25-eth3<->h98-eth0 (OK OK)
    s25-eth4<->h99-eth0 (OK OK)
    s25-eth5<->h100-eth0 (OK OK)
    s26-eth1<->s27-eth6 (OK OK)
    s26-eth2<->s28-eth6 (OK OK)
    s26-eth3<->s29-eth6 (OK OK)
    s26-eth4<->s30-eth6 (OK OK)
    s26-eth5<->s31-eth6 (OK OK)
    s27-eth1<->h101-eth0 (OK OK)
    s27-eth2<->h102-eth0 (OK OK)
    s27-eth3<->h103-eth0 (OK OK)
    s27-eth4<->h104-eth0 (OK OK)
    s27-eth5<->h105-eth0 (OK OK)
    s28-eth1<->h106-eth0 (OK OK)
    s28-eth2<->h107-eth0 (OK OK)
    s28-eth3<->h108-eth0 (OK OK)
    s28-eth4<->h109-eth0 (OK OK)
    s28-eth5<->h110-eth0 (OK OK)
    s29-eth1<->h111-eth0 (OK OK)
    s29-eth2<->h112-eth0 (OK OK)
    s29-eth3<->h113-eth0 (OK OK)
    s29-eth4<->h114-eth0 (OK OK)
    s29-eth5<->h115-eth0 (OK OK)
    s30-eth1<->h116-eth0 (OK OK)
    s30-eth2<->h117-eth0 (OK OK)
    s30-eth3<->h118-eth0 (OK OK)
    s30-eth4<->h119-eth0 (OK OK)
    s30-eth5<->h120-eth0 (OK OK)
    s31-eth1<->h121-eth0 (OK OK)
    s31-eth2<->h122-eth0 (OK OK)
    s31-eth3<->h123-eth0 (OK OK)
    s31-eth4<->h124-eth0 (OK OK)
    s31-eth5<->h125-eth0 (OK OK)
    """

    nodes = parse_dump_output(dump_output)
    links = parse_links_output(links_output)
    print("--- PARSING SUMMARY ---")
    print(f"Realizado o parse de {len(nodes)} nós do comando 'dump'.")
    print(f"Realizado o parse de {len(links)} links do comando 'links'.")
    print("-----------------------")
    
    visualize_topology(nodes, links)
