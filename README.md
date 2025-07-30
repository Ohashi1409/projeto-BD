# Sistema Codeforces - Projeto de Banco de Dados

Sistema de banco de dados inspirado na plataforma Codeforces, modelando usuários, grupos, contests, problemas, submissões, blog entries, comentários e relacionamentos.

## Estrutura do Projeto

### Diretórios e Arquivos Principais

- `codeforces-EER/conceitualProject.eer`  
  Diagrama conceitual do projeto (EER).
- `DBMLschema.dbml`  
  Modelo relacional em DBML.
- `No-SQL/`  
  Scripts de modelagem e consultas MongoDB.
  - `contest_fazParte1.py` a `contest_fazParte4.py`  
    Exemplos dos quatro tipos de relacionamento em MongoDB.
  - `problem_testCase1.py` a `problem_testCase4.py`  
    Exemplos de relacionamento entre problemas e test cases.
  - `init_mongodb.py`  
    Inicialização da conexão com MongoDB.
- `SQL/`  
  Scripts SQL e consultas em SQLite.
  - `create_table.sql`  
    Criação das tabelas.
  - `insert_data.sql`  
    Inserção de dados de exemplo.
  - Scripts de consulta (ex: `inner-join1.py`, `group-by1.py`, etc).
- `README.md`  
  Documentação do projeto.

  ## Esquema Conceitual

![Esquema Conceitual do Projeto](codeforces-EER/Conceitual.png)

  ## Modelo Lógico

![Modelo Lógico do projeto](modelo%20logico/Logico.png)

## Banco de Dados

- `codeforces.db`  
  Banco MySQL gerado a partir dos scripts SQL.

## Como Usar o Sistema

**Criar as tabelas:**
```sh
python3 SQL/tables.py
```

**Inserir dados:**
```sh
python3 SQL/populate_database.py
```

**Consultar dados:**
```sh
python3 SQL/caminhoDaConsulta.py
```

**Modelagem NoSQL (MongoDB):**
```sh
python3 No-SQL/caminhoDaConsulta.py
```

## Estrutura do Banco de Dados

### Entidades Principais

- **User**: Usuários da plataforma (`userName`, `email`, `rating`, `endereço`, etc)
- **Group**: Grupos de usuários (`group_id`, `group_name`, `tipo`, `membros`)
- **Contest**: Competições (`contest_id`, `nome`, `duração`, `início`, etc)
- **Problem**: Problemas de programação (`problem_id`, `statement`, `dificuldade`, `pontos`)
- **Submission**: Submissões de soluções (`submission_id`, `tempo`, `linguagem`, `pontos`)
- **Blog Entry**: Postagens de blog (`entry_id`, `título`)
- **Comment**: Comentários em blogs (`comment_id`, `texto`, `replies`)
- **Testcase**: Casos de teste de problemas

### Relacionamentos

- **Friendship**: Amizade entre usuários
- **Creates**: Usuário cria blog entry ou comentário
- **Participa**: Usuário participa de grupo ou contest
- **Faz parte**: Problema faz parte de contest
- **Sends**: Usuário envia submissão
- **Tem**: Contest tem problemas, problema tem test cases
- **Replies**: Comentários respondem outros comentários

## Tecnologias Utilizadas

- SQLite (SQL)
- MongoDB (NoSQL)
- Python 3

## Consultas Implementadas

- **INNER JOIN**: Usuários e suas submissões, problemas e seus test cases
- **LEFT JOIN**: Usuários sem submissões
- **GROUP BY/HAVING**: Grupos com múltiplos membros, contests com mais de X problemas
- **Subconsultas**: Contagem de submissões por usuário, problemas resolvidos por contest
- **Consultas NoSQL**: Exemplos dos quatro tipos de relacionamento (referência, embutido, array de referências, array embutido)