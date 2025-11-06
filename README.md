# Trabalho final Mininet - Júlio César Juriolli Filho

Repositório com o trabalho final da disciplina C115.

## Organização do Projeto

O trabalho está dividido nas pastas `exercicio1` e `exercicio2`. Cada pasta tem um README próprio com os detalhes e screenshots de cada etapa.

### Exercício 1 - Topologia em Árvore

-   **Onde está:** pasta `/exercicio1`
-   **O que faz:** Cria a topologia em árvore (`depth=3, fanout=5`) direto pela linha de comando do Mininet, já com a configuração de banda. O README da pasta mostra os testes de `ping` e `iperf`.

### Exercício 2 - Topologia Customizada

-   **Onde está:** pasta `/exercicio2`
-   **O que faz:** Contém a topologia customizada. O arquivo `topo.py` define a rede, e o README da pasta mostra os testes de conectividade e a criação das regras para os switches.

### Ferramenta de Visualização (`topology_builder.py`)

Eu criei o script `topology_builder.py` (que está na raiz do projeto) para ajudar a visualizar as topologias. Ele desenha um diagrama da rede usando a saída dos comandos `dump` e `links` do Mininet. Foi útil principalmente no exercício 1, já que a rede era muito grande para analisar na mão.