# Jokenpo Game (Pedra, Papel e Tesoura)

Este é um projeto de um jogo de Jokenpo (Pedra, Papel e Tesoura) em Python, com interface gráfica e diferentes níveis de dificuldade para o jogador. O jogo foi desenvolvido usando a biblioteca `tkinter` para a criação de uma interface amigável e intuitiva, oferecendo uma experiência interativa para o usuário.

## Funcionalidades

- **Escolha de nível de dificuldade:** O jogador pode selecionar entre três níveis de dificuldade - Fácil, Médio e Difícil. Em cada nível, a lógica do jogo se ajusta para oferecer uma experiência diferente:
  - **Fácil:** A máquina faz jogadas aleatórias, tornando o jogo equilibrado.
  - **Médio:** A máquina usa uma probabilidade ligeiramente maior de ganhar, observando as jogadas mais comuns do jogador.
  - **Difícil:** A máquina tenta prever e se adaptar ao padrão de jogadas do jogador, tornando-se um oponente mais desafiador.
  
- **Interface Gráfica (GUI):** O jogo possui uma interface gráfica amigável feita com `tkinter`, permitindo que o usuário faça escolhas clicando em botões e visualize o resultado de cada rodada.

- **Sistema de Pontuação:** O jogo mantém uma contagem dos pontos do jogador e da máquina, com a opção de reiniciar o placar a qualquer momento.

## Pré-requisitos

- **Python 3.x** instalado em seu sistema.
- Bibliotecas Python: `tkinter` (geralmente já incluída no Python).

## Instalação

1. Clone este repositório para o seu ambiente local:
   ```bash
   git clone https://github.com/DevFilipeF/jokenpo-game.git
   cd jokenpo-game
