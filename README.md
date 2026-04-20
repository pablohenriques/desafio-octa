# Trilha de Aprendizado — Desafio Octa

## Regras do Tutor

> Este repositório funciona como uma sessão de tutoria guiada. As regras abaixo são inegociáveis e existem para garantir aprendizado real.

- **Progressão bloqueada**: você só avança para o próximo exercício após demonstrar que entendeu o atual — explicando o raciocínio, não apenas apresentando código que funciona.
- **Sem decoreba**: se você souber o resultado mas não souber explicar o porquê, o exercício não está concluído.
- **Perguntas de verificação**: ao finalizar cada exercício, o tutor fará perguntas sobre os conceitos utilizados. Respostas vagas ou decoradas serão identificadas.
- **Solução ótima**: após você resolver, o tutor apresenta a solução ótima e explica as diferenças. Entender essas diferenças faz parte do checkpoint.
- **Auxílio, não resposta**: o tutor dá dicas, faz perguntas e aponta o caminho — mas não entrega a solução antes de você tentar.

---

## Tabela de Checkpoints

| # | Exercício | Status | Conceitos Verificados | Aprovado pelo Tutor |
|---|-----------|--------|----------------------|---------------------|
| 1 | Ano Bissexto | ✔️ Aprovado pelo tutor | Módulo `%`, condicionais aninhados, ordem de avaliação, truthiness em Python | ✔️ |
| 2 | Maior entre Três Números | ✔️ Aprovado pelo tutor | Operadores de comparação, estrutura condicional aninhada, generalização com `*args`, type hints e validação de entrada, complexidade O(n) | ✔️ |
| 3 | Sequência de Fibonacci | ✔️ Aprovado pelo tutor | Laço iterativo O(n), atribuição simultânea, shadowing de built-ins, recursão ingênua O(2ⁿ) | ✔️ |
| 4 | Vetores: Busca, Inserção e Remoção | ✔️ Aprovado pelo tutor | Listas e indexação, laço com `range`, inserção com deslocamento (`list.insert`), remoção por índice (`del`), retorno de código de erro vs exceção, busca linear O(n) vs binária O(log n) | ✔️ |
| 5 | Número de Armstrong | ✔️ Aprovado pelo tutor | Extração de dígitos via string, operador `**`, list comprehension com `sum()`, retorno booleano direto, async vs multiprocessing para CPU-bound, `armstrong_until(n)` | ✔️ |

> **Legenda**: ⬜ Não iniciado · 🔄 Em andamento · ✅ Resolvido · ✔️ Aprovado pelo tutor · 🔒 Bloqueado

---

## Nível 1 — Iniciante

### Exercício 1 · Verificar se um Ano é Bissexto

**Definição**: Um ano bissexto possui 366 dias (um dia extra). Ocorre a cada quatro anos, **exceto** anos múltiplos de 100 que **não** sejam múltiplos de 400.

**Exemplos**:
- 2000 → bissexto (múltiplo de 400)
- 1900 → não bissexto (múltiplo de 100, mas não de 400)
- 2024 → bissexto (múltiplo de 4, não de 100)
- 2023 → não bissexto

**Desafio**: Escreva um programa que receba um número inteiro positivo representando um ano e determine se é bissexto.

#### Conteúdo que precisa ser dominado

| Conceito | Descrição | Você domina? |
|----------|-----------|--------------|
| Operador de módulo `%` | Obter o resto de uma divisão inteira | ⬜ |
| Operadores lógicos `and` / `or` | Combinar condições | ⬜ |
| Estrutura condicional `if / elif / else` | Executar blocos com base em condições | ⬜ |
| Ordem de avaliação de condições | Entender por que a ordem das verificações importa | ⬜ |
| Entrada de dados com `input()` | Ler dado do usuário e converter tipo | ⬜ |

#### Perguntas de verificação (após resolver)
1. Por que a regra dos múltiplos de 400 precisa ser verificada antes da regra dos múltiplos de 100?
2. O que acontece se você inverter a ordem das condições?
3. Qual seria a expressão booleana mínima que resolve esse problema em uma única linha?

---

### Exercício 2 · Encontrar o Maior entre Três Números

**Definição**: Dados três números, encontre o maior dentre eles **sem utilizar funções builtin** (ex.: `max` do Python).

**Desafio**: Escreva um programa que receba três números e retorne o maior.

#### Conteúdo que precisa ser dominado

| Conceito | Descrição | Você domina? |
|----------|-----------|--------------|
| Operadores de comparação `>`, `<`, `>=` | Comparar valores numéricos | ⬜ |
| Estrutura condicional aninhada | Encadear `if / elif / else` | ⬜ |
| Variáveis e atribuição | Armazenar e atualizar valores | ⬜ |
| Por que evitar builtins aqui | Entender o que `max` faz internamente | ⬜ |

#### Perguntas de verificação (após resolver)
1. Qual é o número mínimo de comparações necessárias para encontrar o maior entre três números?
2. Como você generalizaria sua solução para encontrar o maior entre N números?
3. O que o `max` do Python faz internamente que sua solução replica?

---

## Nível 2 — Intermediário

### Exercício 3 · Imprimir Elementos da Sequência de Fibonacci

**Definição**: A sequência de Fibonacci é definida como:
- `s[0] = 0`
- `s[1] = 1`
- `s[n] = s[n-1] + s[n-2]`, para `n >= 2`

Os 7 primeiros termos: `0, 1, 1, 2, 3, 5, 8`

**Desafio**: Escreva um programa que receba um inteiro `n` e imprima os `n` primeiros termos separados por `"; "`.

**Exemplo**: Para `n = 5`, saída esperada: `0; 1; 1; 2; 3`

#### Conteúdo que precisa ser dominado

| Conceito | Descrição | Você domina? |
|----------|-----------|--------------|
| Laço `for` e `while` | Repetir instruções um número determinado de vezes | ⬜ |
| Definição de sequência por recorrência | Entender que cada termo depende dos anteriores | ⬜ |
| Atualização simultânea de variáveis | Técnica de swap/atualização em uma linha (`a, b = b, a+b`) | ⬜ |
| Formatação de saída (`join`, `sep`) | Imprimir elementos separados por delimitador | ⬜ |
| Complexidade de tempo | Diferença entre solução iterativa O(n) e recursiva ingênua O(2^n) | ⬜ |

#### Perguntas de verificação (após resolver)
1. O que acontece com uma solução recursiva ingênua para `n = 50`? Por quê?
2. Explique o que `a, b = b, a + b` faz em uma única linha.
3. Como você imprimiria os termos sem deixar `"; "` no final?

---

### Exercício 4 · Vetores: Busca, Inserção e Remoção

**Desafio**: Escreva um programa com as seguintes funções:

- `search(v, x)`: retorna o índice da primeira ocorrência de `x` em `v`, ou `-1` se não encontrado.
- `insert(v, x, k)`: insere `x` na posição `k` de `v`. Se `k >= len(v)`, preenche as posições intermediárias com `0`.
- `remove(v, x)`: remove a primeira ocorrência de `x` em `v`. Retorna `-1` se não houver ocorrência.

**Script principal a executar**:

```
v = [0, -1, -2, -2, -4, -5]
rs = search(v, -2)   → imprime rs
rs = search(v, 2)    → imprime rs
insert(v, 2, 3)      → imprime v
insert(v, 10, 10)    → imprime v
rr = remove(v, -2)   → imprime rr
                     → imprime v
```

#### Conteúdo que precisa ser dominado

| Conceito | Descrição | Você domina? |
|----------|-----------|--------------|
| Listas em Python (indexação, `len`) | Acessar, medir e percorrer listas | ⬜ |
| Laço com índice (`range`, `enumerate`) | Iterar com controle de posição | ⬜ |
| Inserção em lista (`insert`, slice) | Adicionar elementos em posição específica | ⬜ |
| Remoção de elemento por valor vs índice | Diferença entre `remove()`, `pop()` e `del` | ⬜ |
| Tratamento de índice fora dos limites | Lidar com `k >= len(v)` sem erro | ⬜ |
| Funções com efeitos colaterais vs retorno | Entender quando modificar in-place vs retornar nova lista | ⬜ |

#### Perguntas de verificação (após resolver)
1. Qual é a diferença entre `list.remove(x)` nativo e a sua função `remove(v, x)`?
2. Por que `insert(v, 10, 10)` precisa de tratamento especial?
3. Sua função `search` tem complexidade O(n). Existe uma forma mais eficiente? Quando ela se aplicaria?

---

## Nível 3 — Avançado

### Exercício 5 · Verificar se um Número é de Armstrong

**Definição**: Um número inteiro positivo `x` de `n` algarismos é um número de Armstrong de ordem `n` se `x` é igual à soma das `n`-ésimas potências de seus algarismos.

**Exemplos**:
- `x = 153`, `n = 3`: Armstrong, pois `1³ + 5³ + 3³ = 153` ✔
- `x = 13`, `n = 2`: não Armstrong, pois `1² + 3² = 10 ≠ 13` ✗
- `x = 9474`, `n = 4`: Armstrong, pois `9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474` ✔

**Desafio**: Escreva um programa que determine se um número é de Armstrong e indique sua ordem.

#### Conteúdo que precisa ser dominado

| Conceito | Descrição | Você domina? |
|----------|-----------|--------------|
| Extração de dígitos de um número | Via operação aritmética (`% 10`, `// 10`) ou conversão de string | ⬜ |
| Operador de potenciação `**` | Calcular `dígito ** n` | ⬜ |
| Contagem de algarismos | Determinar `n` sem usar `len(str(x))` e também com | ⬜ |
| Laço de acumulação | Somar resultados parciais em variável acumuladora | ⬜ |
| Duas abordagens distintas | Aritmética pura vs manipulação de string — prós e contras | ⬜ |
| Compreensão de listas (list comprehension) | Escrever a solução de forma concisa e legível | ⬜ |

#### Perguntas de verificação (após resolver)
1. Qual é a diferença de legibilidade e desempenho entre extrair dígitos via aritmética e via conversão de string?
2. Como você modificaria o programa para listar **todos** os números de Armstrong até um limite `N`?
3. Escreva a solução completa em uma única linha usando list comprehension.

---

## Como usar este guia

1. Leia a definição e os exemplos do exercício atual.
2. Estude os conceitos da tabela de conteúdo antes de tentar resolver.
3. Tente resolver por conta própria e compartilhe seu código.
4. Responda as perguntas de verificação.
5. O tutor revisa, apresenta a solução ótima e marca o checkpoint.
6. Somente após aprovação, avance para o próximo exercício.
