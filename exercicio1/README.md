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

| Comando `ifconfig` para ver informações específicas de um nó

![Imagem do mininet 12 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet12.png)

### c) Ilustração da topologia da rede 

![Imagem do mininet 13 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet13.png)

### d) Testes de ping 

Para os testes de ping, foi utilizado o xterm, para simulação de host 1 e host 2. Além disso, foi utilizado o comando tcpdump


![Imagem do mininet 14 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet14.png)


![Imagem do mininet 15 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet15.png)

### e) Testes com servidor TCP


![Imagem do mininet 16 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet16.png)

| Alterando a topologia da rede (criando uma rede nova, com as mesmas configurações, porém com 40MBps)

![Imagem do mininet 17 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet17.png)


![Imagem do mininet 18 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet18.png)

| Executando o iperf na rede de 40MBps

![Imagem do mininet 19 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet19.png)