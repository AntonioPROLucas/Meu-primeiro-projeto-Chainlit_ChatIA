import chainlit as cl


@cl.on_message
async def main(message: cl.Message):
    # Your custom logic goes here...
    message.content = message.content.replace(" ", "")
    resposta = ""
    if "python" in message.content.lower():
        resposta += "Python é uma das linguagens mais usadas do mercado! Além de ser uma linguagemde altíssimo nível, ela possúi uma indentação bem amígavel! É uma linguagem muito usada para auyomátização e análise de dados(com o auxilio da biblioteca pandas), mas pode ser usada para construção de web pages, games e todo tipo de aplicação. sendo uma linguagem de multiparadigma(Esse programa foi feito em python).Código feito em python: https://github.com/AntonioPROLucas/Automatizacao-de-envio-de-relatorio-Excel-por-email-em-python  " 
    if "java" in message.content.lower() and "script" in message.content.lower():
        resposta += "Javascript é uma linguagem front-end mas pode ser usada para back-end ao usar react.js!! É a linguagem mais usada do mundo, geralmente acompanhada de html e css para criação de paginas web. Exemplos de código: https://github.com/AntonioPROLucas/App-Previsao_do_tempo https://github.com/AntonioPROLucas/mario-celular-  "
    if "java" in message.content.lower():
        resposta += "Java é uma linguagem backend usada para criação de paginas complexas onde se faz necessário uso de programação orientada a objetos! É usada para guardar dados e atributos no back-end sendo uma linguagem muito importante e versátil.  "
    if "c#" in message.content.lower() or "csharp" in message.content.lower():
        resposta +="C# é uma linguagem de programação orientada a objetos muito usada para o back-end de jogos, como os jogos da unity por exemplo ! Exemplo de códigos desta linguagem: https://github.com/AntonioPROLucas/Meu-primeiro-projeto-de-game-Unity-CursoCSJ  "
    if "sql" in message.content.lower():
        resposta += "SQL é o principal SGBD muito importante para o back-end e o database de uma aplicação "
    if "c++" in message.content.lower():
        resposta += "O C++ é uma linguagem de programação de alto nível, de propósito geral e compilada, conhecida por sua eficiência, flexibilidade e poder, amplamente utilizada no desenvolvimento de software em uma variedade de áreas, incluindo sistemas operacionais, jogos, aplicativos de desktop e sistemas embarcados. "
    if "php" in message.content.lower():
        resposta += "O PHP é uma linguagem de script de servidor amplamente utilizada para o desenvolvimento web dinâmico, conhecida por sua facilidade de aprendizado e implementação, integração perfeita com HTML e suporte a uma ampla variedade de bancos de dados, tornando-o ideal para a criação de sites interativos e aplicativos web."
    if "typescript" in message.content.lower():
        resposta += "TypeScript é uma linguagem de programação desenvolvida pela Microsoft, é um superset do JavaScript que adiciona tipagem estática opcional e outros recursos avançados para desenvolvimento de aplicativos web escaláveis. "
    if "rust" in message.content.lower():
        resposta += "Rust é uma linguagem de programação de sistemas de alto desempenho, focada em segurança, concorrência e facilidade de uso, adequada para desenvolvimento de software de baixo nível, como sistemas operacionais e bibliotecas de alto desempenho."
    if "swift" in message.content.lower():
        resposta += "Swift é uma linguagem de programação desenvolvida pela Apple, usada para criar aplicativos iOS e macOS, conhecida por sua segurança, performance e facilidade de uso. "
    if "ruby" in message.content.lower():
        resposta += "Ruby é uma linguagem de programação interpretada, conhecida por sua sintaxe simples e elegante, amplamente utilizada para desenvolvimento web, especialmente com o framework Ruby on Rails. "
    if "scala" in message.content.lower():
        resposta +="Scala é uma linguagem de programação multiparadigma que combina orientação a objetos e programação funcional, usada principalmente para desenvolvimento de aplicativos web e processamento de dados."
    if "go" in message.content.lower() or "golang" in message.content.lower():
        resposta += "Go ou Golang é uma linguagem de programação de código aberto desenvolvida pelo Google, projetada para simplicidade, eficiência e concorrência, adequada para desenvolvimento de sistemas e aplicativos de rede. "
    if "react" in message.content.lower() or ".js" in message.content.lower():
        resposta += "É uma extensão do Javascript. Javascript é uma linguagem front-end mas pode ser usada para back-end ao usar react.js!! É a linguagem mais usada do mundo, geralmente acompanhada de html e css para criação de paginas web. Exemplos de código: https://github.com/AntonioPROLucas/App-Previsao_do_tempo https://github.com/AntonioPROLucas/mario-celular-  https://github.com/AntonioPROLucas/Intensivao-javascript_3-Vite-React-Hashtaurante "
    # Send a response back to the user
    await cl.Message(content=resposta).send()
