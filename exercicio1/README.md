# Exercício 1

| Considerar uma topologia árvore com profundidade de três e ramificação de cinco.

### a) Criar uma topologia com largura de banda 30Mbps e controlador mininet

- Topologia tree com depth 3 e fanout 5
- MAC padronizado --mac
- Largura de banda 30Mbps usando `--link tc,bw=30`


```bash
sudo mn --topo tree,depth=3,fanout=5 --mac --link tc,bw=30
```

| Resultado:

![Imagem do mininet 1 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet1.png)

<br>

![Imagem do mininet 2 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet2.png)

<br>

![Imagem do mininet 3 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet3.png)

### b) Inspecionando a rede

| Comando `nodes` para mostrar os nós da rede

![Imagem do mininet 4 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet4.png)

| Comando `net` para verificar as conexões entre os nós da rede (todo o resultado do comando)


![Imagem do mininet 5 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet5.png)

<br> 

![Imagem do mininet 6 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet6.png)

<br> 

![Imagem do mininet 7 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet7.png)

<br> 

![Imagem do mininet 8 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet8.png)

<br> 

![Imagem do mininet 9 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet9.png)

<br> 

![Imagem do mininet 10 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet10.png)

<br> 

![Imagem do mininet 11 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet11.png)

