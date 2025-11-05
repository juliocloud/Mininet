# Exercício 1

| Considerar uma topologia árvore com profundidade de três e ramificação de cinco.

### a) Criar uma topologia com largura de banda 30Mbps e controlador mininet

```bash
sudo mn --topo tree,depth=3,fanout=5 --mac --link tc,bw=30
```

| Resultado:

![Imagem do mininet 1 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet1.png)

<br>

![Imagem do mininet 2 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet2.png)

<br>

![Imagem do mininet 3 (caso não carregue, as imagens estão dentro da pasta imagens)](./imagens/mininet3.png)

