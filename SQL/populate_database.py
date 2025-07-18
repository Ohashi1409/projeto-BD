import mysql.connector
from mysql.connector import Error
import sys
import os

class DatabasePopulator:
    def __init__(self, host='localhost', port=3306, database='codeforces-db', user='root', password='rootpassword'):
        """
        Inicializa o populador do banco de dados
        """
        self.host = host
        self.port = port
        self.database = database
        self.user = user
        self.password = password
        self.connection = None
        
    def connect(self):
        """
        Estabelece conexão com o banco de dados
        """
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                port=self.port,
                database=self.database,
                user=self.user,
                password=self.password
            )
            
            if self.connection.is_connected():
                print(f"Conectado ao banco de dados MySQL: {self.database}")
                return True
                
        except Error as e:
            print(f"Erro ao conectar ao MySQL: {e}")
            return False
    
    def disconnect(self):
        """
        Fecha a conexão com o banco de dados
        """
        if self.connection and self.connection.is_connected():
            self.connection.close()
            print("Conexão com MySQL encerrada")
    
    def execute_sql_file(self, sql_file_path):
        """
        Executa um arquivo SQL completo
        """
        if not self.connection or not self.connection.is_connected():
            print("Não há conexão ativa com o banco de dados")
            return False
            
        try:
            # Verifica se o arquivo existe
            if not os.path.exists(sql_file_path):
                print(f"Arquivo SQL não encontrado: {sql_file_path}")
                return False
            
            # Lê o conteúdo do arquivo
            with open(sql_file_path, 'r', encoding='utf-8') as file:
                sql_content = file.read()
            
            # Divide o conteúdo em comandos individuais
            sql_commands = sql_content.split(';')
            
            cursor = self.connection.cursor()
            
            for command in sql_commands:
                command = command.strip()
                if command:  # Ignora comandos vazios
                    try:
                        cursor.execute(command)
                        print(f"Executado: {command[:50]}...")
                    except Error as e:
                        print(f"Erro ao executar comando: {e}")
                        print(f"Comando: {command}")
                        # Continua executando os próximos comandos
            
            # Confirma as mudanças
            self.connection.commit()
            cursor.close()
            print("Arquivo SQL executado com sucesso!")
            return True
            
        except Error as e:
            print(f"Erro ao executar arquivo SQL: {e}")
            return False
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return False
    
    def execute_query(self, query, params=None):
        """
        Executa uma query individual
        """
        if not self.connection or not self.connection.is_connected():
            print("Não há conexão ativa com o banco de dados")
            return None
            
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute(query, params)
            
            # Se for uma query SELECT, retorna os resultados
            if query.strip().upper().startswith('SELECT'):
                results = cursor.fetchall()
                cursor.close()
                return results
            else:
                # Para INSERT, UPDATE, DELETE, etc.
                self.connection.commit()
                cursor.close()
                return True
                
        except Error as e:
            print(f"Erro ao executar query: {e}")
            return None
    
    def verify_population(self):
        """
        Verifica se o banco foi populado corretamente
        """
        tables_to_check = [
            'user_table', 'problem_table', 'contest_table', 
            'submission_table', 'user_participates_contest', 'friendship'
        ]
        
        print("=== Verificando população do banco ===")
        
        for table in tables_to_check:
            query = f"SELECT COUNT(*) as count FROM {table}"
            result = self.execute_query(query)
            
            if result:
                count = result[0]['count']
                print(f"Tabela {table}: {count} registros")
            else:
                print(f"Erro ao verificar tabela {table}")
    
    def clear_database(self):
        """
        Limpa todas as tabelas do banco (cuidado!)
        """
        print("ATENÇÃO: Limpando todas as tabelas do banco de dados...")
        
        # Desabilita verificação de chaves estrangeiras temporariamente
        self.execute_query("SET FOREIGN_KEY_CHECKS = 0")
        
        # Lista das tabelas na ordem correta para limpeza
        tables_to_clear = [
            'submissoes', 'participacoes', 'amizades',
            'problemas', 'contests', 'usuarios'
        ]
        
        for table in tables_to_clear:
            query = f"DELETE FROM {table}"
            if self.execute_query(query):
                print(f"Tabela {table} limpa")
            else:
                print(f"Erro ao limpar tabela {table}")
        
        # Reabilita verificação de chaves estrangeiras
        self.execute_query("SET FOREIGN_KEY_CHECKS = 1")
        
        print("Banco de dados limpo!")

def main():
    """
    Função principal para popular o banco de dados
    """
    # Configuração da conexão - ajuste conforme sua configuração
    db_config = {
        'host': 'localhost',
        'port': 3306,
        'database': 'codeforces-db',
        'user': 'root',
        'password': 'rootpassword'
    }
    
    # Caminho para o arquivo populate.sql
    sql_file_path = os.path.join(os.path.dirname(__file__), 'populate_mysql.sql')
    
    # Estabelece conexão
    populator = DatabasePopulator(**db_config)
    
    if not populator.connect():
        print("Não foi possível conectar ao banco de dados")
        sys.exit(1)
    
    try:
        # Menu de opções
        while True:
            print("\n=== POPULADOR DE BANCO DE DADOS ===")
            print("1. Executar populate_mysql.sql")
            print("2. Verificar população do banco")
            print("3. Limpar banco de dados")
            print("4. Sair")
            
            choice = input("Escolha uma opção (1-4): ")
            
            if choice == '1':
                print(f"Executando arquivo: {sql_file_path}")
                if populator.execute_sql_file(sql_file_path):
                    print("Banco de dados populado com sucesso!")
                else:
                    print("Erro ao popular o banco de dados")
            
            elif choice == '2':
                populator.verify_population()
            
            elif choice == '3':
                confirm = input("Tem certeza que deseja limpar o banco? (s/N): ")
                if confirm.lower() == 's':
                    populator.clear_database()
                else:
                    print("Operação cancelada")
            
            elif choice == '4':
                print("Saindo...")
                break
            
            else:
                print("Opção inválida!")
        
    except KeyboardInterrupt:
        print("\nOperação interrompida pelo usuário")
    
    except Exception as e:
        print(f"Erro durante a execução: {e}")
    
    finally:
        # Sempre fechar a conexão
        populator.disconnect()

if __name__ == "__main__":
    main()
