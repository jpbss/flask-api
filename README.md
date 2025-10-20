# API Flask com Jenkins (Demo de CI/CD para Qualidade de Software)

Este projeto foi o que apresentei na matéria de Qualidade de Software. A ideia principal não era fazer uma API super complexa, mas sim mostrar um pipeline de CI/CD (Integração Contínua) a funcionar na prática usando Jenkins.

Basicamente, o objetivo era garantir que qualquer mudança no código fosse testada automaticamente.

## O que tem no projeto?

O repositório tem três partes principais:

1.  **A API (`app.py`):** Uma API em Flask, bem básica, só para ter "algo" para testar. Ela tem umas rotas simples que devolvem JSON:
    * `GET /`: A página inicial.
    * `GET /sobre`: Uma descrição simples.
    * `GET /mult/<int:x>/<int:y>`: Uma rota que multiplica dois números.

2.  **Os Testes (`tests/test_app.py`):** A parte crucial para a matéria de Qualidade! Usei `pytest` para criar testes que verificam se a API está a funcionar como devia. Os testes cobrem:
    * Se as rotas principais (`/` e `/sobre`) respondem corretamente.
    * Se a multiplicação está correta (ex: `3/4` dá `12`).
    * Casos chatos (edge cases), como multiplicar por zero.
    * Se rotas que *deveriam* falhar (como `/mult/texto/texto`) realmente falham com um 404.

3.  **O Pipeline (`Jenkinsfile`):** É o script que diz ao Jenkins o que fazer automaticamente sempre que alguém envia um código novo:

    * **Ambiente Limpo:** Rodei tudo num container Docker com `python:3.10`. Assim, não tem desculpa de "na minha máquina funciona".
    * **Passo 1 (Instalar Coisas):** Ele primeiro cria um ambiente virtual (`venv`) e instala tudo o que o projeto precisa (o `Flask`, o `pytest`, etc., do `requirements.txt`).
    * **Passo 2 (Testar):** Depois, ele roda os testes todos com o `pytest`.
    * **Feedback:** No final, o Jenkins avisava no log se deu tudo certo (✅) ou se algo quebrou (❌).
